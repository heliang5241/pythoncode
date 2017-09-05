#!/bin/bash
count=0
cat 0808a.txt|grep -v ^#|grep -v ^$ |while read line

    do
       REMOTE_IP=`echo $line |awk '{print$1}'`
        if [ $REMOTE_IP -gt 5 ];then
                echo "ok"
                ((count++));
        else
                echo "bad"
        fi
    done
echo $count
