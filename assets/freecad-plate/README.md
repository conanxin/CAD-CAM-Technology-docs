# FreeCAD 带孔矩形板教学资源包

## 用途

本资源包配合教程页面 `examples/freecad-plate-modeling` 使用，帮助读者在完成 FreeCAD 建模练习后，系统整理导出文件、记录学习过程，并为后续 STEP/STL mini-lab 和 G-code 学习建立基础。

## 对应教程

- **建模练习**: [FreeCAD 实操：带孔矩形板建模与导出](https://conanxin.github.io/CAD-CAM-Technology-docs/examples/freecad-plate-modeling.html)
- **导出检查**: [FreeCAD 导出 STEP/STL 检查清单](https://conanxin.github.io/CAD-CAM-Technology-docs/examples/freecad-export-checklist.html)
- **格式实验**: [STEP/STL 数据交换 mini-lab](https://conanxin.github.io/CAD-CAM-Technology-docs/examples/step-stl-mini-lab.html)

## 推荐文件结构

完成练习后，建议按以下结构整理你的学习文件：

```
freecad-plate/
├── freecad-plate.FCStd          ← FreeCAD 原生文件（可继续编辑）
├── freecad-plate.step           ← STEP 格式（CAD/CAM 交换）
├── freecad-plate-fine.stl       ← STL 精细网格（3D 打印）
├── freecad-plate-coarse.stl     ← STL 粗网格（快速预览）
├── notes.md                     ← 练习记录（使用提供的模板）
└── export-checklist.md          ← 导出检查清单
```

## 文件层级说明

| 文件 | 数据层级 | 用途 | 保留信息 |
|------|---------|------|---------|
| `.FCStd` | 设计层 | 继续编辑、修改参数 | 完整特征历史、草图、约束 |
| `.step` | 几何层 | CAD 系统间交换、CAM 编程 | 精确曲面、拓扑、实体边界 |
| `.stl` | 网格层 | 3D 打印、网格预览 | 三角面片近似、无拓扑 |

**重要**: 只有 `.FCStd` 可以"回退修改"。一旦导出为 STEP 或 STL，你就失去了参数化编辑能力（STEP 可有限编辑，STL 几乎不可编辑）。

## 如何使用本资源包

1. **建模阶段**: 跟随 `examples/freecad-plate-modeling` 完成建模
2. **导出阶段**: 使用 `export-checklist.md` 逐项检查后再导出
3. **记录阶段**: 用 `notes-template.md` 记录练习过程和问题
4. **验证阶段**: 对照 `file-manifest.md` 确认文件齐全
5. **学习阶段**: 带着导出的 STEP/STL 文件阅读 `step-stl-mini-lab`

## 注意

> ⚠️ **本资源包是教学示例，不是工业生产文件。**
>
> 其中的尺寸、公差、材料仅用于学习目的，不构成工程图纸或制造指令。如需用于实际加工，请咨询专业工程师并遵循相关行业标准。

---

*本资源包属于 CAD-CAM-Technology-docs 项目的一部分。*
