import cImage
import os
import pandas as pd

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

letterData = []

for letter in letters:
	path = "training/lower/" + letter + "/"
	dirLen = len(os.listdir(path))
	for i in range(dirLen):
		newPath = path + str(i) + ".gif"
		img = cImage.FileImage(newPath)
		data = []
		for row in range(img.getHeight()):
			for col in range(img.getWidth()):
				pixel = img.getPixel(row, col)
				avg = (pixel.getRed() +  pixel.getGreen() + pixel.getBlue()) // 3
				data.append(avg)
		data.append(letter.lower())
		letterData.append(data)


for letter in letters:
	path = "training/upper/" + letter + "/"
	dirLen = len(os.listdir(path))
	for i in range(dirLen):
		newPath = path + str(i) + ".gif"
		img = cImage.FileImage(newPath)
		data = []
		for row in range(img.getHeight()):
			for col in range(img.getWidth()):
				pixel = img.getPixel(row, col)
				avg = (pixel.getRed() +  pixel.getGreen() + pixel.getBlue()) // 3
				data.append(avg)
		data.append(letter)
		letterData.append(data)


ld = pd.DataFrame(letterData)
ld.to_csv('letterData.csv', index=False, header=False)