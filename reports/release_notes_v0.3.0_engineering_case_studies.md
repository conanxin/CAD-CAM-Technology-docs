# Release Notes — v0.3.0-engineering-case-studies

**发布时间：** 2026-06-29  
**Tag：** `v0.3.0-engineering-case-studies`  
**Commit：** `263eccb`  
**Pages URL：** https://conanxin.github.io/CAD-CAM-Technology-docs

---

## 版本定位

从“课程化知识笔记”升级为“可用于自学和展示的工程案例型课程站”。

---

## 新增内容

### 工程案例（examples/）

新增 3 个完整制造案例，每个案例均包含场景设定、详细流程、与课程章节关联：

| 案例 | 主题 | 核心内容 |
|------|------|----------|
| **A** | CAD 到 G-code | 带孔矩形板完整加工流程，含 8 步工序、刀具选择、G-code 示例、质检要求 |
| **B** | 数据交换格式 | STEP / STL / IGES / DXF / G-code 格式对比，跨系统协作，常见问题与解决方案 |
| **C** | CAPP 工艺路线 | 阶梯轴工艺规划，含毛坯选择、9 道工序、机床/刀具/夹具清单、工艺卡片 |

### 案例图示

新增 3 个 SVG 流程图：

- `cad-to-gcode-pipeline.svg` — CAD→G-code 完整流程
- `data-exchange-formats.svg` — 数据交换格式与系统流转
- `capp-process-plan.svg` — CAPP 工艺路线设计流程

### 其他更新

- **examples/index.rst** — 案例总览页，含学习目标、阅读顺序、与课程章节对应关系
- **index.rst** — 新增工程案例入口
- **README.md** — 更新为展示友好版本，含快速入口表格和版本亮点

---

## 线上验收结果

| 检查项 | 结果 |
|--------|------|
| 首页 `/` | HTTP 200 ✅ |
| 课程总览 | HTTP 200 ✅ |
| 章节地图 | HTTP 200 ✅ |
| 复习题 | HTTP 200 ✅ |
| unit1~unit8 | HTTP 200 ✅ (8/8) |
| 案例总览 `/examples/index.html` | HTTP 200 ✅ |
| 案例 A `/examples/cad-to-gcode.html` | HTTP 200 ✅ |
| 案例 B `/examples/data-exchange.html` | HTTP 200 ✅ |
| 案例 C `/examples/capp-process-plan.html` | HTTP 200 ✅ |
| 搜索页 | HTTP 200 ✅ |
| SVG 静态资源 | HTTP 200 ✅ (7/7) |
| CSS 静态资源 | HTTP 200 ✅ (2/2) |
| **总计** | **20/20 HTTP 200** |

---

## 构建验证

```bash
sphinx-build -b html -W --keep-going . _build/html
```

结果：**build succeeded，0 warnings**

---

## 已知限制

- 工程案例以教学示例为主，不追求工业级完整性
- G-code 示例为教学用途，不建议直接在真实机床上运行
- 软件工具链示例（SolidWorks / FreeCAD / Mastercam）尚未加入

---

## 后续建议

1. **V4 工具链示例**：增加 FreeCAD / Fusion 360 / Mastercam 操作截图和说明
2. **小型项目练习**：设计完整零件（如手机支架），从建模到 G-code
3. **视频/动画**：关键流程（如刀具路径）可考虑加入动画说明

---

*Release closed by 辛 🔮*
