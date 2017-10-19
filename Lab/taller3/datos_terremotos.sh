#!/bin/bash

wget https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.csv

awk -F, '{print $2" "$3;}' all_month.csv | tail -n +2 > locations.txt

grep -i CA all_month.csv | awk -F, '{print $5}' | tail -n +2 > magnitudes.txt

rm -f all_month.csv


