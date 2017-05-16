
# coding: utf-8

# In[1]:

#Testing connectivity with Untappd API
import requests #for requesting API calls
import pandas as pd #for building pandas dataframes for analysis
from pandas.io.json import json_normalize #help with converting dictionaries to dataframes
from datetime import datetime #log date and time of activities


# In[2]:

# Assign URL to variable: url
url = 'https://api.untappd.com/v4' #base URL for all API calls
client_id = '?client_id=D9E63A3F203F8A4FDBE5B7E58CEDB2E90FF50AB4'
client_secret = '&client_secret=C861E23878359F93F1EF3FDB7F233095316C6CA5'
code='F1BD60BFBB99F5AA8D23067359210F6370EEE57E'
access_token = '51CDCC3DAECC020BA92A9D959963D27D5D1DA951'


# In[3]:

#Parameters specific to user beer
user_beer = '/user/beers'
username = '/joshuaemayer' #return results for this user
limit = '&limit='
limit_num = 50
offset = '&offset='
offset_num = 0


# In[4]:

#Let's keep track of how many API calls we are making for fun
api_count = []


# In[5]:

#Initialize our zero vars
load_indicator = 0
api_call_counter = 0

#Since the Untappd API only allows 50 results per call, let's iterate until we acquire all of the results
#Hopefully we don't lose our API priveleges ;)
while (load_indicator == 0) & (len(api_count) <= 100) :
    # Package the request, send the request and catch the response: r
    r = requests.get(url+user_beer+username+client_id+client_secret+limit+str(limit_num)+offset+str(offset_num))
    # Let's keep track of how many API calls we are making, limit is 100 per hour
    api_count.append(format(datetime.now()))
    # Decode the JSON data into a dictionary: json_data
    json_data = r.json()
    if (json_data['meta']['code'] == 200) & (json_data['response']['beers']['count'] > 0) :
        df_name = json_normalize(json_data['response']['beers']['items'])
        print('Successfully Loaded & Normalized JSON Data')
        if api_call_counter == 0 :
            orig_df = df_name.copy()
            print('Succesfully Copied Original Dataframe')
        if api_call_counter > 0 :
            orig_df = orig_df.append(df_name, ignore_index=True)
            print('Successfully Appended to Original DataFrame ')
        api_call_counter += 1
        offset_num += limit_num
        print('Dataframes Loaded: ' + str(api_call_counter))
    elif (json_data['meta']['code'] == 200) & (json_data['response']['beers']['count'] == 0) :
        load_indicator = 1
        print('Finished Loading JSON Files')
        print('API Calls Made: ' + str(len(api_count)))
        print('Distinct Beers: ' + str(orig_df.shape[0]))
        print('Ending Time: ' + str(datetime.now()))
    elif (json_data['meta']['code'] != 200) :
            print('API call failed: ' + str('code: ') + str(json_data['meta']['code']) + ' '
                  + str(json_data['meta']['error_detail']))
            print('Ending Time: ' + str(datetime.now()))
    else :
        load_indicator = 1 
        print('Unknown reason for stopping')
        print('Ending Time: ' + str(datetime.now()))


# In[6]:

#Save dataframe to CSV file for analysis
orig_df.to_csv('my-beer-data.csv', index=False)
print('CSV Export Time: ' + str(datetime.now()))


# In[ ]:




# In[ ]:




# In[356]:




# In[ ]:




# In[ ]:




# In[ ]:



