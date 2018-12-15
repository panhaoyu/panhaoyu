Title: Python路径
Date: 2017-08-04 19:53
Summary: 介绍Python中的路径。

# 获取路径

|    操作     |           结果           |
| ----------- | ------------------------ |
| os.getcwd() |  运行程序时您所在的位置  |
| sys.path[0] |  程序入口文件所在的目录  |
| sys.argv[0] |   程序入口文件的文件名   |
|  __file__   | 执行这个代码的文件的路径 |

# 例子

## 文件结构：

```
test
├── main.py
└── pkg
    └── __init__.py
```

main.py：

```
import pkkg
```

pkg/__init__.py：

```
import os
import sys
print('os.getcwd()', os.getcwd())
print('sys.path[0]', sys.path[0])
print('sys.argv[0]', sys.argv[0])
print('__file__', __file__)
```

## 执行：

在test的上一级目录，也就是tmp文件夹，在bash中运行：

```
python3 text/main.py
```

## 输出

```
os.getcwd() /tmp
sys.path[0] /tmp/test
sys.argv[0] test/main.py
__file__ /tmp/test/pkg/__init__.py
```
