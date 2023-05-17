#!/usr/bin/env python
# coding: utf-8

# Canopy’s curated movies
# The steps to perform a holistic analysis of the provided data sets and gather insights to inform future business goals are the following:
# 1.	Load or import the data sets:
# Data set A, contains the list of movie title and platforms where they are streamed.
# Data set B, contains details about the movies such as year, age, runtime, rating(IMDb), directors, genres, country, and language.
# 

# 
# 1. Load and combine the data sets:

# In[25]:


import pandas as pd
# Load data set A
df_a = pd.read_csv('C:/Users/Tofy/Desktop/Scale without Border/Module 6/Final assignment datasets/20220525_movieds.csv')
df_a.head()


# In[26]:


# Load data set B
df_b = pd.read_csv('C:/Users/Tofy/Desktop/Scale without Border/Module 6/Final assignment datasets/20220620_movie2ds.csv')
df_b.head()


# In[27]:


# Merge both data sets based on the movie name
movies_df = pd.merge(df_a, df_b, on='Title')
movies_df.head()


# 2. Handling missing data and cleaning:

# In[15]:


# Remove rows with missing data
movies_df = movies_df.dropna()


# In[16]:


# Convert the year column to integers
movies_df['Year'] = movies_df['Year'].astype(int)


# In[30]:


# Remove any duplicate rows
movies_df = movies_df.drop_duplicates()


# 3. Find the top 20 movies in each genre available in French language:

# In[18]:


# Group the data frame by genre and language
grouped = movies_df.groupby(['Genres', 'Language'])


# In[19]:


# Create a new data frame to store the top 20 movies for each genre
top_movies_df = pd.DataFrame(columns=movies_df.columns)


# In[20]:


# Loop through each group and select the top 20 movies by rating which is in our data is IMDb
for group, data in grouped:
    if 'French' in group[1]:
        top_movies = data[data['IMDb'] > 8.0].sort_values(by='IMDb', ascending=False).head(20)
        top_movies_df = pd.concat([top_movies_df, top_movies])


# In[31]:


top_movies_df


# 4. Analyse the genre distribution in French-language movies:

# In[21]:


import matplotlib.pyplot as plt


# In[22]:


# Filter the data frame to only include French-language movies
french_movies_df = movies_df[movies_df['Language'] == 'French']


# In[23]:


# Count the number of movies in each genre
genre_counts = french_movies_df['Genres'].value_counts()


# In[24]:


# Create a bar chart of the genre distribution
plt.bar(genre_counts.index, genre_counts.values)
plt.xticks(rotation=90)
plt.xlabel('Genres')
plt.ylabel('Number of Movies')
plt.title('Genre Distribution in French-Language Movies')
plt.show()


# 

# In[ ]:




