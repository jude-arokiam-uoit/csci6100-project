# import libraries
import pymongo
import csv

# mongodb connection
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
mydb = myclient["openOffice"]
mycol = mydb["clear"]

# create csv file
# filename = 'raw_mozilla_data.csv'
# filename = 'raw_esmall_clear_data.csv'
filename = 'raw_open_office_clear_data.csv'

with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    
    # query and find all records in collection (table)
    # write record to csv file
    for report in mycol.find():
        if (report.get('short_desc').isascii()):
            if (report.get('dup_id') == '[]'):
                report['dup_id'] = ''
            
            writer.writerow([report.get('bug_id'),
                             report.get('bug_severity'),
                             report.get('dup_id'),
                             report.get('short_desc'),
                             report.get('resolution')])