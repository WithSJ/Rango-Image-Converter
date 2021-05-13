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


def read_ppm(filename):
    with open(filename,"r") as input_file:
        file_lines = input_file.readlines()
        for inline in file_lines:
            if "P3" in inline:
                global WIDTH,HEIGHT
                WIDTH,HEIGHT = inline.split()[1:]        
                WIDTH,HEIGHT = int(WIDTH),int(HEIGHT)
                file_lines.remove(inline)
            if "#" in inline:
                file_lines.remove(inline)

        for row in file_lines[1:]:
            IMG.append(tuple(map(eval,row.split())))

def write_png(filename):
    import png

    with open(filename, 'wb') as out_img:
        write_png = png.Writer(WIDTH, HEIGHT, greyscale=False)
        write_png.write(out_img, IMG)



if(args.Input.split('.')[1] in ("ppm","PPM")):
    read_ppm(args.Input)
             
if args.Output.split(".")[1] in ("png","PNG"):
    write_png(args.Output)

