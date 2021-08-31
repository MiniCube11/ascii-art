from PIL import Image, ImageOps

MAX_PIXEL_VALUE = 255
ASCII_CHARS = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

INVERSE = False


def process_image(photo_name):
    image = Image.open(photo_name)
    im2 = ImageOps.grayscale(image)
    im2.thumbnail((200, 200))

    return im2


def ascii_char(n, inverse=False):
    if inverse:
        n = MAX_PIXEL_VALUE - n
    return ASCII_CHARS[round(n // (255 / 65)) - 1] * 3


def print_ascii_image(data, width, inverse=False):
    column = 0
    for i in data:
        chars = ascii_char(i, inverse)
        print(chars, end='')
        if column % width == 0:
            column = 1
            print()
        else:
            column += 1


def get_ascii_image(data, width, inverse=False):
    res = ""
    column = 0
    for i in data:
        res += ascii_char(i, inverse)
        if column % width == 0:
            column = 1
            res += '\n'
        else:
            column += 1
    return res


def ascii_image(photo_name, inverse=False):
    image = process_image(photo_name)
    width = image.size[0]
    s = get_ascii_image(list(image.getdata()), width, inverse=inverse)
    return s


photo_name = input("Name of photo (with extension) >>> ")
print(ascii_image(photo_name))
