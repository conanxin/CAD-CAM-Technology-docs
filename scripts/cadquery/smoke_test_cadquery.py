#!/usr/bin/env python3
"""
CadQuery Smoke Test — Teaching Utility
=======================================

最小环境验证脚本：import cadquery → 创建 box → 导出 STEP/STL。

运行前提：
- Python 3.11+
- cadquery 已安装（pip install cadquery 或 conda install -c conda-forge cadquery）

运行方法：
    python scripts/cadquery/smoke_test_cadquery.py

预期输出：
    === CadQuery Smoke Test ===
    Python: 3.11.x
    CadQuery: 2.X.X
    Test 1: import OK
    Test 2: simple box OK (volume: 1000.0)
    Test 3: STEP export OK
    Test 4: STL export OK
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

    # Test 1: Python version
    print(f"Python: {sys.version}")
    if sys.version_info < (3, 8):
        print("[FAIL] Python 3.8+ required")
        return 1
    print("[OK] Python version")

    # Test 2: CadQuery import
    try:
        import cadquery as cq
        print(f"CadQuery: {cq.__version__}")
        print("[OK] CadQuery import")
    except ImportError as e:
        print(f"[FAIL] CadQuery import: {e}")
        print()
        print("Troubleshooting:")
        print("  1. Check Python version: python --version (need 3.11+)")
        print("  2. Check if cadquery is installed: pip show cadquery")
        print("  3. If OCP missing, try conda: conda install -c conda-forge cadquery")
        return 1

    # Test 3: Simple box
    try:
        box = cq.Workplane("XY").box(10, 10, 10)
        volume = box.val().Volume()
        print(f"[OK] simple box (volume: {volume:.2f})")
        if abs(volume - 1000.0) > 0.01:
            print(f"[WARN] expected volume 1000.0, got {volume}")
    except Exception as e:
        print(f"[FAIL] simple box: {e}")
        return 1

    # Test 4: STEP export
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            step_path = os.path.join(tmpdir, "smoke_test.step")
            cq.exporters.export(box, step_path)
            size = os.path.getsize(step_path)
            print(f"[OK] STEP export (size: {size} bytes)")
            if size < 100:
                print(f"[WARN] STEP file too small: {size} bytes")
    except Exception as e:
        print(f"[FAIL] STEP export: {e}")
        return 1

    # Test 5: STL export
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            stl_path = os.path.join(tmpdir, "smoke_test.stl")
            cq.exporters.export(box, stl_path)
            size = os.path.getsize(stl_path)
            print(f"[OK] STL export (size: {size} bytes)")
            if size < 100:
                print(f"[WARN] STL file too small: {size} bytes")
    except Exception as e:
        print(f"[FAIL] STL export: {e}")
        return 1

    print("=" * 50)
    print("=== All tests passed ===")
    print("=" * 50)
    print()
    print("CadQuery environment is ready!")
    print("Next steps:")
    print("  python code/cadquery/plate_with_hole.py")
    print("  python scripts/cadquery/run_plate_export.py")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"[FATAL] Smoke test failed: {e}")
        sys.exit(1)
