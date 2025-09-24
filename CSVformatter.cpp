// File Name:   CSVformatter.cpp
// Author Name: Bryson Bargas
// Date:        03/22/2025
// Purpose:     Takes a .txt file and converts it to CSV

#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <iostream>
using namespace std;
int main(){

    const char* file1 = "aggregated_data.txt";
    const char* file2 = "weather_data.csv";

    string label, date, condition;
    double high, low, avg, precip, wind, dew;

    remove(file2);
    ifstream in(file1);
    ofstream out(file2, ios::app);

    out << "Date,Condition,High Tempature,Low Tempature,Average Tempature,Precipitation,Wind Speed,Dew Point";

    while(in >> label){
        if(label == "Date:"){
            in >> date;
            out << date << ",";
            in.ignore();

            getline(in, label, ':'); 
            in >> condition;
            out << condition << ",";
            in.ignore();

            getline(in, label, ':'); 
            in >> high;
            out << high << ",";
            in.ignore();

            getline(in, label, ':'); 
            in >> low;
            out << low << ",";
            in.ignore();

            getline(in, label, ':'); 
            in >> avg;
            out << avg << ",";
            in.ignore();

            getline(in, label, ':'); 
            in >> precip;
            out << precip << ",";
            in.ignore();

            getline(in, label, ':'); 
            in >> wind;
            out << wind << ",";
            in.ignore();

            getline(in, label, ':');
            in >> dew;
            out << dew << "\n";
            in.ignore(); 
        }
    }
    cout << "Conversion complete" << endl;
    return 0;
}