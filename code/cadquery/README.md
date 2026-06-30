# CadQuery 示例代码目录

本目录是 [CAD-CAM-Technology-docs](https://github.com/conanxin/CAD-CAM-Technology-docs) 项目的教学代码示例，配合 [`examples/cadquery-parametric-modeling.rst`](../../examples/cadquery-parametric-modeling.rst) 使用。

## 文件清单

| 文件 | 用途 |
|------|------|
| [`plate_with_hole.py`](./plate_with_hole.py) | 带孔矩形板示例：参数化建模 + STEP/STL 导出 |

## 代码用途

`plate_with_hole.py` 演示如何用 Python + CadQuery 代码生成一个带孔矩形板：

- 80 × 50 × 8 mm 的矩形板
- 中心一个直径 20 mm 的通孔
- 8 条竖直棱边各做 1 mm 倒角

代码覆盖了 CadQuery 的最基础用法：参数化建模 + 标准格式导出。

## 如何阅读

**第 1 步：先读文档**

请先阅读 [`examples/cadquery-parametric-modeling.rst`](../../examples/cadquery-parametric-modeling.rst) 的 C 节（第一个示例：带孔矩形板），文档会逐行解释每段代码的几何含义。

**第 2 步：再读代码**

打开 `plate_with_hole.py`，重点看以下区域：

- **参数集中区**：所有几何尺寸都在文件顶部，修改此处即可改变零件
- **`build_plate_with_hole()` 函数**：建模逻辑分 3 步（建板、打孔、倒角）
- **`main()` 函数**：构造几何 + 导出文件

**第 3 步：动手尝试**

- 不安装 CadQuery：直接在文本编辑器里修改 `length`、`width` 等参数，观察代码结构变化
- 安装 CadQuery：实际运行，观察生成的 STEP/STL 文件

## 本地运行

如果本地安装了 CadQuery，可以这样运行：

```bash
# 1. 安装 CadQuery
pip install cadquery

# 2. 运行示例
python plate_with_hole.py

# 3. 检查输出
ls -lh plate_with_hole.step plate_with_hole.stl
```

运行成功后会在当前目录生成两个文件：

- `plate_with_hole.step` — STEP 格式，保留 B-rep 完整几何
- `plate_with_hole.stl` — STL 格式，三角网格

## 输出文件保存建议

**重要**：本项目不强制提交生成的 STEP/STL 文件。

推荐做法：

1. **本地测试**：把 STEP/STL 文件保存到本地的 `output/` 或 `tmp/` 目录（加入 `.gitignore`）
2. **不要提交**：避免 Git 仓库被几十 KB ~ 几 MB 的二进制文件污染
3. **教学展示**：如果需要在文档中展示，建议截图后用 SVG 重画，而不是直接嵌入二进制文件

`plate_with_hole.py` 中的输出文件名是 `plate_with_hole.step` 和 `plate_with_hole.stl`（相对路径），默认会出现在当前工作目录。如果希望输出到指定目录，修改 `output_step` 和 `output_stl` 两个变量即可，例如：

```python
output_step = "output/plate_with_hole.step"
output_stl = "output/plate_with_hole.stl"
```

## 与文档站的关系

本代码目录不是独立项目，而是文档站的辅助素材。完整学习路径请参考文档站：

- 工作流总览：[`workflow-roadmap.rst`](../../workflow-roadmap.rst)
- FreeCAD 图形化版带孔板：[`examples/freecad-plate-modeling.rst`](../../examples/freecad-plate-modeling.rst)
- STEP/STL 导出检查清单：[`examples/freecad-export-checklist.rst`](../../examples/freecad-export-checklist.rst)
- STEP/STL 格式对比：[`examples/step-stl-mini-lab.rst`](../../examples/step-stl-mini-lab.rst)
- Capstone 项目线：[`examples/capstone-learning-path.rst`](../../examples/capstone-learning-path.rst)

## 环境要求

- **Python**：3.8 或更新版本
- **CadQuery**：2.0 或更新版本
- **操作系统**：Windows / macOS / Linux 均可

CadQuery 依赖较多（OCCT、PythonOCC 等），完整安装可能需要几分钟。如果本地无法安装，可以先阅读代码理解原理，不必立即动手运行。

## 教学声明

本目录下的代码是**教学示例**，不是工业级实现：

- 故意保持简洁，不追求鲁棒性
- 没有参数验证、异常处理、单元测试
- 不考虑装配体、复杂曲面、五轴加工等高级特性
- 真实工程中应根据需求选择合适的库（CadQuery / FreeCAD API / OpenCASCADE Python）

理解原理后再考虑工程化。