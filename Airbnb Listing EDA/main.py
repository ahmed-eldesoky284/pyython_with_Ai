import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
# Load the dataset
airbnb_data = pd.read_csv('listings.csv')  # Replace 'your_dataset.csv' with the actual filename

# Display the first few rows of the dataset
print(airbnb_data.head())

# Check for missing values
print(airbnb_data.isnull().sum())

# Remove columns with all missing values
airbnb_data = airbnb_data.dropna(axis=1, how='all')

# Handle missing values in specific columns (e.g., price, last_review, reviews_per_month)
airbnb_data['price'] = airbnb_data['price'].fillna(0)  # Replace missing price with 0
airbnb_data['last_review'] = pd.to_datetime(airbnb_data['last_review'])  # Convert 'last_review' to datetime
airbnb_data['reviews_per_month'] = airbnb_data['reviews_per_month'].fillna(0)  # Replace missing reviews_per_month with 0

# Remove outliers (if necessary)

# Ensure consistency in the data (e.g., data types, formatting)

# Display the cleaned dataset
print(airbnb_data.head())


# Visualize the distribution of prices
plt.figure(figsize=(10, 6))
sns.histplot(airbnb_data['price'], bins=30, kde=True)
plt.title('Distribution of Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

# Visualize the relationship between price and availability
plt.figure(figsize=(10, 6))
sns.scatterplot(x='price', y='availability_365', data=airbnb_data)
plt.title('Price vs Availability')
plt.xlabel('Price')
plt.ylabel('Availability (in days)')
plt.show()
# Visualize the distribution of room types
plt.figure(figsize=(8, 5))
sns.countplot(x='room_type', data=airbnb_data)
plt.title('Distribution of Room Types')
plt.xlabel('Room Type')
plt.ylabel('Count')
plt.show()
# Visualize the distribution of listings across neighborhoods
plt.figure(figsize=(12, 8))
sns.countplot(y='neighbourhood', data=airbnb_data, order=airbnb_data['neighbourhood'].value_counts().index)
plt.title('Distribution of Listings Across Neighborhoods')
plt.xlabel('Count')
plt.ylabel('Neighbourhood')
plt.show()
