from ..color import Color

class Formatter:
    @staticmethod
    def itemgetter(*items):
        def fn(obj):
            result = []
            for item in items:
                if type(item) is tuple or type(item) is list:
                    result.append(obj.get(item[0], item[1]))
                else:
                    result.append(obj.get(item))
            if len(result) == 1:
                result = result[0]
            return result

        return fn


    def paint(self, color, text, inverse = False):
        if inverse:
            dark = Color.fromhex('#343D46')
            prefix  = color.inverse().trueColor()
            prefix += dark.trueColor()
            return f'{prefix}{text}{Color.reset()}'
        else:
            prefix = color.trueColor()
            return f'{prefix}{text}{Color.reset()}'
