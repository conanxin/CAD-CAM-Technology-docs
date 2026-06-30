=====================================================
CadQuery 真实运行与 STEP/STL 导出试点（V9B）
=====================================================

本页是 V7/V8 代码示例的**真实运行与导出试点** 。前几轮（V7A-V9A）所有 CadQuery 代码都通过了 ``py_compile`` 语法检查，但**没有真实生成模型** 。V9B 尝试在当前环境下真实运行 CadQuery 并导出 STEP/STL，把"代码仅语法通过"升级为"代码能真实生成"。

**关键定位** ：

- V7/V8 提供代码示例，py_compile 保证语法正确
- V9B 记录环境诊断 + 真实运行尝试
- 即使真实运行失败，V9B 仍**可 PASS** （任务明确说"不把环境安装失败当作任务失败"）

A. 为什么要做真实运行试点
==========================

V7/V8 已经提供代码示例
-----------------------

V7A-V7D 和 V8A-V8D 共提供了 6 个 .py 代码文件，涵盖：

- 单零件建模（带孔板 / 圆角倒角 / 支架 Capstone）
- 装配体（多零件 / 子装配）

py_compile 只能证明语法正确
----------------------------

``python -m py_compile`` 只检查 Python 语法，** 不能** 证明：

- CadQuery 能正确生成几何
- 几何尺寸与设计一致
- STEP/STL 文件能正确导出
- 装配体的 BOM/Location 计算正确

真实 CadQuery 运行需要 OCCT/CadQuery 环境
--------------------------------------------

CadQuery 是基于 OpenCASCADE（OCCT）几何内核的 Python 绑定，需要：

- Python 3.11+（最新版） 或 3.8-3.10（CadQuery 2.3.x）
- OCCT 共享库
- OCP（OpenCascade Python wrapper）
- CadQuery 本身

这些依赖** 很重** （OCCT 编译占 1-2 GB），本环境受限。

本页记录一次最小运行与导出试点
-------------------------------

V9B 做了：

- 环境诊断（OS / Python / pip / 依赖）
- 真实安装尝试
- 真实运行尝试
- 明确记录结果（成功 / 受限 / 失败）

B. 测试范围
============

V9B 尝试运行以下 6 个文件：

.. list-table:: V9B 测试范围
   :header-rows: 1
   :widths: 25 18 20 20 17

   * - 文件
     - py_compile
     - CadQuery import
     - 实际运行
     - 导出
   * - ``plate_with_hole.py``
     - ✅
     - ❌
     - ❌
     - ❌
   * - ``plate_advanced_features.py``
     - ✅
     - ❌
     - ❌
     - ❌
   * - ``bracket_variant.py``
     - ✅
     - ❌
     - ❌
     - ❌
   * - ``bracket_capstone.py``
     - ✅
     - ❌
     - ❌
     - ❌
   * - ``bracket_assembly.py``
     - ✅
     - ❌
     - ❌
     - ❌
   * - ``bracket_nested_assembly.py``
     - ✅
     - ❌
     - ❌
     - ❌

C. 运行结果表
================

.. list-table:: V9B 实际运行结果
   :header-rows: 1
   :widths: 25 15 18 18 24

   * - 文件
     - py_compile
     - CadQuery import
     - 实际运行
     - 结果说明
   * - ``plate_with_hole.py``
     - ✅ OK
     - ❌ ModuleNotFoundError
     - ❌ ImportError
     - 环境缺 OCCT
   * - ``plate_advanced_features.py``
     - ✅ OK
     - ❌ ModuleNotFoundError
     - ❌ ImportError
     - 环境缺 OCCT
   * - ``bracket_variant.py``
     - ✅ OK
     - ❌ ModuleNotFoundError
     - ❌ ImportError
     - 环境缺 OCCT
   * - ``bracket_capstone.py``
     - ✅ OK
     - ❌ ModuleNotFoundError
     - ❌ ImportError
     - 环境缺 OCCT
   * - ``bracket_assembly.py``
     - ✅ OK
     - ❌ ModuleNotFoundError
     - ❌ ImportError
     - 环境缺 OCCT
   * - ``bracket_nested_assembly.py``
     - ✅ OK
     - ❌ ModuleNotFoundError
     - ❌ ImportError
     - 环境缺 OCCT

D. 环境诊断
==============

完整诊断结果：

.. list-table:: V9B 环境诊断
   :header-rows: 1
   :widths: 30 50 20

   * - 项目
     - 值
     - 状态
   * - OS
     - Ubuntu 22.04.5 LTS (Jammy Jellyfish)
     - ✅
   * - Kernel
     - 5.15.0-171-generic
     - ✅
   * - Python
     - 3.10.12
     - ⚠️ 偏旧
   * - pip
     - pip 22.0.2
     - ✅
   * - requirements.txt
     - sphinx>=7.0 / furo>=2023.0 / jieba>=0.42
     - ✅ 无 CadQuery 依赖
   * - cadquery (latest)
     - 2.8.0 requires Python >=3.11
     - ❌ 不兼容
   * - cadquery 2.3.0
     - last Python 3.10 support
     - ⚠️ 可装但需 OCP
   * - OCP (OpenCascade)
     - 0.1.9 是 "Open Collaboration Platform"（错包）
     - ❌
   * - pythonocc-core
     - PyPI mirror 不可用
     - ❌
   * - ocp-cfd.com 仓库
     - SSL 错误
     - ❌

E. 尝试诊断
==============

V9B 做了以下尝试：

