=====================================================
CadQuery 本地运行环境：从代码到 STEP/STL 导出（V9C）
=====================================================

本页是 V9B（**服务器端环境诊断**）的后续。V9B 确认云端环境不能真实运行 CadQuery（OCCT 依赖不可用）。本页帮助读者在**自己的机器上**配置环境、运行代码、导出 STEP/STL。

A. 本页解决什么问题
====================

背景回顾
--------

- V7/V8 已提供 6 个 CadQuery 代码示例（:file:`code/cadquery/*.py`）
- V9B 已完成云端运行诊断：Python 3.10 + Ubuntu 22.04，CadQuery 不可用
- 所有代码通过了 ``py_compile`` 语法检查，但**未真实生成模型**

本页提供什么
------------

- 2 条本地环境路线（Python venv + Conda）
- 最小 smoke test 代码
- 运行 V7/V8 示例的推荐顺序
- 导出文件保存策略
- 导出后检查清单
- 8 条常见错误

目标
----

让读者可以在自己的机器上生成 STEP/STL，再回到 :doc:`step-stl-mini-lab` 做格式对比检查。

B. 为什么 py_compile 通过不等于 CadQuery 可运行
================================================

py_compile 只检查语法
---------------------

``python -m py_compile plate_with_hole.py`` 只验证：

- Python 语法正确（无 SyntaxError）
- 缩进正确
- import 语句存在

**不能** 验证：

- CadQuery 能正确生成几何
- OCP（OpenCascade Python wrapper）可加载
- STEP/STL exporters 正常工作
- 几何尺寸与设计一致

CadQuery 运行需要几何内核
--------------------------

CadQuery 依赖 **OCP** （OpenCascade Python wrapper），OCP 依赖 **OCCT** （OpenCascade Technology）C++ 库。这是一套庞大的几何引擎：

.. code-block:: text

   你的 Python 代码
       ↓
   CadQuery（Python API）
       ↓
   OCP（Python → C++ 桥接）
       ↓
   OCCT（C++ 几何内核）
       ↓
   STEP/STL 文件

**任何一层缺失都会导致运行失败。**

V9B 环境诊断结论
----------------

参考 :doc:`cadquery-runtime-export-pilot` （V9B 页面）：

- Python 3.10.12 —— CadQuery 2.8 需要 Python 3.11+
- CadQuery 2.3 支持 Python 3.10，但 OCP 在 PyPI mirror 不可用
- pythonocc-core 也不可用
- **结论**：本服务器不能跑 CadQuery，但读者本地可以

C. 推荐本地环境路线
====================

路线 1：Python 3.11+ 虚拟环境
-----------------------------

适合熟悉 Python 的读者。

.. code-block:: bash

   # 1. 确认 Python 版本（需要 3.11+）
   python3.11 --version
   # 如果没有，从 python.org 或系统包管理器安装

   # 2. 创建虚拟环境
   python3.11 -m venv venv-cadquery
   source venv-cadquery/bin/activate

   # 3. 安装 CadQuery
   pip install cadquery

   # 4. 验证 import
   python -c "import cadquery as cq; print(f'CadQuery {cq.__version__} OK')"

   # 5. 运行 smoke test
   python scripts/cadquery/smoke_test_cadquery.py

   # 6. 运行项目示例
   python code/cadquery/plate_with_hole.py

.. note::

   如果 ``import cadquery`` 报 ``ModuleNotFoundError: No module named 'OCP'``，
   说明 pip 未自动安装 OCP。此时建议改用**路线 2（Conda）**，
   因为 conda-forge 会自动处理 OCCT 二进制依赖。

路线 2：Conda / micromamba 环境
-------------------------------

适合需要更稳定几何依赖的读者。**推荐路线。**

.. code-block:: bash

   # 1. 安装 miniconda 或 micromamba
   #    miniconda:
   wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
   bash Miniconda3-latest-Linux-x86_64.sh

   #    或 micromamba（更轻量）:
   #    curl micro.mamba.pm/install.sh | bash

   # 2. 创建 CadQuery 环境
   conda create -n cadquery python=3.11
   conda activate cadquery

   # 3. 从 conda-forge 安装（自动处理 OCCT）
   conda install -c conda-forge cadquery

   # 4. 验证
   python -c "import cadquery as cq; print(f'CadQuery {cq.__version__} OK')"

   # 5. 运行 smoke test
   python scripts/cadquery/smoke_test_cadquery.py

   # 6. 运行项目示例
   python code/cadquery/plate_with_hole.py

