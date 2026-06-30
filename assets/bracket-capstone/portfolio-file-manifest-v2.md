# Portfolio File Manifest v2 (V9A 升级版)

本清单用于 V9A 升级版 Capstone 作品集的文件结构验证。

> **使用说明**：在提交作品集前逐项检查。✅ = 必选（V6 基础），⭐ = 进阶（V7/V8 升级）。

## 总体结构

```
bracket-capstone-portfolio/
├── README.md                       ✅
├── requirements.md                  ✅
│
├── cad-freecad/                    ✅ V6 图形化
│   ├── bracket.FCStd               ✅
│   └── screenshots/                ⭐
│
├── exports/                         ✅ V6 导出
│   ├── bracket-v1.step             ✅
│   ├── bracket-v1.stl              ✅
│   └── components/                  ⭐ V8 拆分
│       ├── base_plate.step          ⭐
│       ├── vertical_plate.step      ⭐
│       ├── bolt.step                ⭐
│       └── side_pin.step            ⭐
│
├── cam/                             ✅ V6 CAM
│   ├── cam-task-list.md             ✅
│   ├── tool-list.csv                ✅
│   └── worksheet.md                 ✅
│
├── gcode/                           ✅ V6 G-code
│   ├── toolpath.nc                  ⭐
│   └── gcode-interpretation.md      ✅
│
├── cadquery/                        ⭐ V7 CadQuery
│   ├── plate_with_hole.py           ⭐ V7A
│   ├── plate_advanced_features.py   ⭐ V7B
│   ├── bracket_variant.py           ⭐ V7B
│   ├── bracket_capstone.py          ✅ V7C
│   └── README.md                    ⭐
│
├── assembly/                        ⭐ V8 Assembly
│   ├── bracket_assembly.py          ✅ V8A
│   ├── bracket_nested_assembly.py   ⭐ V8C
│   ├── bracket_assembly.step        ⭐
│   ├── bom.md                       ✅ V8B
│   ├── exploded_view.svg            ⭐ V8B
│   ├── placement_checklist.md       ⭐ V8C
│   └── interference_notes.md        ⭐ V8C
│
├── notes/                           ✅ 综合笔记
│   ├── design-notes.md              ⭐
│   ├── export-log.md                ⭐
│   └── self-eval.md                 ⭐
│
└── screenshots/                     ⭐ 截图
    ├── freecad-overview.png         ⭐
    ├── cadquery-render.png          ⭐
    └── assembly-overview.png        ⭐
```

## 必选 vs 进阶统计

| 类型 | 数量 | 占比 |
|------|------|------|
| ✅ 必选 | ~13 | ~46% |
| ⭐ 进阶 | ~15 | ~54% |

## 验收标准

### 基础分（V6 必选）

- [ ] 9 项 V6 必选文件全部就位
- [ ] README.md 串联 V6 完整流程
- [ ] requirements.md 已编写

### 进阶分（V7/V8 升级）

- [ ] V7 CadQuery 4 个 .py 代码文件就位
- [ ] V8 Assembly 2 个 .py 代码文件就位
- [ ] BOM 表格、爆炸图、检查清单就位
- [ ] 几何一致性已验证

### 总评

- 9-10 分（基础 + 进阶都完整）：完整综合作品集
- 6-8 分（基础完整 + 部分进阶）：基础 + 进阶
- < 6 分：仅 V6 基础

## 完整度检查清单

.. list-table:: 文件完整度检查
   :header-rows: 1
   :widths: 30 10 30 30

   * - 文件
     - 必填
     - 检查方法
     - 备注
   * - README.md
     - ✅
     - 打开看是否串联 V6/V7/V8
     - 作品集入口
   * - requirements.md
     - ✅
     - 看是否清晰
     - V6A 需求文档
   * - cad-freecad/bracket.FCStd
     - ✅
     - 用 FreeCAD 打开
     - V6 原始模型
   * - exports/bracket-v1.step
     - ✅
     - 用 FreeCAD 打开
     - V6 导出
   * - exports/components/*.step
     - ⭐
     - 4 个文件齐全
     - V8 拆分
   * - cam/cam-task-list.md
     - ✅
     - 看是否完整
     - V6 CAM
   * - gcode/gcode-interpretation.md
     - ✅
     - 看是否能解释
     - V6 G-code
   * - cadquery/bracket_capstone.py
     - ✅
     - py_compile 通过
     - V7C 核心
   * - cadquery/*.py (V7 进阶)
     - ⭐
     - 3 个 .py
     - V7A/V7B
   * - assembly/bracket_assembly.py
     - ✅
     - py_compile 通过
     - V8A 核心
   * - assembly/bracket_nested_assembly.py
     - ⭐
     - py_compile 通过
     - V8C
   * - assembly/bom.md
     - ✅
     - 看是否与 Assembly 一致
     - V8B
   * - assembly/placement_checklist.md
     - ⭐
     - 看是否完整
     - V8C
   * - notes/self-eval.md
     - ⭐
     - 看是否反思
     - V9A 自评

## 相关资源

- `bracket-project-portfolio`（V6B 模板）
- `portfolio-upgrade-template.md`（V9A 升级模板）
- `capstone-portfolio-upgrade`（V9A 升级指南）