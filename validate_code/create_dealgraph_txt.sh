#search path of all pics
#我们把所有图片路径记录下来create_dealgraph_txt，
#然后用dealAllGraph.py进行预处理
#把验证码中的干扰线条、干扰点去掉，把图片二值化、灰度化，重新写回原路径
#usage: bash create_dealgraph_txt.sh

DATA=~/Data/validate_code

array=(0 1 2 3 4 5 6 7 8 9)
array3=(a b c d e f g h i j k l m n o p q r s t u v w x y z)

echo "create dealgraph.txt"
rm -rf $DATA/dealgraph.txt
touch $DATA/dealgraph.txt

for i in $(seq 0 9)
do
find $DATA/newpics -name ${array[i]}*.jpg >>$DATA/dealgraph.txt
done

for i in $(seq 10 35)
do
find $DATA/newpics -name ${array3[i-10]}*.jpg >>$DATA/dealgraph.txt
done