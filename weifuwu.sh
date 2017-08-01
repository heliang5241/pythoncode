#!/bin/bash
############################################################
# $Name:         Disk_io_sdb.sh
# $Version:      v1.0
# $Function:      Disk IO
# $Description:  Monitor Dist IO sdb Status
############################################################
DISKIO_COMMAND=$1
txt=tmp
Remote_Eureka_server(){
    fanhui=`cat /etc/zabbix/scripts/$txt.txt |grep 'Remote status from Eureka server'|awk '{print $NF}'| sort | uniq`
    result=$(echo "DOWN" | grep "$fanhui")
    if [[ $result != "" ]];then
         #echo $result
	 echo 0
    else
         #echo "UP"
	 echo 1
    fi
}
Spring_Cloud_Eureka_Discovery_Client(){
    fanhui=`cat /etc/zabbix/scripts/$txt.txt |grep 'Spring Cloud Eureka Discovery Client'|awk '{print $NF}'| sort | uniq`
	result=$(echo "DOWN" | grep "$fanhui")
    if [[ $result != "" ]];then
         #echo $result
      	 echo 0
    else
         #echo "UP"
         echo 1
    fi
}
diskSpace(){
    fanhui=`cat /etc/zabbix/scripts/$txt.txt |grep 'diskSpace'|awk '{print $NF}'| sort | uniq`
	result=$(echo "DOWN" | grep "$fanhui")
    if [[ $result != "" ]];then
         #echo $result
         echo 0
    else
         #echo "UP"
         echo 1
    fi
}
mongo(){
    fanhui=`cat /etc/zabbix/scripts/$txt.txt |grep 'mongo'|awk '{print $NF}'| sort | uniq`
	result=$(echo "DOWN" | grep "$fanhui")
    if [[ $result != "" ]];then
         #echo $result
         echo 0
    else
         #echo "UP"
         echo 1
    fi	
}
refreshScope(){
    fanhui=`cat /etc/zabbix/scripts/$txt.txt |grep 'refreshScope'|awk '{print $NF}'| sort | uniq`
	result=$(echo "DOWN" | grep "$fanhui")
    if [[ $result != "" ]];then
         #echo $result
  	 echo 0
    else
         #echo "UP"
       	 echo 1
    fi		
}
hystrix(){
    fanhui=`cat /etc/zabbix/scripts/$txt.txt |grep 'hystrix'|awk '{print $NF}'| sort | uniq`
	result=$(echo "DOWN" | grep "$fanhui")
    if [[ $result != "" ]];then
         #echo $result
	 echo 0
    else
         #echo "UP"
      	 echo 1
    fi		
}
db(){
    fanhui=`cat /etc/zabbix/scripts/$txt.txt |grep 'db'|awk '{print $NF}'| sort | uniq`
        result=$(echo "DOWN" | grep "$fanhui")
    if [[ $result != "" ]];then
         #echo $result
         echo 0
    else
         #echo "UP"
         echo 1
    fi
}
  case $DISKIO_COMMAND in
        Remote_Eureka_server)
                Remote_Eureka_server;
                ;;
        Spring_Cloud_Eureka_Discovery_Client)
                Spring_Cloud_Eureka_Discovery_Client;
                ;;
        diskSpace)
                diskSpace;
                ;;
        mongo)
                mongo;
                ;;
        db)
                db;
                ;;
        refreshScope)
                refreshScope;
                ;;
        hystrix)
                hystrix;
                ;;
              *)
                echo $"USAGE:$0 {Remote_Eureka_server|Spring_Cloud_Eureka_Discovery_Client|diskSpace|mongo|refreshScope|hystrix|db}"
    esac
