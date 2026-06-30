==================
工程案例
==================

本文档通过三个完整的工程案例，帮助你将 unit1~unit8 的理论知识应用到实际制造场景中。每个案例都对应课程中的多个章节，建议在学习完相关章节后再阅读。

在开始案例学习之前，建议先阅读 :doc:`../workflow-roadmap`，了解完整的 CAD/CAM 工具链和学习路线。workflow-roadmap 是总路线，examples 是路线中的案例集合。

工程案例学习目标
==================

1. 理解 CAD/CAM 技术在实际制造中的完整应用流程
2. 掌握从设计模型到加工代码的转换方法
3. 了解不同数据交换格式的特点和使用场景
4. 熟悉 CAPP 工艺路线的设计思路
5. 建立"设计→工艺→制造"的系统性思维

四个案例之间的关系
====================

.. figure:: ../_static/diagrams/cad-to-gcode-pipeline.svg
   :width: 100%
   :align: center
   :alt: 从 CAD 到 G-code 的完整流程

**案例 A — 从 CAD 到 G-code**：
  覆盖完整制造流程：几何建模 → 工艺分析 → 刀具路径 → G-code 生成。对应 unit3、unit4、unit6、unit7。

**案例 B — 数据交换**：
  关注数据在不同系统间的流转：CAD 模型 → CAE 分析 → CAM 编程 → 3D 打印。对应 unit1、unit5、unit8。

**案例 C — CAPP 工艺路线**：
  聚焦工艺规划环节：毛坯选择 → 定位基准 → 工序排序 → 工艺卡片。对应 unit6、unit8。

**案例 D — FreeCAD 实操**：
  第一个动手实验：在 FreeCAD 中创建带孔矩形板，导出 STEP 和 STL。对应 unit3、unit4。

**案例 E — FreeCAD 导出检查**：
  建模完成后的系统验证：导出前检查、STEP 验证、STL 验证、文件命名规范、常见错误排查。对应 V5B。

**案例 F — FreeCAD 到 CAM**：
  从模型到加工：CAM 前置检查、加工任务拆解、刀具与参数选择、加工顺序规划、与 G-code 的衔接。对应 V5C。

**案例 G — FreeCAD 五步学习路线**：
  FreeCAD 实操线的总入口和收口页：五步学习路线、全链路产出物表、初学者完成标准。对应 V5D。

**案例 H — L 型支架 Capstone 项目**：
  FreeCAD 实操线的综合项目：集成 V5A-V5D 全部学习成果，完成从需求分析到 G-code 理解的完整流程。对应 V6A。

**案例 I — Bracket Capstone 项目档案**：
  L 型支架项目的档案模板和使用方法，包含 9 大类项目内容和推荐目录结构。对应 V6B。

**案例 J — Bracket Capstone 项目评分表**：
  L 型支架项目的详细评分标准，包含 3 大维度、20 个评分项、4 级评分等级。对应 V6B。

**案例 K — FreeCAD Path Workbench 入门**：
  FreeCAD 内置 CAM 模块入门：Job/Tool/Operation/Toolpath/Post Processor/G-code 概念、教学型 G-code 样例。对应 V6C。

**案例 L — Capstone 项目线学习路径**：
  V6 项目线总入口和收口页：五步学习路线、产出物清单、完成标准、误区与扩展。对应 V6D。

推荐阅读顺序
============

1. **零基础入门**：先阅读 :doc:`freecad-plate-modeling`，完成第一个 CAD 建模实践
2. **导出检查**：阅读 :doc:`freecad-export-checklist`，系统验证 STEP/STL 导出结果
3. **CAM 规划**：阅读 :doc:`freecad-to-cam-worksheet`，学习如何为零件规划加工任务
4. **学习路线总览**：阅读 :doc:`freecad-workflow-index`，查看 FreeCAD 五步学习路线和完成标准
5. **初学者**：阅读 :doc:`data-exchange`，了解数据如何在不同系统间流转
6. **有一定基础**：阅读 :doc:`capp-process-plan`，理解工艺规划的核心思路
7. **系统学习**：阅读 :doc:`cad-to-gcode`，建立从设计到制造的完整认知
8. **深入理解**：阅读 :doc:`gcode-toolpath-visualization`，逐行理解 G-code 程序如何控制机床动作
9. **格式实验**：阅读 :doc:`step-stl-mini-lab`，通过对比实验理解 STEP 与 STL 的本质差异
10. **综合项目**：完成 :doc:`bracket-capstone-project`，集成全部 V5A-V5D 学习成果
11. **项目档案**：阅读 :doc:`bracket-project-portfolio`，使用模板整理项目成果
12. **项目评分**：阅读 :doc:`bracket-assessment-rubric`，使用评分表自我评估
13. **Path Workbench**：阅读 :doc:`freecad-path-workbench-intro`，了解 FreeCAD CAM 模块
14. **项目线总入口**：阅读 :doc:`capstone-learning-path`，查看 V6 项目线完整学习闭环

