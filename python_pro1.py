# Python Project EDA & Data Viz - AirBnB Listing 2024(New York)
# steps

# importing all dependenices (lib)
# loading datasets
# initial exploration
# Data cleaning
# Data Analysis
# Task 1. Importing All Dependencies

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Path to downloads folder and file
downloads_path = os.path.expanduser('~/Downloads')
file_name1 = 'datasets.csv'  # Change this to match your actual file name
file_path2 = os.path.join(downloads_path, file_name1)

# Read the CSV file into a DataFrame
new_york = pd.read_csv(file_path2)

# Display the DataFrame
print(new_york)

#TASK2:IMporting dataset
# Save DataFrame to CSV
new_york.to_csv('new_york_listings2024.csv')  # Save without index if desired

# Load the saved CSV file into a new DataFrame (optional)
df = pd.read_csv('new_york_listings2024.csv')

# Display the new DataFrame to confirm it loaded correctly
print(df)

# #Task 3:Exploring few functions
df.tail()
df.info()
df.describe()

# # # Task 4 :Data cleaning

# # # dealing with null values
null_values=df.isnull().sum()
print(null_values)
df.dropna(inplace=True)

# # # checking the no of nulls after dropping nulls
after_drop=df.isnull().sum()
print(after_drop)
# # # now we have deleted all the null values

# # # Task5:checking all the duplicate values
dupli=df.duplicated().sum()
print(dupli)
df.drop_duplicates(inplace=True)    # we have removed all the duplicates and checked
check_dupli=df.duplicated().sum()
print(check_dupli)

# # ##checking the datatype
print(df.dtypes)
df['id']=df['id']. astype(object)
df['name']=df['name'].astype(object)

print(df.dtypes)


# # # TASK 5 EDA
# 1. General Overview and Missing Values
# What is the overall structure and size of the dataset?

print(df.info())

# Are there any missing values in the dataset? If so, which columns have the most missing values?

missing_values = new_york.isnull().sum()
print(missing_values[missing_values>0])

# How should missing values be handled for each relevant column (e.g., imputation, removal)?

null_values=df.isnull().sum()
print(null_values)
df.dropna(inplace=True)

# 2. Host Analysis
# How many unique hosts are present, and who are the top hosts in terms of number of listings?

unique_hosts=df['host_name'].nunique
print(f"the no of unique hosts is:{unique_hosts}")

listings=df['host_name'].value_counts().head(10)
print(listings)

# What is the average number of listings per host? Are there any superhosts (hosts with a high number of listings and high rating)?

avg_listings=df['host_id'].value_counts().mean()
print(f"the avg listing per host is:{avg_listings:.2f}")

# What is the distribution of host listings across neighborhoods?

neighbourhood=df['neighbourhood'].value_counts().head(10)
print(neighbourhood)

# 3. Location Insights
# What are the top neighborhoods by the number of listings?
# Group by neighborhood and count listings, then sort by count

top_neighborhoods = df.groupby('neighbourhood').size().sort_values(ascending=False).head(10)
print(top_neighborhoods)

# How are listings distributed across different neighborhood groups (e.g., Manhattan, Brooklyn)?
# Group by neighborhood group and count listings
group_distribution = df['neighbourhood_group'].value_counts()
print(group_distribution)

# # Optional: Plot for visual representation
import seaborn as sns
import matplotlib.pyplot as plt

sns.countplot(data=df, x='neighbourhood_group', order=new_york['neighbourhood_group'].value_counts().index)
plt.title('Distribution of Listings by Neighborhood Group')
plt.savefig('count_plot2.png')
plt.show()

