"""
L 型支架变体 — CadQuery 教学示例 (V7B)
====================================

本文件是 CAD-CAM-Technology-docs 项目的教学示例，
配合 examples/cadquery-advanced-features.rst 使用。

目标
----
演示如何用 CadQuery 从"板"扩展到"支架"：
1. 多实体组合（底板 + 立板）
2. 多种孔（4 个安装孔 + 1 个大孔）
3. 内棱边圆角（缓解应力）
4. 布尔运算（union）

教学定位
--------
- 这是 :doc:`examples/bracket-capstone-project` 的简化代码化版
- 完整 Capstone 涉及更多工程细节，本文件不覆盖
- 重点是参数组织 + 特征组合 + 布尔运算的演示

依赖
----
- cadquery >= 2.0
- 安装：pip install cadquery
- 运行：python bracket_variant.py
"""

import cadquery as cq


# ============================================================
# 参数集中区
# ============================================================

# 底板参数
base_length = 100.0            # 底板长度（X 方向）
base_width = 60.0              # 底板宽度（Y 方向）
base_thickness = 10.0          # 底板厚度（Z 方向）

# 立板参数
vertical_height = 80.0         # 立板高度（Z 方向）
vertical_thickness = 10.0      # 立板厚度（X 方向）

# 孔参数
mounting_hole_diameter = 8.0   # 底板安装孔（4 个角孔）
side_hole_diameter = 12.0      # 立板中心大孔

# 圆角参数
fillet_radius = 5.0            # 内棱边圆角半径

# 输出文件名
output_step = "bracket_variant.step"
output_stl = "bracket_variant.stl"


# ============================================================
# 几何建模
# ============================================================

def build_base_plate():
    """构造底板（含 4 个安装孔）。"""
    # 基础底板
    base = cq.Workplane("XY").box(base_length, base_width, base_thickness)

    # 4 个角孔（安装孔）
    # 孔位置：距板边 mounting_hole_diameter 的中心矩形
    spacing_x = base_length - 2 * mounting_hole_diameter
    spacing_y = base_width - 2 * mounting_hole_diameter

    base = (
        base
        .faces(">Z")
        .workplane()
        .rect(spacing_x, spacing_y, forConstruction=True)
        .vertices()
        .hole(mounting_hole_diameter)
    )

    return base


def build_vertical_plate():
    """构造立板（含 1 个中心大孔）。"""
    # 立板定位：
    # X: 底板右端 - vertical_thickness/2
    # Y: 底板中心 (0)
    # Z: 底板顶面 (base_thickness)
    vertical = (
        cq.Workplane("XY")
        .transformed(
            offset=(
                base_length / 2 - vertical_thickness / 2,
                0,
                base_thickness,
            )
        )
        .box(vertical_thickness, base_width, vertical_height)
    )

    # 立板中心大孔
    vertical = (
        vertical
        .faces(">Z")
        .workplane()
        .hole(side_hole_diameter)
    )

    return vertical


def build_bracket():
    """组装 L 型支架：底板 + 立板 + 圆角。"""
    # 分别构造底板和立板
    base = build_base_plate()
    vertical = build_vertical_plate()

    # 布尔并集：合并两个实体
    bracket = base.union(vertical)

    # 内棱边圆角（底板和立板连接处的内角）
    # |Z：竖直棱边
    # >X：X 正方向的最外侧棱边
    bracket = bracket.edges("|Z or >X").fillet(fillet_radius)

    return bracket


# ============================================================
# 主流程
# ============================================================

def main():
    """主流程：构建 + 导出。"""
    print(f"=== CadQuery 进阶示例：L 型支架变体 ===")
    print(f"底板: {base_length} x {base_width} x {base_thickness} mm")
    print(f"立板: {vertical_thickness} x {base_width} x {vertical_height} mm")
    print(f"安装孔: 4 x Φ{mounting_hole_diameter} mm (底板角孔)")
    print(f"中心孔: 1 x Φ{side_hole_diameter} mm (立板)")
    print(f"圆角: R{fillet_radius} mm")

    # 构建几何
    bracket = build_bracket()

    # 导出
    cq.exporters.export(bracket, output_step)
    cq.exporters.export(bracket, output_stl)
    print(f"[OK] 已导出: {output_step}, {output_stl}")


if __name__ == "__main__":
    main()