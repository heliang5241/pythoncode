#!/usr/bin/env python
#coding=utf-8
import os, sys, time, json, yaml ,pdb
from kazoo.client import KazooClient
from kazoo.exceptions import NoNodeError
from kafka import KafkaClient
from kafka import KafkaConsumer
from kafka import TopicPartition
from kafka import SimpleClient
from kafka.protocol.offset import OffsetRequest, OffsetResetStrategy
from kafka.common import OffsetRequestPayload

class spoorerClient(object):

    def __init__(self, zookeeper_hosts, kafka_hosts, zookeeper_url='/', timeout=3, log_dir='/tmp/spoorer'):
        self.zookeeper_hosts = zookeeper_hosts
        self.kafka_hosts = kafka_hosts
        self.timeout = timeout
        self.log_dir = log_dir
        self.log_file = log_dir + '/' + 'spoorer.log'
        self.kafka_logsize = {}
        self.result = []
        self.log_day_file = log_dir + '/' + 'spoorer_day.log.' + str(time.strftime("%Y-%m-%d", time.localtime()))
        self.log_keep_day = 1
        #将spoorer.yaml中的配置读取出来
        try:
            f = file(os.path.dirname(os.path.abspath(__file__)) + '/' + 'spoorer.yaml')
            self.white_topic_group = yaml.load(f)
        except IOError as e:
            print 'Error, spoorer.yaml is not found'
            sys.exit(1)
        else:
            f.close()
            # print self.white_topic_group
            if self.white_topic_group is None:
                self.white_topic_group = {}

        if not os.path.exists(self.log_dir):
            os.mkdir(self.log_dir)

        #获取到的消费进度会写入到self.log_file，self.log_day_file这两个文件中，self.log_day_file用于存放历史消费进度，self.log_file存放当前最新获取到的消费进度
        #self.log_day_file该文件的创建时间和当前系统时间相隔一天，则删除
        for logfile in [x for x in os.listdir(self.log_dir) if x.split('.')[-1] != 'log' and x.split('.')[-1] != 'swp']:
            if int(time.mktime(time.strptime(logfile.split('.')[-1], '%Y-%m-%d'))) < int(time.time()) - self.log_keep_day * 86400:
                os.remove(self.log_dir + '/' + logfile)

        if zookeeper_url == '/':
            self.zookeeper_url = zookeeper_url
        else:
            self.zookeeper_url = zookeeper_url + '/'

    def spoorer(self):  #连接kafka，获取topics
        try:
            kafka_client = SimpleClient(self.kafka_hosts, timeout=self.timeout)
            # print kafka_client.topics
        except Exception as e:
            print "Error, cannot connect kafka broker."
            sys.exit(1)
        else:
            kafka_topics = kafka_client.topics
        finally:
            kafka_client.close()

        #连接zk，获取当前消费进度current offset
        try:
            zookeeper_client = KazooClient(hosts=self.zookeeper_hosts, read_only=True, timeout=self.timeout)
            zookeeper_client.start()
        except Exception as e:
            print "Error, cannot connect zookeeper server."
            sys.exit(1)

        try:
            groups = map(str,zookeeper_client.get_children(self.zookeeper_url + 'consumers'))
        except NoNodeError as e:
            print "Error, invalid zookeeper url."
            zookeeper_client.stop()
            sys.exit(2)
        else:
            for group in groups:
                print group
                if 'offsets' not in zookeeper_client.get_children(self.zookeeper_url + 'consumers/%s' % group):continue
                topic_path = 'consumers/%s/offsets' % (group)
                print 22
                topics = map(str,zookeeper_client.get_children(self.zookeeper_url + topic_path))
                if len(topics) == 0: continue

                for topic in topics:
                    if topic not in self.white_topic_group.keys():
                        continue
                    elif group not in self.white_topic_group[topic].replace(' ','').split(','):
                        continue
                    partition_path = 'consumers/%s/offsets/%s' % (group,topic)
                    partitions = map(int,zookeeper_client.get_children(self.zookeeper_url + partition_path))
                    for partition in partitions:
                        base_path = 'consumers/%s/%s/%s/%s' % (group, '%s', topic, partition)
                        owner_path, offset_path = base_path % 'owners', base_path % 'offsets'
                        offset = zookeeper_client.get(self.zookeeper_url + offset_path)[0]

                        try:
                            owner = zookeeper_client.get(self.zookeeper_url + owner_path)[0]
                        except NoNodeError as e:
                            owner = 'null'
                        #消费进度放在字典metric中
                        metric = {'datetime':time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), 'topic':topic, 'group':group, 'partition':int(partition), 'logsize':None, 'offset':int(offset), 'lag':None, 'owner':owner}
                        self.result.append(metric)
                        print "ok"
        finally:
            zookeeper_client.stop()
        #获取每个分片的logsize（此处和原文不一样，做了修改）
        try:
            client = SimpleClient(self.kafka_hosts)
        except Exception as e:
            print "Error, cannot connect kafka broker."
            sys.exit(1)
        else:
            for kafka_topic in kafka_topics:
                self.kafka_logsize[kafka_topic] = {}
                partitions = client.topic_partitions[kafka_topic]
                offset_requests = [OffsetRequestPayload(kafka_topic, p, -1, 1) for p in partitions.keys()]
                offsets_responses = client.send_offset_request(offset_requests)
                for r in offsets_responses:
                    self.kafka_logsize[kafka_topic][r.partition] = r.offsets[0]

            #logsize减去current offset等于lag
        f1 = open(self.log_file,'a+')
        f2 = open(self.log_day_file,'a+')
        str1 = "hello"
        print 0
        # print self.result
        for metric in self.result:
            logsize = self.kafka_logsize[metric['topic']][metric['partition']]
            metric['logsize'] = int(logsize)
            metric['lag'] = int(logsize) - int(metric['offset'])
            f1.write(json.dumps(metric,sort_keys=True) + '\n')
            f1.write(str1)
            f1.flush()
            f2.write(json.dumps(metric,sort_keys=True) + '\n')
            f2.flush()
        # finally:
        client.close()
        print 3
        return ''

if __name__ == '__main__':
    check = spoorerClient(zookeeper_hosts='192.168.10.156:2181', zookeeper_url='/', kafka_hosts='192.168.10.157:9092', log_dir='/tmp/spoorer', timeout=3)
    check.spoorer()

