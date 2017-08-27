#! /usr/bin/bash
# Author : Bhishan Poudel
# Date   : Oct-14-2016 Fri

for i in `seq 1 10`;
    do
        python create_rand_num.py && cp temp.txt outputs/out$i.txt &
    done

echo "outputs created inside outputs"
