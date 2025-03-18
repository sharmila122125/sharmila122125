import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
try:
    customers_df = pd.read_csv('C:/Users/DELL/Desktop/Guvi/first ass/zomotadatainsights/customers.csv')
    restaurants_df = pd.read_csv('C:/Users/DELL/Desktop/Guvi/first ass/zomotadatainsights/restaurants.csv')
    orders_df = pd.read_csv('C:/Users/DELL/Desktop/Guvi/first ass/zomotadatainsights/orders_table.csv')
    deliveries_df = pd.read_csv('C:/Users/DELL/Desktop/Guvi/first ass/zomotadatainsights/deliveries_table.csv')
    delivery_persons_df = pd.read_csv('C:/Users/DELL/Desktop/Guvi/first ass/zomotadatainsights/delivery_persons.csv')
    justifications_df = pd.read_csv('C:/Users/DELL/Desktop/Guvi/first ass/zomotadatainsights/justifications.csv')
except FileNotFoundError as e:
    st.error(f"File not found: {e}. Please check the file paths.")
except pd.errors.EmptyDataError:
    st.error("Some files are empty. Please provide valid datasets.")
except Exception as e:
    st.error(f"An error occurred: {e}")

# Streamlit application layout
st.title("Zomato Data Insights")

# Sidebar for navigation
option = st.sidebar.selectbox(
    'Select a dataset',
    ('Customers', 'Restaurants', 'Orders', 'Deliveries', 'Delivery Persons', 'Justifications')
)

# Display selected data
if option == 'Customers':
    st.write(customers_df)
elif option == 'Restaurants':
    st.write(restaurants_df)
elif option == 'Orders':
    st.write(orders_df)
elif option == 'Deliveries':
    st.write(deliveries_df)
elif option == 'Delivery Persons':
    st.write(delivery_persons_df)
elif option == 'Justifications':
    st.write(justifications_df)

# Customer Table Analysis
st.title("Customer Table Analysis")
st.subheader("Customers Table")
st.write(customers_df)

# 1. Calculate and display unique customers
unique_customers = customers_df['customer_id'].nunique()
st.subheader("Total Number of Unique Customers")
st.write(unique_customers)

# 2. Average number of orders by premium status
if 'is_premium' in customers_df.columns and 'total_orders' in customers_df.columns:
    avg_orders_by_premium = customers_df.groupby('is_premium')['total_orders'].mean()
    st.subheader("Average Number of Orders by Premium Status")
    st.write(avg_orders_by_premium)
else:
    st.error("Required columns ('is_premium', 'total_orders') not found in the dataset.")

# 3. Most preferred cuisine
if 'preferred_cuisine' in customers_df.columns:
    preferred_cuisine_counts = customers_df['preferred_cuisine'].value_counts()
    st.subheader("Most Preferred Cuisine")
    st.write(f"The most preferred cuisine is: {preferred_cuisine_counts.idxmax()}")
else:
    st.error("Column 'preferred_cuisine' not found in the dataset.")

# 4. Distribution of customer ratings
if 'average_rating' in customers_df.columns:
    st.subheader("Distribution of Customer Ratings")
    fig, ax = plt.subplots()
    ax.hist(customers_df['average_rating'], bins=10, edgecolor='black')
    ax.set_title('Distribution of Customer Ratings')
    ax.set_xlabel('Average Rating')
    ax.set_ylabel('Number of Customers')
    st.pyplot(fig)
else:
    st.error("Column 'average_rating' not found in the dataset.")

# Restaurants Table Analysis
st.title("Restaurants Table Analysis")
st.subheader("Restaurants Table")
st.write(restaurants_df)

# 1. Total number of restaurants
total_restaurants = restaurants_df.shape[0]
st.subheader("Total Number of Restaurants")
st.write(total_restaurants)

# 2. Average rating by cuisine type
if 'cuisine_type' in restaurants_df.columns and 'rating' in restaurants_df.columns:
    avg_rating_by_cuisine = restaurants_df.groupby('cuisine_type')['rating'].mean().reset_index()
    st.subheader("Average Rating by Cuisine Type")
    st.write(avg_rating_by_cuisine)
else:
    st.error("Required columns ('cuisine_type', 'rating') not found in the dataset.")

# 3. Top 5 restaurants by total orders
if 'total_orders' in restaurants_df.columns:
    top_restaurants_by_orders = restaurants_df.nlargest(5, 'total_orders')[['name', 'total_orders']]
    st.subheader("Top 5 Restaurants by Total Orders")
    st.write(top_restaurants_by_orders)
else:
    st.error("Column 'total_orders' not found in the dataset.")

# 4. Restaurants with delivery time > 40 minutes
if 'average_delivery_time' in restaurants_df.columns:
    restaurants_long_delivery = restaurants_df[restaurants_df['average_delivery_time'] > 40][['name', 'average_delivery_time']]
    st.subheader("Restaurants with Delivery Time > 40 Minutes")
    st.write(restaurants_long_delivery)
else:
    st.error("Column 'average_delivery_time' not found in the dataset.")

# Orders Table Analysis
st.title("Orders Table Analysis")
st.subheader("Orders Table")
st.write(orders_df)

# 1. Total number of orders
total_orders = orders_df.shape[0]
st.subheader("Total Number of Orders")
st.write(total_orders)

# 2. Average total amount per order
if 'total_amount' in orders_df.columns:
    avg_total_amount = orders_df['total_amount'].mean()
    st.subheader("Average Total Amount per Order")
    st.write(f"₹{avg_total_amount:.2f}")
else:
    st.error("Column 'total_amount' not found in the dataset.")

