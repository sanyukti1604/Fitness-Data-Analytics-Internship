import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
df = pd.read_csv("hourlySteps_merged.csv")

# Convert ActivityHour to datetime
df['ActivityHour'] = pd.to_datetime(df['ActivityHour'])

# Extract hour from datetime
df['Hour'] = df['ActivityHour'].dt.hour

# 1. Filter data for one sample user
user_id = df['Id'].unique()[0]
df_user = df[df['Id'] == user_id]

# 2. Get top 10 records with highest steps
top10_steps = df.sort_values(by='StepTotal', ascending=False).head(10)

# 3. Average steps by hour (across all users)
avg_steps_by_hour = df.groupby('Hour')['StepTotal'].mean().reset_index()

# Set style for plots
sns.set(style="whitegrid")

# Create subplot for 3 visuals
fig, axs = plt.subplots(3, 1, figsize=(14, 16))

# 1. Line plot for steps over time for one user
sns.lineplot(data=df_user, x='ActivityHour', y='StepTotal', ax = axs[0])
axs[0].set_title(f"Hourly Step Count Over Time for User {user_id}")
axs[0].set_xlabel("Time")
axs[0].set_ylabel("Steps")
plt.tight_layout()
plt.show()

# 2. Bar plot for top 10 highest step hours
sns.barplot(data=top10_steps, x='StepTotal', y='ActivityHour', ax=axs[1], palette="viridis")
axs[1].set_title("Top 10 Active Hours (by Steps)")
axs[1].set_xlabel("Steps")
axs[1].set_ylabel("Activity Hour")
plt.tight_layout()
plt.show()

# 3. Average steps per hour across all users
sns.barplot(data=avg_steps_by_hour, x='Hour', y='StepTotal', ax=axs[2], palette="coolwarm")
axs[2].set_title("Average Steps per Hour (All Users)")
axs[2].set_xlabel("Hour of Day")
axs[2].set_ylabel("Average Steps")
plt.tight_layout()
plt.show()

# Adjust layout
plt.tight_layout()
plt.show()
