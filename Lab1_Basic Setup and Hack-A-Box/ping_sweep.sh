#! /bin/bash

for ip in {1..254}; do

ping -c 1 $1.$2.$3.$ip | grep "bytes from" | cut -d " " -f  4 | cut -d ":" -f  1 &

#echo "$1.$2.$3.$ip"

done
