import os # imports libraries related to operating system

def rename_files() : # defining function
	#(1) get file names from a folder
	file_list = os.listdir("/media/rohan/3814F06A14F02C8E/Study/Udacity/Python/prank/prank")
	print(file_list)
	#(2) for each file, rename filename

rename_files() # calling this function
