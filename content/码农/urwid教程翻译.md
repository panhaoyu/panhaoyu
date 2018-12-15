Title: Urwid教程翻译
Date: 2017-06-21 21:00
Summary: Urwid是用于在类Unix系统的命令行中构建交互应用的python库.

# 一个简单的小程序

这个简单的小程序将会在屏幕的左上角显示一行`Hello World`.它没有设置退出的按键,所以您需要按下`Ctrl-C`来退出程序.

```

import urwid

txt = urwid.Text('Hello World')
fill = urwid.Filler(txt, 'top')
loop = urwid.MainLoop(fill)
loop.run()

```

* **Text**控件用于处理文本.如果文本很长,将会占用下一行.像这样的大小可变的控件被称为"流动控件".

* **Filler**控件用于框住流动控件,这样他们才能显示在屏幕上.像这样的被限定了行列数的控件被称为"箱子控件".

* **MainLoop**类用于显示我们的控件,并获取用户的输入.传递给MainLoop的控件被称为"顶级控件".顶级控件用来渲染整个屏幕,所以它必须是一个箱子控件.这个例子中,我们的这些控件并不能处理用户输入,因此我们需要按下`Ctrl-C`来退出程序.

# 全局输入

这个程序最初会显示`Hello World`,然后它将会显示用户按下的按键.当用户按下Q的时候,程序退出.

```

import urwid

def show_or_exit(key):
    if key in 'qQ':
        raise urwid.ExitMainLoop()
    txt.set_text(key)

txt = urwid.Text('Hello World')
fill = urwid.Filler(txt, 'top')
loop = urwid.MainLoop(fill, unhandled_input=show_or_exit)
loop.run()

```

* **MainLoop**类有一个可选参数,*unhandled_input*,它接受一个函数作为参数.每次当MainLoop检测到其他控件没有处理的按键时,由于这个示例中,并没有其他的控件来处理用户输入,所以用户每次按下一个按键都会调用*show_or_exit*函数.

* **ExitMainLoop**异常用于彻底地退出MainLoop.run()函数.当您按下Q的时候,函数退出.所有其他的按键将会显示在Text控件上面.

# 显示属性

这个程序将`Hello World`显示在屏幕中央.它用不同的属性来显示这些字符.这些是通过控制它上下左右的空格来实现的.按下Q可以退出程序.

```

import urwid

def show_or_exit(key):
    if key in 'qQ':
        raise urwid.ExitMainLoop()

palette = [
    ('banner', 'black', 'light gray'),
    ('streak', 'black', 'dark red'),
    ('bg', 'black', 'dark blue'),]

txt = urwid.Text(('banner', 'Hello World'), align='center')
map1 = urwid.AttrMap(txt, 'streak')
fill = urwid.Filler(map1, 'top')
map2 = urwid.AttrMap(fill, 'bg')
loop = urwid.MainLoop(map2, palette, unhandled_input=show_or_exit)
loop.run()

```

* 显示属性在palette(调色板)中定义.可用的前景色,背景色和设置选项在`前景背景设置`中有记录.调色板包含下面这几项:

  1. 显示属性的名称,通常是一个字符串

  1. 前景色和设置选项,针对16色模式(通常模式)

  1. 背景色和设置选项,针对16色模式

  1. 针对单色模式的设定(可选的)

  1. 前景色和设置选项,针对88色和256色模式(可选的,见下面的例子)

  1. 背景色和设置选项,针对88色和256色模式(可选的)

* **Text**控件采用了`banner`显示属性.对于Text控件来说,设置显示属性的方式就是将原本的简单的文本字符串替换为`(显示属性`, `字符串)`元组.显示属性将会随着文本而流动.如果你想对一短文本的不同部分应用不同的属性的话,将多个元组放在一个列表中就可以了.

* **AttrMap**控件用显示属性`streak`来包住文本控件.`AttrMap`控件将会把显示属性赋值给所有的字符,但是默认情况下,它并不会覆盖已有显示属性的控件.例如,本例中,文本控件已经有了显示属性,因此除了文本控件之外的位置会被赋值为新的颜色.

* 第二个**AttrMap**控件用显示属性`bg`来包裹`Filter`控件.

运行这个程序,您可以很容易分辨出text控件和filter控件的区域.

# 高级颜色模式

这个程序同样在屏幕中央显示`Hello World`.它采用了256色的颜色模式来修饰文本,而这需要您的显示器支持256色的显示.按下Q可以退出程序.

