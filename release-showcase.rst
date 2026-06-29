========================================
本站发布说明与能力展示
========================================

本文档展示 CAD-CAM-Technology-docs 从 V1 到 V4C 的演进历程、当前版本能力矩阵和后续规划。

从 V1 到 V4C：演进时间线
================================

.. list-table:: 版本演进
   :header-rows: 1
   :widths: 15 20 65

   * - 版本
     - 时间
     - 核心内容
   * - **V1**
     - 2024-06
     - 旧版阅读笔记升级为 Sphinx + Furo 现代化文档站，支持中文搜索、数学公式、响应式布局
   * - **V2**
     - 2024-06
     - 课程化结构：新增课程总览、章节地图、复习题、词汇表、学习路径，每章增加学习目标和结构
   * - **V3**
     - 2024-06
     - 工程案例化：新增 CAD→G-code、数据交换、CAPP 工艺路线三个完整制造案例
   * - **V4A**
     - 2024-06
     - G-code 逐行解释与路径可视化：逐行解读数控程序，配 SVG 路径图，帮助初学者理解机床动作
   * - **V4B**
     - 2024-06
     - STEP/STL 数据交换 mini-lab：格式结构对比、精度分析、格式选择决策，培养"根据场景选格式"的能力
   * - **V4C**
     - 2024-06
     - 工作流路线图：工具链总览、四阶段学习路线、文件格式决策指南、3 个低门槛实践任务

当前版本能力矩阵
================================

.. list-table:: V4C 全站能力一览
   :header-rows: 1
   :widths: 20 25 30 25

   * - 能力维度
     - 内容
     - 对应页面
     - 版本
   * - **基础课程**
     - 8 章完整教材内容
     - unit1 ~ unit8
     - V2
   * - **课程导航**
     - 课程总览、章节地图、学习路径
     - course-overview, chapter-map, learning-path
     - V2
   * - **学习检验**
     - 复习题、词汇表
     - practice-questions, glossary
     - V2
   * - **工程案例**
     - 3 个完整制造流程案例
     - examples/cad-to-gcode, data-exchange, capp-process-plan
     - V3
   * - **G-code 教学**
     - 逐行解释 + 路径可视化
     - examples/gcode-toolpath-visualization
     - V4A
   * - **格式实验**
     - STEP/STL 对比实验
     - examples/step-stl-mini-lab
     - V4B
   * - **工具链认知**
     - 工具链总览、学习路线、格式决策
     - workflow-roadmap
     - V4C
   * - **实践任务**
     - 3 个低门槛动手任务
     - workflow-roadmap（低门槛实践任务章节）
     - V4C

路线图与案例的映射关系
================================

.. list-table:: 学习阶段与内容映射
   :header-rows: 1
   :widths: 20 25 30 25

   * - 学习阶段
     - 目标
     - 对应课程
     - 推荐案例
   * - **阶段 1：建立概念**
     - 理解 CAD/CAM 是什么
     - unit1, unit2
     - course-overview, glossary
   * - **阶段 2：建模技术**
     - 掌握几何表达
     - unit3, unit4, unit5
     - examples/cad-to-gcode（建模部分）
   * - **阶段 3：分析工艺**
     - 理解"设计→制造"决策
     - unit5, unit6
     - examples/capp-process-plan, data-exchange
   * - **阶段 4：编程集成**
     - 实现制造落地
     - unit7, unit8
     - examples/gcode-toolpath-visualization, step-stl-mini-lab

教学亮点
================================

G-code 逐行解释与路径可视化（V4A）
----------------------------------------

- **难点**：G-code 是纯文本指令，初学者难以理解"这些数字如何让机床动起来"
- **解法**：逐行解释每条指令的含义，配合 SVG 绘制的刀具路径图，直观展示运动轨迹
- **效果**：读者可以"看到"G-code 的执行过程，而不是死记硬背指令
- **位置**：:doc:`examples/gcode-toolpath-visualization`

STEP/STL 数据交换 mini-lab（V4B）
----------------------------------------

- **难点**：STEP 和 STL 都是 3D 格式，但本质完全不同——一个精确、一个近似
- **解法**：用同一个零件（立方体/圆柱体）导出两种格式，对比文件结构和几何表达
- **效果**：读者能回答"为什么 3D 打印用 STL、CAD 交换用 STEP"
- **位置**：:doc:`examples/step-stl-mini-lab`

工作流路线图（V4C）
----------------------------------------

- **难点**：学完全部章节后，知识是碎片化的，不清楚如何串联应用
- **解法**：设计四阶段学习路线 + 工具链总览 + 文件格式决策表 + 实践任务
- **效果**：读者知道"我现在该学什么""学完能做什么""用什么格式"
- **位置**：:doc:`workflow-roadmap`

后续版本规划
================================

短期（V5）
------------

- [ ] 引入 Mermaid 流程图或更多 SVG 图示
- [ ] 增加真实软件操作截图（FreeCAD / Fusion 360）
- [ ] 补充 FreeCAD / Fusion 工具链具体操作示例
- [ ] 增加代码示例（Python + CAD 库）

中期（V6）
------------

- [ ] 增加更多工程案例（装配体、曲面加工、多轴编程）
- [ ] 补充参考文献和扩展阅读链接
- [ ] 增加习题答案和解析

长期（V7+）
-------------

- [ ] 视频教程嵌入
- [ ] 交互式 3D 模型展示
- [ ] 在线测验系统

如何为项目做贡献
================================

1. **发现问题**：阅读过程中发现错误、歧义或可以改进的地方
2. **提交 Issue**：在 GitHub 上描述问题或建议
3. **提交 PR**：Fork 仓库，修改后提交 Pull Request

**优先欢迎的内容**：

- 真实软件操作截图和步骤说明
- 更多工程案例（尤其是加工、装配、检测方向）
- 代码示例（Python + CAD/CAM 库）
- 术语翻译和解释优化

项目信息
================================

- **仓库**：https://github.com/conanxin/CAD-CAM-Technology-docs
- **在线版本**：https://conanxin.github.io/CAD-CAM-Technology-docs
- **当前版本**：v0.4.2-workflow-roadmap
- **技术栈**：Sphinx + Furo + jieba + MathJax
- **构建状态**：GitHub Actions 自动部署到 GitHub Pages
