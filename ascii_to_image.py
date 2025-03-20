from sys import argv, exit
from PIL import Image, ImageDraw, ImageFont

class RGB_TRIPLE():
    def __init__(self, colors_val):
        self.red = int(colors_val[0])
        self.green = int(colors_val[1])
        self.blue = int(colors_val[2])
    def __str__(self):
        return f'({self.red},{self.green},{self.blue})'

def ascii_to_color_image(ascii_file, output_image, font_size):
    # Load font (monospace)
    font = ImageFont.truetype(font='/usr/share/fonts/abattis-cantarell-fonts/Cantarell-Regular.otf', size=font_size)

    ascii_lines:list[str] = []
    with open(ascii_file, "r") as f:
        ascii_lines = f.readlines()

    # Break each line with character and color
    ascii_chars_matrice:list[list[str]] = []
    for line in ascii_lines:
        cur:list[str] = []
        s = line.split('\033')
        for i in range(len(s)):
            char_color = s[i]
            if char_color == '[0m\n':
                ascii_chars_matrice.append(cur)
            elif char_color != '[0m' and char_color:
                cur.append(char_color[6:])

    # Associate ascii characters with respective color code
    chars_color_matrice:list[list[tuple[str, RGB_TRIPLE]]] = []
    for line in ascii_chars_matrice:
        cur:list[tuple[str, RGB_TRIPLE]] = []
        for char_color in line:
            colors, char = char_color.split('m')
            cur.append((char, RGB_TRIPLE(colors.split(';'))))
        chars_color_matrice.append(cur)
    
    total_chars_height = len(chars_color_matrice)
    total_chars_width = len(chars_color_matrice[0])

    left, top, width, height = font.getbbox('@')
    char_height = height-top
    char_width = (width-left) // 2

    img_height = char_height * total_chars_height
    img_width = char_width * total_chars_width

    img = Image.new('RGB', (img_width, img_height), 'black')
    draw = ImageDraw.Draw(img)

    for i in range(total_chars_height):
        for j in range(total_chars_width):
            char, rgb = chars_color_matrice[i][j]
            draw.text(xy=(j*char_width, i*char_height), text=char, fill=(rgb.red, rgb.green, rgb.blue))
    
    img.save(output_image)

def ascii_to_image(ascii_file, output_image, font_size=10, useColor=True):
    if useColor:
        return ascii_to_color_image(ascii_file,output_image,font_size)
    
    font = ImageFont.truetype(font='/usr/share/fonts/abattis-cantarell-fonts/Cantarell-Regular.otf', size=font_size)
    ascii_lines:list[str] = []
    with open(ascii_file, "r") as f:
        ascii_lines = f.readlines()
    
    total_chars_height = len(ascii_lines)
    total_chars_width = len(ascii_lines[0])-1

    left, top, width, height = font.getbbox('@')
    char_height = height-top
    char_width = (width-left) // 2

    img_height = char_height * total_chars_height
    img_width = char_width * total_chars_width

    img = Image.new('RGB', (img_width, img_height), 'black')
    draw = ImageDraw.Draw(img)

    for i in range(total_chars_height):
        for j in range(total_chars_width):
            char = ascii_lines[i][j]
            draw.text(xy=(j*char_width, i*char_height), text=char, fill="white")
    
    img.save(output_image)

if __name__ == '__main__':
    argc = len(argv)
    if argc != 3:
        print('Usage: python3 ascii_to_image.py INPUT_ASCII_TEXT OUTPUT_IMAGE')
        exit(1)
    ascii_file = argv[1]
    output_image = argv[2]
    ascii_to_image(ascii_file, output_image)