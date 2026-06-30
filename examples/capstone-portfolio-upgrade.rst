=======================================================
Capstone 作品集升级：加入 CadQuery 与 Assembly 成果
=======================================================

本页是 V6 Capstone 项目线、V7 CadQuery 单零件代码化建模线、V8 CadQuery Assembly 装配体线的**整合收口页** 。学完 V6 + V7 + V8 后，读者应该能够把三条学习线的成果** 合并为一个更完整的 Capstone 作品集**。

本页面是 V6A/V6B/V7C/V8A/V8B/V8C 的"组合提交"指南，而不是 V6 项目制学习的替代品。

A. 本页解决什么问题
====================

V6 已经完成支架 Capstone 项目与作品集提交
-------------------------------------------

V6A 的 :doc:`bracket-capstone-project` 用 FreeCAD 完成了 L 型支架，V6B 的 :doc:`bracket-project-portfolio` 提供了 9 大类项目内容和推荐目录结构。但 V6 时代还没有 CadQuery 成果。

V7 新增 CadQuery 代码化建模成果
--------------------------------

V7A-V7D 演示了如何用 CadQuery 代码化建模生零件，V7C 的 :doc:`cadquery-bracket-capstone` 提供了与 V6A 几何一致的代码化版本。

V8 新增 Assembly / BOM / 装配检查成果
-------------------------------------------

V8A-V8D 演示了如何用 CadQuery Assembly 表达多零件装配体，BOM、爆炸图、检查清单提供了工程表达方法。

升级目标
--------

将 V6/V7/V8 三条线合并为一个** 综合 Capstone 作品集**：

- 保留 V6 图形化建模（作品集必选）
- 加入 V7 CadQuery 参数化建模（作品集进阶）
- 加入 V8 Assembly 装配体表达（作品集高阶）
- 用 V8B 的 BOM 和检查清单做工程化整理
- 用 V6D 的项目线做组织框架

B. 升级后的作品集结构
======================

下方表格展示 V9A 升级后的完整作品集结构：

.. list-table:: 升级版 Capstone 作品集结构
   :header-rows: 1
   :widths: 22 30 25 15 8

   * - 模块
     - 推荐文件
     - 对应页面
     - 说明
     - 必选
   * - FreeCAD 图形化模型
     - ``bracket.FCStd``、截图
     - :doc:`bracket-capstone-project`
     - V6 图形化建模成果
     - ✅
   * - STEP/STL 导出文件
     - ``bracket-v1.step``、``.stl``
     - :doc:`freecad-export-checklist`
     - V6 导出文件
     - ✅
   * - 导出检查记录
     - ``checklist.md``
     - :doc:`freecad-export-checklist`
     - V6/V5B 导出验证
     - ✅
   * - CAM worksheet
     - ``cam-task-list.md``、``tool-list.csv``
     - :doc:`freecad-to-cam-worksheet`
     - V6/V5C 加工任务单
     - ✅
   * - G-code 理解笔记
     - ``gcode-interpretation.md``
     - :doc:`gcode-toolpath-visualization`
     - V6/V4A G-code 解读
     - ✅
   * - CadQuery 参数模型
     - ``plate_with_hole.py`` 等
     - :doc:`cadquery-parametric-modeling`
     - V7A-V7B 基础示例
     - ⭐
   * - CadQuery 支架代码模型
     - ``bracket_capstone.py``
     - :doc:`cadquery-bracket-capstone`
     - V7C 完整支架
     - ✅
   * - Assembly 代码
     - ``bracket_assembly.py``、``bracket_nested_assembly.py``
     - :doc:`cadquery-assembly-intro`
     - V8A/V8C 多零件
     - ✅
   * - BOM
     - ``BOM.md``、``BOM_DATA``
     - :doc:`cadquery-assembly-bom-checklist`
     - V8B 零件清单
     - ✅
   * - 装配检查清单
     - ``checklist.md``、``placement-checklist.md``
     - :doc:`cadquery-assembly-bom-checklist`
     - V8B/V8C 检查
     - ✅
   * - 作品集说明文档
     - ``README.md``、``notes.md``
     - :doc:`bracket-project-portfolio`
     - V6B 模板
     - ✅

**必选** （✅）是 V6 基础要求，** 进阶** （⭐）是 V7/V8 升级要求。

C. 推荐文件夹结构
====================

升级后的目录结构：

