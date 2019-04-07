from copy import deepcopy

class Color:
    def __init__(self, r, g, b, bg=False):
        if not self.valid(r) or not self.valid(g) or not self.valid(b):
            pass

        self.r = r
        self.g = g
        self.b = b
        self.bg = bg

    def inverse(self):
        c = deepcopy(self)
        c.bg = not c.bg
        return c

    @classmethod
    def fromhex(cls, h, bg=False):
        h = h.lstrip('#')
        return Color(int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), bg)

    @classmethod
    def reset(cls):
        return '\x1b[0m'

    @staticmethod
    def valid(v):
        return 0 <= v <= 255

    def trueColor(self):
        return f'\x1b[{48 if self.bg else 38};2;{self.r};{self.g};{self.b}m'


Color.red = Color.fromhex('#EC2049')
Color.green = Color.fromhex('#1FDA9A')
Color.blue = Color.fromhex('#3A9AD9')
Color.yellow = Color.fromhex('#F9D423')
Color.white = Color.fromhex('#FFFFFF')
Color.gray = Color.fromhex('#777777')
Color.black = Color.fromhex('#000000')
