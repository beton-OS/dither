# dither
A small python script to dither an image.\
An adapted copy of mies47 version (https://github.com/mies47/MM-ordered_dithering).
A second script resize the picture while maintaining its ratio.

If you want ot use the avif format fist pip install the avif extension:\
`pip install pillow pillow-avif-plugin --upgrade`

Usage:\
`python diether.py file.png`

Will output `file_diethered.avif`
