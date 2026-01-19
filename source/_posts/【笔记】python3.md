---
title: "【笔记】 python3"
sticky: 100
math: true
index_img: "https://pic.rmb.bdstatic.com/bjh/5a8115df47f79481a7f6103fa85d59b2.jpeg"
tags:
  - Python
  - Note
categories:
  - Programming Language
  - Python
abbrlink: 91245943
date: 2023-10-07 03:00:00
updated: 2023-10-07 03:00:00
---


以下只提及与 C++ 差异较大的定义和语法。

## 语言特色

python 属于解释型语言：最大的特色莫过于使用 `exec()` 函数直接解释括号中的字符串并运行。

python 有很多库：如 NumPy 用于数学运算，Pandas 用于数据处理，Matplotlib 用于画图等。python 不调库就好比 C++ 没有 STL (雾) 。

## 关键字

相比 C++，以下字符也属于 python 的保留字。

* `False` `True` `None`：表示布尔值，空值（注意是大写）。

* `def` ：用于函数定义。

  ```python
  def function_name():
      print("Hrdg kawaii!")
  ```


* `assert` ：检查条件真假。

  ```PYTHON
  x = -1
  assert x > 0, "靠"
  print(x)
  ```

  运行时会报错 `AssertionError: 靠` 而不会执行 `print` 。

* `del` ：用于删除变量或对象。

  ```python
  x = 1
  del x
  print(x)
  ```

  运行时报错 `NameError: name 'x' is not defined` 。

* `elif` ：等同于 C++ 的 `else if` 。

  ```python
  if x < 0:
      print("-1")
  elif x == 0:
      print("0")
  else:
      print("1")
  ```


* `except` ：用于异常处理时捕获异常。

* `finally` ：异常处理中必须执行。

  ```PYTHON
  try:
      result = 10 / 0
  except ZeroDivisionError:
      print("除以零错误")
  finally:
      print("无论如何都会执行这里的代码")
  ```

  其中 `ZeroDivisionError` 是一个内置异常。

{% spoiler 其它内置异常 %}
1. `SyntaxError`：语法错误，通常发生在代码编写时，如拼写错误、缺少冒号等。

2. `IndentationError`：缩进错误，通常发生在代码块的缩进不一致或不正确时。

3. `NameError`：名称错误，通常发生在尝试访问不存在的变量或名称时。

4. `TypeError`：类型错误，通常发生在操作不兼容的数据类型时，如将字符串和数字相加。

5. `ValueError`：值错误，通常发生在操作正确类型的对象，但值无效或不合法时，如尝试将无效的字符串转换为数字。

6. `ZeroDivisionError`：除以零错误，通常发生在除法操作中的除数为零时。

7. `IndexError`：索引错误，通常发生在尝试访问列表、元组或其他序列中不存在的索引时。

8. `KeyError`：键错误，通常发生在尝试访问字典中不存在的键时。

9. `FileNotFoundError`：文件未找到错误，通常发生在尝试打开不存在的文件时。

10. `IOError`：输入/输出错误，通常发生在文件操作失败或无法读取或写入文件时。

11. `ImportError`：导入错误，通常发生在尝试导入不存在的模块或无效的模块时。

12. `AttributeError`：属性错误，通常发生在尝试访问对象上不存在的属性时。

13. `TypeError`：类型错误，通常发生在函数或方法接收到不正确类型的参数时。

14. `AssertionError`：断言错误，通常发生在 `assert` 语句中的条件不满足时。

15. `ArithmeticError`：算术错误的基类，包括 `ZeroDivisionError` 和 `OverflowError` 等。

16. `EOFError`：文件末尾错误，通常发生在尝试从已经读取到文件末尾的文件读取更多数据时。

{% endspoiler %}

* `from` `import` ：从模块中导入函数，变量或类。

  ```PYTHON
  from math import sqrt
  ```


* `global` ：声明全局变量。

  ```PYTHON
  def func():
  	global x
  	x = 10
  
  func()
  print(x)
  ```


