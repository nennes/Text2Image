# Text2Image

## An interesting experiment

On my way home today, I had a thought. Even Extended-ASCII characters fit in 1 byte. 1 byte is also the amount of information required to describe a colour channel in an image.

What if we turned text to images? Surely, even though the distribution of values is not normal, there shouldnt be any significant patterns in th resulting image.

## Methodology

To put this to rest, I wrote a Python script that converts the text from some classical books (found [here](http://www.textfiles.com/etext/)) to both colour and grayscale images.
I used triplets of characters for the colour images and single characters for the grayscale ones.

## Oh the horror!

As visible in the produced images, some books tend to have a *significant* patterns, where other show random noise! Why? How? Is there a conspiracy? :)
Really, the Book of the Dead images are very spooky!!

## ToDo

Actually find out why this occurred! Probably a really simple reason!
