# take an existing csv and add columns to it

from csv import writer
from csv import reader

print('Input file:')
infile = input()
print('Output file:')
outfile = input()

with open(infile, 'r') as read_obj, \
    open(outfile, 'w', newline='') as write_obj:
    #create csv reader
    csv_reader = reader(read_obj)
    #create csv writer
    csv_writer = writer(write_obj)
    #skip the header line
    next(read_obj)
    #write a new header with 3 columns
    csv_writer.writerow(('deck', 'english', 'spanish'))
    #read each row of csv
    for row in csv_reader:
        # add deck number in column 1
        csv_writer.writerow(('1', row[0], row[1]))