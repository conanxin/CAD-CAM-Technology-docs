# CAM 工作单说明

## 用途

本工作单配合教程页面 `examples/freecad-to-cam-worksheet` 使用，帮助读者在 FreeCAD 建模和导出完成后，系统规划 CAM 加工任务。

## 对应教程

- **建模与导出**: [FreeCAD 实操：带孔矩形板建模与导出](https://conanxin.github.io/CAD-CAM-Technology-docs/examples/freecad-plate-modeling.html)
- **导出检查**: [FreeCAD 导出 STEP/STL 检查清单](https://conanxin.github.io/CAD-CAM-Technology-docs/examples/freecad-export-checklist.html)
- **CAM 任务单**: [FreeCAD 到 CAM 加工任务单](https://conanxin.github.io/CAD-CAM-Technology-docs/examples/freecad-to-cam-worksheet.html)
- **G-code 教学**: [G-code 逐行解释与路径可视化](https://conanxin.github.io/CAD-CAM-Technology-docs/examples/gcode-toolpath-visualization.html)

## 文件清单

| 文件 | 说明 |
|------|------|
| `worksheet-template.md` | 工作单填写模板（可打印） |
| `tool-list.csv` | 刀具参数参考表 |

## 使用方法

1. 完成 FreeCAD 建模和导出（参考 V5A、V5B）
2. 阅读 `examples/freecad-to-cam-worksheet`
3. 根据实际零件和机床，填写 `worksheet-template.md`
4. 对照 `tool-list.csv` 选择合适的刀具和参数
5. 继续阅读 G-code 教学，理解 CAM 输出

---

*本工作单属于 CAD-CAM-Technology-docs 项目的一部分。*