# 3. Number of canceled orders
if 'status' in orders_df.columns:
    canceled_orders = orders_df[orders_df['status'] == 'Cancelled'].shape[0]
    st.subheader("Number of Canceled Orders")
    st.write(canceled_orders)
else:
    st.error("Column 'status' not found in the dataset.")

# 4. Most common payment mode
if 'payment_mode' in orders_df.columns:
    most_common_payment_mode = orders_df['payment_mode'].value_counts().idxmax()
    st.subheader("Most Common Payment Mode")
    st.write(most_common_payment_mode)
else:
    st.error("Column 'payment_mode' not found in the dataset.")

# 5. Distribution of order statuses
if 'status' in orders_df.columns:
    order_status_distribution = orders_df['status'].value_counts()
    st.subheader("Distribution of Order Statuses")
    st.write(order_status_distribution)
else:
    st.error("Column 'status' not found in the dataset.")

# Deliveries Table Analysis
st.title("Deliveries Table Analysis")
st.subheader("Deliveries Table")
st.write(deliveries_df)

# 1. Total number of deliveries
total_deliveries = deliveries_df.shape[0]
st.subheader("Total Number of Deliveries")
st.write(total_deliveries)

# 2. Average delivery time
if 'delivery_time' in deliveries_df.columns:
    avg_delivery_time = deliveries_df['delivery_time'].mean()
    st.subheader("Average Delivery Time")
    st.write(f"{avg_delivery_time:.2f} minutes")
else:
    st.error("Column 'delivery_time' not found in the dataset.")

# 3. Number of deliveries still "On the way"
if 'delivery_status' in deliveries_df.columns:
    on_the_way_deliveries = deliveries_df[deliveries_df['delivery_status'] == 'On the way'].shape[0]
    st.subheader("Number of Deliveries Still On the Way")
    st.write(on_the_way_deliveries)
else:
    st.error("Column 'delivery_status' not found in the dataset.")

# 4. Most common vehicle type
if 'vehicle_type' in deliveries_df.columns:
    most_common_vehicle = deliveries_df['vehicle_type'].value_counts().idxmax()
    st.subheader("Most Common Vehicle Type for Deliveries")
    st.write(most_common_vehicle)
else:
    st.error("Column 'vehicle_type' not found in the dataset.")

# 5. Total delivery fee for completed deliveries
if 'delivery_fee' in deliveries_df.columns and 'delivery_status' in deliveries_df.columns:
    total_delivery_fee = deliveries_df[deliveries_df['delivery_status'] == 'Delivered']['delivery_fee'].sum()
    st.subheader("Total Delivery Fee for Completed Deliveries")
    st.write(f"₹{total_delivery_fee:.2f}")
else:
    st.error("Required columns ('delivery_fee', 'delivery_status') not found in the dataset.")

# Delivery Persons Table Analysis
st.title("Delivery Persons Table Analysis")
st.subheader("Delivery Persons Table")
st.write(delivery_persons_df)

# 1. Total number of delivery persons
total_delivery_persons = delivery_persons_df.shape[0]
st.subheader("Total Number of Delivery Persons")
st.write(total_delivery_persons)

# 2. Average number of deliveries per delivery person
if 'total_deliveries' in delivery_persons_df.columns:
    avg_deliveries = delivery_persons_df['total_deliveries'].mean()
    st.subheader("Average Number of Deliveries per Delivery Person")
    st.write(f"{avg_deliveries:.2f}")
else:
    st.error("Column 'total_deliveries' not found in the dataset.")

# 3. Most common vehicle type
if 'vehicle_type' in delivery_persons_df.columns:
    most_common_vehicle = delivery_persons_df['vehicle_type'].value_counts().idxmax()
    st.subheader("Most Common Vehicle Type")
    st.write(most_common_vehicle)
else:
    st.error("Column 'vehicle_type' not found in the dataset.")

# 4. Delivery person with the highest average rating
if 'average_rating' in delivery_persons_df.columns and 'name' in delivery_persons_df.columns:
    highest_rated_delivery_person = delivery_persons_df.loc[delivery_persons_df['average_rating'].idxmax(), 'name']
    st.subheader("Delivery Person with the Highest Average Rating")
    st.write(highest_rated_delivery_person)
else:
    st.error("Required columns ('average_rating', 'name') not found in the dataset.")

# 5. Number of delivery persons with more than 400 deliveries
if 'total_deliveries' in delivery_persons_df.columns:
    high_delivery_persons = delivery_persons_df[delivery_persons_df['total_deliveries'] > 400].shape[0]
    st.subheader("Number of Delivery Persons with More Than 400 Deliveries")
    st.write(high_delivery_persons)
else:
    st.error("Column 'total_deliveries' not found in the dataset.")

# Justifications  Analysis
st.title("Justifications columns")
st.subheader("Justifications columns")
st.write(justifications_df)

# 1. Total number of justifications
total_justifications = justifications_df.shape[0]
st.subheader("Total Number of Justifications")
st.write(total_justifications)

# 2. Unique column names for which justifications are provided
if 'column_name' in justifications_df.columns:
    unique_columns = justifications_df['column_name'].unique()
    st.subheader("Unique Column Names with Justifications")
    st.write(unique_columns)
else:
    st.error("Column 'column_name' not found in the dataset.")

# 3. Most common column name for justifications
if 'column_name' in justifications_df.columns:
    most_common_column = justifications_df['column_name'].value_counts().idxmax()
    st.subheader("Most Common Column Name for Justifications")
    st.write(most_common_column)
else:
    st.error("Column 'column_name' not found in the dataset.")