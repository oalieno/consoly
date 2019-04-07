from sys import stdout

from ..color import Color


class Formatter:
    def __init__(self, file = stdout):
        self.file = file

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

    def write(self, text):
        print(text, file=self.file)
