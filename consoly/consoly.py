from .color import Color

class Consoly:
    def __init__(self, formatter, level = None, defaults = None, types = None):
        if level is None: level = 0
        if defaults is None: defaults = {}
        if types is None: types = {}

        self.formatter = formatter
        self.level = level
        self.defaults = defaults
        self.types = {
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
        }

    def __getattr__(self, attr):
        if attr in self.types:
            data = self.types[attr]
            def fn(text, **kwargs):
                if data['level'] >= self.level:
                    self.formatter.format(text, { 'name': attr, **data }, { **self.defaults, **kwargs })
            return fn
        elif attr in map(lambda t: t.upper(), self.types.keys()):
            return self.types[attr.lower()]['level']
        else:
            raise AttributeError
