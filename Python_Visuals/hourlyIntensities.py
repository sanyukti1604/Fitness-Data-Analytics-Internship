import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load and parse datetime
df = pd.read_csv("hourlyIntensities_merged.csv")
df['ActivityHour'] = pd.to_datetime(df['ActivityHour'])

# Add time components
df['Hour'] = df['ActivityHour'].dt.hour
df['Date'] = df['ActivityHour'].dt.date

# Filter one user
user_id = df['Id'].unique()[0]
user_df = df[df['Id'] == user_id]

# Line Plot:  Intensity Over Time for One User
plt.figure(figsize=(14, 6))
plt.plot(user_df['ActivityHour'], user_df['TotalIntensity'], label="Total Intensity")
plt.title(f"Total Intensity Over Time (User ID: {user_id})")
plt.xlabel("Time")
plt.ylabel("Total Intensity")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show(block = True)

 #Histogram: Distribution of Total Intensity
plt.figure(figsize=(8, 5))
sns.histplot(df['TotalIntensity'], bins=30, kde=True)
plt.title("Distribution of Total Intensity")
plt.xlabel("Total Intensity")
plt.ylabel("Frequency")
plt.show()

#Box Plot: Total Intensity by Hour of Day
plt.figure(figsize=(12, 6))
sns.boxplot(x='Hour', y='TotalIntensity', data=df)
plt.title("Total Intensity by Hour of Day")
plt.xlabel("Hour of Day")
plt.ylabel("Total Intensity")
plt.show()
