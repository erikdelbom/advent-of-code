#!/bin/bash



for i in {1..24}; do 
    if [ $i -lt 10 ]; then
        dir_name=$(pwd)/0$i
    else
        dir_name=$(pwd)/$i
    fi;
    
    mkdir $dir_name
    mkdir $dir_name/python && touch $dir_name/python/part1.py
    mkdir $dir_name/rust && touch $dir_name/rust/part1.rs
    mkdir $dir_name/javascript && touch $dir_name/javascript/part1.js
    

done
