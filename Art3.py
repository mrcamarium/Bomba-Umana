import zipfile, os, shutil, random
from string import ascii_lowercase

def main_file_maker():
	os.mkdir("0")
	for i in range(100):
		file = open("0/%i" %i, "w")
		file.write("0" * 1024 * 1024 * 1)
		# for folders in range(1):
	file.close()

def zipping_folders():
	shutil.make_archive("0", "zip", "0/")

def copping_a_flie():
	os.mkdir("this")
	for i in range(10):
		shutil.copy("0.zip", "this/%i.zip" %i)

def random_name():
	random_names = ascii_lowercase
	this = random.choices(random_names, k=5)
	print(''.join(this))

def remove_folder(name_of_the_folder): 
	#it will remove all folder expect one which is passed
	# in the fucntion 
	folder_file = "this/"
	for file in os.listdir(folder_file):
		if file == name_of_the_folder:
			continue
		else:
			os.remove(os.path.join(folder_file, file))

def copying_zipped_folder(name_of_the_folder):
	for i in range(10):
		print("this%s%i" % (name_of_the_folder ,i))
		shutil.copy(name_of_the_folder, "this/%s%i.zip"% (name_of_the_folder, i))

copying_zipped_folder("this")