```

import urwid

def exit_on_q(key):
    if key in 'qQ':
        raise urwid.ExitMainLoop()

palette = [
    ('banner', '', '', '', '#ffa', '#60d'),
    ('streak', '', '', '', 'g50', '#60a'),
    ('inside', '', '', '', 'g38', '#808'),
    ('outside', '', '', '', 'g27', '#a06'),
    ('bg', '', '', '', 'g7', '#d06'), ]

placeholder = urwid.SolidFill()
loop = urwid.MainLoop(placeholder, palette, unhandled_input=exit_on_q)
loop.screen.set_terminal_properties(colors=256)
loop.widget = urwid.AttrMap(placeholder, 'bg')
loop.widget.original_widget = urwid.Filler(urwid.Pile([]))

div = urwid.Divider()
outside = urwid.AttrMap(div, 'outside')
inside = urwid.AttrMap(div, 'inside')
txt = urwid.Text(('banner', 'Hello World'), align='center')
streak = urwid.AttrMap(txt, 'streak')
pile = loop.widget.base_widget # .base_widget skips the decorations
for item in [outside, inside, streak, inside, outside]:
    pile.contents.append((item, pile.options()))

loop.run()

```

这个调色板仅仅定义了高级颜色模式的前景色和背景色,因为仅仅用到了高级颜色模式.但是,一个真正的程序应该定义所有的颜色.可用的前景色,背景色和设置值可以在文档`前景和背景设置`中查阅.

* **MainLoop**控件的后台会创建一个**raw_display.screen**对象来绘图.这个程序通过screen对象的`set_terminal_properties()`方法来将屏幕设置为256色.

这个示例同时演示了怎样自上而下地布局控件的方法.有些时候,在需要的控件显示出来之前,我们可能需要一个`placeholder`控件占位.

* 我们通过`MainLoop.widget`属性来改变`MainLoop`的顶级控件.

* **装饰控件**,例如`AttrMap`控件,可以通过改变它的`original_widget`属性来控制它所修饰的控件内容.

* **Divider**控件用来创建空行,也是通过AttrMap来改变颜色.

* **容器控件**例如**Pile**有一个`contents`属性,我们可以认为它是一个包含一系列`(widget, options)`元组的序列.`Pile.contents`支持通用的列表操作,例如通过`append()`来添加子控件.`Pile.options()`用来生成新的子控件的默认选项.

# 问答

这个程序将会询问你的名字,并将结果显示在下面.

```

import urwid

def exit_on_q(key):
    if key in 'qQ':
        raise urwid.ExitMainLoop()

palette = [
    ('banner', '', '', '', '#ffa', '#60d'),
    ('streak', '', '', '', 'g50', '#60a'),
    ('inside', '', '', '', 'g38', '#808'),
    ('outside', '', '', '', 'g27', '#a06'),
    ('bg', '', '', '', 'g7', '#d06'), ]

class QuestionBox(urwid.Filler):
    def keypress(self, size, key):
        if key != 'enter':
            return urwid.Filler.keypress(self, size, key)
        self.original_widget = urwid.Text(
            'Nice to meet you,\n{}.\n\nPress Q to exit.'.format(edit.edit_text))

edit = urwid.Edit('What is your name?\n')
fill = QuestionBox(edit)
loop = urwid.MainLoop(fill, unhandled_input=exit_on_q)
loop.run()

```

**Edit**控件基于`Text`控件而实现,但是它可以接受输入的文本,并可以通过`Home`键,`END`键和`方向键`来修改你输入的文本.

这里,我们用定制的`Filter`装饰控件的子类来修饰Text控件,并定义了一个新的`keypress()`函数.通过定制装饰控件或者容器控件来接受用户输入是一个很常用的Urwid应用的写法.这个模式要比将所有的按键都定义在一个`unhandled_input`函数中要易于维护得多.

* 在`QuestionBox.keypress()`函数中,除了`Enter`之外的所有按键都将会被传到默认的`Filler.Keypress()`函数中,而这个默认的函数将会把输入的字符传递到`Edit.keypress()`方法.

* 注意,即使名字中包含`q`字符,也是可以输入到`Edit`控件中,而不是导致程序退出.这是因为,`Edit.keypress`函数处理了按键并返回`None`.更多信息请参见`Widget.keypress()`的文档.

* 当输入`ENTER`的时候,子控件`original_widget`将会变更为一个`Text`控件.

* `Text`控件不会处理任何按键输入,所以所有的按键输入都将会传递到`unhandled_input`函数`exit_on_q`,这时是可以通过q退出程序的.

# 信号机制

这个程序将会询问您的名字,并在你输入名字的同时就显示你的名字.按下`DOWN`和`SPACE`或者`ENTER`来退出程序.

