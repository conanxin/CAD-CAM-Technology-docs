.. sampledoc documentation master file, created by
   sphinx-quickstart on Tue Aug 11 05:04:40 2009.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

CAD/CAM 技术基础 — 现代工程学习站
==================================

.. raw:: html

   <div class="section hero">
     <h1>CAD/CAM Technology Docs</h1>
     <p class="tagline">
       一个从《CAD/CAM 技术基础》阅读笔记演进而来的<strong>现代化工程学习站</strong>，
       覆盖课程基础、FreeCAD 实操、STEP/STL 数据交换、CAM/G-code、Capstone 项目、
       CadQuery 代码化建模与 Assembly 装配体作品集。
     </p>
     <p class="badges">
       <a href="https://conanxin.github.io/CAD-CAM-Technology-docs/">🌐 在线站点</a>
       <a href="https://github.com/conanxin/CAD-CAM-Technology-docs">📦 GitHub 仓库</a>
       <a href="https://github.com/conanxin/CAD-CAM-Technology-docs/releases">🚀 Release Notes</a>
       <a href="project-showcase.html">🎯 项目全景</a>
     </p>
     <p style="font-size:0.85rem;color:#888;">当前版本：<strong>v0.10.0-homepage-showcase</strong> ｜ V9 系列已闭环，正向 v1.0 推进</p>
   </div>

本文档基于 `《CAD/CAM技术基础》`_ 这本书，使用 Sphinx + Furo 主题构建为现代化 GitHub Pages 站点。

**适合人群**：机械工程、工业工程、智能制造专业的学生和从业者

**学习建议**：按 :doc:`course-overview` 中的推荐顺序学习，每章先看学习目标，再读正文，最后做复习题。

源码在 `Github`_ ： ::

    git clone https://github.com/conanxin/CAD-CAM-Technology-docs.git

.. _《CAD/CAM技术基础》: http://book.douban.com/subject/5296837/

.. _Github: https://github.com/conanxin/CAD-CAM-Technology-docs

六大入口
--------

.. raw:: html

   <div class="entry-grid">

.. raw:: html

   <div class="entry-card">
     <h3>📚 课程基础</h3>
     <p>8 章系统教材，从 CAD/CAM 概论到系统集成</p>
     <p><strong>起点</strong>：<a href="course-overview.html">course-overview</a></p>
     <p><strong>关键页面</strong>：unit1-unit8、glossary、practice-questions</p>
     <a class="more" href="course-overview.html">开始 →</a>
   </div>

.. raw:: html

   <div class="entry-card">
     <h3>🛠️ FreeCAD 实操线</h3>
     <p>带孔板建模 → STEP/STL 导出 → CAM 任务单 → 五步收口</p>
     <p><strong>起点</strong>：<a href="examples/freecad-plate-modeling.html">freecad-plate-modeling</a></p>
     <p><strong>关键页面</strong>：freecad-workflow-index（V5D 收口）</p>
     <a class="more" href="examples/freecad-workflow-index.html">开始 →</a>
   </div>

.. raw:: html

   <div class="entry-card">
     <h3>📐 工程案例</h3>
     <p>CAD→G-code、数据交换、CAPP 工艺路线完整案例</p>
     <p><strong>起点</strong>：<a href="examples/cad-to-gcode.html">cad-to-gcode</a></p>
     <p><strong>关键页面</strong>：data-exchange、step-stl-mini-lab</p>
     <a class="more" href="examples/cad-to-gcode.html">开始 →</a>
   </div>

.. raw:: html

   <div class="entry-card">
     <h3>🏗️ Capstone 项目线</h3>
     <p>L 型支架综合项目 + 项目档案 + 评分表 + 路径收口</p>
     <p><strong>起点</strong>：<a href="examples/bracket-capstone-project.html">bracket-capstone-project</a></p>
     <p><strong>关键页面</strong>：capstone-learning-path（V6D 收口）</p>
     <a class="more" href="examples/capstone-learning-path.html">开始 →</a>
   </div>

