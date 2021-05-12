import argparse
parser = argparse.ArgumentParser()
parser.add_argument(
    "-i", "--Input",
    help="[Input] Image file with there extension example image.ppm"
    )

parser.add_argument(
    "-o", "--Output",
    help="[Output] Image file with there extension example image.png"
    )


args = parser.parse_args()


IMG = list()
WIDTH = int()
HEIGHT = int()
COLOR_RANGE = int()
if(args.Input.split('.')[1] in ("ppm","PPM")):
    with open(args.Input,"r") as input_file:
        file_lines = input_file.readlines()
        for inline in file_lines:
            if "P3" in inline:
                WIDTH,HEIGHT = inline.split()[1:]        
                WIDTH,HEIGHT = int(WIDTH),int(HEIGHT)
                file_lines.remove(inline)
            if "#" in inline:
                file_lines.remove(inline)

        for row in file_lines[1:]:
            IMG.append(tuple(map(eval,row.split())))



             
if args.Output.split(".")[1] in ("png","PNG"):
    import png

    with open(args.Output, 'wb') as out_img:
        write_png = png.Writer(WIDTH, HEIGHT, greyscale=False)
        write_png.write(out_img, IMG)

