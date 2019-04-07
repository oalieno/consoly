from .color import Color
from .formatter.fancyFormatter import FancyFormatter


class Consoly:
    def __init__(self, formatter, level = None, types = None):
        if level is None: level = 30
        if types is None: types = {}

        self.formatter = formatter
        self.level = level
        self.setTypes({
            'critical': {
                'level': 50,
                'color': Color.red,
                'icon': '✖'
            },
            'error': {
                'level': 40,
                'color': Color.red,
                'icon': '✖'
            },
            'warning': {
                'level': 30,
                'color': Color.yellow,
                'icon': '❢'
            },
            'info': {
                'level': 20,
                'color': Color.blue,
                'icon': '➜'
            },
            'debug': {
                'level': 10,
                'color': Color.green,
                'icon': '✦'
            },
            **types
        })

    def setTypes(self, types):
        for t, v in types.items():

            def wrapper(t, v):
                def fn(text, **kwargs):
                    if v['level'] >= self.level:
                        self.formatter.format(text, {'name': t, **v}, **kwargs)

                return fn

            setattr(self, t, wrapper(t, v))

    def set(self, member, value):
        setattr(self, member, value)

    def get(self, member):
        return getattr(self, member)


consoly = Consoly(FancyFormatter())

critical = consoly.critical
error    = consoly.error
warning  = consoly.warning
info     = consoly.info
debug    = consoly.debug
set      = consoly.set
get      = consoly.get

__all__ = (
    'consoly',
    'critical',
    'error',
    'warning',
    'info',
    'debug',
    'set',
    'get'
)
