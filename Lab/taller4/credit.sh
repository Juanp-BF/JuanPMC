#!/bin/bash

wget http://www-bcf.usc.edu/~gareth/ISL/Credit.csv

awk -F, '{print $2" "$3" "$4" "$5" "$6" "$7" "$12;}' Credit.csv | tail -n +2 > datacredit.csv



