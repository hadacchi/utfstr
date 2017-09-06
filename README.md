When this class is passed to built-in function `len`, this class returns width
of a string which include 3byte UTF-8 characters.

# get width by `len`

Some multibyte characters, e.g. Kanji, Hiragana and Katakana in Japanese, have
twice width of ascii characters.
Usually we don't care it, however, some modules, like texttables, get width of
columns by `len` and multibyte characters break layout.

# attention

This class may cause confusion of length and width.
This class should be used only if above problem occurs.

# usage

source is

```
import utfstr

a = '日本語 and English'
b = utfstr.utfstr(a)

print(len(a),len(b))
```

output is

```15 18```
