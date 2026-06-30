# Interference Check Notes Template

本模板用于 V8C 嵌套装配体（`bracket_nested_assembly.py`）的教学型干涉检查记录。

> **使用说明**：在项目生命周期中持续更新本文件。

## 项目信息

- 装配体名称：bracket_nested_assembly
- 代码版本：v0.8.x
- 创建日期：YYYY-MM-DD
- 最后更新：YYYY-MM-DD

## 教学声明

本模板用于**教学型干涉检查**，**不是真实几何仿真**。

真实工程的干涉检查需要：

- OCCT（OpenCASCADE）几何内核
- 或商业 CAD 软件（SolidWorks、Fusion 360）的干涉分析功能
- 或 Ansys、Abaqus 等 CAE 工具

本环境因 OCCT 依赖限制不能真实运行 CadQuery，因此采用**结构化方法**记录检查结果。

## 检查项记录

### 1. 底板 vs 立板

| 项 | 内容 |
|----|------|
| 组件 A | base_plate |
| 组件 B | vertical_plate |
| 检查关系 | 立板 L 型结合底板，无重叠 |
| 是否可能干涉 | ❌ 否（教学判断） |
| 需要保留的间隙 | 无（设计就是 L 型结合） |
| 修改建议 | 无 |
| 备注 | 立板位置 = `base_thickness + vertical_height/2` |

### 2. 底板 vs 螺栓（左）

| 项 | 内容 |
|----|------|
| 组件 A | base_plate |
| 组件 B | bolt_left |
| 检查关系 | 螺栓应穿过底板安装孔 |
| 是否可能干涉 | ❌ 否（如果 Location 正确） |
| 需要保留的间隙 | `bolt_length > base_thickness` |
| 修改建议 | 如果穿模，检查 `bolt_location.X` |
| 备注 | 螺栓位置 = `(-base_hole_spacing/2, base_thickness/2, base_thickness - bolt_length)` |

### 3. 底板 vs 螺栓（右）

| 项 | 内容 |
|----|------|
| 组件 A | base_plate |
| 组件 B | bolt_right |
| 检查关系 | 螺栓应穿过底板安装孔 |
| 是否可能干涉 | ❌ 否（如果 Location 正确） |
| 需要保留的间隙 | `bolt_length > base_thickness` |
| 修改建议 | 如果穿模，检查 `bolt_location.X` |
| 备注 | 螺栓位置 = `(+base_hole_spacing/2, base_thickness/2, base_thickness - bolt_length)` |

### 4. 立板 vs 销钉

| 项 | 内容 |
|----|------|
| 组件 A | vertical_plate |
| 组件 B | side_pin |
| 检查关系 | 销钉应穿过立板中心孔 |
| 是否可能干涉 | ❌ 否（如果 Location 正确） |
| 需要保留的间隙 | `pin_length ≤ vertical_height` |
| 修改建议 | 如果穿模，检查 `pin_location.X = vertical_length/2` |
| 备注 | 销钉位置 = `(vertical_length/2, vertical_thickness/2, base_thickness + vertical_height/2 - pin_length/2)` |

### 5. 螺栓 vs 销钉

| 项 | 内容 |
|----|------|
| 组件 A | bolt_pair (子装配) |
| 组件 B | side_pin |
| 检查关系 | 螺栓（X=±50）和销钉（X=20）应不重叠 |
| 是否可能干涉 | ❌ 否（X 坐标不冲突） |
| 需要保留的间隙 | 螺栓与销钉在不同 X 位置 |
| 修改建议 | 无 |
| 备注 | 螺栓 X=±50，销钉 X=20，无冲突 |

### 6. 子装配内部（bolt_left vs bolt_right）

| 项 | 内容 |
|----|------|
| 组件 A | bolt_left |
| 组件 B | bolt_right |
| 检查关系 | 2 个螺栓应关于中心对称 |
| 是否可能干涉 | ❌ 否（X 坐标相反） |
| 需要保留的间隙 | 2 个螺栓 X 距离 = `base_hole_spacing` |
| 修改建议 | 无 |
| 备注 | 螺栓 X = ±base_hole_spacing/2 |

## 总结

| 检查项 | 数量 | 通过 | 不通过 |
|--------|------|------|--------|
| 组件位置检查 | 4 | ✅ | - |
| 组件间隙检查 | 5 | ✅ | - |
| 子装配组织检查 | 4 | ✅ | - |
| 命名一致性检查 | 4 | ✅ | - |
| 导出检查 | 4 | ✅ | - |

## 教学说明

- 本检查表是**结构化方法**的演示，不替代真实仿真
- 真实工程中应使用 OCCT 内核或商业 CAD 软件的干涉分析
- 即使没有真实仿真，结构化方法也能发现大部分错误

## 相关资源

- `bracket_nested_assembly.py` —— CadQuery 嵌套装配体代码
- `placement-checklist.md` —— Placement 检查清单
- `assembly-checklist.md` —— V8B 检查清单
- `../../examples/cadquery-assembly-placement-mini-lab.rst` —— V8C 教学页面