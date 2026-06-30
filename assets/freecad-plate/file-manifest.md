# 文件清单

## 说明

本清单列出完成 FreeCAD 带孔矩形板练习后，建议整理的学习文件。其中 **粗体** 表示由读者在练习中自行生成的文件，*斜体* 表示本仓库提供的教学参考文件。

## 文件清单

| 文件 | 类型 | 来源 | 用途 |
|------|------|------|------|
| **freecad-plate.FCStd** | FreeCAD 原生 | 读者生成 | 保存建模参数，可继续编辑 |
| **freecad-plate.step** | STEP 格式 | 读者生成 | CAD 系统间交换、CAM 编程 |
| **freecad-plate.stl** | STL 网格 | 读者生成 | 3D 打印、网格预览 |
| *freecad-plate-dimensions.svg* | 尺寸图 | 仓库提供 | 教学参考尺寸 |
| *export-checklist.md* | 检查清单 | 仓库提供 | 导出前逐项核对 |
| *notes.md* | 练习记录 | 读者使用模板填写 | 记录学习过程和问题 |

## 文件层级关系

```
设计层 (FCStd)
    ↓ 导出
几何层 (STEP)
    ↓ 精确 CAM/CAE
网格层 (STL)
    ↓ 3D 打印/预览
```

**关键原则**: FCStd 是"源文件"，STEP 和 STL 是"派生文件"。修改设计时，应回到 FCStd 修改，然后重新导出。

## 哪些文件需要保留？

### 必须保留
- `freecad-plate.FCStd` — 唯一可编辑的源文件
- `freecad-plate.step` — 如果需要在其他 CAD 中继续工作

### 建议保留
- `freecad-plate.stl` — 如果计划 3D 打印
- `notes.md` — 记录学习心得和遇到的问题

### 可以删除
- 中间版本的 STL（如 `freecad-plate-v1-coarse.stl`）— 保留最新版本即可
- 失败的导出尝试 — 清理工作空间

## 后续学习路径

带着这些文件，你可以继续：

1. **对照格式实验**: 阅读 `examples/step-stl-mini-lab`，对比你的 STEP 和 STL 文件
2. **进入 CAM 环节**: 了解如何从 STEP 模型生成刀具路径
3. **3D 打印实践**: 用 STL 文件在 Cura/PrusaSlicer 中切片并打印

---

*本清单属于 CAD-CAM-Technology-docs 项目的一部分。*
