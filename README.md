# A Guide to Selecting Your Next Craft Beer 

# Objective

The application “Untappd” was created in late 2010 as a platform that allows its users to “check-in” beers tasted and share these check-ins, along with their individual ratings, with their friends. As an avid user of the application, it is great to be able to maintain a log of personally tasted and rated beers. 

The Untappd application should leverage its user ratings and provides tailored recommendations based on individual user preferences. The objective of my project is to leverage users historical ratings to create predictions for un-tasted beers and create a personalized recommendation for which beer to sample next.

# Target Audience and Why

My target audience will initially be the Untappd user base, however, believe that any craft beer drinker will find the results interesting. 

Since the early 1990s the U.S. craft beer scene has been on the rise. We now have over 5,000 unique craft breweries in the U.S. which may cause newfound confusion for the average consumer when shopping for beer. 

Given the huge rise in the craft brewery scene in the United States, it can be overwhelming trying to decide which new brewery or beer to try. My app will help them decide which beer to try next given their unique tastes and historical ratings.

# The Data

All of the data will be pulled via the Untappd API. My personal dataset consists of ~200 distinct beers and ratings. The total beer set to predict will be roughly 10,000+ new beers. Each beer has a number of factors based on brewery, style, my personal rating, mass user rating, location (city, state, country), IBU (integer, bitterness rating), ABV (alcohol content), and potentially other factors that I still need to explore. 

# Approach

1.	Leverage Python’s rich libraries to pull the data via API (in JSON format) calls for analysis. 
2.	Since I am limited to 100 API calls per hour and 50 records per call, I will write a script to pull as much data as I can at one time and repeat until I have a complete dataset. 
3.	Create my personal beer list (~200 distinct beers) and analyze/clean data.
4.	Create untasted beer list (~10,000+ distinct beers) and analyze/clean data.
5.	Analysis and factor engineering: understand key drivers to beer ratings. 
6.	Leverage machine learning methodologies, test multiple algorithms for prediction approach. Select best algorithm.
7.	Build prediction ratings from ~200 distinct beers and extract upon 10,000+ beers based on a unique user’s ratings data. 
8.	Build prediction ratings from ~200 distinct beers and extract upon 10,000+ beers based on mass user ratings data. 
9.	Compare results from #7 and #8, produce insight and recommendations. 
10.	Identify challenges with approach / results and provide recommendations on how to improve for future analysis.  

# Deliverables

Associated code, paper, and presentation are included in the associated files. 

In addition, the final blog post may be found at https://www.linkedin.com/pulse/using-machine-learning-select-my-next-craft-beer-josh-mayer 
