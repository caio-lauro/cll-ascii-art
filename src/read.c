#include <stdio.h>
#include <stdlib.h>
#include "../include/read.h"

#define ALIGN 4

void readHeaders(FILE *fin, BITMAPFILEHEADER *header, BITMAPINFOHEADER *info) {
    fread(header, sizeof(BITMAPFILEHEADER), 1, fin);
    fread(info, sizeof(BITMAPINFOHEADER), 1, fin);

    // Ensure 24-bit bmp uncompressed image
    if (header->Signature != 0x4d42 || header->DataOffset != 54 || 
    info->Size != 40 || info->BitCount != 24 || info->Compression != 0) {
        fclose(fin);
        printf("Unsupported file format.\n");
        exit(EXIT_FAILURE);
    }
}

void readPixels(FILE *fin, RGBTRIPLE **image, int height, int width) {
    const int OFFSET = width * sizeof(RGBTRIPLE);
    // Padding for scanlines
    const int PADDING = (ALIGN - (OFFSET % ALIGN)) % ALIGN;

    for (int i = 0; i < height; i++) {
        // Read entire row
        fread(image[i], sizeof(RGBTRIPLE), width, fin);

        // Skip padding
        fseek(fin, PADDING, SEEK_CUR);
    }
}