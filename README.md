# New York Airbnb EDA Project

## Project Overview
This project performs **Exploratory Data Analysis (EDA)** on New York Airbnb data to uncover trends and patterns in rental listings. I have used libraries like **Pandas**, **Numpy**, **Matplotlib**, and **Seaborn** for data cleaning, visualization, and analysis.
![img alt](https://github.com/codebyug/python-pro1/blob/49df6231e58f999d44682df2f85dc7e7bfa91f4f/newyork_airbnb.jpg)
---

## Objective
The goal of this project is to:
- Analyze room types, prices, and availability across different neighborhoods.
- Understand host behavior and listing patterns.
- Detect potential outliers in prices.
- Provide recommendations for guests and hosts based on insights.

---

## Dataset
The dataset contains **20,765 entries** and **22 features**, including:
- **id**: Unique identifier for each listing
- **name**: Title of the Airbnb listing
- **host_name**: Name of the host
- **neighborhood_group**: Group (borough) where the listing is located
- **latitude/longitude**: Geolocation of listings
- **price**: Nightly rental price
- **room_type**: Type of accommodation (e.g., entire home, private room)
- **reviews_per_month**: Average monthly reviews for the listing
- **availability_365**: Number of available days in the year

---

## Steps and Workflow

### 1. Data Cleaning
- **Handle missing data**: Fixed null values in `price`, `neighborhood`, and `beds` columns.
- **Fix data types**: Converted `id ` and `name` to a datatype object.
- **Remove outliers**: Capped prices > $1,000 to avoid skewed visualizations.

### 2. Exploratory Data Analysis (EDA)
#### Room Type Distribution:
- Visualized room type counts using bar plots.
- Identified **Entire home/apt** as the most common room type.

#### Neighborhood Group Insights:
- Analyzed price variations by boroughs.
- Found **Manhattan** to have the highest average prices.

#### Availability Trends:
- Used heatmaps to show correlations among `price`, `availability_365`, `number_of_reviews`, and `beds`.

#### Price Distribution:
- Plotted histograms showing most listings priced between $50-$300.

#### Host Listings:
- Analyzed hosts managing multiple listings using boxplots.

#### Review Behavior:
- Explored relationships between `number_of_reviews`, `price`, and `availability` using pair plots.

### 3. Data Visualization
- **Pairplot**: To see correlations among price, availability, and number of reviews.
- **Heatmap**: Show correlations among numerical features.
- **Histograms and Boxplots**: Detect outliers in price.
- **Bar Charts**: Display room type and neighborhood group distributions.

---

## Key Findings and Insights

### Price Trends:
- **Manhattan** has the most expensive listings, followed by **Brooklyn**.
- **Entire homes/apartments** are pricier than private or shared rooms.

### Room Type Distribution:
- **Entire homes/apartments** are the most common, but private rooms offer budget-friendly options.

### Outliers in Price:
- Listings priced at $10,000+ were identified and filtered out.

### Availability Patterns:
- High availability correlates with lower prices and more reviews, likely indicating better guest experiences.

### Host Behavior:
- Some hosts manage multiple listings, pointing to professional hosting trends.

---

## How to Run This Project
1. Clone the repository:
   ```bash
  https://github.com/codebyug/python-pro1

