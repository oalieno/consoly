from datetime import datetime

from .formatter import Formatter
from ..color import Color


class FancyFormatter(Formatter):
    def format(self, text, typeData, formatData):
        name, color, icon = self.itemgetter('name', 'color', 'icon')(typeData)
        badge, time, short = self.itemgetter(('badge', False), ('time', False), ('short', False))(formatData)

        header = ''
        if short:
            name = name[0].upper()
        if badge:
            if time:
                t = datetime.now().strftime('%H:%M:%S')
                header += Color.gray.inverse.paint(f' {t} ')
            header += color.inverse.paint(f' {name.upper()} ')
        else:
            if time:
                t = datetime.now().strftime('%H:%M:%S')
                header += Color.gray.paint(f'⧗ {t} ┃ ')
            header += color.paint(f'{icon} {name}')

        self.write(f'{header} {text}')
