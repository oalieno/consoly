from datetime import datetime

from . import Formatter
from ..color import Color

class FancyFormatter(Formatter):
    def format(self, text, typeData, **kwargs):
        name, color, icon = self.itemgetter('name', 'color', 'icon')(typeData)
        badge, time = self.itemgetter(('badge', False), ('time', False))(kwargs)

        header = ''
        if badge:
            if time:
                t = datetime.now().strftime('%H:%M:%S')
                header += self.paint(Color.gray, f' {t} ', inverse = True)
            header += self.paint(color, f' {name.upper()} ', inverse = True)
        else:
            if time:
                t = datetime.now().strftime('%H:%M:%S')
                header += self.paint(Color.gray, f'{t} ┃ ')
            header += self.paint(color, f'{icon} {name}')

        print(f'{header} {text}')
