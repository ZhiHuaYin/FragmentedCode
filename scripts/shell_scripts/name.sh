#!/bin/bash
SAVEIFS=$IFS
IFS=$(echo -en "\n\b")
#for filepath in `find test -name "*.ann"`
for filepath in `find Annotated20190219XIMEACervix-Negative -name "*.ann"`
do 
arr=(`echo $filepath | tr '/' '-'`)
cp ${filepath} ./tmp/${arr}
echo ${arr}
done
IFS=$SAVEIFS
