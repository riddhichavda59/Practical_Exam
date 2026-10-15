# 🛍️ Retail Sales Data Analyzer

## 📌 Project Overview

The **Retail Sales Data Analyzer** is a Python-based project designed to analyze retail sales data. It helps users calculate sales statistics, filter data, identify top-selling products, and visualize sales performance through charts.

This project uses Python, NumPy, Pandas, Matplotlib, and Seaborn to perform data analysis and visualization.

## 🎯 Project Objectives

- Load retail sales data from a CSV file.
- Calculate total sales and average sales.
- Calculate the total quantity of products sold.
- Identify the top-selling product.
- Filter sales data by category and date range.
- Display a summary of the dataset.
- Visualize sales data using different charts.

## 🧰 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| NumPy | Numerical calculations |
| Pandas | Data loading and analysis |
| Matplotlib | Creating graphs and charts |
| Seaborn | Creating a correlation heatmap |
| CSV | Storing retail sales data |

## 📁 Project Structure

```text
RetailSalesAnalyzer/
│
├── retail_analyzer.py
├── retail_sales.csv
└── README.md
```

## ✨ Features

### 1. Load Sales Data
Loads retail sales information from a CSV file using Pandas.

### 2. Sales Metrics
Calculates:
- Total sales
- Average sales
- Total quantity sold
- Sales by product
- Top-selling product by quantity

### 3. Data Filtering
Allows users to filter records using:
- Product category
- Date range

### 4. Data Summary
Displays descriptive statistics and checks for missing values.

### 5. Data Visualization
Creates three visualizations:
- **Bar Chart:** Displays sales by category.
- **Line Chart:** Shows daily sales trends.
- **Heatmap:** Shows correlations between numeric columns.

## ⚙️ Installation and Setup

### Step 1: Install Python
Install Python on your computer if it is not already installed.

### Step 2: Open the Project
Open the project folder in Visual Studio Code.

### Step 3: Install Required Libraries
Open the VS Code terminal and run:

```bash
pip install pandas numpy matplotlib seaborn
```

### Step 4: Run the Project

Make sure that `retail_analyzer.py` and `retail_sales.csv` are in the same folder.

Run this command in the terminal:

```bash
python retail_analyzer.py
```

## 🖥️ Program Menu

```text
===== RETAIL SALES DATA ANALYZER =====

1. Load Data
2. Calculate Sales Metrics
3. Filter Data
4. Display Summary and Charts
5. Exit
```

### How to Use
1. Select option 1 to load the dataset.
2. Select option 2 to calculate sales statistics.
3. Select option 3 to filter the data.
4. Select option 4 to display the summary and charts.
5. Select option 5 to exit the program.

**Note:** Load the dataset before performing calculations, filtering, or visualization.

## 📊 Expected Output

The program displays:
- Total and average sales
- Total quantity sold
- Sales grouped by product
- Top-selling product
- Filtered sales records
- Dataset summary
- Bar chart, line chart, and heatmap

The results depend on the records available in the CSV file.

## 📚 Learning Outcomes

Through this project, students can learn:
- Python fundamentals and Object-Oriented Programming
- CSV file handling
- NumPy calculations
- Data analysis using Pandas
- Data filtering and grouping
- Data visualization using Matplotlib and Seaborn

## 🏁 Conclusion

The Retail Sales Data Analyzer is a useful beginner-level data analysis project. It demonstrates how Python libraries can be used to analyze sales information, calculate important statistics, filter records, and present insights through visualizations.

---

**Project Name:** Retail Sales Data Analyzer  
**Programming Language:** Python  
**Project Type:** Data Analysis and Visualization
