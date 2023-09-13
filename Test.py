import os
path = "C:\\TEST"
file = os.listdir(path)
for f in file:
    fn = os.path.join(path, f)
    if os.path.isdir(fn):
        print("Direktori: ",fn)
    else:
        print("File: ",fn)