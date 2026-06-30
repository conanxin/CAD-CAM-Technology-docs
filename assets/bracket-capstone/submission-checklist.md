# Bracket Capstone 项目提交清单

## 提交前必读

完成 L 型支架 Capstone 项目后，使用本清单逐项检查你的提交包。每个项目都标记了是否为必需、可选、还是加分项。

## 1. 必需文件（缺失任一项 = 提交不通过）

### 1.1 需求与规划

- [ ] requirements.md — 需求分析文档
  - [ ] 包含零件功能描述
  - [ ] 包含材料选择理由
  - [ ] 包含关键尺寸和公差
  - [ ] 包含加工难点分析

### 1.2 建模文件

- [ ] bracket.FCStd — FreeCAD 原生文件
  - [ ] 文件可正常打开
  - [ ] 模型尺寸正确
  - [ ] 草图完全约束
  - [ ] 孔特征完整

### 1.3 导出文件

- [ ] bracket-v1.step — STEP 格式
  - [ ] 文件头为 ISO-10303-21
  - [ ] 可在其他 CAD 软件中打开
  - [ ] 实体边界完整
  - [ ] 圆柱孔/圆角保留

- [ ] bracket-v1.stl — STL 格式
  - [ ] 可在切片软件中打开
  - [ ] 无破洞
  - [ ] 法向一致
  - [ ] 网格密度合理

### 1.4 检查记录

- [ ] export-checklist.md — 导出检查记录
  - [ ] 导出前检查（7 项）全部通过
  - [ ] STEP 验证（5 项）全部通过
  - [ ] STL 验证（6 项）全部通过
  - [ ] 记录了遇到的问题和解决方法

### 1.5 CAM 规划

- [ ] cam-task-list.md — 工序列表
  - [ ] 至少包含 5 个工序
  - [ ] 每个工序有明确的目标
  - [ ] 工序顺序合理（先面后孔、先粗后精）

- [ ] tool-list.csv — 刀具参数表
  - [ ] 每个工序对应一种刀具
  - [ ] 包含主轴转速、进给速度、切削深度
  - [ ] 格式正确（CSV）

- [ ] worksheet-template.md — CAM 工作单
  - [ ] 填写完整（无空白项）
  - [ ] 装夹方案明确
  - [ ] 加工顺序有说明

### 1.6 G-code

- [ ] bracket.gcode — CAM 生成的 G-code
  - [ ] 文件可正常打开
  - [ ] 包含完整的工序指令
  - [ ] 包含主轴启动/停止指令
  - [ ] 包含换刀指令（如果有多把刀）

- [ ] gcode-notes.md — G-code 解读笔记
  - [ ] 至少解读 5 行 G-code
  - [ ] 对应 G-code 到工序
  - [ ] 解释 G00/G01/G02/G03 的使用

### 1.7 反思笔记

- [ ] reflection.md — 反思笔记
  - [ ] 描述遇到的最大困难
  - [ ] 描述解决方法
  - [ ] 总结学到的技术
  - [ ] 总结学到的方法论
  - [ ] 描述下一步计划

## 2. 可选文件（缺失不扣分，但建议提供）

- [ ] bracket-screenshots/ — 建模过程截图
- [ ] bracket-dimension.svg — 零件尺寸示意图
- [ ] cam-toolpath-screenshot.png — CAM 刀路截图
- [ ] gcode-simulation.png — G-code 仿真截图

## 3. 加分项（提供可获得额外分数）

- [ ] 添加了额外的特征（如倒角、螺纹孔、铭牌槽）
- [ ] 提供了 STEP 214 格式（更现代的 STEP 子集）
- [ ] G-code 包含注释和分组（更易读）
- [ ] 反思笔记包含具体案例和量化数据
- [ ] 提供了完整的 3D 打印切片过程

## 4. 提交包结构检查

### 4.1 目录结构

确认你的提交包目录如下：

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
│   └── gcode-notes.md
├── 06-reflection/
│   └── reflection.md
└── README.md  (项目档案主页)
```

### 4.2 命名规范

- [ ] 文件名使用小写
- [ ] 文件名使用连字符而非空格
- [ ] 版本号在文件名中（如 -v1）
- [ ] 没有特殊字符（中文、空格、特殊符号）

### 4.3 文件大小

- [ ] .FCStd < 10 MB
- [ ] .step < 50 MB
- [ ] .stl < 100 MB
- [ ] .md 文件 < 1 MB

## 5. 最终检查

- [ ] 所有文件都能正常打开
- [ ] 文件路径中没有中文（避免跨平台问题）
- [ ] 提交包总大小 < 200 MB
- [ ] README.md 中有项目说明和使用指南

## 6. 提交方式

### 6.1 个人学习

如果你只是个人学习，可以将提交包压缩为：

```
bracket-capstone-你的名字-日期.zip
```

### 6.2 课程作业

如果是课程作业，请按教师要求提交（可能包括：

- 提交到学习管理系统（LMS）
- 提交到 Git 仓库
- 提交到云盘

## 7. 提交后

提交后，你可以：

- 使用评分表（reference `bracket-assessment-rubric.rst`）进行自我评估
- 回顾项目档案（reference `bracket-project-portfolio.rst`）
- 继续下一个项目或深入学习

---

*本清单属于 CAD-CAM-Technology-docs 项目的一部分。*