.. tip::

   conda-forge 的 CadQuery 包会自动安装 OCP 和 OCCT 二进制，
   不需要手动处理 C++ 依赖。这是最省心的路线。

环境配置示例文件
----------------

本仓库提供了 :file:`environment-cadquery.yml` 示例文件：

.. code-block:: bash

   conda env create -f environment-cadquery.yml
   conda activate cadquery

.. note::

   安装前请查看 CadQuery `官方安装说明 <https://github.com/CadQuery/cadquery#installation>`_
   或 `PyPI 页面 <https://pypi.org/project/cadquery/>`_ 确认当前版本要求。

D. 最小 smoke test
==================

以下是最小验证代码。也可以直接运行 :file:`scripts/cadquery/smoke_test_cadquery.py`。

.. code-block:: python

   import cadquery as cq
   import tempfile
   import os

   print(f"CadQuery version: {cq.__version__}")

   # 创建一个 10x10x10 的 box
   box = cq.Workplane("XY").box(10, 10, 10)
   print(f"Box volume: {box.val().Volume()}")

   # 导出 STEP
   step_path = os.path.join(tempfile.gettempdir(), "smoke_test.step")
   cq.exporters.export(box, step_path)
   print(f"STEP exported: {os.path.getsize(step_path)} bytes")

   # 导出 STL
   stl_path = os.path.join(tempfile.gettempdir(), "smoke_test.stl")
   cq.exporters.export(box, stl_path)
   print(f"STL exported: {os.path.getsize(stl_path)} bytes")

   print("Smoke test passed!")

预期输出：

.. code-block:: text

   CadQuery version: 2.X.X
   Box volume: 1000.0
   STEP exported: ~7000 bytes
   STL exported: ~3000 bytes
   Smoke test passed!

E. 运行本项目示例
=================

推荐运行顺序
------------

按从简单到复杂的顺序：

1. :file:`plate_with_hole.py` —— V7A，带孔板（最简单）
2. :file:`plate_advanced_features.py` —— V7B，圆角/倒角/孔阵列
3. :file:`bracket_variant.py` —— V7B，L 型支架变体
4. :file:`bracket_capstone.py` —— V7C，完整 Capstone 支架
5. :file:`bracket_assembly.py` —— V8A，多零件装配体
6. :file:`bracket_nested_assembly.py` —— V8C，子装配嵌套

运行方法
--------

.. code-block:: bash

   cd /path/to/CAD-CAM-Technology-docs
   python code/cadquery/plate_with_hole.py

注意事项
--------

- **先跑单零件**，确认导出正常后再跑 assembly
- 如果 assembly 示例失败，先确认单零件导出正常
- assembly 示例依赖更多几何内核能力（装配约束、干涉检查），可能需要更新版本
- **不要直接把教学导出文件用于真实机床或生产**

F. 导出文件保存策略
====================

建议目录结构
------------

.. code-block:: text

   CAD-CAM-Technology-docs/
   ├── code/cadquery/          # 源代码
   ├── scripts/cadquery/       # 辅助脚本
   └── local-exports/          # 本地导出（.gitignore 忽略）
       ├── plate_with_hole.step
       ├── plate_with_hole.stl
       ├── plate_advanced_features.step
       ├── plate_advanced_features.stl
       ├── bracket_capstone.step
       ├── bracket_capstone.stl
       ├── bracket_assembly.step
       └── bracket_nested_assembly.step

创建目录并运行
--------------

.. code-block:: bash

   mkdir -p local-exports
   python scripts/cadquery/run_plate_export.py

Git 策略
--------

- ``local-exports/`` 已加入 ``.gitignore``，默认不提交
- 小型教学文件（< 100KB）可手动检查后用 ``git add -f`` 精确加入
- 大型文件不建议提交仓库
- 参考资源包说明：:file:`assets/cadquery-exports/README.md`

G. 导出后检查
==============

检查清单
--------

