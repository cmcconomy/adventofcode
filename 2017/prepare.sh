#!/bin/bash

DAY=$1
echo "Creating resources for Day $DAY"
 
mkdir day$DAY
cp skeleton.py day$DAY/day$DAY.py
cd day$DAY
subl day$DAY.py
subl input.txt
