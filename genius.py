#made by Joseph Novembre
#use with readfile.py for cool notepad reading magic
#purpose of script is to parse api and pull data down from subgenius and
#drop into csv files

import requests
import csv
import readfile
import time






#generates csv file to be populated, can edit with name of your choice
filename = "historynewtest.csv"

with open(filename, 'w') as csvfile:
    cswriter = csv.writer(csvfile)
    fields = ['Subscriber_id','Date', 'notes', 'history_id', 'renewal_code']
    cswriter.writerow(fields)
    
    for i in range (len(readfile.lines)):
        subid = readfile.lines[i]
        query = {'subscriber_id': int(subid)}
        renewal_code = readfile.codes[i]
        
    
        response = requests.get(readfile.api_url, params= query, auth = (readfile.api_key_id, readfile.api_password))
        if response.json().get('history') is None:
            print('subscriber doesnt exist or was deleted')
        else:
            for y in range (len(response.json().get('history'))):
        
                try: date = response.json().get('history')[y].get('date') 
                except IndexError: date = 'null'

                try: notes = response.json().get('history')[y].get('notes')
                except IndexError: notes = 'null'
    
                try: history_id = response.json().get('history')[y].get('history_id')
                except IndexError: history_id = 'null'

            

                rows = [subid, date, notes, history_id, renewal_code]
        
                cswriter.writerow(rows)
        time.sleep(10) #set time between api requests in seconds
        csvfile.flush()
        
        
 