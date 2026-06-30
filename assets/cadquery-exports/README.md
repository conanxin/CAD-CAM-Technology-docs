# CadQuery Exports

本目录用于存放 V9B 真实运行导出的 STEP/STL 文件。

## 当前状态

**V9B 试点结果**：当前环境**未能**真实生成 STEP/STL 文件。

详细诊断见 :doc:`examples/cadquery-runtime-export-pilot`（V9B 页面）。

## 为什么没有 STEP/STL 文件

V9B 时间点（2026-06-30）的环境状态：

- Python 3.10.12
- CadQuery 2.8.0 需要 Python 3.11+
- CadQuery 2.3.0 last Python 3.10，但需要 OCP（OpenCascade wrapper）
- OCP for Python 3.10 在 PyPI mirror 不可用
- 替代包 pythonocc-core 也不可用

**结论**：所有 .py 文件通过 py_compile 语法检查，但 CadQuery 实际运行因 OCCT 依赖不可用而失败。

## 目录用途

**当前**：

- 保留目录结构
- 包含本 README 说明
- **不**包含任何 STEP/STL 文件（避免假文件）

**未来（如果环境改善）**：

- `plate_with_hole.step` —— V7A 导出的 STEP
- `plate_with_hole.stl` —— V7A 导出的 STL
- `plate_advanced_features.step` / `.stl` —— V7B
- `bracket_capstone.step` / `.stl` —— V7C
- `bracket_assembly.step` —— V8A
- `bracket_nested_assembly.step` —— V8C

## 读者本地如何生成

如果你想在本地生成这些文件：

```bash
# 方法 1：conda（推荐）
conda create -n cadquery python=3.11
conda activate cadquery
conda install -c conda-forge cadquery

# 方法 2：pip（需要先装 OCCT 共享库）
pip install cadquery

# 验证
python -c "import cadquery as cq; print(cq.__version__)"

# 运行示例
cd /path/to/CAD-CAM-Technology-docs
python code/cadquery/plate_with_hole.py

# 生成的 STEP/STL 应该在当前目录：
# - plate_with_hole.step
# - plate_with_hole.stl
```

## 文件检查建议

生成 STEP 后，用 FreeCAD 打开：

1. 检查尺寸（外轮廓 80×50×8）
2. 检查中心孔（直径 20 mm，位置居中）
3. 检查 8 条棱边倒角（1 mm）
4. 用 FreeCAD 测量工具验证

生成 STL 后：

1. 检查三角面片数量（应该几百到几千）
2. 检查没有"破面"
3. 视觉对比 STEP 和 STL（应该看起来一致）

## 教学声明

- 本目录**不**包含任何假文件
- 当前环境受 OCCT 依赖限制
- 读者本地可参考 README 自助生成
- 教学诚信优先于"看起来完成"

## 相关页面

- V9B 主页面：:doc:`examples/cadquery-runtime-export-pilot`
- V4B STEP/STL mini-lab：:doc:`examples/step-stl-mini-lab`
- V5B 导出检查：:doc:`examples/freecad-export-checklist`