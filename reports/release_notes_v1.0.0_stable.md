# Release Notes: v1.0.0 - CAD/CAM Technology Docs Stable

**Tag**: `v1.0.0`
**Title**: v1.0.0 - CAD/CAM Technology Docs Stable
**Date**: 2026-07-01
**RC1 Validation**: v1.0.0-rc1 验证通过（V10D）

## Overview

这是 **CAD/CAM Technology Docs** 的第一个稳定版（v1.0.0）。从 v0.2.0 的课程化结构开始，经历了 v3-v4 工程案例化、v5-v6 FreeCAD 实操 + Capstone 项目、v7-v9 CadQuery 代码建模 + Assembly + Runtime/Portfolio、v10 首页 Showcase + 全站质量审计，最终形成完整的工程学习站。

## 项目定位

**CAD/CAM Technology Docs** 是一个从《CAD/CAM 技术基础》阅读笔记演进而来的**现代化工程学习站**，覆盖课程基础、FreeCAD 实操、STEP/STL 数据交换、CAM/G-code、Capstone 项目、CadQuery 代码化建模与 Assembly 装配体作品集。

**核心特点**：

- 课程化结构（8 章基础教材）
- 完整的工程案例（CAD→G-code、数据交换、CAPP）
- 实战线（FreeCAD 五步路线 + Capstone 项目）
- 代码化建模（CadQuery + Assembly）
- 作品集归档（V9 Runtime / Portfolio）
- 现代化站点（Hero / 入口矩阵 / 推荐路径 / 能力矩阵 / v1.0 路线图）

## 入口链接

- **在线站点**：https://conanxin.github.io/CAD-CAM-Technology-docs/
- **GitHub 仓库**：https://github.com/conanxin/CAD-CAM-Technology-docs
- **GitHub Releases**：https://github.com/conanxin/CAD-CAM-Technology-docs/releases
- **项目全景页**：https://conanxin.github.io/CAD-CAM-Technology-docs/project-showcase.html

## 从旧笔记到现代课程站的演进

| 阶段 | 时间 | 主要交付 |
|------|------|---------|
| V1-V2 | 2024-06 | 旧 Sphinx 笔记 → 现代化 Sphinx + Furo + GitHub Pages；课程化结构（unit1-unit8） |
| V3-V4C | 2024-06 | 工程案例（CAD→G-code、数据交换、CAPP）+ G-code 教学 + STEP/STL mini-lab + 工具链路线图 |
| V5A-V5D | 2024-06 | FreeCAD 实操线（建模 → 导出 → CAM → 收口） |
| V6A-V6D | 2024-06 | 支架 Capstone 项目线（5 阶段 + 项目档案 + 评分表 + 路径收口） |
| V7A-V7D | 2024-06 | CadQuery 代码化建模线（参数化 → 进阶特征 → 支架代码 → 学习路径） |
| V8A-V8D | 2024-06 | CadQuery Assembly 装配体线（多零件 → BOM → Placement → 学习路径） |
| V9A-V9D | 2026-07 | Runtime / Portfolio 作品集收口线 |
| V10A | 2026-07 | 首页 Showcase 化 + project-showcase 全景页 |
| V10B | 2026-07 | 全站质量审计（v1.0 readiness: READY） |
| **V10C** | **2026-07** | **最终发布收口（本版本）** |
| **v1.0.0** | **本次** | **稳定版发布** |

## 主要功能模块

### 课程基础
- 8 章完整教材（unit1-unit8）
- 学习辅助（章节地图、词汇表、复习题、学习路径）
- 课程总览、章节地图

### 工程案例
- CAD → G-code 完整制造流程
- 数据交换（STEP/STL/IGES 等格式）
- CAPP 工艺路线

### FreeCAD 实操线（V5A-V5D）
- 带孔矩形板建模 + STEP/STL 导出
- 导出检查清单
- CAM 任务单
- 五步学习路线收口

### Capstone 项目线（V6A-V6D）
- L 型支架综合项目（5 阶段）
- 项目档案 + 评分表
- Path Workbench 入门
- 项目线收口

### CadQuery 代码化建模线（V7A-V7D）
- Python + CadQuery 参数化建模
- 圆角/倒角/孔阵列/支架变体
- 完整 L 型支架代码模型（与 V6A 几何一致）
- V7 系列三步走收口

### Assembly 装配体线（V8A-V8D）
- 多零件装配（Location 概念）
- BOM + 爆炸图 + 检查清单
- 子装配 + 干涉检查
- V8 系列三步走收口

