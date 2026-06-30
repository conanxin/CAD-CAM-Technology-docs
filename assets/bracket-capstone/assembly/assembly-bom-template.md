# Assembly BOM Template

本模板用于 V8A 装配体（`bracket_assembly.py`）的 BOM 整理。

> **使用说明**：复制本文件，按实际装配体填写。

## 项目信息

| 项目 | 值 |
|------|-----|
| 装配体名称 | bracket_assembly |
| CadQuery 代码 | `code/cadquery/bracket_assembly.py` |
| 装配体 STEP | `bracket_assembly.step`（如本地能导出） |
| 创建日期 | YYYY-MM-DD |
| 维护者 | （爸爸 / 团队） |

## BOM 表格

| 编号 | 组件名 | 数量 | 作用 | 建议材料 | 对应 CadQuery 函数 | 检查要点 |
|------|--------|------|------|----------|--------------------|----------|
| 1 | base_plate | 1 | 装配体"地面"，承载其他组件 | Q235 钢（教学示意） | `make_base_plate()` | 孔位正确、尺寸正确 |
| 2 | vertical_plate | 1 | 装配体"立面"，与底板 L 型结合 | Q235 钢（教学示意） | `make_vertical_plate()` | 销钉孔位置正确、立板高度正确 |
| 3 | mounting_bolt | 2 | 把底板固定到外部设备 | 8.8 级钢（教学示意） | `make_bolt()` | 直径 = 8 mm、长度足够 |
| 4 | side_pin | 1 | 立板与外部设备的定位 | 45 钢（教学示意） | `make_pin()` | 直径 = 6 mm、长度足够 |
| - | **合计** | **5** | - | - | - | 数量必须 = 5 |

## 字段说明

- **编号**：组件在 BOM 中的唯一标识（整数）
- **组件名**：与 CadQuery `name=` 参数保持一致
- **数量**：该组件在装配体中的出现次数
- **作用**：该组件的功能描述
- **建议材料**：教学示意值，**不可直接用于实际工程**
- **对应 CadQuery 函数**：与 `bracket_assembly.py` 中的 `make_xxx()` 函数对应
- **检查要点**：该组件需要验证的关键几何特征

## 教学声明

- 材料只是教学示意，**不可直接用于实际工程**
- 螺栓、销钉的等级和材料需要按 GB/T / ISO 标准选择
- 真实 BOM 还应包含表面处理、采购编号、单价等字段（本节简化）
- 紧固件（M 螺栓、销钉）通常**外购**，不是本车间加工

## 同步要求

- BOM 表格**必须**与 `bracket_assembly.py` 中的 `assembly.add()` 调用保持一致
- 修改 Assembly 代码后必须同步更新 BOM
- 在 PR / 评审中同时检查 Assembly 代码和 BOM 表格

## 相关资源

- `bracket_assembly.py` —— CadQuery 装配体代码
- `assembly-checklist.md` —— 装配体检查清单
- `assembly-notes-template.md` —— 装配说明模板
- `../README.md` —— 资源包总览
- `../../examples/cadquery-assembly-bom-checklist.rst` —— V8B 教学页面