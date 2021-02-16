import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')



# TODO: Use the glob.glob() function to obtain the list of filena>>>

for py in glob.glob("*.py"):
    print(py)

# TODO: use os.path.getsize to find each file's size

path = "main.py"

size = os.path.getsize(path)
print(size)

path = "globfile.py"

size = os.path.getsize(path)
print(size)

path = "ex10_starter.py"

size = os.path.getsize(path)
print(size)



# TO
path = "C:\\Users\esout\PycharmProjects\excercise10.py"

size = os.path.getsize(path)

if path < 0:
    print(size)

# TODO: Remove the leading directory name(s) from each filename before you print it - 
# using os.path.basename()

