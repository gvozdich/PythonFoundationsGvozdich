import sys, os, csv
import thermal_desktop as td

#This script runs through an Thermal Desktop outfile, printing the maximum temperature at each time step for a
#specific submodel

def get_input():
	#gets the file name and submodel name from the user
	try:
		file_name = sys.argv[1]
		submodel_name = sys.argv[2]
	except:
		print('You forgot to include input on the command line. Do you even know how to run this script!? ' +
			'Now you must manually enter the file name and submodel without tab...')
		file_name = input('Enter the file name: ')
		submodel_name = input('Enter the submodel name: ')	
	return file_name, submodel_name
	
def getallfiles(extension):
	#finds all files with .out extension in directory
	files = []
	for file in os.listdir():
		if file.endswith(extension):
			files.append(file)
	return files

if __name__ == '__main__':
	#Get list of all files in current directory -- make directoy an input
	list_files = getallfiles('.out')
	
	#get file name and submodel name
	file_id, submodel_id = get_input()

	#Create a td class instance
	file = td.outfile(file_id)
	
	#Read in file contents
	file.read() #
	
	#Search file for temperature data and store
	results = file.findmax(submodel_id)
		
	#Print results to a .csv file
	outfile = open('results_'+file_id[:-4]+'.csv', 'w', newline='')
	writer=csv.writer(outfile)
	writer.writerows(results)
	outfile.close()