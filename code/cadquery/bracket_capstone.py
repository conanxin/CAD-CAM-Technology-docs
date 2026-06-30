"""
L 型支架 Capstone — CadQuery 代码化建模
=====================================

本文件是 CAD-CAM-Technology-docs 项目的 V7C 教学示例，
配合 examples/cadquery-bracket-capstone.rst 使用。

目标
----
用 CadQuery 重写 V6A FreeCAD 支架 Capstone。
关键约束：与 bracket-capstone-project 的几何参数完全一致。

V6A 支架参数（来自 bracket-capstone-project.rst）：
- 整体尺寸: 200 × 140 × 10 mm (L × H × T)
- 底板: 200 × 40 × 10 mm
- 立板: 40 × 100 × 10 mm（X × Z × Y）
- 底板安装孔: 2 × Φ8 mm, 间距 100 mm
- 立板安装孔: 2 × Φ6 mm, 间距 50 mm
- 圆角: R3 mm
- 倒角: 0.5 × 45° (CAM 友好)

注意
----
本文件是教学示例，重在清晰度和可读性：
- 不追求工业级鲁棒性
- 不做参数验证、异常处理、单元测试
- 不考虑装配体、五轴加工等高级特性
- 真实工程中应根据需求选择工具

依赖
----
- cadquery >= 2.0
- 安装：pip install cadquery
- 运行：python bracket_capstone.py

输出
----
bracket_capstone.step    (STEP 格式，保留 B-rep)
bracket_capstone.stl     (STL 格式，三角网格)
"""

import cadquery as cq


# ============================================================
# 参数集中区
# ============================================================

# 整体尺寸（毫米）
outer_length = 200.0      # X 方向
outer_height = 140.0      # Z 方向
thickness = 10.0          # Y 方向（板厚）

# 底板参数
base_length = 200.0       # 与 outer_length 相同
base_height = 40.0        # 底板在 Z 方向高度
# 注：底板厚度（Y 方向）= thickness

# 立板参数
vertical_length = 40.0    # 立板 X 方向厚度
vertical_height = 100.0   # 立板在 Z 方向高度（140-40=100）
# 注：立板厚度（Y 方向）= thickness

# 底板安装孔
base_hole_diameter = 8.0
base_hole_count = 2
base_hole_spacing = 100.0  # 两个孔中心间距

# 立板安装孔
vertical_hole_diameter = 6.0
vertical_hole_count = 2
vertical_hole_spacing = 50.0

# 圆角 / 倒角
fillet_radius = 3.0        # 内棱边圆角
chamfer_size = 0.5         # 外棱边倒角（CAM 友好，便于入刀）

# 输出文件名
output_step = "bracket_capstone.step"
output_stl = "bracket_capstone.stl"


# ============================================================
# 几何建模
# ============================================================

def build_base_plate():
    """构造底板（含 base_hole_count 个安装孔）。

    底板坐标系：以原点为底板底面中心，底板向 +Z 方向延伸。
    占据空间：X=[-100, 100], Y=[-5, 5], Z=[0, 40]
    """
    # 基础底板（中心在原点，向 +Z 方向延伸）
    base = cq.Workplane("XY").box(
        base_length,
        thickness,        # Y 方向
        base_height,      # Z 方向
    )

    # 底板安装孔（在底板顶面，X 方向上均匀分布）
    if base_hole_count >= 2:
        # 构造矩形：用于定位孔位
        # 矩形的 X 跨度 = 孔间距，Y 跨度 = 0（即孔在 X 方向两端）
        base = (
            base
            .faces(">Z")                                    # 底板顶面
            .workplane()
            .rect(base_hole_spacing, 0, forConstruction=True)  # 构造矩形
            .vertices()                                       # 2 个顶点
            .hole(base_hole_diameter)                         # 每个顶点打孔
        )
    elif base_hole_count == 1:
        # 中心孔
        base = (
            base
            .faces(">Z")
            .workplane()
            .hole(base_hole_diameter)
        )

    return base


