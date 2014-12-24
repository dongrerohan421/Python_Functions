import os # imports libraries related to operating system

def rename_files() : # defining function
	#(1) get file names from a folder
	file_list = os.listdir("/media/rohan/3814F06A14F02C8E/Study/Udacity/Python/prank/prank")
	print(file_list)
	saved_path = os.getcwd() # gives current working directory
	print("Current Working Directory is "+saved_path)
	os.chdir("/media/rohan/3814F06A14F02C8E/Study/Udacity/Python/prank/prank")
	#(2) for each file, rename filename
	for file_name in file_list:
		print("Old Name - "+file_name)
		print("New Name - "+file_name.translate(None,"0123456789"))
		os.rename(file_name, file_name.translate(None, "0123456789")) # file_name.translate(): translate or delete characters from file name
	os.chdir(saved_path)

rename_files() # calling this function
