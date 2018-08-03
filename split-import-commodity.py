#!/usr/bin/env python
# -*- coding: utf-8 -*-


### USE
### python split-import-commodity.py China-import.csv extract-import.csv

import csv
import sys

with open(sys.argv[1]) as csvfile, open(sys.argv[2],"wb") as outfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    writer= csv.writer(outfile)
    row = []
    row.append('digit code')
    row.append('commodity')
    row.append('country')
    row.append('time')
    row.append('value')

    writer.writerow(row)

    digit_bit = []
    # count_2 = 0
    # count_4 = 0
    # count_6 = 0
    # count_10 = 0

    for row_r in readCSV:
    	# print row_r
    	row = []
    	if row_r[0] == "Commodity" or row_r[0] == "All Commodities":
    		continue
    	# print row_r[0]
    	space_number = row_r[0].find(' ')
    	# print space_number
    	if space_number >= 0:
    		# if len(row_r[0][0:space_number]) == 10:
    		# 	row.append(row_r[0][0:space_number-2])
    		# else:
    		row.append(row_r[0][0:space_number])
    		if len(row[0]) not in digit_bit:
    			digit_bit.append(len(row[0]))
    		# if len(row[0]) == 2:
    		# 	count_2 += 1
    		# if len(row[0]) == 4:
    		# 	count_4 += 1
    		# if len(row[0]) == 6:
    		# 	count_6 += 1
    		# if len(row[0]) == 8:
    		# 	count_10 += 1
    		row.append(row_r[0][space_number+1:])
    		row.append(row_r[2])
    		row.append(row_r[3])
    		row.append(row_r[4])
    		# print row
    		writer.writerow(row)
    		# break
    print digit_bit
    # print count_2, count_4, count_6, count_10
