from PIL import Image
import os.path, sys

path1 = ".\\cropper\\n"
path2 = ".\\cropper\\d"
dirs = os.listdir(path1)

def crop():
	for item in dirs:
		fullpath1 = os.path.join(path1,item)
		fullpath2 = os.path.join(path2,item)
		newpath1 = os.path.join(".\\cropper\\n\\cropped\\",item[:-4])
		newpath2 = os.path.join(".\\cropper\\d\\cropped\\",item[:-4])
		if os.path.isfile(fullpath1):
			im1 = Image.open(fullpath1)
			im2 = Image.open(fullpath2)
			f1, e1 = os.path.splitext(fullpath1)
			f2, e2 = os.path.splitext(fullpath2)
			coord =im2.getbbox()
			imCrop1 = im1.crop(coord) #corrected
			imCrop1.save(newpath1 + 'Cropped.png', "PNG")
			imCrop2 = im2.crop(coord) #corrected
			imCrop2.save(newpath2 + 'Cropped.png', "PNG")

crop()