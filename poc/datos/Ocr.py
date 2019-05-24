try:
	from PIL import Image, ImageChops, ImageEnhance, ImageOps, ImageFilter
except ImportError:
	import Image
import pytesseract

class Ocr(object):
	def __init__(self,texto):
	 	self.texto = texto

	def getTexto(self):
	 	return  self.texto
	def setTexto(self, texto):
		self.texto = texto

	def imagenATexto(self):
		im= Image.open(self.texto)
		new_image = ImageOps.grayscale(im)
		#new_image = ImageEnhance.Contrast(new_image).enhance(4)
		new_image = new_image.filter(ImageFilter.SHARPEN)
		new_image.save("img.jpg")
		return (pytesseract.image_to_string(Image.open('img.jpg')))