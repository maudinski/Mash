class Tile(object):

    properties = []
    img = 1 # this will hold img
    pixel_length = 0
    x_coor = 0
    y_coor = 0

    def __init__(self, image, props, x, y, pixel):
        self.img = image
        self.properties = props
        self.pixels = pixel
        self.x_coor = x
        self.y_coor = y


    def get_properties(self):
        return self.properties

    def get_img(self):
        return self.img

    def get_pixel_length(self):
        return self.pixel_length

    def get_x(self):
        return self.x_coor

    def get_y(self):
        return self.y_coor




