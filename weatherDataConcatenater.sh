#!/bin/bash

target="/home/bryson/Midterm/midterm-project-BryceMani4c/weather_data"
file="aggregated_data.txt"

rm "$file"

echo "Concatenating files from weather_data into WeatherData.txt"

for item in "$target"/*; do
    if [ -f "$item" ]; then
        cat "$item" >> $file
        echo >> $file
    fi
done