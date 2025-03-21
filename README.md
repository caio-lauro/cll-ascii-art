# Author: Caio Lauro de Lima
## Project Description
Simple project of converting BMP images into ASCII art without color and with True Color.\
Heavily inspired by CS50x's Filter https://cs50.harvard.edu/x/2024/psets/4/filter/less/ or https://cs50.harvard.edu/x/2024/psets/4/filter/more/ \
While it is inspired by CS50x's Filter, I did not use any of its original code (I didn't copy-paste), instead I used a BMP structure reference so that I could read the image correctly. I used the original code to name `bmp.h` and to include `__attribute__((__packed__))` on each struct there, as I did not know this even existed before.\
Used BMP structure reference present in http://www.ue.eti.pg.gda.pl/fpgalab/zadania.spartan3/zad_vga_struktura_pliku_bmp_en.html \
Added `ASCII_to_image.py` to create image from ASCII text, and `run.py` to create ASCII art from command line, and automatically use this ASCII art to create an image containing each character (with and without color).

## Requirements
To run this project (with `run.py`) you will need:
* Makefile (make)
* GCC (gcc)
* Python3
* PIP
* Pillow (PIL)
To install all of the above, on a linux terminal, run:
```
>   install make gcc python3 pip
>   pip install pillow
```
Note: install refer to the system's package manager.
## Usage
To use this project, run:
```
> make
> python3 run.py [--color --font-size=? --scaling-factor=?] INPUT_IMAGE OUTPUT_ASCII_TEXT OUTPUT_ASCII_IMAGE
```
The `[--color]` is an optional argument that displays ASCII characters with color, that can be used either via `-c` or `--color`. If not used, the default is to not display color. \
The `[--font-size=?]` is an optional argument that changes the font-size used in the output ASCII image, that can be used either via `-s ?` or `--font-size=?`. If not used, the default font-size is 10. \
The `[--scaling-factor=?]` is an optional argument that changes the scaling-factor used in the input image, either mantaining the image's default size, or resizing to fix 200px, 100px or 50px (options 1, 2, 3, 4, respectively), that can be used either via `-f ?` or `--scaling-factor=?`. If not used, the user will be prompted to enter one via `input()`. \
Notice that the output image will have a big resolution.

One must run `make` to compile the project into the executable (main) and then use the python command to generate the image. \
You can directly run `main` if you have a BMP image with a good resolution (usually less than 200px) with:
```
> ./main [--color] PATH_TO_FILE
```

## Examples of ASCII Art Generated
### Original Image:
![image](https://github.com/caio-lauro/cll-ascii-art/blob/main/examples/me.jpg?raw=true)
### ASCII Image:
![image](https://github.com/caio-lauro/cll-ascii-art/blob/main/examples/me-ascii.png?raw=true)
### ASCII Colored Image:
![image](https://github.com/caio-lauro/cll-ascii-art/blob/main/examples/me-ascii-colored.png?raw=true)

## Personal choices

### Language choice for ASCII Art Generation (C)
I used C because I am already familiar with its structures and actually prefer it over other languages for reading binary files. I also recurred to this option to amplify my knowledge and understand better how the BMP file format works.

### Image format choice for ASCII Art Generation (BMP)
I used the BMP format solely for its lack of compression on most images on this format. Dealing with image compression is somewhat complicated for me still, but maybe in the future.

### Language for running the application (Python)
I used python for the sake of simplicity, although I would've liked to use C, it would be simply too hard to do everything that I wanted to do, that is, convert an image (almost any format), convert to ASCII (done in C) and then use the generated text to create an image containing each character (I don't even know how you could do it in the first place).