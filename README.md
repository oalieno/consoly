# 🖥 Consoly

Elegant Console Logger for Python

![MIT](https://img.shields.io/github/license/oalieno/consoly.svg)

## Installation

From PyPI

```bash
pip install consoly
```

From Github

```bash
pip install git+https://github.com/OAlienO/consoly.git
```

## Getting Started

```python
from consoly import consoly

consoly.critical('Bomb!!')
consoly.error('Oh shit...')
consoly.warning('Chill')
consoly.info('Just some information')
consoly.debug('Fuck bugs')
```

<img src="https://i.imgur.com/5gH6eBX.png" width="350">

```python
from consoly import consoly

consoly.level = consoly.DEBUG
consoly.defaults = { 'badge': True, 'time': True }

consoly.critical('Bomb!!')
consoly.error('Oh shit...')
consoly.warning('Chill')
consoly.info('Just some information')
consoly.debug('Fuck bugs')
```

<img src="https://i.imgur.com/XV7IBPy.png" width="350">

## Document

### type of levels

| type | level | alias |
| --- | --- | --- |
| critical | 50 | consoly.CRITICAL |
| error | 40 | consoly.ERROR |
| warning | 30 | consoly.WARNING |
| info | 20 | consoly.INFO |
| debug | 10 | consoly.DEBUG |

#### custom type of level

```python
consoly.types['success'] = {
    'level': 25,
    'color': Color.green,
    'icon': '✔'
}
consoly.level = consoly.SUCCESS
consoly.success('it works')
```

### Consoly

default instance `consoly` is created by [`Consoly(FancyFormatter())`](/consoly/__init__.py#L5)

#### `consoly.level`

default to `0` ( print every messages )

```python
consoly.level = consoly.ERROR
```

#### `consoly.defaults`

default to `{}`

this is the default options pass to formatter

```python
consoly.defaults = { 'badge': True }
```

#### `consoly.types`

see [type of levels](#type-of-levels)

#### `consoly.formatter`

see [Formatter](#formatter)

### Formatter

default formatter is [FancyFormatter](/consoly/formatter/fancyFormatter.py)

#### set output file ( default is sys.stdout )

```python
consoly.formatter.file = open('service.log', 'w')
```

#### custom formatter

```python
from consoly import Formatter

class MyFormatter(Formatter):
    def format(self, text, typeData, formatData):
        name  = typeData['name']
        color = typeData['color']
        bold  = formatData.get('bold', False)
        if bold: color = color.bold
        self.write(f'{color.paint(name)} - {text}')

consoly.formatter = MyFormatter()
```

For example `consoly.error('test', testOption = 10)`

##### `text` will be `test`

##### `typeData` will be

```python
{
    'name': 'error',
    'level': 40,
    'color': Color.red,
    'icon': '✖'
}
```

##### `formatData` will be

```python
{
    'testOption': 10
}
```
