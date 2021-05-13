import png

def write_png(filename,width,height,image,_greyscale=False):
    """ Write PNG image

    Args:
        filename (string): Image name with path where you want to write image.
                            image name should be with .png extention

        width (int): Width of image.

        height (int): Height of image.
        
        image (list): image rows contain in this list row should be in tuple
        
        _greyscale (bool, optional): color scale of image. Defaults to False.
    """

    with open(filename, 'wb') as out_img:
        write_png = png.Writer(width, height, greyscale=_greyscale)
        write_png.write(out_img, image)

def write_ppm(filename,width,height,image):
    pass