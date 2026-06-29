# CAD/CAM Technology Docs

《CAD/CAM技术基础》课程化学习文档 — 现代化 Sphinx 文档站

## 项目定位

本项目已从旧版阅读笔记升级为**课程化学习文档站**，基于 [《CAD/CAM技术基础》](http://book.douban.com/subject/5296837/) 教材，使用 Sphinx 构建为适合自学的在线课程。

- **在线版本**：https://conanxin.github.io/CAD-CAM-Technology-docs
- **当前版本**：`v0.4.0-annotated-gcode-visualization`
- **历史版本**（SAE）：http://conanxincv.sinaapp.com/project2/index.html（已归档，不再更新）

## 当前版本亮点

| 模块 | 说明 |
|------|------|
| **现代文档站** | 基于 Sphinx + Furo 主题，支持中文搜索、数学公式、响应式布局 |
| **8 章课程结构** | 完整覆盖 CAD/CAM 概论、建模、图形变换、工程分析、CAPP、数控编程、系统集成 |
| **学习辅助** | 课程总览、章节地图、复习题、词汇表、学习路径 |
| **工程案例** | 3 个完整制造案例：CAD→G-code、数据交换、CAPP 工艺路线 |
| **G-code 教学** | 逐行解释 + 路径可视化，帮助初学者理解数控程序 |

## 快速入口

| 内容 | 链接 |
|------|------|
| 课程总览 | https://conanxin.github.io/CAD-CAM-Technology-docs/course-overview.html |
| 章节地图 | https://conanxin.github.io/CAD-CAM-Technology-docs/chapter-map.html |
| 复习题 | https://conanxin.github.io/CAD-CAM-Technology-docs/practice-questions.html |
| 词汇表 | https://conanxin.github.io/CAD-CAM-Technology-docs/glossary.html |
| **工程案例：CAD 到 G-code** | https://conanxin.github.io/CAD-CAM-Technology-docs/examples/cad-to-gcode.html |
| **工程案例：数据交换格式** | https://conanxin.github.io/CAD-CAM-Technology-docs/examples/data-exchange.html |
| **G-code 逐行解释** | https://conanxin.github.io/CAD-CAM-Technology-docs/examples/gcode-toolpath-visualization.html |

## 版本演进

- **V1**（2024-06）：Sphinx/Furo 现代化，GitHub Pages 部署
- **V2**（2024-06）：课程化结构（课程总览、章节地图、复习题、每章学习结构）
- **V4A**（2024-06）：G-code 逐行解释与路径可视化（教学增强）

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
- **工程案例**：CAD→G-code（含逐行解释）、数据交换、CAPP 工艺规划

## 后续完善方向

- [x] G-code 逐行解释与路径可视化
- [x] 增加工程案例（CAD→G-code、数据交换、CAPP）
- [x] 增加 G-code / STEP / STL 示例
- [ ] 加入真实软件截图（SolidWorks / FreeCAD / Fusion）
- [ ] 增加 FreeCAD / Fusion / Mastercam 工具链示例
- [ ] 补充更多图示和公式
- [ ] 增加软件工具链说明（SolidWorks/CATIA/UG NX/Mastercam）
- [ ] 添加更多参考文献链接
- [ ] 引入 Mermaid 流程图
- [ ] 增加代码示例（Python + CAD 库）

## 贡献

欢迎提交 Issue 或 PR。
