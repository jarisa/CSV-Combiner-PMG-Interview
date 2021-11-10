# CSV-Combiner-PMG-Interview

As a part of the final interview with PMG, I have created a python program named csv-combiner.py. 

This python program is designed to combine all CSV files from the command line into a new CSV file.
The output of this program is a CSV file named "Combined.csv" that contains all concatenated CSV data from different files.

## The Process

Run csv-combiner.py on your terminal with the following command:

```
$ python csv-combiner.py csvfileA csvfileB > combined.py
```
After that, the process starts when the program converts these CSV files from the command line into arguments with a function. Then, the program will store the CSV data and its file name into an array. After that, the program will combine all CSV files into one CSV file with a function. In the end, the array is getting converted into a CSV file that is ready to get printed by the program.

## Pandas Library

I used a third-party library named Pandas because of its usefulness for data anaylsis and manipulation, especially for CSV files. It is more effective and efficient for me to use the Pandas library. It is important to have the Pandas library ready before you run the program.

If you do not have the Pandas library in your Python environment, I provide the steps to install the Pandas library from scratches. The whole process is for Linux OS:
1. Install the Pandas library with the following command:
```
$ sudo apt install python3-pandas
```
2. Install the documentation package with the following command:
```
$ sudo apt install python-pandas-doc
```
If you do not use Linux OS, I also provide a documentation about the installation process for other platforms. This following link lets you know about a cross platform distribution named Anaconda.
https://pandas.pydata.org/docs/getting_started/install.html
