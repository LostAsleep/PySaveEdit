# PySaveEdit

This is program is intended to to handle .save files from html games, 
that are encode as lz-string. 

For more information on lz-string visit:
[pieroxy.net/blog/pages/lz-string](https://pieroxy.net/blog/pages/lz-string/index.html)

Example on how to use the lzstring module.

```python
import lzstring
x = lzstring.LZString()
compressed = x.compressToBase64(u'你好') # 'gbyl9NI='
x.decompressFromBase64(compressed) # '你好'
```