def build_vertical_plate():
    """构造立板（含 vertical_hole_count 个安装孔）。

    立板定位：在底板左侧上方，垂直于底板。
    - X：底板左端 → 立板中心 → 立板厚度 40
    - Y：与底板同厚
    - Z：从底板顶面（40）→ 立板顶面（140）

    占据空间：X=[0, 40], Y=[-5, 5], Z=[40, 140]
    """
    # 立板的中心位置
    # 底板占据 Z=[0, 40]，立板从 Z=40 开始
    # X 方向：底板中心在 X=0，立板中心应在 X=vertical_length/2 = 20
    #   （即立板左端紧贴底板左端，立板占据 X=[0, 40]）
    vertical_offset_x = vertical_length / 2.0
    vertical_offset_z = base_height + vertical_height / 2.0

    # 基础立板
    vertical = (
        cq.Workplane("XY")
        .transformed(offset=(vertical_offset_x, 0, vertical_offset_z))
        .box(vertical_length, thickness, vertical_height)
    )

    # 立板安装孔
    if vertical_hole_count >= 2:
        # 在立板左侧（朝外的一面）打孔
        # 孔位中心：Z 在 ±vertical_hole_spacing/2 附近
        vertical = (
            vertical
            .faces("<X")                                     # 立板左侧（朝外）
            .workplane()
            .rect(0, vertical_hole_spacing, forConstruction=True)  # Z 方向两端
            .vertices()
            .hole(vertical_hole_diameter)
        )
    elif vertical_hole_count == 1:
        vertical = (
            vertical
            .faces("<X")
            .workplane()
            .hole(vertical_hole_diameter)
        )

    return vertical


def build_bracket():
    """组装 L 型支架：底板 + 立板 + 圆角 + 倒角。"""
    # 分别构造底板和立板
    base = build_base_plate()
    vertical = build_vertical_plate()

    # 合并为一个实体
    bracket = base.union(vertical)

    # 内棱边圆角（底板和立板连接处的内角）
    # 选择条件：|Z（竖直棱边）OR >X（X+方向的最外侧棱边）
    # 注意：fillet 必须在所有 hole 之后
    bracket = bracket.edges("|Z or >X").fillet(fillet_radius)

    # 外棱边倒角（CAM 友好，便于刀具入料）
    # 简化版：对所有 >X 的外棱边做倒角
    # 注：完整倒角需要更复杂的选择器，本例仅演示 CAM 友好倒角
    if chamfer_size > 0:
        try:
            bracket = bracket.edges(">X").chamfer(chamfer_size)
        except Exception as e:
            # 如果倒角选择器失败，跳过倒角（教学容错）
            print(f"[WARN] 倒角失败，已跳过: {e}")

    return bracket


# ============================================================
# 验证函数（教学性）
# ============================================================

def verify_dimensions(bracket):
    """打印关键尺寸（教学性验证，不实际运行）。

    在真实运行中，可以通过 FreeCAD 导入 STEP 后目视检查。
    """
    print(f"\n=== 几何验证 ===")
    print(f"整体长度: {outer_length} mm")
    print(f"整体高度: {outer_height} mm")
    print(f"板厚: {thickness} mm")
    print(f"底板: {base_length} x {thickness} x {base_height} mm")
    print(f"立板: {vertical_length} x {thickness} x {vertical_height} mm")
    print(f"底板孔: {base_hole_count} x Φ{base_hole_diameter} mm")
    print(f"立板孔: {vertical_hole_count} x Φ{vertical_hole_diameter} mm")
    print(f"圆角 R{fillet_radius}, 倒角 {chamfer_size} mm")
    print(f"\n（运行后请用 FreeCAD 打开 {output_step} 验证几何）")


# ============================================================
# 主流程
# ============================================================

def main():
    """主流程：构建 + 验证 + 导出。"""
    print(f"=== CadQuery 支架 Capstone (V7C) ===")
    print(f"建模方式: CadQuery 代码化")
    print(f"对照: V6A FreeCAD 图形化 (bracket-capstone-project)")

    # 构建支架
    bracket = build_bracket()

    # 打印验证信息
    verify_dimensions(bracket)

    # 导出 STEP 和 STL
    cq.exporters.export(bracket, output_step)
    cq.exporters.export(bracket, output_stl)
    print(f"\n[OK] 已导出:")
    print(f"  - {output_step}  (CAD/CAM 流转用)")
    print(f"  - {output_stl}   (3D 打印用)")


if __name__ == "__main__":
    main()