* `in` ：检查一个值是否存在于一个容器中，如列表，元组，字典等。

  ```PYTHON
  if 5 in [1, 2, 3, 4, 5]:
      print("5 存在于列表中")
  ```


* `is` ：比较两个对象是否是同一个对象。（比较的不是值而是内存地址）

  ```PYTHON
  x = [1, 2, 3]
  y = x
  if x is y:
      print("x 和 y 是同一个对象")
  ```


* `lambda` ：创建匿名函数。


  * 语法：`lambda arguments: expression` ，依次对应关键字，函数参数和表达式。

    ```PYTHON
    add = lambda x, y: x + y * 2
    print(add(2, 3))  # 输出 8
    ```



* `nonlocal` ：在嵌套函数中声明一个外部（封闭）函数的变量，而不是创建一个新的局部变量。

  ```PYTHON
  def outer_function():
      x = 10
      def inner_function():
          nonlocal x
          x = 20
      inner_function()
      print(x)  # 输出 20
  ```


* `pass` ：占位符，表示一个空的代码块或函数体。

  ```PYTHON
  def func():
      pass
  ```


* `with` ：用于创建一个上下文管理器，通常用于管理资源，如文件或数据库连接。

  ```PYTHON
  with open("example.txt", "r") as file:
      data = file.read()
  ```


* `yield` ：允许你编写一种特殊类型的函数，这种函数可以在迭代时逐个产生值，而不是一次性生成所有值。


  * 如以下程序会输出前10个斐波那契数。

    ```PYTHON
    def fib_generator(n):
        a, b = 0, 1
        count = 0
        while count < n:
            yield a
            a, b = b, a + b
            count += 1
    
    for value in fib_generator(10):
        print(value,end=" ")  # 0 1 1 2 3 5 8 13 21 34
    ```

    可以发现程序遇到 `yield` 时立即返回对应值。


## 注释

* 单行注释：

  ```python
  # 啊?OP?
  ```


* 多行注释：

  ```PYTHON
  '''
  原来你也玩原神?
  原神怎么你了?
  '''
  ```

## 多行语句

运用反斜杠 `\` 。


```python
a,b,c = 0,1,2
t = a + b + \
	+c

print(t)  # 3
```

## 字符串

* 不同于 C++ 中的 "单引号括字符，双引号括字符串" ，python 中单引号与双引号用法**完全相同**。

* 三引号：指定多行字符串。

  ```PYTHON
  word = '''这合
  理吗'''
  print(word)
  ```

  输出：

  ```python
  这合
  理吗
  ```


* 使用 `r` 以防止转义。

  ```PYTHON
  word = r'hrdg yyds\n'
  print(word)  # "hrdg yyds\n"
  ```


{% spoiler 常见转义符 %}
1. `\\`：表示一个反斜杠字符。

2. `\'`：表示一个单引号字符。

3. `\"`：表示一个双引号字符。

4. `\n`：表示换行符，用于在字符串中创建新的一行。

5. `\t`：表示制表符，用于在字符串中创建水平制表位。

6. `\r`：表示回车符，通常与 `\n` 一起使用，用于在字符串中创建新行并将光标移到行首。

7. `\b`：表示退格符，用于在字符串中删除前一个字符。

8. `\f`：表示换页符，通常用于在字符串中创建新的一页。

9. `\v`：表示垂直制表符，通常用于在字符串中创建垂直制表位。

10. `\ooo`：表示一个八进制值，其中 `ooo` 是三个八进制数字，用于表示特定的字符。

11. `\xhh`：表示一个十六进制值，其中 `hh` 是两个十六进制数字，用于表示特定的字符。

{% endspoiler %}

* 可以用 `*` 使字符串重复。

  ```PYTHON
  a = 'a'
  print(a * 3) # aaa
  ```


