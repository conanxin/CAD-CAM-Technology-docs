# Portfolio Upgrade Template

本模板用于 V9A 升级版 Capstone 作品集（V6/V7/V8 综合）的说明文档结构。

> **使用说明**：复制本文件，按实际作品集内容填写。

## 1. 项目信息

| 项目 | 值 |
|------|-----|
| 作品集名称 | bracket-capstone-portfolio |
| 维护者 | （爸爸 / 团队） |
| 提交日期 | YYYY-MM-DD |
| 涉及学习线 | V6 + V7 + V8 |

## 2. 项目目标

简述项目背景和目标：

- 这个支架 Capstone 是什么？
- 为什么做这个项目？
- 涉及哪些学习能力？

## 3. 图形化建模过程（V6A）

描述 FreeCAD 操作步骤：

- 使用的工作区（Part Design / Path）
- 关键特征（底板/立板/孔/圆角/倒角）
- 草图约束策略
- 引用 `cad-freecad/bracket.FCStd`

## 4. 导出文件说明（V6 + V5B）

- `exports/bracket-v1.step`（完整装配体 STEP）
- `exports/bracket-v1.stl`（完整 STL）
- `exports/components/base_plate.step`（拆分单件 STEP）
- `exports/components/vertical_plate.step`
- `exports/components/bolt.step`
- `exports/components/side_pin.step`
- 导出检查清单结果（参考 `freecad-export-checklist`）

## 5. CAM/G-code 理解（V6 + V5C + V4A）

- `cam/cam-task-list.md` —— 加工任务列表
- `cam/tool-list.csv` —— 刀具清单
- `cam/worksheet.md` —— 加工工作单
- `gcode/toolpath.nc` —— G-code 程序
- `gcode/gcode-interpretation.md` —— G-code 解读笔记

## 6. CadQuery 参数化模型（V7）

- `cadquery/plate_with_hole.py`（V7A 基础示例）
- `cadquery/plate_advanced_features.py`（V7B 进阶示例）
- `cadquery/bracket_variant.py`（V7B 简化支架）
- `cadquery/bracket_capstone.py`（V7C 完整支架，与 V6A 几何一致）

**几何一致性验证**：

- 用 FreeCAD 打开 V7C 的 `bracket_capstone.step`
- 与 V6A 的 `bracket-v1.step` 视觉对比
- 用 FreeCAD 测量关键尺寸
- 记录验证结果到 `notes/`

## 7. Assembly / BOM（V8）

- `assembly/bracket_assembly.py`（V8A 多零件装配体）
- `assembly/bracket_nested_assembly.py`（V8C 子装配 + PLACEMENT_TABLE）
- `assembly/bracket_assembly.step`（完整装配体 STEP）
- `assembly/bom.md`（V8B BOM 表格）
- `assembly/exploded_view.svg`（V8B 爆炸图）
- `assembly/placement_checklist.md`（V8C Placement 检查）
- `assembly/interference_notes.md`（V8C 干涉检查记录）

## 8. 遇到的问题

列出 V6/V7/V8 过程中遇到的关键问题：

- 问题 1：...
- 解决方法：...
- 反思：...

## 9. 自评与下一步

### 9.1 自评清单

参考 `capstone-portfolio-upgrade` 页面的自评清单：

- [ ] 9 项必选检查全部通过
- [ ] README 串联了 V6/V7/V8 三条线
- [ ] 几何一致性已验证
- [ ] BOM 表格与 Assembly 代码一致

### 9.2 进阶方向

- [ ] 真实软件截图（SolidWorks / FreeCAD / Fusion 360）
- [ ] OCCT 真实环境运行 CadQuery
- [ ] 第二 Capstone（带圆角/倒角/多特征）

## 10. 相关资源

- `bracket-project-portfolio`（V6B 模板）
- `cadquery-learning-path`（V7D 收口）
- `cadquery-assembly-learning-path`（V8D 收口）
- `capstone-learning-path`（V6D 项目线收口）
- `capstone-portfolio-upgrade`（V9A 升级指南）