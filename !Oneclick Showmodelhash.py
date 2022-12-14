#etherealxx
import os as os
import sys
import platform  # add import statement for the platform module

cdir = os.getcwd()  # get the current working directory

def model_hash(filename):
    try:
        with open(filename, "rb") as file:
            import hashlib as hashlib
            m = hashlib.sha256()
            file.seek(0x100000)
            m.update(file.read(0x10000))
            thehash = m.hexdigest()[0:8]
            nameoffile = os.path.basename(filename)
            print(thehash, "|", nameoffile)
    except FileNotFoundError:
        return 'NOFILE'

print("  Hash   | Model Name")
print("----------------------")

# search for all files with .ckpt or .safetensors extensions in the current working directory and subdirectories
for root, dirs, files in os.walk(cdir):
    for file in files:
        if file.endswith('.ckpt') or file.endswith('.safetensors'):
            # use the os.path.join() function to join the directory path and the file name
            filenamex = os.path.join(root, file)
            model_hash(filenamex)

print("----------------------")
print("Writing file...")

og_stdout = sys.stdout

# redirect output to a file named "!modelhash.txt"
with open('!modelhash.txt', 'w') as f:
    sys.stdout = f 
    # search for all files with .ckpt or .safetensors extensions in the current working directory and subdirectories
    for root, dirs, files in os.walk(cdir):
        for file in files:
            if file.endswith('.ckpt') or file.endswith('.safetensors'):
                # use the os.path.join() function to join the directory path and the file name
                filenamex = os.path.join(root, file)
                model_hash(filenamex)
    sys.stdout = og_stdout

print("File !modelhash.txt written.")
print("----------------------")

# check the operating system
if platform.system() == 'Windows':
    # pause the program until the user presses any key
    os.system('pause')
else:
    # pause the program until the user presses the Enter key
    input("Press Enter to continue...")