.. code-block:: text

   bracket-capstone-portfolio/
   ├── README.md                       # 作品集总说明
   ├── requirements.md                  # 需求文档（V6A）
   │
   ├── cad-freecad/                    # V6 图形化建模
   │   ├── bracket.FCStd
   │   └── screenshots/
   │
   ├── exports/                         # V6 导出文件
   │   ├── bracket-v1.step
   │   ├── bracket-v1.stl
   │   └── components/
   │       ├── base_plate.step
   │       ├── vertical_plate.step
   │       ├── bolt.step
   │       └── side_pin.step
   │
   ├── cam/                             # V6 CAM 任务
   │   ├── cam-task-list.md
   │   ├── tool-list.csv
   │   └── worksheet.md
   │
   ├── gcode/                           # V6 G-code 理解
   │   ├── toolpath.nc
   │   └── gcode-interpretation.md
   │
   ├── cadquery/                        # V7 CadQuery 代码化建模
   │   ├── plate_with_hole.py           # V7A
   │   ├── plate_advanced_features.py   # V7B
   │   ├── bracket_variant.py           # V7B
   │   ├── bracket_capstone.py          # V7C（与 V6A 几何一致）
   │   └── README.md
   │
   ├── assembly/                        # V8 Assembly 装配体
   │   ├── bracket_assembly.py          # V8A（多零件）
   │   ├── bracket_nested_assembly.py   # V8C（子装配 + PLACEMENT_TABLE）
   │   ├── bracket_assembly.step
   │   ├── bom.md                       # V8B BOM 表格
   │   ├── exploded_view.svg            # V8B 爆炸图
   │   ├── placement_checklist.md       # V8C 检查清单
   │   └── interference_notes.md        # V8C 干涉检查记录
   │
   ├── notes/                           # 综合笔记
   │   ├── design-notes.md              # 设计修改记录
   │   ├── export-log.md                # 导出记录
   │   └── self-eval.md                 # 自评记录
   │
   └── screenshots/                     # 截图集合
       ├── freecad-overview.png
       ├── cadquery-render.png
       └── assembly-overview.png

** 推荐**：

- 保留 V6 原有结构（V6 基础作品集已用）
- 在 V6 目录基础上** 新增** `cadquery/` 和 `assembly/` 子目录
- 用 `notes/` 统一记录修改、导出、自评

D. V6/V7/V8 对照表
===================

下方对照表展示 V6/V7/V8 各页面的产出物在作品集中的位置：

.. list-table:: V6/V7/V8 页面在作品集中的位置
   :header-rows: 1
   :widths: 22 30 30 18

   * - 学习线
     - 页面
     - 产出物
     - 在作品集中的位置
   * - V6
     - :doc:`bracket-capstone-project`
     - FreeCAD 模型、需求文档
     - ``cad-freecad/``、``requirements.md``
   * - V6
     - :doc:`bracket-project-portfolio`
     - 作品集模板
     - 整体框架
   * - V6
     - :doc:`bracket-assessment-rubric`
     - 评分表
     - 评审参考
   * - V7
     - :doc:`cadquery-learning-path`
     - 学习路径总览
     - 参考（不直接提交）
   * - V7
     - :doc:`cadquery-bracket-capstone`
     - ``bracket_capstone.py``
     - ``cadquery/bracket_capstone.py``
   * - V8
     - :doc:`cadquery-assembly-learning-path`
     - 装配体学习路径
     - 参考（不直接提交）
   * - V8
     - :doc:`cadquery-assembly-bom-checklist`
     - BOM 表格
     - ``assembly/bom.md``
   * - V8
     - :doc:`cadquery-assembly-placement-mini-lab`
     - Placement 检查
     - ``assembly/placement_checklist.md``

**关系说明** ：

- V6 是**必选基础** （作品集核心）
- V7 是** 进阶** （CadQuery 代码化补充）
- V8 是** 高阶** （装配体工程表达）

E. 作品集提交说明模板
======================

下方提供可复制的作品集说明结构：

