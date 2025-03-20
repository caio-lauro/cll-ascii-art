#ifndef READ_HEADER
#define READ_HEADER

#include "bmp.h"

void readHeaders(FILE *fin, BITMAPFILEHEADER *header, BITMAPINFOHEADER *info);
void readPixels(FILE *fin, RGBTRIPLE **image, int height, int width);

#endif