import os
import shutil

directory = input("Path: ")

for f in os.scandir(directory):
    if f.is_file():
        fname = f.name
        split = os.path.splitext(fname)
        name = split[0]
        ext = split[1]
        print(fname)

        source = f.path
        destination = directory + "\\" + ext[1:] + "\\" + fname
        try:
            os.mkdir(directory + "\\" + ext[1:])
        except:
            pass
        finally:
            shutil.move(source, destination)