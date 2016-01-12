from PIL import Image
import math
import os

def file2string(fname):
    with open('books/' + fname, 'r') as myfile:
        return myfile.read().replace('\n', '')


def txt2colour_img(fname):
    input = file2string(fname)
    img_dim = math.floor(math.sqrt(len(input)/3))
    input_pos = 0;
    img = Image.new( 'RGB', (img_dim,img_dim), "black") # create a new black image
    pixels = img.load() # create the pixel map
    for i in range(img_dim):    # for every pixel:
        for j in range(img_dim):
            pixels[i,j] = (ord(input[input_pos]), ord(input[input_pos+1]), ord(input[input_pos+2])) # set the colour accordingly
            input_pos+=3
    return img


def txt2grayscale_img(fname):
    input = file2string(fname)
    img_dim = math.floor(math.sqrt(len(input)))
    img = Image.new( 'RGB', (img_dim,img_dim), "black") # create a new black image
    pixels = img.load() # create the pixel map
    for i in range(img_dim):    # for every pixel:
        for j in range(img_dim):
            val = ord(input[(img_dim*i)+j])
            pixels[i,j] = (val, val, val) # set the colour accordingly
    return img

def Text2Image(format):
    for i in os.listdir(os.getcwd()+ '/books/'):
        if i.endswith("." + format):
            img = txt2colour_img(i)
            img.save(os.getcwd()+ '/images/colour/' + i + '_colour.png', 'png')
            img = txt2grayscale_img(i)
            img.save(os.getcwd()+ '/images/grayscale/' + i + '_grayscale.png', 'png')


Text2Image('txt')