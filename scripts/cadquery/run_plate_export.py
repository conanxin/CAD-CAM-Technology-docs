#!/usr/bin/env python3
"""
Run Plate Export — Teaching Utility
====================================

运行 plate_with_hole.py 的逻辑并导出 STEP/STL 到 local-exports/ 目录。

运行前提：
- Python 3.11+
- cadquery 已安装

运行方法：
    python scripts/cadquery/run_plate_export.py

输出：
    local-exports/plate_with_hole.step
    local-exports/plate_with_hole.stl

如果 cadquery 不可用，打印清晰错误并退出非 0。
"""

import sys
import os


def main():
    # 确认 cadquery 可用
    try:
        import cadquery as cq
    except ImportError as e:
        print("[ERROR] Cannot import cadquery.")
        print(f"  Detail: {e}")
        print()
        print("Troubleshooting:")
        print("  1. Check Python version: python --version (need 3.11+)")
        print("  2. Install cadquery: pip install cadquery")
        print("  3. Or use conda: conda install -c conda-forge cadquery")
        print()
        print("See: examples/cadquery-local-environment-guide.rst")
        return 1

    # 创建输出目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(os.path.dirname(script_dir))
    output_dir = os.path.join(repo_root, "local-exports")
    os.makedirs(output_dir, exist_ok=True)

    print(f"CadQuery version: {cq.__version__}")
    print(f"Output directory: {output_dir}")
    print()

    # 复用 plate_with_hole.py 的核心逻辑
    # 参数与 V7A 一致：80×50×8 矩形板，中心孔直径 20
    length = 80
    width = 50
    thickness = 8
    hole_diameter = 20

    print(f"Creating plate: {length}×{width}×{thickness} mm, hole Ø{hole_diameter} mm")

    plate = (
        cq.Workplane("XY")
        .box(length, width, thickness)
        .faces(">Z")
        .workplane()
        .hole(hole_diameter)
    )

    # 添加 8 条棱边倒角（1mm），与 V7A 一致
    plate = plate.edges("not(|Z)").chamfer(1.0)

    volume = plate.val().Volume()
    print(f"Plate volume: {volume:.2f} mm³")

    # 导出 STEP
    step_path = os.path.join(output_dir, "plate_with_hole.step")
    cq.exporters.export(plate, step_path)
    step_size = os.path.getsize(step_path)
    print(f"[OK] STEP exported: {step_path} ({step_size} bytes)")

    # 导出 STL
    stl_path = os.path.join(output_dir, "plate_with_hole.stl")
    cq.exporters.export(plate, stl_path)
    stl_size = os.path.getsize(stl_path)
    print(f"[OK] STL exported: {stl_path} ({stl_size} bytes)")

    print()
    print("Export complete!")
    print("Next: verify with scripts/cadquery/verify_exports.py")
    print(f"  python scripts/cadquery/verify_exports.py {step_path} {stl_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
