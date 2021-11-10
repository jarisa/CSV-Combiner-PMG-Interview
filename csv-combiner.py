# Creator: Jason Arisa
# PMG Coding Interview: CSV-Combiner
# Sources:
# https://pandas.pydata.org/docs/user_guide/io.html#csv-text-files (To understand pandas functions)
# https://www.educative.io/edpresso/how-to-combine-multiple-csv-files-in-python (To understand combining csv files)
# https://stackoverflow.com/questions/44837012/the-function-in-python-that-returns-extension-of-a-file (To understand getting file name with rfind and index)

#Import Python modules, including a third-party library from pandas
import sys
import os
import unittest
import pandas as pa

#function to retrieve and return file name
def get_filename(n):
        #look for the '/' from the file path
	index = n.rfind('/')
	#look for the file name after getting the last '/'
	filename = n[index+1:]
        #return the retrived file name to be used for the combine function
	return filename

#function to combine and return all CSV file
def combine(combined_csv, csv_file):
        #for loop to go through all CSV files, insert CSV files to the array, and concatenate them into one file
	for i in range(1, len(csv_file)):
		combined_csv_1 = pa.read_csv(csv_file[i])
		combined_csv_1['filename'] = get_filename(csv_file[i])
		combined_csv = pa.concat([combined_csv, combined_csv_1])
        #return the CSV file to the main function that has concatenated CSV files from the input 
	return combined_csv

#the main function to convert CSV files into arguments, combine them, and create a new file
def main():
        #create an array of CSV files
	csv_file = []

	#for loop to go through CSV files from the cmd/terminal and append them into arguments
	for n in range(1, len(sys.argv)):
		if os.path.isfile(sys.argv[n]):
			if(sys.argv[n][-4:] == '.csv'):
				csv_file.append(sys.argv[n])

        #read and convert CSV files to the csv_file array that already exists
	combined_csv = pa.read_csv(csv_file[0])

        #call the get_filename function with the input of csv_file array to get the file name
	combined_csv['filename'] = get_filename(csv_file[0])

        #if condition to check whether to call the combine function to merge CSV files
	#if there are more than one file from the cmd/terminal
	if len(csv_file) > 1:
		combined_csv = combine(combined_csv, csv_file)

        #set the column of the file with index
	combined_csv = combined_csv.set_index(combined_csv.columns[0])
	
        #convert csv_file array into a CSV file and save it as "combined.csv" based on the cmd/terminal
	final_csv = combined_csv.to_csv()

        #print the "combined.csv"
	print(final_csv)

#if condition to make sure the script run properly without possible errors
if __name__ == "__main__":
	main()
