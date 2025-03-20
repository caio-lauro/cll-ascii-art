#include <math.h>
#include <stdio.h>

#include "../include/convert.h"

#define brightnessArrayLength 13

int getBrightnessIndex(RGBTRIPLE pixel) {
    int maxRGBvalue = pixel.rgbBlue;
    if (pixel.rgbGreen > maxRGBvalue)
        maxRGBvalue = pixel.rgbGreen;
    maxRGBvalue = maxRGBvalue > pixel.rgbRed ? maxRGBvalue : pixel.rgbRed;

    int index = round(round((float) 10 * maxRGBvalue / 255) * (brightnessArrayLength-1) / 10);

    return index;
}

void asciiConvert(RGBTRIPLE **image, char **asciiMatrice, int height, int width) {
    char brightnessArray[] = {' ', '.', ',', '-', '~', ':', ';', '=', '!', '*', '#', '$', '@'};

    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++) {
            int index = getBrightnessIndex(image[i][j]);
            if (index < 0 || index >= brightnessArrayLength)
                printf("%i %i %i %i\n", index, image[i][j].rgbBlue, image[i][j].rgbRed, image[i][j].rgbGreen);
            asciiMatrice[i][j] = brightnessArray[index%14];
        }
    }
}