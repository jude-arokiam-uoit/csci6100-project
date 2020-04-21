# import libraries
import pymongo
import csv

# mongodb connection
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
mydb = myclient["esmall"]
mycol = mydb["pairs"]

# create csv file
# filename = 'raw_mozilla_data.csv'
filename = 'raw_esmall_pairs_data.csv'

with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    
    # query and find all records in collection (table)
    # write record to csv file
    for report in mycol.find():
        # if (report.get('short_desc').isascii()):
        #     if (report.get('dup_id') == '[]'):
        #         report['dup_id'] = ''
            
            writer.writerow([report.get('_id'),
                             report.get('bug1'),
                             report.get('bug2'),
                             report.get('dec')])