* 字符串的索引与截取


  * 从左往右索引以 `0` 开始，从右往左以 `-1` 开始。

  * 截取格式：`[Begin:End:Step]` ：截取 `Begin` 到 `End-1` 的字符，步长为 `Step` 。

  * 以下是一个实例：

    ```PYTHON
    s = '123456789'
    print(s[0])     # 1
    print(s[-1])    # 9
    print(s[3:6])   # 456
    print(s[0:-1])  # 12345678
    print(s[2:])    # 3456789
    print(s[:2])    # 12
    print(s[:-1])   # 12345678
    print(s[1:5:2]) # 24
    print(s[1::3])  # 258
    print(s[:-1:2]) # 1357
    ```



* 字符串格式化

  ```PYTHON
  name = input()
  greeting = f"Hello, {name}!"
  print(greeting)
  ```

## 输入输出

* 使用 `input()` 输入

  * 基本用法： `a = input()`

  * 传递字符串作为输入提示： `a = input("a = ")`

  * 类型转换： `a = int(input())`

  * 运用 `.split()` 分隔

    ```PYTHON
    a,b,c = input().split() # 输入“1 2 3”
    print(b) # 输出2
    ```



* 使用 `print()` 输出


  * 换行： `print(x)`

  * 不换行： `print(x,end="")`

    ```PYTHON
    a, b = 0, 1
    print(a, end=" ")
    print(b, end="")
    print(a) 
    #输出 "0 10"
    ```



* 其它输出方式


  * 文件输出

    ```PYTHON
    with open("output.txt", "w") as file:
        file.write("This is written to a file.")
    ```


  * 格式化字符串输出

    ```PYTHON
    name = "学生"
    age = 24
    print("{}岁,是{}".format(age,name))
    # 24岁,是学生
    ```

    或者使用 f-strings 等价：

    ```PYTHON
    print(f"{age}岁,是{name}")
    # 24岁,是学生
    ```


  * 标准错误输出（一般输出至终端或命令行）

    ```PYTHON
    import sys
    sys.stderr.write("寄了,哈哈\n")
    ```


## 模块导入

* 只导入模块： `import somemodule`

  * 后续调用使用 `somemodule.func_a` 形式

* 导入模块成员： `from somemodule import func_a,func_b`

  * 后续直接调用 `func_a` `func_b`

* 导入模块中的全部函数： `from somemodule import *`

* 什么是 `if __name__ == "__main__":` ?

  * 当你创建了一个模块（比如一个 .py 文件），这个模块就会有一个内置属性 `name` 生成。当你 import 一个模块时，`name` 通常是文件名。如果你直接运行该模块，那么 `__name__ == "__main__"` ，否则不等。

  * 例如你创建了两个 .py 文件：

    ```PYTHON
    # test1.py
    
    print('a',end=" ")
    if __name__ == "__main__": 
    	print('b')
    ```

    ```PYTHON
    # test2.py
    import test1
    ```

    直接运行 `test1.py` 输出 `a b` ;

    而运行 `test2.py` 则输出 `a` 。


* 模块搜索顺序：

  * 当前目录

  * shell 变量 PYTHONPATH 下的每个目录（PYTHONPATH 由装在一个列表里的许多目录组成）
  * 查看默认路径（UNIX下，默认路径一般为/usr/local/lib/python/）

* 利用 `dir(somemodule)` 查看模块中定义的子模块，变量，函数。

* 利用 `locals()` 访问**局部**命名空间，`globals()` 访问**全局**命名空间。

* 利用 `reload(somemodule)` 重新执行顶层导入代码。

## 数值对象

* 乘方用 `**` ，如 `2 ** 3 = 8`

* 数值除法包括：

  * `/` 返回一个**浮点数** 。`3 / 2 = 1.5`

  * `//` 类似 C 整数除法，**下取整** 。`3 // 2 = 1`

* 混合计算时，整型会被转化为浮点数。

* 利用 `type(object)` 获取对象类型

  ```PYTHON
  a = 2.0
  print(type(a))
  # 输出“<class 'float'>”
  ```


