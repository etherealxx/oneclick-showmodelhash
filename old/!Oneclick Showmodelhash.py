#etherealxx
import os as os
import sys
from pathlib import Path

cdir = os.getcwd()

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

for filenamex in Path(cdir).rglob('*.ckpt'):
    model_hash(filenamex)

print("----------------------")
print("Writing file...")

og_stdout = sys.stdout

with open('!modelhash.txt', 'w') as f:
    sys.stdout = f #
    for filenamex in Path(cdir).rglob('*.ckpt'):
        model_hash(filenamex)
    sys.stdout = og_stdout

print("File !modelhash.txt written.")
print("----------------------")
os.system("pause")

#below are old methods, i'm still learning python :)

#import glob
#for filenamex in glob.iglob(cdir + '**/*.ckpt', recursive=True):
#     model_hash(filenamex)

#for filenamex in os.listdir(cdir):
#    filepath = os.path.join(cdir, filenamex)
#    filenamey, fileext = os.path.splitext(filenamex)
#    if fileext == '.ckpt':
#        model_hash(filepath)
