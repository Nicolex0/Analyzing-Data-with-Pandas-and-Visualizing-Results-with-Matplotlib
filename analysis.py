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

    # Show data types
    print("\nData types:")
    print(df.dtypes)

    # Check for missing data
    print("\nMissing data:")
    print(df.isnull().sum())
    print("No missing data.")

except:
    print("Error loading data. Check pandas and scikit-learn.")
    exit()

# Basic Data Analysis
try:
    # Show stats (average, min, max)
    print("\nBasic stats:")
    print(df.describe())

    # Group by species and find averages
    group_means = df.groupby('species').mean()
    print("\nAverages by species:")
    print(group_means)

    # Simple findings
    print("\nFindings:")
    print("- Setosa has small petals.")
    print("- Virginica has big petals.")

except:
    print("Error in math.")
    exit()

# Making plots
try:
    # Make a 'plots' folder
    if not os.path.exists('plots'):
        os.makedirs('plots')

    # Plot 1: Line plot (average sepal length by species)
    plt.plot(group_means.index, group_means['sepal_length'], 'o-')
    plt.title('Sepal Length by Species')
    plt.xlabel('Species')
    plt.ylabel('Length (cm)')
    plt.savefig('plots/line_plot.png')
    plt.close()
    print("\nSaved line plot.")

    # Plot 2: Bar plot (average petal length by species, using Seaborn)
    sns.barplot(x='species', y='petal_length', data=df)
    plt.title('Petal Length by Species')
    plt.xlabel('Species')
    plt.ylabel('Length (cm)')
    plt.savefig('plots/bar_plot.png')
    plt.close()
    print("Saved bar plot.")

    # Plot 3: Histogram (sepal width)
    plt.hist(df['sepal_width'], bins=10)
    plt.title('Sepal Width Distribution')
    plt.xlabel('Width (cm)')
    plt.ylabel('Count')
    plt.savefig('plots/histogram.png')
    plt.close()
    print("Saved histogram.")

    # Plot 4: Scatter plot (sepal vs petal length, using Seaborn)
    sns.scatterplot(x='sepal_length', y='petal_length', hue='species', data=df)
    plt.title('Sepal vs Petal Length')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Petal Length (cm)')
    plt.savefig('plots/scatter_plot.png')
    plt.close()
    print("Saved scatter plot.")

except:
    print("Error making plots. Check matplotlib and seaborn.")
    exit()

print("\nDone! Check 'plots' folder for pictures.")