'''
Esteban Camarillo
ID #: 1636095

'''

import datetime
import os
from typing  import TextIO

today = datetime.datetime.now()
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
months = 0
date_changes: str = ''
sum_num = 1

while sum_num == 1:
    file_to_open: str = str(input())
    if os.path.exists(file_to_open):
        file: TextIO = open(file_to_open, 'r')
    else:
        continue

    lines = file.readlines()
    line: str
    file.close()
    for line in lines:
        input_dates: str = line
        if input_dates == '-1':
            ran_num = 0
            break

        remove_next_line = input_dates.replace('\n', '')
        date_split = remove_next_line.split(' ')

        length = len(date_split)
        if length !=3:
            continue
        month = date_split[0]
        day =  date_split[1]
        year = date_split[2]
        day_number: int = day.split(",")[0]
        x: int
        for x in range(8,12):
            if month ==  months[x]:
                month_num = int + x + 1
        date_changes = str(month_num) + '/' + str(day_number) + '/' + str(year)