```

import urwid

def exit_on_q(key):
    if key in 'qQ':
        raise urwid.ExitMainLoop()

palette = [
    ('I say', 'default', 'default', 'bold'), ]
ask = urwid.Edit(('I say', 'What is your name?\n'))
reply = urwid.Text('')
button = urwid.Button('Exit')
div = urwid.Divider()
pile = urwid.Pile([ask, div, reply, div, button])
top = urwid.Filler(pile, valign='top')

def on_ask_change(edit, new_edit_text):
    reply.set_text(('I say', 'Nice to meet you, {}'.format(new_edit_text)))

def on_exit_clicked(button):
    raise urwid.ExitMainLoop()

urwid.connect_signal(ask, 'change', on_ask_change)
urwid.connect_signal(button, 'click', on_exit_clicked)

urwid.MainLoop(top, palette).run()

```

* 就像之前一样,我们创建了一个`Edit`控件和一个`Text`控件.

* **connect_signal()**函数用来绑定我们的`on_ask_change()`函数到`Edit`控件的`change`信号上.现在,每次`Edit`控件的变化都会调用`on_ask_change()`函数,并传入新的值.

* 最后,我们将`on_exit_clicked()`函数绑定到`Exit`按键的`click`信号上.

* `on_ask_change()`函数会在每次用户输入他们名字的同时,更新文本内容,而`on_exit_click()`函数用来退出.

# 多个问题

这个程序要求您循环输入名字,然后会输出`Nice to meet you, (your name).`当您按下回车的时候,屏幕显示将会更新.空行直接回车就可以退出程序.

```

import urwid

def question():
    return urwid.Pile([urwid.Edit(('I say', 'What is your name?\n'))])

def answer(name):
    return urwid.Text(('I say', 'Nice to meet you, {}\n'.format(name)))

class ConversationListBox(urwid.ListBox):
    def __init__(self):
        body = urwid.SimpleFocusListWalker([question()])
        urwid.ListBox.__init__(self, body)

    def keypress(self, size, key):
        key = urwid.ListBox.keypress(self, size, key)
        if key != 'enter':
            return key
        name = self.focus[0].edit_text
        if not name:
            raise urwid.ExitMainLoop()
        # replace or add response
        self.focus.contents[1:] = [(answer(name), self.focus.options())]
        pos = self.focus_position
        # add a new question
        self.body.insert(pos + 1, question())
        self.focus_position = pos + 1

palette = [
    ('I say', 'default', 'default', 'bold'), ]
urwid.MainLoop(ConversationListBox(), palette).run()

```

**ListBox**控件让你可以在一系列的流动控件中垂直滚动.`UP`,`DOWN`,`PAGE UP`,`PAGE DOWN`几个按键可以改变当前焦点.`list walker`用于管理`ListBox Contents`,而最简单的`list walker`就是`SimpleFocusListWalker`.

**SimpleFocusListWalker**就像一个装有控件的普通python列表一样,不管什么时候你像里面添加或者删除元素,焦点都会自动改变.

这里,我们通过子类继承并重写方法的方式定制`ListBox`的按键操作.

* `question()`函数用来生成用户交互控件.这里,我们返回了一个装有`Edit`控件的`Pile`控件.

* 我们通过`ListBox.focus`取得焦点的`Pile`对象,然后采用标准`容器对象`的方法`[0]`来获得它的第一个子对象,也就是`Edit`,然后通过`Edit.edit_text`方法获得用户输入的文本.

* 再来看程序的响应.我们可以将`Pile.contents`看作是一个`(控件, 选项)`的列表,我们通过为它的`contents[1:]`来进行赋值,以创建一个新的响应,或者替换掉已经存在的响应.我们通过`Pile.options()`来创建默认的选项.

* 至于如何添加新的问题,我们可以认为,我们在`ListBox.body`处存放的变量,`SimpleFocusListWalker`,是一个装有控件的列表.我们对这个ListWalker调用`insert()`方法,然后更新焦点的位置到我们新创建的对象,就完成了.

# 简单的菜单

我们可以通过一系列的`Button`控件来创建一个非常简单的菜单.这个程序让你选择一个选项,然后告诉你你选择了哪个选项.

```

import urwid

choices = u'选项1 选项2 选项3 选项4 选项5 选项6'.split()

def menu(title, choices):
    body = [urwid.Text(title), urwid.Divider()]
    for c in choices:
        button = urwid.Button(c)
        urwid.connect_signal(button, 'click', item_chosen, c)
        body.append(urwid.AttrMap(button, None, focus_map='reversed'))
    return urwid.ListBox(urwid.SimpleFocusListWalker(body))

def item_chosen(button, choice):
    response = urwid.Text(['You chose ', choice, '\n'])
    done = urwid.Button('Ok')
    urwid.connect_signal(done, 'click', exit_program)
    main.original_widget = urwid.Filler(urwid.Pile(
        [response, urwid.AttrMap(done, None, focus_map='reversed')]))

def exit_program(button):
    raise urwid.ExitMainLoop()

main = urwid.Padding(menu('请选择', choices), left=2, right=2)
top = urwid.Overlay(main, urwid.SolidFill('\N{MEDIUM SHADE}'),
    align='center', width=('relative', 60),
    valign='middle', height=('relative', 60),
    min_width=20, min_height=9)
urwid.MainLoop(top, palette=[('reversed', 'standout', '')]).run()

```

