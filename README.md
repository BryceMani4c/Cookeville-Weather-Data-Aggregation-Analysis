![Shell Script](https://img.shields.io/badge/Shell_Script-121011?logo=gnu-bash&logoColor=white)  
![C++](https://img.shields.io/badge/C++-00599C?logo=cplusplus&logoColor=white)  
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)  
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?logo=githubactions&logoColor=white)  

# 🌦️ Weather Data Aggregation & Analysis  

> A multi-language project for **aggregating, formatting, and visualizing weather data** using Shell, C++, and Python.  

---

## 📙 Table of Contents  
- [About](#-about)  
- [Usage](#usage)  
- [Deliverables](#deliverables)  
- [Learn More](#-learn-more)  

---

## 📌 About  

This project was completed as the **Spring 2025 Midterm Exam**. It demonstrates the process of **data aggregation, formatting, and visualization** with an integrated workflow:  

- A **Shell script** concatenates raw weather reports.  
- A **C++ program** converts the aggregated file into a CSV.  
- A **Driver script** automates compilation, conversion, and visualization.  
- A **Python script** generates plots for temperature, precipitation, and wind speed.  
- A **GitHub Actions workflow** ensures the CSV formatter compiles on push.  

---

## 🛠️ Usage  

1. Run the aggregation script: `./aggregate.sh`  
2. Compile & run the CSV formatter: `g++ formatter.cpp -o formatter && ./formatter aggregated_data.txt weather_data.csv`  
3. Execute the driver script: `./driver.sh`  
4. Run the visualization: `python3 weather_visualizations.py weather_data.csv`  

Results are saved in the `visualizations/` folder.  

---

## 🗒️ Deliverables  

- **Shell Script** → aggregates daily reports into one file.  
- **C++ Program** → formats data into `weather_data.csv`.  
- **Driver Script** → automates the entire workflow.  
- **Python Visualizations** → outputs plots from CSV.  
- **GitHub Actions Workflow** → validates compilation automatically.  

---

## 📬 Learn More  

For additional details or collaboration opportunities:  
- Assignment Link: [GitHub Classroom](https://classroom.github.com/a/Mmoke3L8)  
- Portfolio: [brycemani4c.github.io](https://brycemani4c.github.io)  
- Email: [Bryson.A.Bargas@gmail.com](mailto:Bryson.A.Bargas@gmail.com)  
