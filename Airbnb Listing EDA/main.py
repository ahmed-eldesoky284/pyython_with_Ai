import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_p = "AB_NYC_2019.csv"
airbnb_data = pd.read_csv(file_p)
airbnb_data.head()

# 1. Data Cleaning and Preparation
airbnb_data.dropna(inplace=True) 

# 2. Exploratory Data Analysis
plt.figure(figsize=(10, 6))
sns.histplot(airbnb_data['price'], bins=30, kde=True)
plt.title('Distribution of Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='neighbourhood', y='price', data=airbnb_data)
plt.title('Price Distribution by Neighbourhood')
plt.xticks(rotation=90)
plt.xlabel('Neighbourhood')
plt.ylabel('Price')
plt.show()

# 3. Statistical Analysis
try:
    # Exclude non-numeric columns from correlation analysis
    numeric_columns = airbnb_data.select_dtypes(include=[np.number])
    correlation_matrix = numeric_columns.corr()
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix')
    plt.show()
except Exception as e:
    print("Error during correlation analysis:", e)

# Improved Histogram
plt.figure(figsize=(10, 6))
sns.histplot(airbnb_data['price'], bins=100, kde=True, color='skyblue')
plt.title('Distribution of Prices')
plt.xlabel('Price ($)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Enhanced Boxplot (Violin Plot)
plt.figure(figsize=(14, 8))
sns.violinplot(x='neighbourhood_group', y='price', data=airbnb_data, palette='coolwarm')
plt.title('Price Distribution by Neighbourhood Group')
plt.xlabel('Neighbourhood Group')
plt.ylabel('Price ($)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Deeper Correlation Analysis
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()

# Richer Business Insights
print("Business Insights and Recommendations:")
print("Based on the analysis, here are some recommendations for property owners:")
print("1. Price Adjustment: Property owners should review their prices based on the analysis to ensure they are competitive and reflective of market demand.")
print("2. Geographical Targeting: Property owners can explore opportunities to adjust pricing based on location, focusing on areas where prices are higher.")
print("3. Improved Offerings: It's recommended to provide additional amenities such as high-speed internet or fitness facilities to attract more guests.")
print("4. Seasonal Pricing: Consider implementing dynamic pricing strategies to adjust prices based on seasonal demand and events.")


# 4. Business Insights and Recommendations
print("Business Insights and Recommendations:")
print("Based on the analysis, here are some recommendations for property owners:")
print("1. Price Adjustment: Property owners should review their prices based on the analysis to ensure they are competitive and reflective of market demand.")
print("2. Geographical Targeting: Property owners can explore opportunities to adjust pricing based on location, focusing on areas where prices are higher.")
print("3. Improved Offerings: It's recommended to provide additional amenities such as high-speed internet or fitness facilities to attract more guests.")