* 利用 `isinstance(object, classinfo)` 检查一个对象是否是特定类或类型的实例。其返回一个布尔值。


  * 类型判断：

    ```PYTHON
    a = 2.0
    print(isinstance(a,int)) # False
    ```


  * 实例判断：

    ```PYTHON
    class op:
    	qiye_nana7 = 1
    
    print(isinstance(op(),op)) # True
    ```

    那如果想判断 `qiye_nana7` 是否属于 `op` 怎么办呢？

    其中`qiye_nana7` 属于类属性，那么使用 `hasattr(class_name,attribute_name)` 判断：

    ```PYTHON
    class op:
    	qiye_nana7 = 1
    
    print(hasattr(op, 'qiye_nana7')) # True
    print(hasattr(op, 'KisuraOP')) # False
    ```


## 列表（List）

* 类似数组，是有序对象集合。

* 中括号定义：`list = [123, 1.0, 'str', 'nmsl']`

* 调用和截取与字符串相同，略。

* 与字符串不同的是，列表中的元素可以改变：

  ```python
  a = 'cnm'
  # a[0] = 'a' # 编译错误
  
  a = ['原神', '牛批']
  print(a[0][0] + a[1][1])  # 原批
  
  a[0] = 'o'
  a[1] = 'p'
  print(a[0]+a[1])  # op
  ```

## 元组（Tuple）

* 与列表类似，元组一样可以通过 `+` 连接，`*` 重复，不过其**元素不能修改**。

* 小括号定义：`tup = (123, 1.0, 'str', 'nmsl')` 。

* 只包含一个元素时，需添加逗号。 `tup2 = (114514,)`

## 集合（Set）

* 特点：无序，可变，元素不会重复。

* 大括号定义：`setA = {'Codeforces', 'Atcoder', 'Luogu'}`

* 函数定义：`setB = set('AAACMCA')` $\to$ `setB = {'A', 'C', 'M'}`

* 集合运算：

  ```PYTHON
  A = {'Codeforces', 'Atcoder', 'Luogu', 'Lutece'}
  B = {'Lutece', 'TopCoder'}
  
  if 'Atcoder' in A:
      print("Yes")
  else:
      print("No")
  # Yes
  
  print(A - B)  # 差集 {'Luogu', 'Codeforces', 'Atcoder'}
  print(B - A)  # 差集 {'TopCoder'}
  print(A | B)  # 并集 {'Codeforces', 'Atcoder', 'TopCoder', 'Luogu', 'Lutece'}
  print(A & B)  # 交集 {'Lutece'}
  print(A ^ B)  # 异或,不同时出现 {'Codeforces', 'Atcoder', 'TopCoder', 'Luogu'}
  ```

## 字典（Dict）

* 无序对象集合，键值对存储，键必须唯一。类似 STL 中的 `map` 。

  ```python
  a = {
      'op': '我',
      55: '芙宁娜大人',
      '啊': 4
  }
  
  print(a['op'] + str(a['啊']) + a[55] + '的狗')
  # 我4芙宁娜大人的狗
  
  print(a)
  # {'op': '我', 55: '芙宁娜大人', '啊': 4}
  
  print(a.keys())
  # dict_keys(['op', 55, '啊'])
  
  print(a.values())
  # dict_values(['我', '芙宁娜大人', 4])
  
  
  a['op'] = '芙宁娜'  # 更改键值对
  a[44] = '我'  # 增添键值对
  
  print(a['op'] + str(a['啊']) + a[44] + '的狗')
  # 芙宁娜4我的狗
  
  print(a)
  # {'op': '芙宁娜', 55: '芙宁娜大人', '啊': 4, 44: '我'}
  
  
  for i in a:
      print(i, end="")  # op55啊44
  
  for i, j in a.items():
      print(i, j, end="")  # op 芙宁娜55 芙宁娜大人啊 444 我
  
  print(len(a))  # 4
  
  if '我' in a:
      print("oh yeah")
  else:
      print("No")
  # No
  
  if 'op' in a:
      print("oh yeah")
  else:
      print("No")
  # oh yeah
  
  a.clear()  # 清空字典
  print(a)  # {}
  if 'op' in a:
      print("这河里吗")
  else:
      print("op似光辣")
  # op似光辣
  ```

