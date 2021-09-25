import os, filecmp, sys, time



def main():
	print("If your will input home directory at '~':\n Program will not working\n Please input a full path to directory \t /home/username/path")

	def log_file(text):
		now = str(time.strftime("%d.%m.%Y %H-%M-%S : "))
		print(str(now) + text + "\n")
		with open(wr_file, 'a') as f:
			f.write(str(now) + text + "\n")

	def check(first_directory,diff_directory):
			dc = filecmp.dircmp(first_directory,diff_directory, ignore = 'none' , hide = 'none')
			only_first = dc.left_only
			changed_files = dc.diff_files
			deleted_files = dc.right_only
			dirs = dc.common_dirs
			for i in range(len(dirs)):
				check(first_directory+"/"+dirs[i],diff_directory+"/"+dirs[i])



			if only_first:
				for i in range(len(only_first)):
					log_file("Added: " + diff_directory + " " + str(only_first[i]))
					os.system("cp -r "+first_directory + "/" + str(only_first[i])+" "+ diff_directory)
			else:
				pass
			if changed_files:
				for i in range(len(changed_files)):
					log_file("Changed: " + diff_directory + " " + str(changed_files[i]))
					os.system("cp -r " + first_directory + "/" + str(changed_files[i]) + " " + diff_directory)
			else:
				pass
			if deleted_files:
				for i in range(len(deleted_files)):
					log_file("Deleted: " + diff_directory + " "  + deleted_files[i])
					os.system("rm -r " + diff_directory+ "/" + str(deleted_files[i]))
			else:
				pass

		



	working = True
	try:
		first_directory = input("Plese input full path to first directory:")
		diff_directory = input("Plese input full path second directory:")
		wr_file = input("Plese input full path to writed log .txt file:")

		set_interval = float(input("Input sync interval min:")) * 60
	except ValueError as e:
		print("Bad time input, Please input decemal: "+str(e))
		sys.exit()






	while working:

		try:
			check(first_directory,diff_directory)
			filecmp.clear_cache()	
			time.sleep(set_interval)
			
		except Exception as e:
			print("Bad input or dir have attr read_only:\n" + str(e))
			sys.exit()			


if __name__ == '__main__':
	main()


