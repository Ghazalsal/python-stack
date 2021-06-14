Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  4 2021, 13:27:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print("hello world!")
hello world!
>>> name="Noelle"
>>> print("Hello", name)
Hello Noelle
>>> print("Hello," , name)
Hello, Noelle
>>> print("Hello+", name)
Hello+ Noelle
>>> name=42
>>> print("Hello", name)
Hello 42
>>> print("hello," name)
  File "<stdin>", line 1
    print("hello," name)
                   ^
SyntaxError: invalid syntax
>>> print("hello,", name)
hello, 42
>>> print("hello"+ name)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> fave_food1="sushi"
>>> fave_food2="pizza"
>>> print("my favefood1 {} and my FaveFood2 {}.".format(fave_food1,fave_food2))
my favefood1 sushi and my FaveFood2 pizza.
>>> name="Ghazal"
>>> print("Hello" , name)
Hello Ghazal
>>> name="Ghazal"
>>> print("Hello" + name)
HelloGhazal
>>> num=9
>>> print("Hello" , num)
Hello 9
>>> num=9
>>> print("Hello" + num)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> num="9"
>>> print("hello" + num)
hello9
>>> favfood1="makloba"
>>> favfood2="shoshbrak"
>>> print("my fav food 1 {} and my fav food 2 {}".format(favfood1,favfood2))
my fav food 1 makloba and my fav food 2 shoshbrak
