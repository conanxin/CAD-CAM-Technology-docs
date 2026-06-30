# Placement Checklist

本清单用于系统验证 V8C 嵌套装配体（`bracket_nested_assembly.py`）的组件位置和子装配组织。

> **使用说明**：在提交作品集前逐项检查。带 ✅ 的为必填项。

## 基本信息

- 装配体名称：
- 代码路径：
- 提交日期：
- 维护者：

## 坐标系检查

- [ ] ✅ **装配体全局原点 = 底板底面中心**
- [ ] ✅ **第一个 `add()` 的 loc = Location(Vector(0, 0, 0))**
- [ ] ✅ **每个组件的 Location 都以全局原点为参考**
- [ ] ✅ **子装配内的零件 Location 是相对子装配，不是全局**

## 组件位置检查

- [ ] ✅ **螺栓穿过底板安装孔** — `bolt.X = ±base_hole_spacing/2`
- [ ] ✅ **螺栓长度足以穿出底板** — `bolt_length > base_thickness`
- [ ] ✅ **立板 L 型结合底板** — `vertical.Z = base_thickness + vertical_height/2`
- [ ] ✅ **销钉穿过立板中心孔** — `pin.X = vertical_length/2`, `pin.Z = base_thickness + vertical_height/2`
- [ ] ✅ **所有紧固件留有足够间隙**

## 子装配组织

- [ ] ✅ **子装配命名语义化**（`bolt_pair` 而非 `sub1`）
- [ ] ✅ **子装配的 Location 合理**（子装配作为整体的位置）
- [ ] ✅ **子装配内零件的 Location 合理**（相对子装配）
- [ ] ✅ **主装配包含：base + vertical + bolt_pair + pin**

## 展示位置 vs 真实装配位置

- [ ] ✅ **爆炸图用于展示，教学性地拉开组件**
- [ ] ✅ **真实装配位置 = 螺栓穿过孔、销钉穿过孔**
- [ ] ✅ **不在 STEP 中把爆炸图的"拉开"距离当真**
- [ ] ✅ **观众能看到爆炸图，不会误以为是真实装配**

## 命名一致性

- [ ] ✅ 组件名与 BOM 表格一致
- [ ] ✅ 组件名与 PLACEMENT_TABLE 一致
- [ ] ✅ 组件名与 Assembly 代码中 `name=` 参数一致
- [ ] ✅ 子装配的命名与子装配内零件命名层级清晰

## 导出检查

- [ ] ✅ **用 FreeCAD 打开 STEP，目视验证**
- [ ] ✅ STEP 文件无损坏
- [ ] ✅ 子装配在 STEP 中正确显示
- [ ] ✅ 所有组件位置符合预期

## 教学型干涉检查（用结构化方法）

- [ ] ✅ **螺栓没穿入底板实体** — 验证 `bolt_location.Z < base_thickness`
- [ ] ✅ **立板没穿透底板** — 验证 `vertical_offset` 合理
- [ ] ✅ **销钉没突出立板太多** — 验证 `pin_length` 与 `vertical_thickness`
- [ ] ✅ **螺栓和销钉不重叠** — 验证 X 坐标不冲突

## 完成签名

- 提交者：________________  日期：________
- 评审者：________________  日期：________

## 教学声明

- 本清单是**教学型**的，不替代真实 CAD 内核的干涉求解
- 真实工程的干涉检查需要 OCCT 等几何内核
- 本环境因 OCCT 依赖限制不能真实运行 CadQuery

## 相关资源

- `bracket_nested_assembly.py` —— CadQuery 嵌套装配体代码
- `bracket_assembly.py` —— V8A 单层装配体（无子装配）
- `interference-check-notes-template.md` —— 干涉检查记录模板
- `assembly-bom-template.md` —— BOM 模板
- `assembly-checklist.md` —— V8B 检查清单
- `../../examples/cadquery-assembly-placement-mini-lab.rst` —— V8C 教学页面