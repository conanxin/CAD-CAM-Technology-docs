#!/usr/bin/env python3
"""
Verify Exported STEP/STL Files — Teaching Utility
===================================================

验证导出的 STEP/STL 文件格式：
- 文件存在
- 文件大小合理
- STEP 包含 ISO-10303-21 头
- STL 以 solid 开头（ASCII）或为二进制

运行方法：
    python scripts/cadquery/verify_exports.py [file1.step] [file2.stl] ...

如果无参数，检查 local-exports/ 目录下的常见文件。
"""

import os
import sys
import glob


def verify_step(filepath):
    """验证 STEP 文件。"""
    issues = []

    if not os.path.exists(filepath):
        issues.append("file does not exist")
        return issues

    size = os.path.getsize(filepath)
    if size < 1024:
        issues.append(f"file too small: {size} bytes (expect > 1KB)")

    with open(filepath, "r", errors="ignore") as f:
        head = f.read(100)
    if "ISO-10303-21" not in head:
        issues.append("missing ISO-10303-21 header (not a STEP file?)")

    return issues


def verify_stl(filepath):
    """验证 STL 文件。"""
    issues = []

    if not os.path.exists(filepath):
        issues.append("file does not exist")
        return issues

    size = os.path.getsize(filepath)
    if size < 100:
        issues.append(f"file too small: {size} bytes (expect > 100B)")

    with open(filepath, "rb") as f:
        head = f.read(80)
    if head.startswith(b"solid"):
        pass  # ASCII STL
    elif len(head) >= 80:
        pass  # Binary STL (header is 80 bytes)
    else:
        issues.append("unknown STL format")

    return issues


def main():
    if len(sys.argv) > 1:
        files = sys.argv[1:]
    else:
        # 默认检查 local-exports/ 目录
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.dirname(os.path.dirname(script_dir))
        export_dir = os.path.join(repo_root, "local-exports")
        files = sorted(glob.glob(os.path.join(export_dir, "*.step")))
        files += sorted(glob.glob(os.path.join(export_dir, "*.stp")))
        files += sorted(glob.glob(os.path.join(export_dir, "*.stl")))

    if not files:
        print("No files to verify.")
        print("Usage: python verify_exports.py [file1.step] [file2.stl] ...")
        print("  Or export files to local-exports/ first.")
        return 1

    print("=" * 60)
    print("=== Verify Exported Files ===")
    print("=" * 60)

    total = 0
    passed = 0
    for f in files:
        total += 1
        size = os.path.getsize(f) if os.path.exists(f) else 0
        print(f"\n[{os.path.basename(f)}] ({size} bytes)")

        if f.endswith(".step") or f.endswith(".stp"):
            issues = verify_step(f)
        elif f.endswith(".stl"):
            issues = verify_stl(f)
        else:
            print("  [SKIP] unknown extension")
            total -= 1
            continue

        if not issues:
            print("  [OK] all checks passed")
            passed += 1
        else:
            for issue in issues:
                print(f"  [WARN] {issue}")

    print()
    print("=" * 60)
    print(f"Summary: {passed}/{total} files passed all checks")
    print("=" * 60)
    print()
    print("Note: These checks only verify file format, not geometry.")
    print("To verify geometry, open the files in FreeCAD.")

    return 0 if passed == total else 1


if __name__ == "__main__":
    sys.exit(main())
