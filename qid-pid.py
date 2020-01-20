# find qualtrics id and rename it to id in csv
# qid - qualtrics id
# pid - participant id

import os
import csv

_path = '.'
with open('qid_and_pid.csv') as f:
    lines = csv.reader(f)
    for line in lines:
        #print(line[0], line[1])
        for filename in os.listdir(_path):
            if(line[0] in filename):
                print("Match: {}, {}, {}".format(line[0] ,filename, line[1]))
                rename = filename
                os.rename(rename, line[1]+'.jpg')
                print('\n')
                print("File {} renamed to {}".format(rename,line[1] ))