![image alt](https://github.com/codebyug/python-pro1/blob/b1620c90632430c4d21e76b9698ac8584c672630/count_plot2.png)

# What are the average prices for listings across different neighborhoods and neighborhood groups?
# Average prices by neighborhood
avg_price_neighborhood = df.groupby('neighbourhood')['price'].mean().sort_values(ascending=False)
print(avg_price_neighborhood)

# Average prices by neighborhood group
avg_price_neighborhood_group = df.groupby('neighbourhood_group')['price'].mean().sort_values(ascending=False)
print(avg_price_neighborhood_group)

# What is the geographical distribution of room types? Can this be visualied on a map?
# Scatter plot for a quick visualization

sns.scatterplot(data=df, x='longitude', y='latitude', hue='room_type', alpha=0.5)
plt.title('Geographical Distribution of Room Types')
plt.savefig('scatter_plot2.png')
plt.show()

# 4. Room Type and Price Analysis
# What are the most common room types in each neighborhood or neighborhood group?
# Most common room types by neighborhood
room_type_counts = df.groupby('neighbourhood')['room_type'].value_counts().unstack().fillna(0)
print("Room type distribution by neighborhood:")
print(room_type_counts)

# What is the distribution of room types across the entire dataset?
# Distribution of room types
room_type_distribution = df['room_type'].value_counts()
print(room_type_distribution)

# Optional: Visualize the distribution using a bar plot
import seaborn as sns
import matplotlib.pyplot as plt

sns.countplot(data=df, x='room_type', order=new_york['room_type'].value_counts().index)
plt.title('Distribution of Room Types')
plt.savefig('count_plot3.png')
plt.show()

# What is the average price for each room type? How does price vary by room type across neighborhoods?
# Average price by room type
avg_price_room_type = df.groupby('room_type')['price'].mean().sort_values(ascending=False)
print(avg_price_room_type)


# Average price by room type across neighborhoods (using barplot for better clarity)
plt.figure(figsize=(12, 6))  # Optional: Adjust figure size for better readability
sns.barplot(data=df, x='neighbourhood', y='price', estimator='mean', errorbar=None,color='Set2')
plt.xticks(rotation=90)  # Rotate x-axis labels if necessary
plt.title('Average Price by Room Type Across Neighborhoods')
plt.xlabel('Neighborhood')
plt.ylabel('Average Price')
plt.savefig('avg_price_by_room_type_across_neighborhoods_barplot.png')
plt.show()
# # Price variation by room type across neighborhoods (boxplot)
# plt.figure(figsize=(12, 6))  # Optional: Adjust figure size for readability
# sns.boxplot(data=df, x='neighbourhood', y='price', hue='room_type', showfliers=False)
# plt.xticks(rotation=90)  # Rotate x-axis labels for better visibility
# plt.title('Price Variation by Room Type Across Neighborhoods')
# plt.xlabel('Neighborhood')
# plt.ylabel('Price')
# plt.savefig('box_plot22.png')
# plt.show()


# Are there any outliers in prices? Which room types or neighborhoods have the highest/lowest prices?
# Boxplot for identifying outliers in price
# Highest and Lowest Price by Room Type
highest_price_room_type = df.groupby('room_type')['price'].max()
lowest_price_room_type = df.groupby('room_type')['price'].min()
print("Highest Prices by Room Type:\n", highest_price_room_type)
print("\nLowest Prices by Room Type:\n", lowest_price_room_type)

# Highest and Lowest Price by Neighborhood
highest_price_neighborhood = df.groupby('neighbourhood')['price'].max()
lowest_price_neighborhood = df.groupby('neighbourhood')['price'].min()
print("\nHighest Prices by Neighborhood:\n", highest_price_neighborhood)
print("\nLowest Prices by Neighborhood:\n", lowest_price_neighborhood)

sns.boxplot(data=df, x='room_type', y='price',hue='room_type',palette='Set2')
plt.title('Price Distribution and Outliers for Room Types')
plt.ylim(0, 2000) 
plt.savefig('box_plot3.png')
plt.show()

# Boxplot for identifying outliers in price by neighborhood
sns.boxplot(data=df, x='neighbourhood_group', y='price',hue='neighbourhood_group',palette='Set2')
plt.title('Price Distribution and Outliers Across Neighborhood Groups')
plt.ylim(0, 2000) 
plt.savefig('box_plotxx.png')
plt.show()

# 5. Minimum Nights Requirement
# What are the minimum nights required for each room type?
# Minimum nights required by room type (using median to avoid extreme values)
min_nights_room_type = df.groupby('room_type')['minimum_nights'].median()
print(min_nights_room_type)

# Optional: Visualize the minimum nights by room type
sns.barplot(data=df, x='room_type', y='minimum_nights', estimator='median',color='skyblue')
plt.title('Minimum Nights Required for Each Room Type')
plt.savefig('bar_plot2.png')
plt.show()


# How does the minimum nights requirement vary across different neighborhoods?
# Minimum nights required by neighborhood
min_nights_neighbourhood = df.groupby('neighbourhood')['minimum_nights'].median()
print(min_nights_neighbourhood)

# Optional: Visualize the minimum nights by neighborhood (boxplot)
plt.figure(figsize=(12,6))
sns.boxplot(data=df, x='neighbourhood', y='minimum_nights')
plt.xticks(rotation=90)
plt.ylim(0,40)
plt.title('Minimum Nights Required Across Neighborhoods')
plt.savefig('box_plot4.png')
plt.show()

# Are there any patterns in listings with unusually high minimum nights?
# Filter listings with unusually high minimum nights (e.g., greater than 30)
high_min_nights = df[df['minimum_nights'] > 30]

# Check how many listings have high minimum nights
print(high_min_nights[['name', 'room_type', 'neighbourhood', 'minimum_nights']])

# Optional: Visualize listings with high minimum nights
sns.countplot(data=high_min_nights, x='room_type')
plt.title('Distribution of Room Types with Unusually High Minimum Nights')
plt.savefig('count_plot5.png')
plt.show()

