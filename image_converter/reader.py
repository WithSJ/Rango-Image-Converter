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


def read_png(_filename):
    """ Read PNG file data.

    Args:
        _filename (string): Image file name or path with there .png extention

    Returns:
        [tuple]: Width,Height,Image,Info
    """
    img = list()

    read_img = png.Reader(filename=_filename)
    width,height,rows,info = read_img.read()
    for row in rows:
        img.append(tuple(row))

    return width,height,img,info

def read_jpg(filename):
    """ Read jpg or jpeg files data.

    Args:
        filename (string): filename with .jpg or .jpeg extention.

    Returns:
        [tupple]: Width,Height,Image data.
    """
    width = int()
    height = int()
    img = list()

    return width,height,img