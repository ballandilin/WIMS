import os
import pathlib
import glob

dir = input("Entrez le nom du dossier : ")

for dic in glob.glob(dir  + "/*/"):
    index = 0
    for path in pathlib.Path(dic).iterdir():

        if path.is_file():

            old_name = path.stem

            old_extension = path.suffix

            directory = path.parent

            new_name = dic + str(index) + ".jpg"

            index+=1
            try:
                path.rename(pathlib.Path(directory, new_name))
            except Exception as e:
                print(e)
