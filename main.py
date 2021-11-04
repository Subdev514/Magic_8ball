from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import random
#Importing modules that are needed

possible_texts = []
with open('magic_8ball_possible_answers.txt') as file:
    possible_texts = file.readlines()
# This will read the file magic_8ball_possible_answers.txt and store it in array possible_txts

text = random.choice(possible_texts)
# Getiing a random item in the array

img = Image.open("magic_8ball_template.jpg")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("FONTS/arial.ttf", 20)
draw.text((132,140),text,(225,0,0),font=font)
img.show('sample-out.jpg')
# This will baically draw the text at the middle of the image and then show it
