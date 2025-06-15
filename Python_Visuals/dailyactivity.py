import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Excel file
df = pd.read_excel("dailyactivity_cleaneddata.xlsx")

# Convert 'ActivityDate' to datetime format
df['ActivityDate'] = pd.to_datetime(df['ActivityDate'])

# Bar chart of steps
plt.figure(figsize=(12, 6))
sns.barplot(x='ActivityDate', y='TotalSteps', data=df)
plt.xticks(rotation=45)
plt.title("Total Steps per Day")
plt.xlabel("Date")
plt.ylabel("Total Steps")
plt.tight_layout()
plt.show()

 #Line Chart – Steps and Calories Over Time

plt.figure(figsize=(12, 6))
plt.plot(df['ActivityDate'], df['TotalSteps'], marker='o', label='Steps')
plt.plot(df['ActivityDate'], df['Calories'], marker='s', label='Calories')
plt.xticks(rotation=45)
plt.title("Steps and Calories Over Time")
plt.xlabel("Date")
plt.ylabel("Count")
plt.legend()
plt.tight_layout()
plt.show()


# Area Chart – Distance Types
import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
df = pd.read_excel("dailyactivity_cleaneddata.xlsx")

# Convert ActivityDate to datetime
df['ActivityDate'] = pd.to_datetime(df['ActivityDate'])

# Sort by date to ensure correct plotting
df = df.sort_values('ActivityDate')

# Create an area chart
plt.figure(figsize=(10, 5))
plt.fill_between(df['ActivityDate'], df['TotalSteps'], color='skyblue', alpha=0.5)
plt.plot(df['ActivityDate'], df['TotalSteps'], color='blue')  # Optional line on top

plt.title("Total Steps Over Time (Area Chart)")
plt.xlabel("Date")
plt.ylabel("TotalSteps")
plt.grid(True)
plt.tight_layout()

# Show the chart
plt.show()
