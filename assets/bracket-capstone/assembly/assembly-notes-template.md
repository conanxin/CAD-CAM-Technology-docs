# Assembly Notes Template

本模板用于 V8A 装配体（`bracket_assembly.py`）的装配说明、设计修改记录、导出记录和自评记录。

> **使用说明**：在项目生命周期中持续更新本文件。

## 1. 项目概述

- **装配体名称**：bracket_assembly
- **项目目标**：（为什么做这个装配体）
- **代码版本**：（v0.8.x）
- **创建日期**：YYYY-MM-DD
- **最后更新**：YYYY-MM-DD

## 2. 组件关系

### 2.1 装配顺序

按以下顺序装配：

1. **底板**（base_plate）放在工作台上
2. **立板**（vertical_plate）从底板左侧上方垂直插入
3. **螺栓 × 2**（mounting_bolt）从底板上方穿入
4. **销钉 × 1**（side_pin）从立板外侧穿入

### 2.2 关键位置

| 组件 | X | Y | Z | 备注 |
|------|---|---|---|------|
| base_plate | 0 | 0 | 0 | 装配体原点 |
| vertical_plate | (见代码) | 0 | base_thickness + ... | 与底板 L 型结合 |
| bolt_left | -spacing/2 | base_thickness/2 | base_thickness - bolt_length | 左侧孔位 |
| bolt_right | +spacing/2 | base_thickness/2 | base_thickness - bolt_length | 右侧孔位 |
| side_pin | vertical_length/2 | vertical_thickness/2 | base_thickness + vertical_height/2 - pin_length/2 | 立板中心 |

### 2.3 紧固件

- **螺栓**：M8（教学示意），外购
- **销钉**：Φ6（教学示意），外购

## 3. 设计修改记录

| 日期 | 修改人 | 修改内容 | 影响 |
|------|--------|----------|------|
| YYYY-MM-DD | 爸爸 | 初始版本 | - |
| YYYY-MM-DD | 团队 | （示例）修改螺栓长度 | 影响 bolt_length 参数 |
| YYYY-MM-DD | 评审 | （示例）调整销钉位置 | 修改 pin Location |

## 4. 导出记录

| 日期 | 文件 | 格式 | 用途 | 检查结果 |
|------|------|------|------|----------|
| YYYY-MM-DD | bracket_assembly.step | STEP | 完整装配体 | ✅ 通过 / ❌ 未通过 |
| YYYY-MM-DD | components/base_plate.step | STEP | 加工 | ✅ / ❌ |
| YYYY-MM-DD | components/vertical_plate.step | STEP | 加工 | ✅ / ❌ |

## 5. 自评记录

### 5.1 第一次自评（YYYY-MM-DD）

- ✅ 组件完整性：所有 5 个组件齐全
- ✅ 数量正确：1 + 1 + 2 + 1 = 5
- ❌ 螺栓位置需要微调
- ✅ 销钉位置正确
- ✅ 命名规范
- 改进：调整 `bolt_left` 的 Z 坐标

### 5.2 第二次自评（YYYY-MM-DD）

- ✅ 组件完整性
- ✅ 数量正确
- ✅ 螺栓位置（已调整）
- ✅ 销钉位置
- ✅ 命名规范
- ✅ 导出 STEP 通过 FreeCAD 检查

## 6. 与 CAM 关系

- 装配体用于**理解装配关系**，**不直接用于 CAM 加工**
- 加工需要回到单件：
  - 底板：单独导出 STEP → 工艺规划 → G-code
  - 立板：单独导出 STEP → 工艺规划 → G-code
  - 螺栓 / 销钉：外购，无需加工
- 相关页面：
  - :doc:`freecad-to-cam-worksheet`
  - :doc:`freecad-path-workbench-intro`

## 7. 教学声明

- 本装配体是**教学示例**，不作为工业生产模型
- 螺栓 / 销钉 / 材料是**教学示意值**，不可直接用于实际工程
- 真实工程中应根据 GB/T / ISO 标准选择材料和紧固件

## 8. 相关资源

- `bracket_assembly.py` —— CadQuery 装配体代码
- `assembly-bom-template.md` —— BOM 模板
- `assembly-checklist.md` —— 检查清单
- `../../examples/cadquery-assembly-bom-checklist.rst` —— V8B 教学页面
- `../../examples/cadquery-assembly-intro.rst` —— V8A 教学页面