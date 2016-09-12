#!/bin/bash
date=$(date --iso)
wget -O sbk_shifts_$date.csv http://calc.sankey.info/sbk_shifts.csv
wget -O sbk_start_dates_$date.csv http://calc.sankey.info/sbk_start_dates.csv
