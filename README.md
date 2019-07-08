# Переводит фотографии в текст
Использовать преимущественно для фотографий кода ¯\\\_(ツ)\_/¯
Хотя, можно переделать

У функции несколько параметров:
* img - путь к картинке. (например: 1.png)
* spaces - вид табуляции или пробелов (по умолчанию 1 таб)
* text - текст в начале того, что считается с картинки

Зависимости:
```python
from PIL import Image
from tesserocr import PyTessBaseAPI, RIL, image_to_text
import locale
```
Нужно для tesserocr в некоторых языках, причем поменять нужно до импорта tesserocr
```python
locale.setlocale(locale.LC_ALL, 'C')
```

# Translates photos into text
Use primarily for code photos ¯\\\_(ツ)\_/¯
Although, it is possible to alter

The function has several parameters:
* img - the path to the picture (for example: 1.png)
* spaces - tab or space view (default is 1 tab)
* text - text at the beginning of what counts from the picture

Dependences:
```python
from PIL import Image
from tesserocr import PyTessBaseAPI, RIL, image_to_text
import locale
```
Need for tesserocr in some languages, and you need to change before importing tesseract
```python
locale.setlocale(locale.LC_ALL, 'C')
```