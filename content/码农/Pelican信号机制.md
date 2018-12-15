Title: Pelican信号机制
Summary: Pelican的信号机制测试并记录
Date: 2017-09-09 23:00

# 想法

Pelican写插件必然离不开信号机制，而在看不懂Pelican源码的情况下，用这种曲线救国的方式来了解一下Pelican的内部实现。

别问我为啥不看文档，我看得懂，但文档的介绍太少了。

# 结论

先把结论仍出来方便查阅。

## 操作markdown字符串

没发现什么好用的信号用于操作markdown字符串，可用markdown插件实现。

## 操作html字符串

article_generator_write_article信号用于在每次写入文章之前调用，它的content参数的_content属性是markdown渲染之后的html字符串。

# 信号次序

## 初始化


initialized

readers_init

get_generators

readers_init

generator_init

article_generator_init

readers_init

generator_init

page_generator_init

readers_init

generator_init

static_generator_init

## 遍历文章

这三个信号在遍历每一篇文章时都会发出一次。

{

article_generator_preread

article_generator_context

content_object_init

}

\* 30

## 暂不分析

article_generator_pretaxonomy


article_generator_finalized

page_generator_preread

page_generator_context

content_object_init

page_generator_finalized

static_generator_finalized

all_generators_finalized

get_writer

## 写入文件

{

article_generator_write_article

content_written

} * 30

## 暂不分析

{

content_written

} * 15

article_writer_finalized

content_written

page_writer_finalized

finalized