.. list-table:: 导出后检查项
   :header-rows: 1
   :widths: 5 30 15 50

   * - #
     - 检查项
     - 方法
     - 说明
   * - 1
     - 文件是否生成
     - ``ls -la local-exports/``
     - 确认文件存在且大小 > 0
   * - 2
     - 文件大小是否异常
     - ``ls -lh``
     - STEP 通常几 KB～几十 KB；STL 几 KB～几 MB
   * - 3
     - STEP 能否在 CAD 查看器打开
     - FreeCAD / Online Viewer
     - 打开后应显示完整几何
   * - 4
     - STL 能否在网格查看器打开
     - 切片软件 / MeshLab
     - 打开后应显示三角面片
   * - 5
     - 单位是否一致
     - FreeCAD 测量工具
     - 尺寸应为 mm（毫米）
   * - 6
     - 孔和圆角是否保留
     - FreeCAD 测量
     - 中心孔直径、倒角尺寸
   * - 7
     - STL 是否明显粗糙或破洞
     - 视觉检查
     - 面片数量太少 → 调整 tolerance
   * - 8
     - STEP vs STL 视觉对比
     - 并排打开
     - 几何应一致

相关页面
--------

- :doc:`freecad-export-checklist` —— FreeCAD 导出检查清单
- :doc:`step-stl-mini-lab` —— STEP vs STL 格式对比实验
- :doc:`cadquery-runtime-export-pilot` —— V9B 服务器端环境诊断

自动化检查
-----------

使用 :file:`scripts/cadquery/verify_exports.py` 自动检查文件格式：

.. code-block:: bash

   python scripts/cadquery/verify_exports.py local-exports/*.step local-exports/*.stl

H. 常见错误
===========

.. list-table:: 常见错误与解决方法
   :header-rows: 1
   :widths: 5 35 50 10

   * - #
     - 错误
     - 解决方法
     - 严重度
   * - 1
     - Python 版本不匹配（CadQuery 2.8 需要 3.11+）
     - 升级 Python 或降级 CadQuery 到 2.3
     - ⭐⭐⭐
   * - 2
     - cadquery 安装成功但 OCP 缺失
     - 改用 conda-forge 安装（自动处理 OCCT）
     - ⭐⭐⭐
   * - 3
     - ``import cadquery`` 报 ModuleNotFoundError
     - 确认虚拟环境已激活，确认 pip install 成功
     - ⭐⭐⭐
   * - 4
     - exporters 导出失败（PermissionError / 路径不存在）
     - 确认输出目录存在：``mkdir -p local-exports``
     - ⭐⭐
   * - 5
     - 当前目录不对导致文件没生成
     - 确认在仓库根目录运行，或用绝对路径
     - ⭐⭐
   * - 6
     - 输出路径不存在
     - 创建 ``local-exports/`` 目录
     - ⭐⭐
   * - 7
     - STEP/STL 文件为空或过小（< 100 bytes）
     - 检查模型是否为空，检查 exporter 参数
     - ⭐⭐
   * - 8
     - assembly 示例依赖更多几何内核能力
     - 升级 CadQuery 和 OCP 到最新版
     - ⭐⭐
   * - 9
     - 把教学导出文件当成生产文件
     - 教学文件**不**适合真实机床或生产环境
     - ⭐⭐⭐

I. 相关页面
===========

- :doc:`cadquery-runtime-export-pilot` —— V9B 服务器端环境诊断
- :doc:`cadquery-parametric-modeling` —— V7A 带孔板
- :doc:`cadquery-advanced-features` —— V7B 圆角/倒角
- :doc:`cadquery-bracket-capstone` —— V7C 完整支架
- :doc:`cadquery-learning-path` —— V7D 学习路径
- :doc:`cadquery-assembly-intro` —— V8A 装配体
- :doc:`cadquery-assembly-learning-path` —— V8D 装配路径
- :doc:`step-stl-mini-lab` —— STEP vs STL 格式对比
- :doc:`freecad-export-checklist` —— FreeCAD 导出检查

J. 相关脚本
===========

- :file:`scripts/cadquery/smoke_test_cadquery.py` —— 最小环境验证
- :file:`scripts/cadquery/run_plate_export.py` —— 导出 plate_with_hole
- :file:`scripts/cadquery/verify_exports.py` —— 验证导出文件格式
- :file:`scripts/cadquery/README.md` —— 脚本使用说明
- :file:`environment-cadquery.yml` —— Conda 环境配置示例