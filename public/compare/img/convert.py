from PIL import Image
import pathlib

dir = input("entrez le nom du dossier : ")

for path in pathlib.Path(dir).iterdir():

    if path.is_file():
        print(path)
        old_name = path.stem

        im = Image.open(path)
        rgb_im = im.convert('RGB')

        new_name = old_name

        try:
            rgb_im.save(new_name+'jpg')
        except Exception as e:
            print(e)
