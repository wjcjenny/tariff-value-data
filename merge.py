#!/usr/bin/env python
# -*- coding: utf-8 -*-


### USE
### python merge.py extract-import.csv master.csv master-value.csv

import csv
import sys

digit_value = {}
digit_10 = {}
digit_6_value = {}
digit_4_value = {}
digit_2_value = {}

with open(sys.argv[1]) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if row[0] == 'digit code':
            continue
        if len(row[0]) == 6:
            digit_6_value[row[0]] = row[4]

        if len(row[0]) == 4:
            digit_4_value[row[0]] = row[4]

        if len(row[0]) == 2:
            digit_2_value[row[0]] = row[4]

        if len(row[0]) == 10:
            key = row[0][0:8]

            if key not in digit_value:
                digit_value[key] = int(row[4])
                digit_10[key] = []
                digit_10[key].append(row[0])
            else:
                digit_value[key] += int(row[4])
                digit_10[key].append(row[0])
            	# break


# print digit_value

with open(sys.argv[2]) as csvfile, open(sys.argv[3],"wb") as outfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    writer= csv.writer(outfile)

    for row in readCSV:
        if row[0] == "HS 8 digit code ":
            row.append("HS 6 digit code")
            row.append("Value-6")
            row.append("HS 4 digit code")
            row.append("Value-4")
            row.append("HS 2 digit code")
            row.append("Value-2")
            writer.writerow(row)
            continue
        if row[1] in digit_value:
            row[3] = digit_value[row[1]]
            row[2] = digit_10[row[1]]
        key = row[1][0:6]
        if key in digit_6_value:
            row.append(str(key))
            row.append(digit_6_value[key])
        else:
            row.append(' ')
            row.append(' ')

        key = row[1][0:4]
        if key in digit_4_value:
            row.append(str(key))
            row.append(digit_4_value[key])
        else:
            row.append(' ')
            row.append(' ')

        key = row[1][0:2]
        if key in digit_2_value:
            row.append(str(key))
            row.append(digit_2_value[key])
        else:
            row.append(' ')
            row.append(' ')
        writer.writerow(row)


