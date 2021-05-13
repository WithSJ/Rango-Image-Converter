import png 

def read_ppm(filename):
    """ Function use to read PPM file

    Args:
        filename (string): [file name with path should contain .ppm extention]

    Returns:
        [tupple]: [Elements (WIDTH,HEIGHT,IMAGE)]
    """
    img = list()
    width = int()
    height = int()
    
    with open(filename,"r") as input_file:
        file_lines = input_file.readlines()
        
        for inline in file_lines:
            # Get width and height and remove all comments line from list

            if "P3" in inline:
                width,height = map(eval,inline.split()[1:])
                file_lines.remove(inline)

            if "#" in inline:
                file_lines.remove(inline)

        for row in file_lines[1:]:
            # all list elements are number but in str() 
            # to convert in int() and then in tupple
            # example ["1","2","3"]  => [1,2,3]

            img.append(tuple(map(eval,row.split())))

    return width,height,img


def read_png(filename):
    pass