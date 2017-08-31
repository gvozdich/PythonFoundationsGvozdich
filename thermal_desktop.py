'''
This module imports the 'outfile' class. The 'outfile' class loads and reads through a thermal desktop
output file to find the maximum temperature associated with a speccific submodel.
'''

class outfile:
	#class attributes
	#initialize
	def __init__(self, file_name):
		self.name = file_name
		self.file = []
		
	#class methods
	def read(self):
		#This method reads in an outfile with the name: file.name, storing the file contents in self.file
		#with open(file.name, 'r') as file:
		#	self.file = file.readlines()
		file=open(self.name, 'r') 
		self.file = file.readlines()
		file.close
		
	def findmax(self, submodel_id):
		#This method sifts through the data stored in self.file and saves the maximum temperature at each timestep.
		#The method returns a n x 2 array with the timestep and temperature
		
		n_submodel = 0 #flag: if a submodel is found that matches the input, set to 1
		n_timestep = 0 #flag: while in submodel block and timestep is found, set to 1
		timedata, tempdata = [], []
		nodelist, templist = [], []
		
		for line in self.file:
			if n_submodel == 0: #Submodel matching input not found
				#Find lines declaring submodel
				if '  SUBMODEL NAME =' in line:
					line=line.strip()
					if line[16:] == submodel_id:
						n_submodel = 1
						
			else: #Submodel matching input found
				if n_timestep == 0: #Timestep in submodel card not found
					#Find lines defining the timestep
					if '         PROBLEM TIME' in line: 
						time = float(line[64:73]) #record time
						timedata.append(time)
						n_timestep = 1

				else: #Timestep in submodel card found
					#Find lines with node, temperature data
					if line[:4] == '   T':
						index = 4
						for dummy in range(0,line.count('T')):
							#Record node, temperature data if submodel matches id and time step provided
							node = int(line[index:index+8]); nodelist.append(node)
							temp = float(line[index+9:index+17]); templist.append(temp)
							index+=23
				
					#Reset flag at end of card (prevents reading erroneous information)
					elif 'PAGE' in line: 	#stop on strange return character instead?
						tempdata.append(max(templist))
						#nodes.append(max(temp))
						n_submodel = 0; n_timestep = 0
						nodelist, templist = [], []
						
		data = zip(timedata, tempdata)
		return data
		
#Module not intended to run on its own... Use for debugging?		
if __name__ == '__main__':
	pass
