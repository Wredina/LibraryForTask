# Байты и массивы байт

байты - неизменяемые

массивы байт - изменяемые

b'' - обозначение байта

**Получение байт из строки**

- encode('untf-8') - получение байт из строки (рекомендуется явно прописывать utf-8)

- bytes(b'') - получение байт из форматированной строки

- bytearray(b'') - получение байт из форматированной строки

## Примеры

- encode('untf-8')

```py
text_en = 'Hello world!'
res = text_en.encode('utf-8')
print(res, type(res))
# b'Hello world!' <class 'bytes'>

text_ru = 'Привет, мир!'
res = text_ru.encode('utf-8') # русский язык представляется в 16-тиричной системе
print(res, type(res))
# b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82, \xd0\xbc\xd0\xb8\xd1\x80!' <class 'bytes'>
```

- bytes(b''), bytearray(b'')

```py
x = bytes(b'\xd0\x9f\xd1\x80\xd0\xb8')
y = bytearray(b'\xd0\x9f\xd1\x80\xd0\xb8')
print(f'{x = }\n{y = }')
# x = b'\xd0\x9f\xd1\x80\xd0\xb8'
# y = bytearray(b'\xd0\x9f\xd1\x80\xd0\xb8')
```
