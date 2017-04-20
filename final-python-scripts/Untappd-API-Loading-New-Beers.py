
# coding: utf-8

# In[2]:

#Testing connectivity with Untappd API
import requests #for requesting API calls
import pandas as pd #for building pandas dataframes for analysis
from pandas.io.json import json_normalize #help with converting dictionaries to dataframes
import re #for parsing file names
import glob, os #for reading file names
import datetime # for tracking API call counts


# In[3]:

#IMPORTANT TO SET AS DESIRED, UNTAPPD LIMITS TO 100 PER HOUR
max_api_call = 100


# In[4]:

#DO NOT EDIT - Initial Vars ONLY EXECUTE ONCE IF IN IPYTHON NOTEBOOK
#Let's keep track of how many API calls we are making for fun
api_count = []
load_indicator = 0
beer_counter = 1


# In[5]:

#Change directory to read existing file names
os.chdir('/Users/joshuaemayer/Programming/Springboard/capstone-1/new_beers')
cwd = os.getcwd()
print('Changing Directory to: ' + cwd)


# In[6]:

#Reading CSV files in the DIR
file_names = []
file_names = glob.glob('*.csv')


# In[7]:

#Creating a list with all of the file names, searching for the last BID
BID_list = []
for file in file_names :
    temp = re.split('_*', file)
    BID_list.append(int(temp[4]))


# In[8]:

#Used for API calls and authentication
url = 'https://api.untappd.com/v4' #base URL for all API calls
client_id = '?client_id=D9E63A3F203F8A4FDBE5B7E58CEDB2E90FF50AB4' #required for authentication
client_secret = '&client_secret=C861E23878359F93F1EF3FDB7F233095316C6CA5' #required for authentication


# In[9]:

#Parameters specific to "beer info" API calls
beer_info = '/beer/info/' #extend URL for the "beer info" requests
compact = '&compact=true' #only return basic beer info (and not social media garbage)


# In[10]:

#Beer ID - unique identifier for each beer
if bool(len(BID_list) > 0) :
    BID = max(BID_list) #Beer ID - unique identifier for each beer
else :
    BID = 1 #if no files exist, let's start with the first BID


# In[11]:

#Callout starting BID for this file
print('Starting with BID: ' + str(BID))


# In[26]:

#Untappd limits API calls to 100 per hour
while (load_indicator == 0) & (len(api_count) < max_api_call) :
    # Package the request, send the request and catch the response: r
    r = requests.get(url+beer_info+str(BID)+client_id+client_secret+compact)
    # Let's keep track of how many API calls we are making, limit is 100 per hour
    api_count.append(format(datetime.datetime.now()))
    # Decode the JSON data into a dictionary: json_data
    json_data = r.json()
    if (json_data['meta']['code'] == 200) :
        df_name = json_normalize(json_data['response']['beer'])
        print('Successfully Loaded & Normalized JSON Data' + ' for Beer ID ' + str(BID))
        if beer_counter == 1 :
            orig_df = df_name.copy()
            print('Succesfully Copied Original Dataframe')
        if beer_counter > 1 :
            orig_df = orig_df.append(df_name, ignore_index=True)
            print('Successfully Appended Beer ' + str(BID) + ' to Original Dataframe')
        print('Dataframes created:' + str(beer_counter), 'Total API Calls Made: ' + str(len(api_count)))
    elif (json_data['meta']['code'] != 200) & (beer_counter == 1) :
        print('API call failed: ' + str('code: ') + str(json_data['meta']['code']) + ' '
              + str(json_data['meta']['error_detail']))
        orig_df = 'Cannot Export because No Data Exists'
        print('Failed to load any data.')
        break
    elif (json_data['meta']['code'] != 200) :
        print('API call failed: ' + str('code: ') + str(json_data['meta']['code']) + ' '
              + str(json_data['meta']['error_detail']))
        if 'This Beer ID is invalid.' in str(json_data['meta']['error_detail']) :
            print('BID ' + str(BID) + ' does not exist. Skipping this BID')
            BID += 1 #Continue to the next beer
        else :
            break
    else :
        load_indicator = 1
        print('Finished Loading JSON Files')
        print('Total API Calls Made: ' + str(len(api_count)))
    if (json_data['meta']['code'] == 200) & (load_indicator == 0) & (len(api_count) < max_api_call) :
        BID += 1 #Continue to the next global beer
        beer_counter += 1 #local beer counter


# In[27]:

#print to console the final BID
if isinstance(orig_df, str) :
    print('Cannot Export because No Data Exists')
else :
    #Created unique CSV file name
    cwd = os.getcwd()
    csv_name = 'dataframe' + '_apicalls_' + str(len(api_count)) + '_finalBID_' + str(BID) + '_' + '.csv'
    print('Total Beers Acquired: ' + str(beer_counter))
    print('Final BID Loaded: ' + str(BID))
    print('Exporting CSV File to: ' + cwd)
    print('Exporting CSV file as: ' + csv_name)
    orig_df.to_csv(csv_name, index=False)


# In[ ]:



