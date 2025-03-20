#ifndef DEFINITIONS_HEADER
#define DEFINITIONS_HEADER

#include <stdint.h>

#define BYTE uint8_t    // Single byte (character)
#define HALF uint16_t   // Half-word (MIPS)
#define WORD int32_t    // Word (MIPS)
#define UWORD uint32_t  // Unsigned Word (MIPS)

typedef struct {
    HALF Signature;
    UWORD FileSize;
    HALF reserved1;
    HALF reserved2;
    UWORD DataOffset;
} __attribute__((__packed__)) BITMAPFILEHEADER;

typedef struct {
    UWORD Size;
    WORD Width;
    WORD Height;
    HALF Planes;
    HALF BitCount;
    UWORD Compression;
    UWORD ImageSize;
    WORD XpixelsPerM;
    WORD YpixelsPerM;
    UWORD ColorsUsed;
    UWORD ColorsImportant;
} __attribute__((__packed__)) BITMAPINFOHEADER;

typedef struct {
    BYTE rgbBlue;
    BYTE rgbGreen;
    BYTE rgbRed;
} __attribute__((__packed__)) RGBTRIPLE;

#endif