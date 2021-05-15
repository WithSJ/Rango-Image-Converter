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
    """ Write PPM image file.

    Args:
        filename (string): Image file name with there .ppm extention
        width (int): Width of image
        height (int): Height of image
        image (list): Image data contain image rows.
    """
    with open(filename,"w") as out_img:
        out_img.write(f"P3 {width} {height}\n255\n")
        for row in image:
            for ele in row:
                out_img.write(f"{ele} ")
            out_img.write("\n")
        

def write_jpg(filename,width,height,image):
    """ Write jpg or jpeg file

    Args:
        filename (string): filename with .jpg or .jpeg extention.
        width (int): size of coloumns
        height (int): size of row
        image (list): list contain rows in tupple
    """
    pass