每个案例对应的课程章节
========================

.. list-table:: 案例与课程章节对应关系
   :header-rows: 1
   :widths: 25 35 40

   * - 案例
     - 核心内容
     - 对应课程章节
   * - CAD 到 G-code
     - 几何建模、刀具路径、后处理
     - unit3, unit4, unit6, unit7
   * - G-code 逐行解释
     - 数控程序结构、指令含义、路径可视化
     - unit7
   * - 数据交换
     - STEP/STL/IGES 格式、跨系统协作
     - unit1, unit5, unit8
   * - STEP/STL Mini-Lab
     - 格式结构对比、精度分析、格式选择
     - unit4, unit8
   * - CAPP 工艺路线
     - 工艺规划、工序设计、工艺卡片
     - unit6, unit8
   * - FreeCAD 实操
     - FreeCAD 建模、STEP/STL 导出
     - unit3, unit4
   * - FreeCAD 导出检查
     - 导出前检查、STEP/STL 验证、错误排查
     - V5B
   * - FreeCAD 到 CAM
     - CAM 前置检查、加工任务拆解、刀具参数
     - V5C
   * - FreeCAD 五步学习路线
     - 五步路线、产出物表、完成标准
     - V5D
   * - L 型支架 Capstone
     - 集成项目、5个阶段、提交包
     - V6A
   * - Bracket 项目档案
     - 9 大类内容、目录结构、模板
     - V6B
   * - Bracket 评分表
     - 3 维度、20 评分项、4 级等级
     - V6B
   * - FreeCAD Path Workbench
     - Job/Tool/Operation/Post 概念
     - V6C
   * - Capstone 项目线
     - 五步路线、产出物、完成标准
     - V6D

如何用案例复习 unit1~unit8
============================

1. **学完 unit1（概论）后**
   - 阅读 :doc:`data-exchange` 中的格式对比部分
   - 理解 CAD/CAM 系统间的数据流转

2. **学完 unit3（图形变换）和 unit4（建模）后**
   - 阅读 :doc:`cad-to-gcode` 中的几何建模部分
   - 理解模型如何用于后续加工
   - **动手实践**：阅读 :doc:`freecad-plate-modeling`，在 FreeCAD 中创建你的第一个零件
   - **导出验证**：阅读 :doc:`freecad-export-checklist`，确保导出文件质量可靠
   - **CAM 规划**：阅读 :doc:`freecad-to-cam-worksheet`，理解如何从模型到加工任务
   - **路线收口**：阅读 :doc:`freecad-workflow-index`，查看完整学习闭环

3. **学完 unit5（工程分析）后**
   - 阅读 :doc:`data-exchange` 中 CAE 分析的数据准备
   - 理解分析结果如何反馈给设计

4. **学完 unit6（CAPP）后**
   - 阅读 :doc:`capp-process-plan` 完整案例
   - 对照教材中的 CAPP 设计步骤

5. **学完 unit7（数控加工）后**
   - 阅读 :doc:`cad-to-gcode` 中的 G-code 生成部分
   - 理解刀具路径如何转化为机床指令
   - 阅读 :doc:`gcode-toolpath-visualization`，逐行理解每个 G-code 指令的含义

6. **学完 unit4（建模）和 unit8（集成）后**
   - 阅读 :doc:`step-stl-mini-lab`，通过立方体和圆柱体对比实验
   - 理解 B-rep 与三角网格的本质差异，培养格式选择能力

7. **学完 unit8（集成）后**
   - 回顾三个案例中的数据流
   - 思考如何实现更高效的系统集成
   - **总收口**：再次阅读 :doc:`freecad-workflow-index`，确认是否所有完成标准都已达成

8. **综合项目**：完成 :doc:`bracket-capstone-project` L 型支架 Capstone 项目，集成 V5A-V5D 全部学习成果，验证你已具备 FreeCAD 实践线的完整能力。

.. toctree::
   :hidden:

   cad-to-gcode
   gcode-toolpath-visualization
   data-exchange
   step-stl-mini-lab
   capp-process-plan
   freecad-plate-modeling
   freecad-export-checklist
   freecad-to-cam-worksheet
   freecad-workflow-index
   bracket-capstone-project
   bracket-project-portfolio
   bracket-assessment-rubric
   freecad-path-workbench-intro
   capstone-learning-path
