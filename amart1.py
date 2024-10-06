import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set Streamlit page title
st.title("Imports & Exports Data Visualization Dashboard")

# Load the dataset
df = pd.read_csv("Imports_Exports_Dataset.csv")

# Generate a sample of 3001 records
random_df = df.sample(n=3001, random_state=55053)

# Sidebar for filtering options
st.sidebar.title("Filter Options")
import_export_selection = st.sidebar.selectbox('Select Import or Export:', df['Import_Export'].unique())

# 1. Scatter plot of Quantity vs Value
st.subheader('Scatter Plot of Quantity vs Value')
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(df['Quantity'], df['Value'], color='blue', alpha=0.5)
ax.set_title('Scatter Plot of Quantity vs Value')
ax.set_xlabel('Quantity')
ax.set_ylabel('Value')
ax.grid(True)
st.pyplot(fig)

# 2. Line plot of Quantity over Date
st.subheader('Line Plot of Quantity Over Time')
if 'Date' in df.columns:
    # Convert Date column to datetime if it's not already
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    # Plot only if 'Date' and 'Quantity' columns exist
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df['Date'], df['Quantity'], color='green', linestyle='-', marker='o')
    ax.set_title('Line Plot of Quantity Over Time')
    ax.set_xlabel('Date')
    ax.set_ylabel('Quantity')
    plt.xticks(rotation=45)
    ax.grid(True)
    st.pyplot(fig)
else:
    st.write("The 'Date' column does not exist in the dataset.")

# 3. Box-Whisker plot of Quantity by Import/Export
st.subheader('Box-Whisker Plot of Quantity by Import/Export')
fig, ax = plt.subplots(figsize=(8, 6))
sns.boxplot(x='Import_Export', y='Quantity', data=df, ax=ax)
ax.set_title('Box-Whisker Plot of Quantity by Import/Export')
ax.set_xlabel('Import/Export')
ax.set_ylabel('Quantity')
st.pyplot(fig)

# 4. Histogram of the 'Value' column
st.subheader('Distribution of Transaction Values')
fig, ax = plt.subplots(figsize=(8, 6))
sns.histplot(data=df, x='Value', bins=30, kde=True, ax=ax)
ax.set_title('Distribution of Values')
st.pyplot(fig)

# 5. Pie Chart of Import vs Export
st.subheader('Proportion of Import vs Export')
import_export_counts = random_df['Import_Export'].value_counts()
fig, ax = plt.subplots(figsize=(7, 7))
ax.pie(import_export_counts, labels=import_export_counts.index, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightgreen'])
ax.set_title('Proportion of Import vs Export in Random Sample')
st.pyplot(fig)
