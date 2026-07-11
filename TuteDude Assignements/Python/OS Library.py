import os 
print(os.getcwd())
path = "/home/user/documents/notes.txt"
print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.splitext(path))


folder = "reports"
file = "sales.txt"

full_path = os.path.join(folder, file)
print(os.path.basename(full_path))

folder = "reports"
file = "sales.txt"

# ---------------------------------

print(os.getcwd()) # Current working directory
os.chdir('/path/to/folder') # Change directory
print(os.listdir('.')) # List files in current dir
# Create / remove directories
os.mkdir('new_folder') # Create single directory
os.makedirs('a/b/c') # Create nested directories
os.rmdir('new_folder') # Remove empty directory
os.rename('old.txt', 'new.txt')
os.remove('file.txt')
print(os.path.exists('file.txt')) # True / False
print(os.path.getsize('data.csv')) # Size in bytes