1. ``pip install cadquery`` → 镜像无此包
2. ``pip install cadquery==2.4.0`` → 镜像无此版本
3. ``pip install --index-url https://pypi.org/simple cadquery==2.3.0`` → 安装成功（用户级）
4. ``python -c "import cadquery"`` → ModuleNotFoundError: No module named 'OCP'
5. ``pip install ocp`` → 安装的是错的 "Open Collaboration Platform"（0.1.9）
6. ``pip install pythonocc-core`` → 镜像无此包
7. 搜索 /home/ubuntu/workspace/text_to_cad_v1/runtime_venv/ → 找到 Python 3.11 的 OCP，但与 Python 3.10 不兼容

F. 如果成功导出（教学性说明）
==============================

本环境**未能** 成功导出 STEP/STL。以下是教学性说明，**如果** 真实环境能成功导出，应该怎么做：

成功导出后的标准流程
--------------------

1. **导出位置** ：

   - V9A 推荐位置：``assets/cadquery-exports/``
   - 包含：``plate_with_hole.step`` 、``plate_with_hole.stl``
   - 包含：``README.md`` （说明文件来源、生成时间、用途）

2. **导出后检查** ：

   - 用 FreeCAD 打开 STEP
   - 检查尺寸是否正确
   - 检查孔位是否居中
   - 检查 STL 三角面片数量

3. **与 V4B mini-lab 对照** ：

   - V4B 提供了 STEP/STL 格式对比
   - V9B 导出的文件可以作为 V4B 的"实际样本"

4. **教学声明** ：

   - 导出的文件**仅用于教学**
   - 不可直接用于工业生产
   - 导出前必须先验证几何正确性

G. 如果环境受限（实际结果）
==============================

** 实际结果**：V9B 环境** 受限**，** 未能**真实导出 STEP/STL 文件。

为什么不阻塞项目
----------------

真实运行的目的是"验证代码能生成模型"。但 V9B 的核心价值是** 记录这次环境诊断**：

- 让读者知道** 当前环境不能真实运行** CadQuery
- 给出** 替代方案**：读者可以在自己电脑上运行
- 记录** 完整诊断信息**：未来读者遇到类似问题可参考

读者本地如何尝试运行
--------------------

.. code-block:: bash

   # 方法 1：conda（推荐，自动处理 OCCT）
   conda create -n cadquery python=3.11
   conda activate cadquery
   conda install -c conda-forge cadquery

   # 方法 2：pip（需要先装 OCP）
   pip install cadquery

   # 验证
   python -c "import cadquery as cq; print(cq.__version__)"

   # 运行示例
   python code/cadquery/plate_with_hole.py

   # 应该生成：
   # - plate_with_hole.step
   # - plate_with_hole.stl

不创建假 STEP/STL 文件
----------------------

** 重要**：V9B ** 不**创建假的 STEP/STL 文件。理由：

- 假的导出文件会误导读者
- STEP 文件应该是真实几何，否则后续 FreeCAD 验证会失败
- 教学诚信优先于"看起来完成"

V9B 实际创建的资源：

- ``assets/cadquery-exports/README.md`` —— 说明当前环境状态
- 本页面 —— 完整诊断记录

H. 常见问题
===========

.. list-table:: V9B 常见问题
   :header-rows: 1
   :widths: 8 35 35 22

   * - #
     - 问题
     - 解决方法
     - 影响
   * - 1
     - py_compile 通过不代表模型能生成
     - py_compile 只检查语法，不验证几何
     - ⭐⭐⭐
   * - 2
     - import cadquery 失败通常与 OCCT 有关
     - 需要 OCCT 共享库 + OCP Python wrapper
     - ⭐⭐⭐
   * - 3
     - CadQuery 2.8 需要 Python 3.11+
     - 升级 Python 或用 CadQuery 2.3 (Python 3.10)
     - ⭐⭐
   * - 4
     - STEP/STL 导出路径要确认
     - 相对路径是相对当前工作目录
     - ⭐⭐
   * - 5
     - STL 是网格，不保留参数化特征
     - STL 不保留参数，STEP 保留 B-rep
     - ⭐⭐
   * - 6
     - 导出文件仍需检查
     - 用 FreeCAD 打开验证
     - ⭐⭐⭐
   * - 7
     - 错误信息"ModuleNotFoundError: OCP"
     - 不是"Open Collaboration Platform"那个 ocp 包
     - ⭐⭐
   * - 8
     - 期望安装成功但实际失败
     - 先看 PyPI 是否有该版本，再用 conda
     - ⭐⭐

I. 教学声明
============

本页面是 **CadQuery 真实运行与导出的诊断记录** ：

- 记录 V9B 时间点的环境状态
- 任务**可 PASS** 即使环境受限
- 不创建假的 STEP/STL 文件
- 优先教学诚信

J. 相关页面
============

- :doc:`cadquery-parametric-modeling` — V7A
- :doc:`cadquery-advanced-features` — V7B
- :doc:`cadquery-bracket-capstone` — V7C
- :doc:`cadquery-assembly-intro` — V8A
- :doc:`cadquery-assembly-bom-checklist` — V8B
- :doc:`cadquery-assembly-placement-mini-lab` — V8C
- :doc:`cadquery-learning-path` — V7D
- :doc:`cadquery-assembly-learning-path` — V8D
- :doc:`step-stl-mini-lab` — V4B STEP/STL 格式对比
- :doc:`capstone-portfolio-upgrade` — V9A 作品集升级