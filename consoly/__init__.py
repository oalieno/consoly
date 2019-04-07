from .color import Color
from .consoly import Consoly
from .formatter import Formatter, FancyFormatter

__version__ = '0.0.1'

consoly = Consoly(FancyFormatter())

__all__ = ['DO_NOT_WILD_IMPORT']
