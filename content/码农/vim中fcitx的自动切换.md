Title: vim中fcitx的自动切换
Date: 2017-07-22 20:06
Summary: 一个困扰我很久的问题。

# 问题

vim切换插入模式与命令模式的时候，总是要手动切换输入法，很烦。

# 解决

## 初步方案

```
autocmd InsertLeave * call system('fcitx-remote -c')
autocmd InsertLeave * call system('fcitx-remote -o')
```

这是在`.vimrc`中的简单配置项，`fcitx-remote`命令用来操作`fcitx`的输入法切换功能。

## 更好的方案

linux下不要重复开发轮子！

插件`fcitx.vim`完美解决了这个问题。

采用`bundle`管理插件的话，问题就很好解决了。

```
Plugin 'lilydjwg/fcitx.vim'
```

easy, 搞定。

