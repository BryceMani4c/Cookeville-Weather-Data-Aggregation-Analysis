<a id="readme-top"></a>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![project_license][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/BryceMani4c/weather-midterm">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Spring 2025 Midterm Exam – Weather Data Aggregation & Analysis</h3>

  <p align="center">
    Multi-language pipeline for aggregating, formatting, and visualizing Cookeville weather data.
    <br />
    <a href="https://classroom.github.com/a/Mmoke3L8"><strong>Assignment Link »</strong></a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This project demonstrates the process of **data aggregation, formatting, and visualization** using a combination of **Shell scripts, C++**, and **Python**.  

The workflow:  
- Concatenate multiple raw weather reports into a single file.  
- Convert the aggregated file into a clean CSV format using C++.  
- Automate the process with a `driver.sh` script that compiles, runs, and executes the full pipeline.  
- Visualize results with a provided Python script.  
- Verify C++ compilation automatically with **GitHub Actions**.  

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* ![Shell Script](https://img.shields.io/badge/Shell_Script-121011?logo=gnu-bash&logoColor=white)
* ![C++](https://img.shields.io/badge/C++-00599C?logo=cplusplus&logoColor=white)
* ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
* ![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?logo=githubactions&logoColor=white)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

1. Run the shell script to aggregate daily weather reports: `./aggregate.sh`  
2. Compile and run the C++ CSV formatter: `g++ formatter.cpp -o formatter && ./formatter aggregated_data.txt weather_data.csv`  
3. Execute the driver script to run the entire workflow: `./driver.sh`  
4. Run the visualization: `python3 weather_visualizations.py weather_data.csv`  

The `visualizations/` folder will be created with plots for **temperature, precipitation, and wind speed**.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed as part of coursework. No external license provided.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Bryson Bargas  
Portfolio: [brycemani4c.github.io](https://brycemani4c.github.io)  
Email: [Bryson.A.Bargas@gmail.com](mailto:Bryson.A.Bargas@gmail.com)  

Project Link: [https://github.com/BryceMani4c/weather-midterm](https://github.com/BryceMani4c/weather-midterm)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/BryceMani4c/weather-midterm.svg?style=for-the-badge  
[contributors-url]: https://github.com/BryceMani4c/weather-midterm/graphs/contributors  
[forks-shield]: https://img.shields.io/github/forks/BryceMani4c/weather-midterm.svg?style=for-the-badge  
[forks-url]: https://github.com/BryceMani4c/weather-midterm/network/members  
[stars-shield]: https://img.shields.io/github/stars/BryceMani4c/weather-midterm.svg?style=for-the-badge  
[stars-url]: https://github.com/BryceMani4c/weather-midterm/stargazers  
[issues-shield]: https://img.shields.io/github/issues/BryceMani4c/weather-midterm.svg?style=for-the-badge  
[issues-url]: https://github.com/BryceMani4c/weather-midterm/issues  
[license-shield]: https://img.shields.io/github/license/BryceMani4c/weather-midterm.svg?style=for-the-badge  
[license-url]: https://github.com/BryceMani4c/weather-midterm/blob/master/LICENSE.txt  