.. code-block:: text

   # 支架 Capstone 综合作品集

   ## 1. 项目目标
   - 简述项目背景和目标
   - 引用 requirements.md

   ## 2. 图形化建模过程（V6A）
   - FreeCAD 操作步骤
   - 关键特征说明
   - 引用 cad-freecad/

   ## 3. 导出文件说明（V6 + V5B）
   - bracket-v1.step（完整装配体 STEP）
   - components/*.step（拆分单件 STEP）
   - 导出检查清单结果

   ## 4. CAM/G-code 理解（V6 + V5C + V4A）
   - 加工任务单
   - G-code 解读笔记

   ## 5. CadQuery 参数化模型（V7）
   - bracket_capstone.py（与 V6A 几何一致）
   - 4 个 .py 代码文件角色
   - 用 FreeCAD 打开 STEP 验证几何一致性

   ## 6. Assembly / BOM（V8）
   - bracket_assembly.py（多零件）
   - bracket_nested_assembly.py（子装配）
   - BOM 表格（5 个组件）
   - 装配检查清单

   ## 7. 遇到的问题
   - 列出 V6/V7/V8 过程中遇到的关键问题
   - 解决方法 + 反思

   ## 8. 自评与下一步
   - 完成 V6/V7/V8 三条线的所有要求
   - 下一步：真实软件截图 / OCCT 仿真 / 第二 Capstone

F. 自评升级清单
================

提交作品集前，逐项检查：

.. list-table:: 自评升级清单
   :header-rows: 1
   :widths: 8 30 50 12

   * - #
     - 检查项
     - 验证方法
     - 必填
   * - 1
     - 是否包含 FreeCAD 模型
     - 检查 ``cad-freecad/bracket.FCStd``
     - ✅
   * - 2
     - 是否包含 STEP/STL
     - 检查 ``exports/`` 目录
     - ✅
   * - 3
     - 是否完成导出检查
     - 检查 ``checklist.md``
     - ✅
   * - 4
     - 是否有 CAM worksheet
     - 检查 ``cam/`` 目录
     - ✅
   * - 5
     - 是否能解释 G-code
     - 检查 ``gcode/gcode-interpretation.md``
     - ✅
   * - 6
     - 是否包含 CadQuery 参数模型
     - 检查 ``cadquery/`` 目录（V7A-V7C）
     - ✅
   * - 7
     - 是否包含支架代码模型
     - 检查 ``cadquery/bracket_capstone.py``
     - ✅
   * - 8
     - 是否包含 Assembly/BOM/装配检查
     - 检查 ``assembly/`` 目录
     - ✅
   * - 9
     - 是否有 README 或项目说明
     - 检查作品集根目录的 README.md
     - ✅

**总评公式** ：

.. code-block:: text

   基础分 = V6 必选 6 项 = 6 分
   进阶分 = V7/V8 必选 4 项 = 4 分
   满分 = 10 分

   9-10 分：完整综合作品集
   6-8 分：基础作品集 + 部分进阶
   < 6 分：仅 V6 基础

G. 常见误区
===========

.. list-table:: Capstone 作品集升级常见误区
   :header-rows: 1
   :widths: 8 35 35 22

   * - #
     - 误区
     - 正确做法
     - 影响等级
   * - 1
     - 只有截图，没有模型与代码
     - 必须有 .FCStd / .step / .py 等原始文件
     - ⭐⭐⭐
   * - 2
     - 只有 STEP/STL，没有说明导出检查
     - 必须有 ``checklist.md`` 记录导出验证
     - ⭐⭐⭐
   * - 3
     - 只提交代码，不解释参数意义
     - 代码 + README + 注释，解释每个参数
     - ⭐⭐
   * - 4
     - 把 Assembly 当成加工模型
     - 加工要回到单件 STEP
     - ⭐⭐⭐
   * - 5
     - 忽略 BOM 与检查清单
     - 必须用 V8B 的 BOM 和 checklist
     - ⭐⭐
   * - 6
     - 没有区分必选材料和扩展材料
     - 用 ✅/⭐ 标注必选/进阶
     - ⭐⭐
   * - 7
     - 没有版本记录和反思
     - 用 ``notes/`` 目录记录修改、导出、自评
     - ⭐⭐
   * - 8
     - 拼凑 V6/V7/V8 但没有 README 串联
     - 必须有作品集总 README 串联三条线
     - ⭐⭐

**前 3 个和 4 是 V9A 特有误区** ，必须避免。

H. 教学声明
============

本页面是 **V6/V7/V8 综合作品集的升级指南** ：

- 不重写 V6/V7/V8 的内容
- 不替代 :doc:`bracket-project-portfolio` （V6B 作品集模板）
- 仅作为"如何把三条线合并提交"的整合指南
- 真实工程中应根据项目需求选择提交内容

I. 相关页面
============

V6 Capstone 项目线
------------------

- :doc:`bracket-capstone-project` — V6A 支架 Capstone
- :doc:`bracket-project-portfolio` — V6B 作品集模板
- :doc:`bracket-assessment-rubric` — V6B 评分表
- :doc:`capstone-learning-path` — V6D 项目线收口

V7 CadQuery 单零件
-------------------

- :doc:`cadquery-learning-path` — V7D V7 系列收口
- :doc:`cadquery-bracket-capstone` — V7C 支架代码模型

V8 CadQuery Assembly
---------------------

- :doc:`cadquery-assembly-learning-path` — V8D V8 系列收口
- :doc:`cadquery-assembly-bom-checklist` — V8B BOM + 检查清单
- :doc:`cadquery-assembly-placement-mini-lab` — V8C Placement