### Runtime / Portfolio 路线（V9A-V9D）
- Capstone 作品集升级（V9A）
- CadQuery 真实运行试点（V9B）
- CadQuery 本地环境指南（V9C）
- CadQuery 运行与作品集路线（V9D）

### Showcase 首页（V10A）
- Hero 区块（项目定位 + 当前版本 + GitHub 入口）
- 六大入口矩阵（卡片式）
- 推荐阅读路径（5 种读者类型）
- 项目能力矩阵
- v1.0 前路线图
- 项目全景页（project-showcase）

## 质量门摘要

| 指标 | 结果 |
|------|------|
| **Sphinx 构建** | ✅ 0 warning |
| **py_compile code/cadquery** | ✅ 6/6 OK |
| **py_compile scripts/cadquery** | ✅ 4/4 OK |
| **本地链接审计** | ✅ 47 HTML / 3,654 引用 / 0 broken |
| **线上关键页面** | ✅ 13/13 HTTP 200（首页 / project-showcase / V9B-D / search 等）|
| **README 必含元素** | ✅（一句话定位 / 快速入口 / 能力矩阵 / 版本演进 / v1.0 Roadmap）|
| **Release/tag 基线** | ✅ 一致 |

## 已知限制

### 1. 云端环境未能真实运行 CadQuery/OCP

**限制**：当前 GitHub Pages / Sphinx 构建环境为 Ubuntu + Python 3.10 + 无 OCCT 共享库。

**影响**：

- 6 个 CadQuery .py 文件通过 `py_compile` 语法检查，但 `import cadquery` 因 OCCT 不可用而失败
- 云端不能真实生成 STEP/STL 文件
- `scripts/cadquery/smoke_test.py` 在云端运行会失败

**替代方案**：

- 读者按 :doc:`cadquery-local-environment-guide` 在本地配置环境
- 推荐 conda 路线（自动处理 OCCT 二进制）
- 备选 pip 路线（需 Python 3.11+）

### 2. 不提交伪造 STEP/STL

**原则**：教学诚信优先于"看起来完成"。

**具体措施**：

- `assets/cadquery-exports/` 目录仅包含 README 说明，不包含假 STEP/STL 文件
- 所有 .gitignore 已忽略 `*.step/*.stp/*.stl`（本地导出默认不提交）
- 真实的导出文件由读者按本地指南生成

### 3. 真实导出需按本地环境指南操作

读者如需在本地运行 CadQuery：

1. 阅读 :doc:`cadquery-local-environment-guide`（V9C）
2. 选择路线：conda（推荐）或 pip + Python 3.11+
3. 运行 smoke test 验证环境
4. 运行 V7/V8 示例，导出 STEP/STL
5. 用 `verify_exports.py` 验证导出文件格式

## 后续路线

v1.0.0 稳定版发布后，下一步可选方向：

1. **真实软件截图** — 加入 SolidWorks / FreeCAD / Fusion 等软件的真实截图
2. **第二 Capstone** — 带圆角/倒角/多特征的 Capstone 综合项目
3. **真实 CadQuery 环境运行结果** — 用 conda 在本地生成真实 STEP/STL 并归档
4. **教学视频或录屏** — 录屏演示完整作品集提交流程
5. **第二 Showcase 增强** — 增加 Mermaid 流程图、动态元素

## v1.0.0 与 V10A/V10B 的关系

| 版本 | 角色 |
|------|------|
| V10A | 首页 Showcase 化（视觉升级） |
| V10B | 全站质量审计（v1.0 readiness: READY） |
| V10C | 最终发布收口（v1.0.0 release candidate 准备） |
| **v1.0.0** | **稳定版发布（长期支持里程碑）** |

## Build & Verification

| 项目 | 结果 |
|------|------|
| Build Command | `sphinx-build -b html -W --keep-going . _build/html` |
| Build Result | ✅ succeeded |
| Warning Count | **0** |
| py_compile code/cadquery/*.py | ✅ 6/6 OK |
| py_compile scripts/cadquery/*.py | ✅ 4/4 OK |
| Local Link Audit | ✅ 0 broken / 3,654 refs |
| Online URL Audit | ✅ 13/13 HTTP 200 |
| Release/Tag Consistency | ✅ |

## Teaching Notes

- 不新增大型课程内容
- 不重写 unit1~unit8
- 不破坏已完成的 V5/V6/V7/V8/V9 页面
- 不引入后端、数据库或复杂前端
- 保持 Sphinx + Furo + GitHub Pages 静态站路线
- 教学诚信：不伪造 STEP/STL 文件

---

_Released by OpenClaw Agent (longxia2) on 2026-07-01._

_This is the first stable release (v1.0.0) of CAD/CAM Technology Docs._