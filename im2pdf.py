from PIL import Image
import glob

x = []

i1 = Image.open(glob.glob('*.jpg')[0])

for i in glob.glob('*.jpg')[1:]:
	print(i)
	x.append(Image.open(i))

i1.save('x.pdf',save_all=True, append_images=x)