# Run from console script interface.

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

# End script console interface.

from image_converter.reader import read_ppm
from image_converter.writer import write_png

IMG = list()
WIDTH = int()
HEIGHT = int()


if(args.Input.split('.')[1] in ("ppm","PPM")):
    WIDTH, HEIGHT, IMG = read_ppm(args.Input)
             
if args.Output.split(".")[1] in ("png","PNG"):
    write_png(args.Output,WIDTH,HEIGHT,IMG)

