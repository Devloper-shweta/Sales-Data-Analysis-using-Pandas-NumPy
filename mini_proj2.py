import pandas as pd
import numpy as np

#load the data
df=pd.read_csv('sales_data.csv')
print(df)

#Display first 5 rows
print("First 5 rows of the data:")
print(df.head(5))

# check the data types 
print("Data types of each column:")
print(df.info())

# check for missing values
print("Missing values in each column:")
print(df.isnull().sum())

#Fill missing values
print("Filling missing values in 'Delivery_Days' column with mean value.")
df['Delivery_Days'].fillna(df["Delivery_Days"].mean())
print(df)

#Fill missing Discount with 0
print("Filling missing values in 'Discount' column with 0.")
df['Discount'].fillna(0)
print(df)

#Convert Order_Date to datetime
print("Converting 'Order_Date' column to datetime format.")
df['Order_Date'] = pd.to_datetime(df['Order_Date'])
print(df)

#Remove duplicate rows
print("Removing duplicate rows from the data.")
df.drop_duplicates(inplace=True)
print(df)

#Rename columns (e.g., Price → Product_Price)
print("Renaming 'Price' column to 'Product_Price'.")
df.rename(columns={'Price': 'Product_Price'}, inplace=True)
print(df)

#Calculate total sales = Price × Quantity
print("Calculating total sales for each order.")
df['Total_Sales'] = df['Product_Price'] * df['Quantity']
print(df)   

#Find total revenue
print("Calculating total revenue from all sales.")
total_revenue = df['Total_Sales'].sum()
print("Total Revenue: ", total_revenue)

#Find average order value
print("Calculating average order value.")
average_order_value = df['Total_Sales'].mean()
print("Average Order Value: ", average_order_value)

#Find highest selling product
print("Finding the highest selling product based on total sales.")
highest_selling_product = df.groupby('Product')['Total_Sales'].sum().idxmax()
print("Highest Selling Product: ", highest_selling_product) 

#Find total sales by region
print("Calculating total sales by region.")
sales_by_region = df.groupby('Region')['Total_Sales'].sum()
print("Total Sales by Region: ")
print(sales_by_region)

#Find total sales by category
print("Calculating total sales by category.")
sales_by_category = df.groupby('Category')['Total_Sales'].sum()
print("Total Sales by Category: ")

#Find customer who spent the most
print("Finding the customer who spent the most.")
top_customer = df.groupby('Customer_Name')['Total_Sales'].sum().idxmax()
print("Top Customer: ", top_customer)

#Convert Price column to NumPy array
print("Converting 'Product_Price' column to NumPy array.")
price_array = df['Product_Price'].to_numpy()
print("Price Array: ", price_array)

#Calculate mean, median, std deviation of Price
print("Calculating mean, median, and standard deviation of 'Product_Price'.")
mean_price = df['Product_Price'].mean()
median_price = df['Product_Price'].median()
std_price = df['Product_Price'].std()
print("Mean Price: ", mean_price)
print("Median Price: ", median_price)
print("Standard Deviation of Price: ", std_price)

#Normalize Price values
print("Normalizing 'Product_Price' values using Min-Max scaling.")
df['Normalized_Price'] = (df['Product_Price'] - df['Product_Price'].min()) / (df['Product_Price'].max() - df['Product_Price'].min())
print(df)   

#Find max and min price using NumPy
print("Finding maximum and minimum price using NumPy.")
max_price = np.max(price_array)
min_price = np.min(price_array)
print("Maximum Price: ", max_price)
print("Minimum Price: ", min_price)

#Apply discount using NumPy formula
print("Applying discount to 'Product_Price' using NumPy formula.")
df['Discounted_Price'] = df['Product_Price'] * (1 - df['Discount'])
print(df)   

#Create new column: Final Price after discount
print("Creating new column 'Final_Price' after applying discount.")
df['Final_Price'] = df['Product_Price'] - df['Discounted_Price']
print(df)   

#Find top 3 customers by revenue
print("Finding top 3 customers by revenue.")
top_customers = df.groupby('Customer_Name')['Total_Sales'].sum().nlargest(  3)
print("Top 3 Customers by Revenue: ", top_customers)   

#Group by Region and Category
print("Grouping data by 'Region' and 'Category' to find total sales.")
sales_by_region_category = df.groupby(['Region', 'Category'])['Total_Sales'].sum()
print("Total Sales by Region and Category: ")           
print(sales_by_region_category)

#Find monthly sales trend
print("Finding monthly sales trend.")
df['Month'] = df['Order_Date'].dt.to_period('M')
monthly_sales_trend = df.groupby('Month')['Total_Sales'].sum()
print("Monthly Sales Trend: ")
print(monthly_sales_trend)
    
#Sort data by revenue
print("Sorting data by 'Total_Sales' in descending order.")
sorted_data = df.sort_values(by='Total_Sales', ascending=False)
print("Data sorted by Total Sales: ")
print(sorted_data)

#Filter orders with sales > 50000
print("Filtering orders with 'Total_Sales' greater than 50000.")
high_value_orders = df[df['Total_Sales'] > 50000]
print("High Value Orders: ")
print(high_value_orders)    

#Find correlation between Price & Quantity
print("Finding correlation between 'Product_Price' and 'Quantity'.")
correlation = df['Product_Price'].corr(df['Quantity'])
print("Correlation between Price and Quantity: ", correlation)

#Create pivot table (Region vs Category)
print("Creating pivot table for 'Region' vs 'Category' with total sales.")
pivot_table = df.pivot_table(values='Total_Sales', index='Region', columns='Category', aggfunc='sum')
print("Pivot Table (Region vs Category): ")
print(pivot_table)

