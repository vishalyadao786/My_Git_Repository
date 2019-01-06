from xopen import xopen
import glob
import json
import pandas as pd
import numpy

files = glob.glob("colorsinart_/2018*xz") #load all files in directory to be parsed through the xopen read
content = ""
counter = 1
list_item = []
list_header = ['description', 'date_posted', 'likes', 'comments', 'post_id', 'username', 'is_connected_fb', 'is_video']

for file in files:
    with xopen(file) as f:
        if counter == 1: #identify first record
            content = content + "[" + str(f.read()) + ", \n"
            counter += 1
        elif counter == len(files): #identify last record
            content = content + str(f.read()) + "]"
            counter += 1
        else:
            content = content + str(f.read()) + ", \n"
            counter += 1

#convert string to listed dict format
data = json.loads(content)

#extract the required metric from the json data
for data in data:
    list_item += [(data['node']['edge_media_to_caption']['edges'][0]['node']['text'],
                datetime.datetime.fromtimestamp(data['node']['taken_at_timestamp']).strftime('%Y-%m-%d %H:%M:%S'), #transform the date format from ms
                data['node']['edge_liked_by']['count'],
                data['node']['edge_media_to_comment']['count'],
                data['node']['id'],
                data['node']['owner']['username'],
                data['node']['owner']['connected_fb_page'],
                data['node']['is_video'])]

print(pd.DataFrame((list_item), columns = list_header)) #print the output as dataframe
