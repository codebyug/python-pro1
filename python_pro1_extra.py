# 6. Availability and Reviews
# What is the average availability (days per year) of listings? Are there patterns in high or low availability listings?
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
# Calculate average availability
avg_availability = df['availability_365'].mean()
print("Average Availability (Days per Year):", avg_availability)

# Optional: Plot the distribution of availability
sns.histplot(df['availability_365'], bins=50, color='skyblue')
plt.title("Distribution of Availability (Days per Year)")
plt.xlabel("Days Available per Year")
plt.ylabel("Number of Listings")
plt.savefig('hist_plot(b).png')
plt.show()

# How many reviews per month do listings generally receive? Which neighborhoods or room types tend to have higher review rates?
# Average reviews per month
avg_reviews_per_month = df['reviews_per_month'].mean()
print("Average Reviews per Month:", avg_reviews_per_month)

# Optional: Visualize average reviews per month by neighborhood and room type
sns.barplot(data=df, x='neighbourhood_group', y='reviews_per_month', hue='room_type', estimator='mean')
plt.title("Average Reviews per Month by Neighborhood and Room Type")
plt.xlabel("neighborhood_group")
plt.ylabel("Average Reviews per Month")
plt.xticks(rotation=45)
plt.savefig('bar_plot(a).png')
plt.show()

# # What is the distribution of the number of reviews? Do certain types of listings receive more reviews than others?

# Plot distribution of the number of reviews
sns.histplot(df['number_of_reviews'], bins=50, kde=True, color='green')
plt.title("Distribution of Number of Reviews")
plt.xlabel("Number of Reviews")
plt.ylabel("Frequency")
plt.savefig('hist_plot2.png')
plt.show()

# Optional: Compare number of reviews by room type
sns.boxplot(data=df, x='room_type', y='number_of_reviews',hue='room_type',palette='Set2')
plt.title("Number of Reviews by Room Type")
plt.xlabel("Room Type")
plt.ylabel("Number of Reviews")
plt.ylim(0,500)
plt.savefig('box_plot3.png')
plt.show()

# 7. Relationships Between Features
# Is there a correlation between price and the number of reviews? Does high price impact the number of reviews?

# Scatter plot to observe price vs. number of reviews
sns.scatterplot(data=df, x='price', y='number_of_reviews', hue='room_type', alpha=0.6)
plt.title("Price vs. Number of Reviews")
plt.xlabel("Price")
plt.ylabel("Number of Reviews")
plt.savefig('scatter_plot3.png')
plt.show()

# Correlation calculation
correlation_price_reviews = df['price'].corr(df['number_of_reviews'])
print("Correlation between Price and Number of Reviews:", correlation_price_reviews)

# Is there a relationship between availability and price? Are highly available listings generally more or less expensive?
# Scatter plot to visualize availability vs. price
sns.scatterplot(data=df, x='availability_365', y='price', hue='room_type', alpha=0.6)
plt.title("Availability vs. Price")
plt.xlabel("Days Available per Year")
plt.ylabel("Price")
plt.savefig('scatter_plot4.png')
plt.show()

# Correlation calculation
correlation_availability_price = df['availability_365'].corr(df['price'])
print("Correlation between Availability and Price:", correlation_availability_price)

# How does the number of bedrooms/beds/baths relate to price?
# Pair plot to see relationships between number of bedrooms, beds, baths, and price
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Convert relevant columns to numeric, setting errors='coerce' to handle any non-numeric entries
df['bedrooms'] = pd.to_numeric(df['bedrooms'], errors='coerce')
df['beds'] = pd.to_numeric(df['beds'], errors='coerce')
df['baths'] = pd.to_numeric(df['baths'], errors='coerce')
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# Drop rows with NaN values in the specified columns to avoid issues in plotting
df = df.dropna(subset=['bedrooms', 'beds', 'baths', 'price'])

# Create pair plot
sns.pairplot(df, vars=['bedrooms', 'beds', 'baths', 'price'], kind='reg')
plt.suptitle("Relationships between Bedrooms, Beds, Bathrooms, and Price", y=1.02)
plt.savefig('pair_plot2.png')
plt.show()



# Are there any patterns or trends in room type, minimum nights, or availability based on host activity or rating?
# Box plot to compare minimum nights by room type and host activity level
sns.boxplot(data=df, x='room_type', y='minimum_nights', hue='room_type')
plt.yticks(range(0, 1500, 50)) 
plt.title("Minimum Nights Requirement by Room Type and Host Activity")
plt.xlabel("Room Type")
plt.ylabel("Minimum Nights")
plt.savefig('boxy_plot.png')
plt.show()



