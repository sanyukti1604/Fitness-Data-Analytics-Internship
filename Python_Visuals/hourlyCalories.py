import pandas as pd

# Load the CSV file
df = pd.read_csv("hourlyCalories_merged.csv")

# Show first few rows
print(df.head())

df['ActivityHour'] = pd.to_datetime(df['ActivityHour'])
import matplotlib.pyplot as plt
import seaborn as sns

# Optional: Filter one user to make the chart clearer
user_df = df[df['Id'] == df['Id'].unique()[0]]

# Plot Line Chart of Calories Over Time
plt.figure(figsize=(14, 6))
sns.lineplot(x='ActivityHour', y='Calories', data=user_df)
plt.title('Calories Burned Over Time (Sample User)')
plt.xlabel('Time')
plt.ylabel('Calories')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
 
 #Average Calories by Hour of Day:
df['Hour'] = df['ActivityHour'].dt.hour
avg_hourly = df.groupby('Hour')['Calories'].mean().reset_index()

plt.figure(figsize=(10, 5))
sns.barplot(x='Hour', y='Calories', data=avg_hourly)
plt.title('Average Calories Burned by Hour of Day')
plt.xlabel('Hour')
plt.ylabel('Average Calories')
plt.show()

