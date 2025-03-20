#include <stdio.h>
#include <stdlib.h>

#include "../include/print.h"

void printAsciiImage(char **asciiMatrice, int height, int width) {
    for (int i = height-1; i > -1; i--) {
        for (int j = 0; j < width; j++) {
            for (int amount = 0; amount < 2; amount++)
                printf("%c", asciiMatrice[i][j]);
        }
        printf("\n");
    }
}

void printColoredAsciiImage(RGBTRIPLE **image, char **asciiMatrice, int height, int width) {
    for (int i = height-1; i > -1; i--) {
        for (int j = 0; j < width; j++) {
            for (int amount = 0; amount < 2; amount++)
                printf("\033[38;2;%d;%d;%dm%c\033[0m", 
                    image[i][j].rgbRed, image[i][j].rgbGreen, image[i][j].rgbBlue, asciiMatrice[i][j]);
        }
        printf("\n");
    }
}

void printAscii(RGBTRIPLE **image, char **asciiMatrice, int height, int width, int useColor) {
    if (useColor) {
        printColoredAsciiImage(image, asciiMatrice, height, width);
        return;
    }
    printAsciiImage(asciiMatrice, height, width);
}
