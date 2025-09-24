import matplotlib.pyplot as plt
import pandas as pd
import datetime
import numpy as np
import sys
import os

# Load CSV
df = pd.read_csv(sys.argv[1])

# Ensure visualizations folder exists
os.makedirs("./visualizations", exist_ok=True)

# ---------- TEMPERATURE CHART ----------
fig, ax = plt.subplots(figsize=(16, 10), facecolor='white')

for column in df.columns[2:5]:
    plt.plot(df["Date"], df[column], label=column)

plt.ylabel("Temperature (F)")
plt.xlabel("Measurement Date")
plt.title("Temperature from 2024-12-01 to 2025-02-28")
plt.legend()

# Tick labels every 7 days
x_ticks = list(range(0, len(df["Date"]), 7))
x_labels = [df["Date"].iloc[i] for i in x_ticks if i < len(df["Date"])]
plt.xticks(x_ticks, x_labels, rotation=45)

plt.savefig("./visualizations/temperature_chart.png")

# ---------- PRECIPITATION CHART ----------
fig, ax = plt.subplots(figsize=(16, 10), facecolor='white')

precip_df = df[["Date", "Condition", "Precipitation"]].copy()

rain_mask = precip_df['Condition'].apply(lambda x: x.strip() != "Snowy")
precip_df.insert(1, 'Rain', np.where(rain_mask, precip_df['Precipitation'], 0.00))

snow_mask = precip_df['Condition'].apply(lambda x: x.strip() == "Snowy")
precip_df.insert(1, 'Snow', np.where(snow_mask, precip_df['Precipitation'], 0.00))

plt.bar(precip_df["Date"], precip_df["Rain"], label="Rain")
plt.bar(precip_df["Date"], precip_df["Snow"], label="Snow", color="lightblue")

plt.ylabel("Precipitation (in)")
plt.xlabel("Measurement Date")
plt.title("Precipitation from 2024-12-01 to present")
plt.legend()

x_ticks = list(range(0, len(df["Date"]), 7))
x_labels = [df["Date"].iloc[i] for i in x_ticks if i < len(df["Date"])]
plt.xticks(x_ticks, x_labels, rotation=45)

plt.savefig("./visualizations/precipitation_chart.png")

# ---------- WIND SPEED CHART ----------
fig, ax = plt.subplots(figsize=(16, 10), facecolor='white')

plt.plot(df["Date"], df['Wind Speed'], label='Wind Speed')

plt.ylabel("Wind Speed (mph)")
plt.xlabel("Measurement Date")
plt.title("Wind Speeds from 2024-12-01 to present")
plt.legend()

x_ticks = list(range(0, len(df["Date"]), 7))
x_labels = [df["Date"].iloc[i] for i in x_ticks if i < len(df["Date"])]
plt.xticks(x_ticks, x_labels, rotation=45)

plt.savefig("./visualizations/wind_speed_chart.png")
