《CAD/CAM技术基础》
=======================

使用sphinx整理的[《CAD/CAM技术基础》](http://book.douban.com/subject/5296837/)这本书的文档，花的时间不多，所以内容有些简略，有时间再继续整理。

模版是参考的：[sampledoc](https://github.com/matplotlib/sampledoc)

主要是修改了conf.py中的内容，然后是加入了exts/chinese_search.py中文搜索模块。

clone这个项目后，使用reStructuredText格式来修改.rst文件，然后使用命令： sphinx-build -b html ./ builddir

生成的网页就在builddir这个文件夹中。

上传到SAE上，在线版的文档：[CAD/CAM技术基础](http://conanxincv.sinaapp.com/project2/index.html)

这个文档中依然没有使用图片和公式，下次可以尝试，然后可以参考：[sampledoc tutorial](http://matplotlib.org/sampledoc/)
