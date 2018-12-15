Title: urwid控件介绍
Date: 2017-06-22 23:30

# 控件基类

## Widget

## WidgetWrap

## WidgetDecoration

## WidgetContainerMixin

# 基本控件

## Text

用法:`Text(markup, align='left', wrap='space', layout=None)`

一个水平的大小可变的文本控件.

参数:

* markup,Text Markup,文本内容.

* align,对齐方式,通常为`left`,`center`或者`right`

* wrap,打包方式,通常为`space`,`any`或者`clip`

* layout,文本排版,默认是一个共享的`StandardTextLayout`实例

## Edit

## IntEdit

## Button

用法:`Button(label, on_press=None, user_data=None)`

参数:

* label, 标签文本,markup格式

* on_press, connect_signal()函数的快捷方式,一个简单的回调函数

* user_data, on_press函数的参数

支持的信号: `click`

调用方式:`callback(button[, user_data])`

## CheckBox

## RadioButton

## TreeWidget

## SelectableIcon

# 装饰控件

## AttrMap

## Padding

## Filling

## Divider

## LineBox

## SolidFill

## PopUpLauncher

## PopUpTarget


