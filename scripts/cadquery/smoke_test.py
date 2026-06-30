"""
CadQuery Smoke Test
===================

快速验证 CadQuery 环境是否配置成功。
不依赖 V7/V8 的完整代码，只做最小测试。

依赖
----
- cadquery >= 2.0
- 安装：conda install -c conda-forge cadquery

运行
----
python scripts/cadquery/smoke_test.py

预期输出
--------
=== CadQuery Smoke Test ===
Python: 3.11.x
CadQuery: 2.X.X
Test 1: import OK
Test 2: simple box OK
Test 3: box with hole OK
Test 4: STEP export OK
Test 5: STL export OK
=== All tests passed ===

如果失败，参考：
- examples/cadquery-local-environment-guide.rst
- examples/cadquery-runtime-export-pilot.rst
"""

import sys
import os
import tempfile


def main():
    print("=" * 50)
    print("=== CadQuery Smoke Test ===")
    print("=" * 50)

    # 测试 1: Python 版本
    print(f"Python: {sys.version}")
    if sys.version_info < (3, 8):
        print("[FAIL] Python 3.8+ required")
        return 1
    print("[OK] Python version")

    # 测试 2: CadQuery import
    try:
        import cadquery as cq
        print(f"CadQuery: {cq.__version__}")
        print("[OK] CadQuery import")
    except ImportError as e:
        print(f"[FAIL] CadQuery import: {e}")
        return 1

    # 测试 3: 简单 box
    try:
        box = cq.Workplane("XY").box(10, 10, 10)
        volume = box.val().Volume()
        print(f"[OK] simple box (volume: {volume:.2f})")
    except Exception as e:
        print(f"[FAIL] simple box: {e}")
        return 1

    # 测试 4: box with hole
    try:
        plate = cq.Workplane("XY").box(10, 10, 10)
        plate = plate.faces(">Z").workplane().hole(3)
        volume = plate.val().Volume()
        print(f"[OK] box with hole (volume: {volume:.2f})")
    except Exception as e:
        print(f"[FAIL] box with hole: {e}")
        return 1

    # 测试 5: STEP 导出
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            step_path = os.path.join(tmpdir, "smoke.step")
            cq.exporters.export(plate, step_path)
            size = os.path.getsize(step_path)
            print(f"[OK] STEP export (size: {size} bytes)")
    except Exception as e:
        print(f"[FAIL] STEP export: {e}")
        return 1

    # 测试 6: STL 导出
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            stl_path = os.path.join(tmpdir, "smoke.stl")
            cq.exporters.export(plate, stl_path)
            size = os.path.getsize(stl_path)
            print(f"[OK] STL export (size: {size} bytes)")
    except Exception as e:
        print(f"[FAIL] STL export: {e}")
        return 1

    print("=" * 50)
    print("=== All tests passed ===")
    print("=" * 50)
    print("CadQuery environment is ready!")
    print("Now you can run V7/V8 .py files:")
    print("  python code/cadquery/plate_with_hole.py")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"[FATAL] Smoke test failed: {e}")
        sys.exit(1)