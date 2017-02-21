from PIL import Image
import numpy

def image_to_pixels(filename):
	img = Image.open(filename)
	#pixels = img.load()
	print img.size
	return numpy.asarray(img, dtype='float64')/256.

pixels = image_to_pixels('everest.jpg')
print pixels.shape
