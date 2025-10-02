#This is the past tense me learning:
#  how to make a gif using a library form pyton
import imageio.v3 as iio

filenames = ['team-pic1.png', 'team-pic2.png']#The pictures which new gif is base on
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('team.gif', images, duration = 500, loop = 0)