.. raw:: html

   <div class="entry-card">
     <h3>🐍 CadQuery 代码化建模</h3>
     <p>Python + CadQuery 参数化建模、支架代码模型</p>
     <p><strong>起点</strong>：<a href="examples/cadquery-parametric-modeling.html">cadquery-parametric-modeling</a></p>
     <p><strong>关键页面</strong>：cadquery-learning-path（V7D 收口）</p>
     <a class="more" href="examples/cadquery-learning-path.html">开始 →</a>
   </div>

.. raw:: html

   <div class="entry-card">
     <h3>🔧 Assembly 装配体</h3>
     <p>多零件装配、BOM、爆炸图、Placement、子装配</p>
     <p><strong>起点</strong>：<a href="examples/cadquery-assembly-intro.html">cadquery-assembly-intro</a></p>
     <p><strong>关键页面</strong>：cadquery-assembly-learning-path（V8D 收口）</p>
     <a class="more" href="examples/cadquery-assembly-learning-path.html">开始 →</a>
   </div>

.. raw:: html

   <div class="entry-card">
     <h3>📦 Runtime / Portfolio 收口</h3>
     <p>作品集升级 + 运行诊断 + 本地环境 + 路线总入口</p>
     <p><strong>起点</strong>：<a href="examples/capstone-portfolio-upgrade.html">capstone-portfolio-upgrade</a></p>
     <p><strong>关键页面</strong>：cadquery-runtime-portfolio-path（V9D 收口）</p>
     <a class="more" href="examples/cadquery-runtime-portfolio-path.html">开始 →</a>
   </div>

.. raw:: html

   </div>

推荐阅读路径
------------

按读者类型给出推荐路径：

.. raw:: html

   <div class="path-card">
     <strong>🟢 零基础读者</strong>
     <ul>
       <li>:doc:`course-overview` → :doc:`workflow-roadmap` → :doc:`chapter-map`</li>
       <li>按 unit1 → unit8 系统学习，每章做 :doc:`practice-questions`</li>
       <li>最终看 :doc:`glossary` 巩固术语</li>
     </ul>
   </div>

.. raw:: html

   <div class="path-card">
     <strong>🛠️ 想做实操的读者</strong>
     <ul>
       <li>:doc:`examples/freecad-plate-modeling` → :doc:`examples/freecad-export-checklist`</li>
       <li>:doc:`examples/freecad-to-cam-worksheet` → :doc:`examples/freecad-workflow-index`</li>
       <li>完成后做 :doc:`examples/bracket-capstone-project` 综合项目</li>
     </ul>
   </div>

.. raw:: html

   <div class="path-card">
     <strong>📦 想看项目作品集的读者</strong>
     <ul>
       <li>:doc:`project-showcase` → :doc:`examples/capstone-portfolio-upgrade`</li>
       <li>:doc:`examples/cadquery-runtime-portfolio-path` → :doc:`examples/capstone-learning-path`</li>
       <li>查看 :doc:`release-showcase` 了解版本演进</li>
     </ul>
   </div>

.. raw:: html

   <div class="path-card">
     <strong>🐍 想学 CadQuery 代码建模的读者</strong>
     <ul>
       <li>:doc:`examples/cadquery-parametric-modeling` → :doc:`examples/cadquery-advanced-features`</li>
       <li>:doc:`examples/cadquery-bracket-capstone` → :doc:`examples/cadquery-learning-path`</li>
       <li>进阶：:doc:`examples/cadquery-local-environment-guide` 本地运行</li>
     </ul>
   </div>

.. raw:: html

   <div class="path-card">
     <strong>🔧 想理解 Assembly 装配体的读者</strong>
     <ul>
       <li>:doc:`examples/cadquery-assembly-intro` → :doc:`examples/cadquery-assembly-bom-checklist`</li>
       <li>:doc:`examples/cadquery-assembly-placement-mini-lab` → :doc:`examples/cadquery-assembly-learning-path`</li>
       <li>对照：:doc:`examples/step-stl-mini-lab` 看 STEP vs STL</li>
     </ul>
   </div>

项目能力矩阵
------------

