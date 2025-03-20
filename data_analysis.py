import pandas as pd
import matplotlib.pyplot as plt

# Correct file path
file_path = "/Users/neerakumar/Downloads/GS Eng.Sco. Moderate mistakes 22-24.xlsx"

# Load dataset
df = pd.read_excel(file_path, sheet_name="Export")

# Display first few rows
print(df.head())

# Remove missing values
df.dropna(inplace=True)

# Convert StartDate to datetime format
df['StartDate'] = pd.to_datetime(df['StartDate'])

# Extract Year for trend analysis
df['Year'] = df['StartDate'].dt.year

# Display dataset structure after cleaning
print(" Data cleaned successfully!")
print(df.info())

# Display basic statistics of numerical columns
print("\n Summary Statistics:")
print(df.describe())

# Check unique mistake types
print("\n Unique Mistake Types:", df['MistakeType'].unique())

# Check mistake categories
print("\n Unique Mistake Categories:", df['MistakeTypeCategory'].unique())

# Count of mistakes per year
mistakes_per_year = df.groupby('Year')['Mistake ID'].count()
print("\n Mistakes per Year:\n", mistakes_per_year)


# Plot trend of moderate mistakes over time
plt.figure(figsize=(8,5))
plt.plot(mistakes_per_year.index, mistakes_per_year.values, marker='o', linestyle='-', color='blue')
plt.xlabel('Year')
plt.ylabel('Total Moderate Mistakes')
plt.title('Trend of Moderate Mistakes (2022-2024)')
plt.grid(True)
plt.show()

# Count of mistakes by type
mistakes_by_type = df['MistakeType'].value_counts()

# Bar plot for mistake type distribution
plt.figure(figsize=(6,4))
mistakes_by_type.plot(kind='bar', color=['lightblue', 'salmon'])
plt.xlabel('Mistake Type')
plt.ylabel('Count')
plt.title('Distribution of Mistake Types (Yellow Card vs. Corner)')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.show()

# Count of mistakes by country
mistakes_by_country = df['Country'].value_counts()

# Bar plot for mistakes by country
plt.figure(figsize=(6,4))
mistakes_by_country.plot(kind='bar', color=['lightcoral', 'lightblue'])
plt.xlabel('Country')
plt.ylabel('Count of Mistakes')
plt.title('Comparison of Mistakes: England vs. Scotland')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.show()


# Define the required variables before exporting
mistakes_per_year = df.groupby('Year')['Mistake ID'].count()
most_common_type = df['MistakeType'].value_counts().idxmax()
most_errors_country = df['Country'].value_counts().idxmax()
missed_count = (df['MistakeTypeCategory'] == 'Missed').sum() if 'Missed' in df['MistakeTypeCategory'].values else 0

# Export insights summary to CSV
insights_data = {
    "Insight": [
        "Total mistakes trend over time",
        "Most common mistake type",
        "Missed mistakes occurrence",
        "Country with highest mistakes",
        "Recommendations"
    ],
    "Details": [
        "Increasing over time" if mistakes_per_year.iloc[-1] > mistakes_per_year.iloc[0] else "Stable or decreasing",
        most_common_type,
        f"{missed_count} occurrences" if missed_count > 0 else "Not a major issue",
        most_errors_country,
        "AI-based validation, training improvements, and country-specific strategies"
    ]
}

insights_df = pd.DataFrame(insights_data)
insights_df.to_csv("Insights_Summary.csv", index=False)

print(" Insights exported successfully to 'Insights_Summary.csv'")

