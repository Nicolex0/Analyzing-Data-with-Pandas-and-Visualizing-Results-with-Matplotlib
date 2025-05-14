import pandas as pd  # For working with tables
import matplotlib.pyplot as plt  # For making plots
import seaborn as sns  # For making plots look nice
from sklearn.datasets import load_iris  # For getting the Iris dataset
import os

sns.set(style="whitegrid")

# Load and check data
try:
    # Load Iris dataset
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
    df['species'] = iris.target_names[iris.target]

    # Show first 5 rows
    print("First 5 rows:")
    print(df.head())

except:
    print("Error loading data. Check pandas and scikit-learn.")
    exit()