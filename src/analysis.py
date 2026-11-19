#!/usr/bin/env python
# coding: utf-8

# # Week 1 Assessment - Employee Data Analysis
# 
# ## 1. Introduction
# 
# This notebook analyzes the employee dataset using Python.
# 
# ## 2. Objectives
# 
# - Load the employee dataset.
# - Explore the dataset.
# - Calculate employee salary statistics.
# - Visualize the results.
# - Summarize the findings.

# In[ ]:





# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Pandas:", pd.__version__)
print("NumPy:", np.__version__)
print("All imports successful!")


# In[4]:


df = pd.read_csv("../data/employees.csv")

print("Dataset loaded successfully!")
df.head()


# In[5]:


print("Dataset Shape:", df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nDataset Information:")
df.info()


# In[6]:


print("Missing Values:")
print(df.isnull().sum())


# In[7]:


df.describe(include="all")


# In[8]:


print("Duplicate Rows:", df.duplicated().sum())


# In[9]:


print("First 5 Records:")
display(df.head())

print("Last 5 Records:")
display(df.tail())


# In[10]:


numeric_columns = df.select_dtypes(include="number").columns.tolist()

print("Numeric Columns:", numeric_columns)


# In[11]:


df[numeric_columns].mean()


# In[12]:


df[numeric_columns].mean()


# In[13]:


print("Minimum Values:")
print(df[numeric_columns].min())

print("\nMaximum Values:")
print(df[numeric_columns].max())


# In[14]:


get_ipython().run_line_magic('timeit', 'df[numeric_columns].mean()')


# # Week 1 Assessment - Employee Data Analysis
# 
# ## Project Overview
# 
# This project analyzes employee data using Python, Pandas, NumPy,
# and Matplotlib.
# 
# ## Project Structure
# 
# - data/ - Employee CSV dataset
# - notebooks/ - Jupyter analysis notebook
# - reports/ - Analysis reports
# - src/ - Exported Python script
# 
# ## Setup Instructions
# 
# 1. Clone the repository.
# 2. Create and activate a Python virtual environment.
# 3. Install the required packages:
# 
#    pip install pandas numpy matplotlib requests python-dotenv notebook nbconvert
# 
# 4. Open the notebook:
# 
#    jupyter notebook notebooks/analysis.ipynb
# 
# ## Summary of Findings
# 
# 1. The employee dataset was loaded and explored using Pandas.
# 2. Dataset dimensions and column names were examined.
# 3. Missing values and duplicate records were checked.
# 4. Numeric columns were analyzed using descriptive statistics.
# 5. Data distributions were visualized using Matplotlib.