.. list-table:: 项目能力矩阵
   :header-rows: 1
   :widths: 22 30 28 20

   * - 能力模块
     - 覆盖内容
     - 对应页面
     - 当前成熟度
   * - CAD/CAM 基础
     - 8 章系统教材
     - :doc:`course-overview` + unit1-8
     - ⭐⭐⭐⭐⭐
   * - FreeCAD 建模
     - 矩形板 / L 型支架 / Path Workbench
     - :doc:`examples/freecad-workflow-index`
     - ⭐⭐⭐⭐⭐
   * - STEP/STL 数据交换
     - 格式对比 / 精度 / 决策指南
     - :doc:`examples/step-stl-mini-lab`
     - ⭐⭐⭐⭐⭐
   * - CAM/G-code 理解
     - 任务单 / 刀具路径 / G-code 解读
     - :doc:`examples/gcode-toolpath-visualization`
     - ⭐⭐⭐⭐⭐
   * - Capstone 项目
     - 5 阶段支架综合项目
     - :doc:`examples/bracket-capstone-project`
     - ⭐⭐⭐⭐⭐
   * - CadQuery 代码建模
     - 参数化建模 / 圆角倒角 / 支架代码
     - :doc:`examples/cadquery-learning-path`
     - ⭐⭐⭐⭐
   * - Assembly 装配体
     - 多零件 / BOM / 子装配 / Placement
     - :doc:`examples/cadquery-assembly-learning-path`
     - ⭐⭐⭐⭐
   * - Portfolio 作品集
     - 升级版结构 / 运行诊断 / 本地环境
     - :doc:`examples/capstone-portfolio-upgrade`
     - ⭐⭐⭐⭐

v1.0 前路线图
-------------

.. raw:: html

   <div class="roadmap-block">
     <h3>从 v0.9.x 到 v1.0.0 稳定版</h3>
     <p>当前已发布 v0.9.3（V9 系列闭环），下一步进入 v1.0 准备阶段：</p>
     <ol>
       <li><strong>V10A：首页与 Showcase</strong>（本次）— 首页视觉升级 + project-showcase 全景页</li>
       <li><strong>V10B：全站质量审计</strong>— 死链 / 拼写 / Sphinx 0 warning / HTML CSS 验证</li>
     </ol>
     <ol start="3">
       <li><strong>V10C：最终发布收口</strong>— README / release notes / 导航标签完整</li>
       <li><strong>v1.0.0：稳定版发布</strong>— 长期支持里程碑</li>
     </ol>
     <p style="font-size:0.9rem;color:#666;">详细路线图：<a href="_static/diagrams/v1-roadmap.svg">v1-roadmap.svg</a></p>
   </div>

快速入口（旧版）
----------------

- **课程总览**：:doc:`course-overview` — 了解这门课解决什么问题
- **章节地图**：:doc:`chapter-map` — 快速定位每章内容与能力要求
- **学习路径**：:doc:`learning-path` — 推荐阅读顺序与扩展方向
- **工作流路线图**：:doc:`workflow-roadmap` — 从设计到制造的完整工具链认知
- **工程案例**：:doc:`examples/index` — 从 CAD 到 G-code 的完整制造流程
- **项目全景**：:doc:`project-showcase` — V10A 新增，全站模块与演进时间线
- **版本发布说明**：:doc:`release-showcase` — V1 到 V4C 的能力矩阵与教学亮点
- **词汇表**：:doc:`glossary` — 查阅 CAD/CAM 核心术语
- **复习题**：:doc:`practice-questions` — 检验学习效果

如何使用本站
------------

1. **新手入门**：从 :doc:`course-overview` 开始，建立整体框架
2. **系统学习**：按 unit1 → unit8 顺序学习，每章先看学习目标
3. **快速查阅**：使用 :doc:`chapter-map` 或搜索功能定位内容
4. **项目视角**：阅读 :doc:`project-showcase` 了解全站模块与读者入口
5. **作品集视角**：阅读 :doc:`examples/cadquery-runtime-portfolio-path` 了解 V9 闭环
6. **检验效果**：完成 :doc:`practice-questions` 中的复习题

目录
----

.. toctree::
    :maxdepth: 2

    course-overview
    chapter-map
    learning-path
    workflow-roadmap
    project-showcase
    release-showcase
    modern-cadcam-context
    unit1
    unit2
    unit3
    unit4
    unit5
    unit6
    unit7
    unit8
    glossary
    practice-questions
    examples/index

索引与搜索
==========

* :ref:`search`