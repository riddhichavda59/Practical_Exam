import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class RetailAnalyzer:
    def __init__(self):
        self.data = None

    # 1. Load CSV data
    def load_data(self, file_path):
        try:
            self.data = pd.read_csv(file_path)
            self.data["Date"] = pd.to_datetime(self.data["Date"], errors="coerce")
            print("\nData loaded successfully!")
            print(self.data.head()) # Poora data print karne ke bajaye head() dekhna behtar hai
        except FileNotFoundError:
            print("CSV file not found! Kripya sahi path dalein.")

    # 2. Calculate sales metrics
    def calculate_metrics(self):
        if self.data is None or self.data.empty:
            print("Please load data first.")
            return
        
        sales = self.data["Total Sales"].to_numpy()
        quantity = self.data["Quantity Sold"].to_numpy()
        
        total_sales = np.sum(sales)
        average_sales = np.mean(sales)
        total_quantity = np.sum(quantity)
        
        print("\n--- Sales Summary ---")
        print("Total Sales:", total_sales)
        print("Average Sales:", round(average_sales, 2))
        print("Total Quantity Sold:", total_quantity)
        
        print("\nSales by Product:")
        print(self.data.groupby("Product")["Total Sales"].sum())
        
        print("\nTop Selling Product:")
        max_idx = self.data["Quantity Sold"].idxmax()
        print(self.data.loc[max_idx, "Product"])

    # 3. Filter sales data (condition parameter hata diya kyunki jarurat nahi thi)
    def filter_data(self):
        if self.data is None or self.data.empty:
            print("Please load data first.")
            return
            
        print("\n1. Filter by Category")
        print("2. Filter by Date Range")
        choice = input("Enter Choice: ")
        
        result = pd.DataFrame() # Khali dataframe initialize kiya safely
        
        if choice == "1":
            categories = self.data["Category"].unique()
            print("Available Categories:", categories)
            category_input = input("Enter Category: ")
            # Yahan spelling thik ki hai (Category aur category_input)
            result = self.data[self.data["Category"].str.lower() == category_input.lower()]
            
        elif choice == "2":
            start = pd.to_datetime(input("Enter start date (YYYY-MM-DD): "))
            end = pd.to_datetime(input("Enter end date (YYYY-MM-DD): "))
            result = self.data[(self.data["Date"] >= start) & (self.data["Date"] <= end)]
            
        else:
            print("Invalid choice!")
            return
            
        print("\nFiltered Data:")
        print(result)
        
        if len(result) == 0:
            print("No records found.")
        else:
            print("Filtered Total Sales:", result["Total Sales"].sum())

    # 4. Display summary and charts
    def display_summary(self):
        if self.data is None or self.data.empty:
            print("Please load data first.")
            return
            
        print("\n--- Data Summary ---")
        print(self.data.describe())
        print("\nMissing Values:")
        print(self.data.isnull().sum())
        
        # Bar chart fix: Data pass kiya
        category_sales = self.data.groupby("Category")["Total Sales"].sum()
        plt.figure(figsize=(10,5))
        plt.bar(category_sales.index, category_sales.values, color="green")
        plt.title("Sales by Category")
        plt.xlabel("Category")
        plt.ylabel("Total Sales")
        plt.show()
        
        # Line chart fix: Data pass kiya
        daily_sales = self.data.groupby("Date")["Total Sales"].sum()
        plt.figure(figsize=(10,5))
        plt.plot(daily_sales.index, daily_sales.values, marker="o", color="orange")
        plt.title("Daily Sales Trend")
        plt.xlabel("Date")
        plt.ylabel("Total Sales")
        plt.show()
        
        # Heatmap fix: Numeric columns check karein
        plt.figure(figsize=(6,4))
        numeric_data = self.data[["Price", "Quantity Sold", "Total Sales"]]
        sns.heatmap(numeric_data.corr(), annot=True, cmap="coolwarm")
        plt.title("Sales Data Heatmap")
        plt.tight_layout()
        plt.show()

# Main program
analyzer = RetailAnalyzer()
while True:
    print("\n===== RETAIL SALES DATA ANALYZER =====")
    print("1. Load Data")
    print("2. Calculate Sales Metrics")
    print("3. Filter Data")
    print("4. Display Summary and Charts")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    if choice == "1":
        analyzer.load_data("retail_sales.csv")
    elif choice == "2":
        analyzer.calculate_metrics()
    elif choice == "3":
        analyzer.filter_data() # argument hata diya
    elif choice == "4":
        analyzer.display_summary()
    elif choice == "5":
        print("Thank you for using Retail Sales Analyzer!")
        break
    else:
        print("Invalid choice! Try again.")
