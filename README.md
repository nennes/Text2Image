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

## Explanation

The non-alphanumeric characters in the scripts have very different ASCII values than the alphanumeric ones. As a result, any block of text with a lot of line breaks or special characters will produce an image that does not look like it's completely random.

## Thoughts

The images would be useful as a quick inspection tool for any large block of text, as they indicate the formatting style across the document. Another experiment would be to run a lossy algorithm on these images and then convert them back to text, although I'm sure the result wouldn't look pleasing! :)
