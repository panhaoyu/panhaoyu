Title: Pelican主题制作
Date: 2017-09-09 20:00
Summary: 自制Pelican主题

# 预备工作

工欲善其事，必先利其器。

1. 会基本的jinja2模版操作
2. 会基本的html+css+javascript设计
3. 会基本的python写法
4. 有一定的英文功底，能看得懂文档。

# 设计

首先要设计出你喜欢的Html页面。

这个就是html+css的工作了，就看你的设计功力了。

我比较喜欢的是bootstrap库，简单易用。

# 转为主题

有了html文件之后，转为pelican主题就相对简单多了。

pelican用jinja2为模版引擎，将html文件转为jinja2的格式即可。

官方文档说了，用pelican自带的simple主题开始写，可以节省工作量。simple主题在pelican库里面可以找到。

修改base.html，加入自制的导航栏。

修改article.html，改变博文的外观。

然后就是page，category，categories，index界面的小修补了。
