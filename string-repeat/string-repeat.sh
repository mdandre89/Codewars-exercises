#!/bin/bash
repeat=$1
string=$2
s=$string

for i in `seq 2 $repeat`
do
    s=${s}${string}
done

echo $s