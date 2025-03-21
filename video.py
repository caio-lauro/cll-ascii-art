import subprocess
import cv2

def main():
    print("""\
    Generate ASCII Art from video file.\n
    Firstly, create a path for the project, that has the following:
        > A video file.
        > A directory called 'images', where the video frames will be stored.
        > A directory called 'text', where the ASCII text will be stored.
        > A directory called 'output', where the ASCII images will be stored.
    """)

    PATH = input('Enter path for project: ')
    VIDEO_NAME = input('Enter the video name (with format): ')
    frame_reduction = input('Enter the frame reduction (empty for default): ')

    try:
        frame_reduction = int(frame_reduction)
    except:
        print('Using default frame reduction: 5')
        frame_reduction = 5

    scaling_factor = input('Enter scaling factor (1-4, empty for default): ')
    if scaling_factor not in {'1','2','3','4'}:
        print('Using default scaling factor: 3')
        scaling_factor = '3'

    font_size = input('Enter font-size for ASCII images (empty for default): ')
    try:
        font_size = int(font_size)
    except:
        print('Using default font-size: 10')
        font_size = 10

    useColor = False
    match input('Use color in images? (y/N) '):
        case 'y'|'Y':
            useColor = True
        case 'n'|'N':
            pass
        case _:
            print('Using default: No color')

    vidcap = cv2.VideoCapture(f'{PATH}/{VIDEO_NAME}')
    ORIGINAL_FPS = vidcap.get(cv2.CAP_PROP_FPS)
    success,image = vidcap.read()
    count = 0

    frames = []
    while success:
        if count % frame_reduction == 0:
            frames.append(f'{PATH}/images/{(count // frame_reduction)}.bmp')
            try:
                cv2.imwrite(frames[-1], image)
            except:
                pass
        success,image = vidcap.read()
        count += 1

    cmd = ['python3', 'run.py', '-c', f'--font-size={font_size}', f'--scaling-factor={scaling_factor}', 'INPUT_IMG', 'OUTPUT_ASCII', 'OUTPUT_IMG']
    if not useColor:
        cmd.remove('-c')
    output = []
    for i in range(len(frames)):
        cmd[-3] = frames[i]
        cmd[-2] = f'{PATH}/text/{i}.txt'
        cmd[-1] = f'{PATH}/output/{i}.jpg'
        output.append(cmd[-1])
        subprocess.run(cmd)

    for i in range(len(output)):
        output[i] = cv2.imread(output[i])

    height, width, _ = output[0].shape
    FPS = ORIGINAL_FPS // frame_reduction

    video = cv2.VideoWriter(f'{PATH}/out.avi', cv2.VideoWriter_fourcc(*'DIVX'), FPS, (width, height))
    for i in range(len(output)):
        video.write(output[i])

    video.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()