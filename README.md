# CAD/CAM Technology Docs

《CAD/CAM技术基础》阅读笔记 — 现代化 Sphinx 文档站

## 项目定位

本项目是 [《CAD/CAM技术基础》](http://book.douban.com/subject/5296837/) 的阅读笔记，使用 Sphinx 构建为现代化文档站。

- **在线版本**：https://conanxin.github.io/CAD-CAM-Technology-docs
- **历史版本**（SAE）：http://conanxincv.sinaapp.com/project2/index.html（已归档，不再更新）

## 本地构建

```bash
# 安装依赖
python -m pip install -r requirements.txt

# 构建文档
sphinx-build -b html . _build/html

# 或者使用 Makefile
make html
```

构建完成后，打开 `_build/html/index.html` 查看。

## 技术栈

- [Sphinx](https://www.sphinx-doc.org/) — 文档构建工具
- [Furo](https://pradyunsg.me/furo/) — 现代文档主题
- [jieba](https://github.com/fxsjy/jieba) — 中文搜索分词
- MathJax — 数学公式渲染

## 内容结构

- **现代 CAD/CAM 背景**：技术发展趋势与全流程概述
- **学习路径**：推荐阅读顺序与扩展方向
- **第1章**：CAD/CAM 概论
- **第2-4章**：CAD 技术基础、图形变换、曲面/实体建模
- **第5章**：计算机辅助工程分析（有限元、优化设计）
- **第6-8章**：CAPP、数控编程、系统开发
- **词汇表**：核心术语与缩写

## 后续完善方向

- [ ] 补充更多图示和公式
- [ ] 增加章节练习题
- [ ] 添加更多参考文献链接
- [ ] 引入 Mermaid 流程图
- [ ] 增加代码示例（Python + CAD 库）

## 贡献

欢迎提交 Issue 或 PR。
