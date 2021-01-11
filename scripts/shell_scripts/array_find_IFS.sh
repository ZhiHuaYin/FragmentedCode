#!/bin/bash
SAVEIFS=$IFS
IFS=$(echo -en "\n\b")

for i in {0..16}
do
    array[$i]=0
done

for example in `find ./ -name "*.txt"`
do
    for line in `sed -n '2,$p' $example | cut -f 1`
    do
       array[$line]=`expr ${array[$line]} + 1`
    done
done

count=0
for NUM in ${array[*]}
do
    echo catID_$count : $NUM
    count=`expr $count + 1`
done



IFS=$SAVEIFS
