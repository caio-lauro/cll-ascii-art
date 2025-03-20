/*
Author: Caio Lauro de Lima
Inspired by CS50x's Filter
Check out: https://cs50.harvard.edu/x/2024/psets/4/filter/less/ or https://cs50.harvard.edu/x/2024/psets/4/filter/more/
Used BMP structure reference: http://www.ue.eti.pg.gda.pl/fpgalab/zadania.spartan3/zad_vga_struktura_pliku_bmp_en.html
*/

#include <stdio.h>
#include <stdlib.h>
#include <getopt.h>

#include "../include/read.h"
#include "../include/convert.h"
#include "../include/print.h"

int main(int argc, char *argv[]) {
    if (argc == 1 || argc > 3) {
        printf("Wrong usage.\nUse ./main [--color] PATH_TO_FILE\n");
        return EXIT_FAILURE;
    }

    int useColor = 0;

    static struct option long_options[] = {
        {"color", no_argument, 0, 'c'},  // --color não recebe argumento
        {0, 0, 0, 0}  // Fim da lista
    };
    int opt = getopt_long(argc, argv, "c", long_options, NULL);
    if (opt == 'c') {
        useColor = 1;
    }

    char *filePath = argv[optind];
    FILE *fin = fopen(filePath, "r");

    BITMAPFILEHEADER *header = malloc(sizeof(BITMAPFILEHEADER));
    BITMAPINFOHEADER *info = malloc(sizeof(BITMAPINFOHEADER));
    readHeaders(fin, header, info);

    int height = info->Height;
    int width = info->Width;

    RGBTRIPLE **image = calloc(height, sizeof(RGBTRIPLE*));
    if (image == NULL) {
        printf("Could not allocate RGBTRIPLE matrice.\n");
        fclose(fin);
        return EXIT_FAILURE;
    }

    image[0] = calloc(height*width, sizeof(RGBTRIPLE));
    if (image[0] == NULL) {
        printf("Could not allocate RGBTRIPLE matrice.\n");
        fclose(fin);
        return EXIT_FAILURE;
    }

    for (int i = 1; i < height; i++) {
        image[i] = image[0]+i*width;
    }

    readPixels(fin, image, height, width);

    char **asciiMatrice = calloc(height, sizeof(char*));
    if (asciiMatrice == NULL) {
        printf("Could not allocate matrice of ascii characters.\n");
        free(image[0]);
        free(image);
        fclose(fin);
        return EXIT_FAILURE;
    }

    asciiMatrice[0] = calloc(height*width, sizeof(char));
    if (asciiMatrice[0] == NULL) {
        printf("Could not allocate matrice of ascii characters.\n");
        free(image[0]);
        free(image);
        fclose(fin);
        return EXIT_FAILURE;
    }

    for (int i = 1; i < height; i++) {
        asciiMatrice[i] = asciiMatrice[0]+i*width;
    }

    asciiConvert(image, asciiMatrice, height, width);
    printAscii(image, asciiMatrice, height, width, useColor);

    free(asciiMatrice[0]);
    free(asciiMatrice);
    free(image[0]);
    free(image);
    free(info);
    free(header);
    fclose(fin);

    return 0;
}