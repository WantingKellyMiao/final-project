#!/usr/bin/env python
# coding: utf-8

# # PROBLEM & BACKGROUND

# Toronto is one of the most famous places in the world. We want to explore how to establish a new business from a market point of view regarding food, accommodation, beautiful places, and many more.When it comes to a new business, it is important to explore the competition in the area, especially for a busy area. As we all known, establishing a good business idea is one of the pillars of the success and the people most often fails if there is not enough researches from a market prospective, like friendly environment. Every city is unique in their own way and give something new. And now the information is so common regarding location of every place around the world on your fingertips which make it easier to explore. Therefore, this project designed to explore the existed business around the Toronto on the basis of available information, which will generate the new business ideas based on the research.

# # DATA DESCRIPTION

# For this problem, we will get the services of Foursquare API to explore the data, in terms of their neighborhoods. The data also include the information about the places around each neighborhood like restaurants, hotels, coffee shops, parks. We selected one Borough from each city to analyze their neighborhoods. 'https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M'

# # METHODOLOGY

# We will use machine learning technique, “Clustering”, K-means to segment the neighborhoods with similar objects on the basis of each neighborhood data and explore more about these clusters based on the model. This will help to locate the target business’s areas and hubs, and then we can judge the best location to start a new business.

# # EXPLORATION

# For our target country: Toronto, we first have to clean and tidy our dirty data, including extracting table from Wikipedia page by beautifulsoup method. Then we plan to explore the data according to our requirements. In the processing phase, which applied multiple steps, eliminating “Not assigned” values, combine neighborhoods. For data verification and further exploration, we use Foursquare API to get the coordinates of Toronto and explore its neighborhoods. The neighborhoods are further characterized as venues and venue categories.We cluster our locations based on their characters and explore each cluster after our kmeans methodology. This appoarch will help us to generate the whole picture of the business existed in Toronto place and help us to decide our ultimate business location and type.

# # PROCESSING

# In[3]:


# This Python 3 environment comes with many helpful analytics libraries installed


# In[4]:


# please see the processing in the part1 for week 5


# In[ ]:




