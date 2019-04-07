from copy import deepcopy


class Color:
    def __init__(self, rgb = None, bold = False, italic = False, underline = False, inverse = False):
        if rgb is None: rgb = []

        self.rgb = rgb
        self._bold = bold
        self._italic = italic
        self._underline = underline
        self._inverse = inverse

    @classmethod
    def fromhex(cls, h, **kwargs):
        h = h.lstrip('#')
        return Color([int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)], **kwargs)

    @property
    def bold(self):
        c = deepcopy(self)
        c._bold = True
        return c

    @property
    def italic(self):
        c = deepcopy(self)
        c._italic = True
        return c

    @property
    def underline(self):
        c = deepcopy(self)
        c._underline = True
        return c

    @property
    def inverse(self):
        c = deepcopy(self)
        c._inverse = True
        return c

    def trueColor(self):
        s = ''
        if self._bold:
            s += '\x1b[1m'
        if self._italic:
            s += '\x1b[3m'
        if self._underline:
            s += '\x1b[4m'
        if self._inverse:
            s += '\x1b[7m'
        if self.rgb:
            r, g, b = self.rgb
            s += f'\x1b[38;2;{r};{g};{b}m'
        return s

    def paint(self, text):
        return f'{self.trueColor()}{text}\x1b[0m'


Color.red    = Color.fromhex('#EC2049')
Color.green  = Color.fromhex('#1FDA9A')
Color.blue   = Color.fromhex('#3A9AD9')
Color.yellow = Color.fromhex('#F9D423')
Color.white  = Color.fromhex('#FFFFFF')
Color.gray   = Color.fromhex('#777777')
Color.black  = Color.fromhex('#000000')
