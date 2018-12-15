Title: Debian下搭建Hexo博客
Summary: 在Debian下搭建Hexo博客的笔记,重点是安装Node.js的过程.
Date: 2017-05-18 22:52

# 安装Node.js

访问[Node.js官网](https://nodejs.org/en/)下载稳定版本的Node.js安装程序.下载二进制文件即可.写本文的时候稳定版是`node-v6.10.3-linux-x64.tar.xz`.

## 解压

```
cd ~/Downloads
xz -d node-v6.10.3-linux-x64.tar.xz
```

## 解包

```
tar -xf node-v6.10.3-linux-x64.tar
```
## 安装

所谓安装,就是将解压好的文件复制到任意目录下.其实直接在解压好的目录中就可以用了,但是显然不方便.

推荐将解包的文件复制到usr目录中,推荐放在`/usr/local/lib/node`中.我的电脑安装了sudo,没装的切到root用户吧.什么?你没有自己电脑的root权限?拆了吧兄弟.

```
sudo mv node-v6.10.3-linux-x64 /usr/local/lib/node
```

## 软连接

创建软连接.这里我被坑了,由于不懂ln命令,用相对路径创建软连接,错误,改用绝对路径,正确.

```
sudo ln -s /usr/local/lib/node/bin/node /usr/local/bin/node
sudo ln -s /usr/local/lib/node/bin/npm /usr/local/bin/npm
```

node.js安装完毕.npm命令可用.

# 安装hexo

很简单了,直接按照中文说明做就好了.

## 安装

```
sudo npm install -g hexo-cli
```

会有警告,不用管.

安装之后同样需要链接到bin目录下,否则无法直接用hexo命令的.

## 软连接

```
sudo ln -s /usr/local/lib/node/lib/node_modules/hexo-cli/bin/hexo /usr/local/bin/node
```

愉快,hexo命令可用了.

## 开始hexo

随便找个目录创建hexo工作文件夹,我就在根目录下创建了,这条命令会在当前文件夹下创建blog根目录.

```
cd
hexo init blog
```

进入工作目录,可以开始写作了.剩下的就按照hexo帮助文档过一遍基本就会了.

