# Author: Caio Lauro de Lima
## Project Description
Simple project of converting BMP images into ASCII art without color and with True Color.\
Heavily inspired by CS50x's Filter https://cs50.harvard.edu/x/2024/psets/4/filter/less/ or https://cs50.harvard.edu/x/2024/psets/4/filter/more/ \
While it is inspired by CS50x's Filter, I did not use any of its original code (I didn't copy-paste), instead I used a BMP structure reference so that I could read the image correctly. I used the original code to name `bmp.h` and to include `__attribute__((__packed__))` on each struct there, as I did not know this even existed before.\
Used BMP structure reference present in http://www.ue.eti.pg.gda.pl/fpgalab/zadania.spartan3/zad_vga_struktura_pliku_bmp_en.html

## Language choice
I used C because I am already familiar with its structures and actually prefer it over other languages for reading binary files. I also recurred to this option to amplify my knowledge and understand better how the BMP file format works.

## Image format choice (BMP)
I used the BMP format solely for its lack of compression on most images on this format. Dealing with image compression is somewhat complicated for me still, but maybe in the future.