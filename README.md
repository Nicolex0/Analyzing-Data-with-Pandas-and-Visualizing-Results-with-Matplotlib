# Analyzing-Data-with-Pandas-and-Visualizing-Results-with-Matplotlib

This project analyzes the Iris dataset for a school assignment. It loads the data, explores it, does basic calculations, and creates four plots to visualize the data.

## What the Project Does
- **Loads Data**: Uses the Iris dataset (flower measurements: sepal length, sepal width, petal length, petal width, and species).
- **Explores Data**: Shows the first 5 rows, data types, and checks for missing values (none found).
- **Analyzes Data**: Calculates stats (like averages) and averages by species (Setosa, Versicolor, Virginica).
- **Makes Plots**: Creates 4 visualizations:
  - Line plot: Average sepal length by species.
  - Bar plot: Average petal length by species.
  - Histogram: Sepal width distribution.
  - Scatter plot: Sepal length vs- vs. petal length by species.
- **Saves Plots**: Saves plots as PNG files in the `plots` folder (line_plot.png, bar_plot.png, histogram.png, scatter_plot.png).

## Files
- `analysis.py`: The main Python script that does all the analysis and plotting.
- `plots/`: Folder with the four plot PNG files.

## How to Run
1. **Requirements**:
   - Python 3.8.13 (or compatible version).
   - Libraries: pandas, matplotlib, seaborn, scikit-learn.
   - Install them with:
     ```bash
     pip install pandas matplotlib seaborn scikit-learn