## 数据类型转换

1. `int(x[,base])` ：将 `x` 作为 `base` 进制转换。

   * `int('101') = 101` , `int('101',2) = 5` 。


2. `float(x)` ：转换为浮点数

3. `str(x)` `repr(x)` ：转换为字符串/字符串字面量。

   * 有什么区别？

     ```PYTHON
     s="校区 \t清水河\t沙河\n提档线\t629 \t631"
     print(str(s))
     print(repr(s))
     ```

     将会输出：

     ```python
     校区 	清水河	沙河
     提档线	629   631
     '校区 \t清水河\t沙河\n提档线\t629 \t631'
     ```



4. `complex(real[,imag])` ：创建一个复数（实虚部）

5. `tuple(x)` `list(x)` `set(x)` `dict(x)` ：转换为元组/列表/集合/字典

6. `chr(x)` `ord(x)` `hex(x)` `oct(x)` ：整数转字符/字符转整数/转十六进制/转八进制

7. `eval(x)` ：表达式计算

   ```PYTHON
   a = eval("2 ** 5")
   print(a) # 32
   ```

   和 `exec()` 的区别在于 `eval()` **只能执行表达式而不能执行代码块** 。

## 对象的可更改性

* 可变：类似 C++ 引用传递，如列表，字典。

* 不可变：类似 C++ 值传递，如数字，字符串，元组。

* 区别：

  ```PYTHON
  def change_num(x):
  	x = x + 1
  
  def change_list(x):
  	x.append([1,2])
  
  A = 3;
  change_num(A)
  print(A)   # 3
  
  B = [1,2,3,4]
  change_list(B)
  print(B)   # [1, 2, 3, 4, [1, 2]]
  ```

## python包

包是一个分层次文件目录结构，基础构成如下：


```cpp
test.py
packageA
|-- __init__.py
|-- A.py
|-- B.py
packageB
|-- __init__.py
|-- A.py
|-- B.py
VIM
```


可以通过以下方法调用模块：


```cpp
# test.py
from packageB.A import funcion_name
from packageA.B import funcion_name
PYTHON
```


其中 `__init__.py` 是必须的，目的是标识当前目录是一个包。

## 内置函数

* `enumerate(sequence, [start = 0])`

  * `sequence` ：一个序列，迭代器等支持迭代的对象。

  * `start` ：下标起始位置的值。

  * 将一个可迭代对象（如列表、元组或字符串）组合为一个索引序列，同时列出数据和数据下标。

    ```PYTHON
    a = ['a', 'b', 'd', 'c']
    for i in enumerate(a):
        print(i)
    '''
    (0, 'a')
    (1, 'b')
    (2, 'd')
    (3, 'c')
    '''
        
    for i, j in enumerate(a):
        print(i, j)
    '''
    0 a
    1 b
    2 d
    3 c
    '''
    ```


* `map(function, iterable, ...)`

  * `function` ：要应用于每个元素的函数。

  * `iterable` ：输入到 `function` 的可迭代对象，可以是一个或多个。

  * 将一个函数应用于可迭代对象（如列表、元组或字符串）的所有元素，返回一个迭代器。

    ```python
    def square(x):
        return x ** 2
    
    numbers = [1, 2, 3, 4, 5]
    
    squared_numbers = map(square, numbers)
    
    print(list(squared_numbers)) # 1, 4, 9, 16, 25
    ```


  * 一个应用是求出一个数 $x$ 的各数位之和（将 `int` 作为 `function` 应用到 $x$ 每一位）

    ```PYTHON
    def digit_sum(n):
        return sum(map(int, str(n)))
    ```