* `menu()`通过参数`title`和一列`Button`控件创建了一个`ListBox`控件.每个按钮的`item_chosen`都有它自己的信号,传递选项的名称.焦点下的按钮通过`AttrMap`装饰以赋予一个显示属性.

* `item_choosen()`将显示的菜单替换为用户的选项.

* `exit_program()`接受任意按键而退出.

* 这个菜单通过**Overlay**来装饰,背景为**SolidFill**.**Overlay**定义了一个最小宽度,但是当用户的命令行足够宽的时候,是可以扩展到命令行宽度的60%的.

# 多级菜单

嵌套的菜单的实现方式有很多,比如可以通过一些弹出新的菜单的按钮来实现.这个程序给了您一个嵌套的菜单,您可以按`ESC`来返回上一层.

```

import urwid

def menu_button(caption, callback):
    button = urwid.Button(caption)
    urwid.connect_signal(button, 'click', callback)
    return urwid.AttrMap(button, None, focus_map='reversed')

def sub_menu(caption, choices):
    contents = menu(caption, choices)
    def open_menu(button):
        return top.open_box(contents)
    return menu_button([caption, '...'], open_menu)

def menu(title, choices):
    body = [urwid.Text(title), urwid.Divider()]
    body.extend(choices)
    return urwid.ListBox(urwid.SimpleFocusListWalker(body))

def item_chosen(button):
    response = urwid.Text(['You chose ', button.label, '\n'])
    done = menu_button('Ok', exit_program)
    top.open_box(urwid.Filler(urwid.Pile([response, done])))

def exit_program(button):
    raise urwid.ExitMainLoop()

menu_top = menu('Main menu', [
    sub_menu('Applications', [
        sub_menu('Accessories', [
            menu_button('Text Editor', item_chosen),
            menu_button('Terminal', item_chosen)])]),
    sub_menu('System', [
        sub_menu('Preferences', [
            menu_button('Appearance', item_chosen)]),
        menu_button('Lock Screen', item_chosen)])])

class CascadingBoxes(urwid.WidgetPlaceholder):
    max_box_levels = 4

    def __init__(self, box):
        super().__init__(urwid.SolidFill('/'))
        self.box_level = 0
        self.open_box(box)

    def open_box(self, box):
        self.original_widget = urwid.Overlay(urwid.LineBox(box),
            self.original_widget,
            align='center', width=('relative', 80),
            valign='middle', height=('relative', 80),
            min_width=24, min_height=8,
            left=self.box_level*2,
            right=(self.max_box_levels - self.box_level - 1) * 3,
            top=self.box_level*2,
            bottom=(self.max_box_levels - self.box_level - 1) * 2)
        self.box_level += 1

    def keypress(self, size, key):
        if key == 'esc' and self.box_level > 1:
            self.original_widget = self.original_widget[0]
            self.box_level -= 1
        else:
            super().keypress(size, key)

top = CascadingBoxes(menu_top)
urwid.MainLoop(top, palette=[('reversed', 'standout', '')]).run()

```

* `menu_button()`返回一个`AttrMap`装饰的`Button`,并给它的`click`信号绑定了一个回调函数.子菜单和最后的的选择按钮都有回调函数.

* `sub_menu()`是一个闭包,它创建了一个可以打开一个新的菜单的按钮.注意一下这个`text markup`的用法,它在每一个`menu_button`的`caption`也就是按键名后面都加上了`'...'`.

* `menu()`是一个有标题有一系列控件的`ListBox`.

* `item_chosen()`会显示用户的选择,和之前的例子差不多.

* `menu_top()`是顶级菜单,它的所有子菜单和选项都都是通过上面的函数来构建的.

这个例子介绍了**WidgetPlaceholder**控件.`WidgetPlaceholder`控件是一个`装饰控件`,它不会对它所装饰的控件做任何事情.如果你需要一个简单的方式来重新布局一个控件,或者像这个例子一样,作为一个控件的基类来布局它的内容.

* `CascadingBoxes`是从`WidgetPlaceholder`继承而来的一个新的控件.它提供了一个`open_box()`方法,用来在顶层显示一个箱子控件.它通过`Overlay`和`LineBox`来显示.每个箱子都会相对于前一个箱子有一些移动.

* `CascadingBoxes.keypress()`拦截了`ESC`键,用以删除当前的箱子对象,并显示前一个对象.这种方式使得用户可以返回上级菜单.

# 水平菜单

暂时不打算学习.

# 冒险游戏

暂时不打算学习.



