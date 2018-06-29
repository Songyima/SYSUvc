#!/usr/bin/en sh
DATA=~/Data/validate_code

echo "rm train lmdb"
rm -rf $DATA/train/train.lmdb

~/caffe-master/build/tools/convert_imageset --gray --shuffle \
--resize_height=32 --resize_width=32 \
$DATA/ $DATA/train.txt  $DATA/train/train.lmdb

echo "rm test lmdb"
rm -rf $DATA/test/test.lmdb

~/caffe-master/build/tools/convert_imageset --gray --shuffle \
--resize_height=32 --resize_width=32 \
$DATA/ $DATA/test.txt  $DATA/test/test.lmdb
