#!/bin/bash
date=$(date --iso)
wget -O sgmc_shifts_$date.csv      http://calc.sankey.info/sgmc_shifts.csv
wget -O sgmc_start_dates_$date.csv http://calc.sankey.info/sgmc_start_dates.csv
