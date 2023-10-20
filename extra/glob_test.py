import glob

my_files = glob.glob("**", recursive=True)

print(my_files)