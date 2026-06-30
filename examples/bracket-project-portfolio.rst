========================================
Bracket Capstone 项目档案
========================================

本页面提供 L 型支架 Capstone 项目的档案模板和使用方法。完成 V6A 项目后，使用本页面的模板整理你的项目档案。

A. 为什么需要项目档案
======================

完成 Capstone 项目后，你可能面临以下问题：

- 几个星期后忘记了当时为什么做某个决策
- 想向别人展示自己的项目，但文件散落各处
- 想复盘学习过程，但缺少记录
- 找工作时需要项目证据，但只有零散文件

项目档案帮助你解决这些问题：

- 记录关键决策的"为什么"，而不仅是"怎么做"
- 整理所有产出物到一个清晰的目录结构
- 提供完整的项目复盘材料
- 作为学习成果的可展示证据

B. 项目档案包含什么
====================

一个完整的 Bracket Capstone 项目档案应包含以下 9 大类内容：

1. **项目基本信息**：项目名称、完成日期、耗时、完成人
2. **需求分析**：零件功能、材料选择理由、关键尺寸与公差
3. **CAD 建模记录**：建模顺序、草图约束情况、模型截图
4. **STEP/STL 导出记录**：文件信息、文件大小、验证结果
5. **导出检查结果**：18 项检查的逐项结果
6. **CAM 工艺规划**：工序列表、装夹方案、加工顺序逻辑
7. **G-code 理解**：至少 5 行 G-code 解读、与工序的对应
8. **反思笔记**：困难、解决方法、学到的技术、计划
9. **自评分**：根据评分表给自己打分

C. 项目档案目录结构
====================

推荐的目录结构：

```
bracket-capstone/
├── 01-requirements/
│   └── requirements.md
├── 02-models/
│   ├── bracket.FCStd
│   ├── bracket-v1.step
│   └── bracket-v1.stl
├── 03-export/
│   └── export-checklist.md
├── 04-cam/
│   ├── cam-task-list.md
│   ├── tool-list.csv
│   └── worksheet-template.md
├── 05-gcode/
│   ├── bracket.gcode
│   ├── gcode-notes.md
│   └── reference/  (可选：教学参考 G-code)
│       └── bracket-demo-teaching.gcode
├── 06-reflection/
│   └── reflection.md
└── README.md  (项目档案主页)
```

每个目录对应项目的一个阶段，方便整理和复盘。

D. 如何使用本模板
==================

步骤 1：下载模板
----------------

下载 ``assets/bracket-capstone/portfolio-template.md`` 到你的项目目录。

步骤 2：逐项填写
----------------

按照模板的 8 个章节，逐项填写你的项目内容。建议按以下顺序：

1. 先填写"项目基本信息"和"需求分析"（最容易）
2. 再填写"CAD 建模记录"（对照你的 FreeCAD 文件）
3. 然后填写"STEP/STL 导出记录"和"导出检查结果"（对照你的导出文件）
4. 接着填写"CAM 工艺规划"（对照你的 worksheet）
5. 再填写"G-code 理解"（对照你的 G-code 文件）
6. 最后撰写"反思笔记"（项目完成后立即写，趁记忆清晰）

步骤 3：自评分
---------------

参考 ``bracket-assessment-rubric.rst`` 页面，使用评分表给自己打分。

步骤 4：提交包检查
-------------------

使用 ``submission-checklist.md`` 检查你的提交包是否完整。

步骤 5：归档
------------

将完整的项目档案打包（.zip），保存到：

- 个人备份（云盘、外部硬盘）
- 学习展示（GitHub、个人网站）
- 求职材料（作品集）

E. 配套资源
============

本仓库提供了完整的资源包：

- ``assets/bracket-capstone/README.md`` — 资源包说明
- ``assets/bracket-capstone/portfolio-template.md`` — 项目档案模板
- ``assets/bracket-capstone/submission-checklist.md`` — 提交清单
- ``assets/bracket-capstone/reflection-template.md`` — 反思笔记模板
- ``assets/bracket-capstone/rubric-summary.md`` — 评分标准摘要

F. 常见问题
============

Q1：项目档案和提交清单有什么区别？
------------------------------------

A：项目档案是完整的项目记录（包含所有细节），提交清单是检查文件是否齐全的工具。先完成项目档案，再用提交清单检查。

Q2：项目档案必须用 Markdown 格式吗？
------------------------------------

A：推荐使用 Markdown 格式（与本站一致），便于版本控制和阅读。也可以使用其他格式（Word、PDF），但 Markdown 更适合技术文档。

Q3：项目档案需要多详细？
------------------------

A：至少要让 6 个月后的自己（或其他人）能看懂你当时为什么这么做、怎么做的。参考评分表的"深度"维度。

Q4：反思笔记需要多长？
----------------------

A：建议 500-1000 字。太短无法深入反思，太长可能偏离重点。

Q5：项目档案可以公开吗？
------------------------

A：可以。如果你在 GitHub 上公开，这本身就是很好的学习展示。注意不要包含敏感信息（如真实姓名、联系方式）。

相关页面
========

- :doc:`bracket-capstone-project`：V6A 主项目页面
- :doc:`bracket-assessment-rubric`：V6B 评分表页面
- :doc:`freecad-path-workbench-intro`：V6C FreeCAD Path Workbench 入门
- :doc:`freecad-plate-modeling`：V5A 建模基础
- :doc:`freecad-export-checklist`：V5B 导出检查
- :doc:`freecad-to-cam-worksheet`：V5C CAM 任务规划
- :doc:`gcode-toolpath-visualization`：V4A G-code 理解
- :doc:`freecad-workflow-index`：V5D 五步学习路线总览
