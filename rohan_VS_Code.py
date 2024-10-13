#!/usr/bin/env python
# coding: utf-8

# Import Relevant Python Libraries
import streamlit as st
import pandas as pd
import plotly.express as px

# Set Streamlit app title
st.title("Imports & Exports Data Visualization Dashboard")

# Load the dataset
@st.cache_data
def load_data():
    df = pd.read_csv("Imports_Exports_Dataset.csv")
    return df

# Load dataset
df = load_data()

# Random sample fixed at 3001
sdf = df.sample(n=3001, random_state=55057)


st.dataframe(sdf.head())

# Filter option for Category
st.sidebar.header('Filter Options')
selected_category = st.sidebar.selectbox("Select Category", options=sdf['Category'].unique())

# Filter dataset based on selected category
filtered_sdf = sdf[sdf['Category'] == selected_category]

# Heatmap for correlation between Quantity, Value, and Weight
st.subheader("Correlation Between Quantity, Value, and Weight")
heatmap_data = filtered_sdf[['Quantity', 'Value', 'Weight']]
correlation_matrix = heatmap_data.corr()

heatmap = px.imshow(correlation_matrix, text_auto=True, 
                    title="Correlation Between Quantity, Value, and Weight",
                    labels={'color': 'Correlation'})

st.plotly_chart(heatmap)

# Pie chart for Exports vs Imports distribution
st.subheader("Distribution of Exports vs Imports")
pie_chart = px.pie(filtered_sdf, names='Import_Export', values='Value', 
                   title='Distribution of Exports vs Imports')
st.plotly_chart(pie_chart)

# Scatter plot for relationship between Quantity and Value
st.subheader("Relationship between Quantity and Value")
scatter_plot = px.scatter(filtered_sdf, x='Quantity', y='Value', color='Category', 
                          size='Weight', hover_data=['Country', 'Product'], 
                          title="Relationship between Quantity and Value")
st.plotly_chart(scatter_plot)

# Box plot for Trade Value by Product Category (Imports vs Exports)
st.subheader("Trade Value by Product Category (Imports vs Exports)")
box_plot = px.box(filtered_sdf, x='Category', y='Value', color='Import_Export',
                  title="Trade Value by Product Category (Imports vs Exports)",
                  points='all',  # Displays all data points
                  labels={'Value': 'Trade Value'})
st.plotly_chart(box_plot)
