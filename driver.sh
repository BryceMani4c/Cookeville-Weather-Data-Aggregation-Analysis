#!/bin/bash

echo "Starting Driver.sh"

echo "Running Concatenater Script"
./weatherDataConcatenater.sh
echo "Sucesfully Ran Concatenater Script"

echo "Compiling CSVformatter.cpp"
g++ CSVformatter.cpp -o CSVFormatter
echo "Running CSVFormatter.exe"
./CSVFormatter

echo "Running Weather_Visualizations.py"
python3 weather_visualizations.py weather_data.csv
