from getopt import getopt
from sys import argv, exit
from subprocess import run
from PIL import Image
from ascii_to_image import ascii_to_image

def main():
    try:
        opts, args = getopt(argv[1:], 'cs:', ['color', 'font-size='])
    except Exception as e:
        print(e)
        exit(1)

    useColor = False
    font_size = 10
    for opt, val in opts:
        if opt in ('-c', '--color'):
            useColor = True
        elif opt in ('-s', '--font-size'):
            font_size = val
        else:
            assert False, 'Option does not exist'

    if len(args) != 3:
        print('Usage: python3 run.py [--color] INPUT_IMAGE OUTPUT_ASCII_TEXT OUTPUT_ASCII_IMAGE')
        exit(1)

    input_image = args[0]
    output_ascii_text = args[1]
    output_ascii_image = args[2]

    img = Image.open(input_image)
    factor = 0
    print('Choose an option for image scaling.\n1. Original Size\n2. Reduce to 200px\n3. Reduce to 100px\n4. Reduce to 50px')
    match input('Option: '):
        case '1':
            factor = 0
        case '2':
            factor = round(max(img.height, img.width) / 200)
        case '3':
            factor = round(max(img.height, img.width) / 100)
        case '4':
            factor = round(max(img.height, img.width) / 50)
        case _:
            print('Unsupported option, using original size.')

    out = img.split()
    r, g, b = out[0], out[1], out[2]
    img = Image.merge('RGB', (r, g, b))
    if factor > 0:
        img = img.resize(size=(img.width // factor, img.height // factor))
    img.save('./buffer.bmp')

    cmd = ['./main']
    if useColor:
        cmd.append('-c')
    cmd.append('./buffer.bmp')

    with open(output_ascii_text, 'w') as fp:
        run(cmd, stdout=fp)
    
    ascii_to_image(output_ascii_text, output_ascii_image, font_size, useColor)
    run(['rm', './buffer.bmp'])


if __name__ == '__main__':
    main()