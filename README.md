# Author: Caio Lauro de Lima
## Project Description
Simple project of converting BMP images into ASCII art without color and with True Color.\
Heavily inspired by CS50x's Filter https://cs50.harvard.edu/x/2024/psets/4/filter/less/ or https://cs50.harvard.edu/x/2024/psets/4/filter/more/ \
While it is inspired by CS50x's Filter, I did not use any of its original code (I didn't copy-paste), instead I used a BMP structure reference so that I could read the image correctly. I used the original code to name `bmp.h` and to include `__attribute__((__packed__))` on each struct there, as I did not know this even existed before.\
Used BMP structure reference present in http://www.ue.eti.pg.gda.pl/fpgalab/zadania.spartan3/zad_vga_struktura_pliku_bmp_en.html \
Added `ASCII_to_image.py` to create image from ASCII text, and `run.py` to create ASCII art from command line, and automatically use this ASCII art to create an image containing each character (with and without color).

## Usage
To use this project, run:
```
> make
> python3 run.py [--color] INPUT_IMAGE OUTPUT_ASCII_TEXT OUTPUT_ASCII_IMAGE
```
The `[--color]` is an optional argument that displays ASCII characters with color, that can be used either via `-c` or `--color`. If not used, the default is to not display color. \
When using `run.py`, you can choose a new "resolution" for the input image. Notice that the output image will have a big resolution.

One must run `make` to compile the project into the executable (main) and then use the python command to generate the image. \
You can directly run `main` if you have a BMP image with a good resolution (usually less than 200px) with:
```
> ./main [--color] PATH_TO_FILE
```

## Examples of ASCII Art Generated
### Original Image:
![image](./images/me.jpg)
### ASCII Image:
![image](./output/me-ascii.png)
### ASCII Colored Image:
![image](./output/me.png)

## Language choice for ASCII Art Generation
I used C because I am already familiar with its structures and actually prefer it over other languages for reading binary files. I also recurred to this option to amplify my knowledge and understand better how the BMP file format works.

## Image format choice for ASCII Art Generation (BMP)
I used the BMP format solely for its lack of compression on most images on this format. Dealing with image compression is somewhat complicated for me still, but maybe in the future.