#!/bin/bash
monitor_count=0
while :
do
monitor_count=`expr ${monitor_count} + 1`
id=0
ret=`nvidia-smi --query-gpu=memory.used,utilization.gpu --format=csv | sed '1d'`
for num in `echo $ret | grep -o '[0-9]\+'`
do
array[$id]=$num
echo $num
id=`expr $id + 1`
done

for idx in `seq 0 3`
do
# find the free gpu
id_1=`expr $idx \* 2`
id_2=`expr $idx \* 2 + 1`
if [ ${array[$id_1]} -eq 0 -a ${array[$id_2]} -lt 10 ]
then
echo gpu: ${idx} is free
fi
done

sleep 2

if [ $monitor_count -eq 4 ]
then 
break
fi

done
