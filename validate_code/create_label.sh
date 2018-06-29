#!/bin/bash
#label.txt looks like:
#10 a
#11 b
#12 c
#use it to change class number to class name
DATA=~/Data/validate_code
array=(0 1 2 3 4 5 6 7 8 9)
array3=(a b c d e f g h i j k l m n o p q r s t u v w x y z)

echo "create label.txt"
rm -rf $DATA/label.txt
for i in $(seq 0 9)
do
echo "$i ${array[i]}">>$DATA/label.txt
done
for i in $(seq 10 35)
do
echo "$i ${array3[i-10]}">>$DATA/label.txt
done

echo "All done"
