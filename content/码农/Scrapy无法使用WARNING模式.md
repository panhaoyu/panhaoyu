---
title: Scrapy无法使用WARNING模式
date: 2017-12-11 00:45
summary: 
---

先放一下Scrapy的报错信息。

```
:0: UserWarning: You do not have a working installation of the service_identity module: 'cannot import name 'opentype''.  Please install it from <https://pypi.python.org/pypi/service_identity> and make sure all of its dependencies are satisfied.  Without the service_identity module, Twisted can perform only rudimentary TLS client hostname verification.  Many valid certificate/hostname mappings may be rejected.
```

说的很明确，请安装`service_identity`模块。

可是呢，`service_identity`模块明明是安装了的。

再留意到报错信息中的一句话，请确保`service_identity`中的所有依赖已安装。

上pypi翻文档，文档中提到了这么四个依赖：
```
attrs
pyOpenSSL >= 0.14 (0.12 and 0.13 may work but are not part of CI anymore)
pyasn1
pyasn1-modules
```

一个一个地`pip install`一下，发现`pyasn1-modules`没装。

这就尴尬了哦，不知道pypi的包管理机制是什么样，有时间学一下。

装好，`scrapy crawl ctrip --loglevel=WARNING`，成功，不报错。

没错，就是想爬一下特价机票。