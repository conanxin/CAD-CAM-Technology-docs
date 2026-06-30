"""
简化支架装配体 — CadQuery Assembly 教学示例 (V8A)
==================================================

本文件是 CAD-CAM-Technology-docs 项目的 V8A 教学示例，
配合 examples/cadquery-assembly-intro.rst 使用。

教学目的
--------
演示如何用 CadQuery 的 Assembly 表达"底板 + 立板 + 螺栓 + 销钉"的多零件关系。

注意
----
本文件是教学示例（teaching example），不作为工业生产模型（not for industrial production）：
- 螺栓和销钉的尺寸是教学示意值，不可直接用于实际设计
- 不包含工程约束（公差、配合、过盈/间隙等）
- 不替代商业 CAD 装配设计工具
- 真实工程中应根据需求选择合适的工具

与 V7C 区别
----------
- V7C bracket_capstone.py：底板 + 立板 union 成一个实体
- V8A bracket_assembly.py：底板、立板、螺栓、销钉作为独立零件 + Assembly 容器

依赖
----
- cadquery >= 2.0
- 安装：pip install cadquery
- 运行：python bracket_assembly.py

输出
----
bracket_assembly.step    (STEP 格式，包含所有装配体零件)
"""

import cadquery as cq


# ============================================================
# 参数集中区
# ============================================================

# 底板参数（与 V6A / V7C 一致）
base_length = 200.0
base_width = 60.0
base_thickness = 10.0
base_hole_diameter = 8.0
base_hole_spacing = 100.0

# 立板参数
vertical_length = 40.0
vertical_height = 100.0
vertical_thickness = 10.0
vertical_hole_diameter = 6.0
vertical_hole_spacing = 50.0

# 螺栓参数（教学示意）
bolt_diameter = 8.0          # 螺栓直径（与底板孔匹配）
bolt_head_diameter = 13.0    # 螺栓头直径
bolt_head_height = 5.0       # 螺栓头高度
bolt_length = 25.0           # 螺栓总长
bolt_count = 2               # 螺栓数量

# 销钉参数（教学示意）
pin_diameter = 6.0           # 销钉直径（与立板孔匹配）
pin_length = 15.0            # 销钉长度

# 圆角
fillet_radius = 3.0

# 输出文件名
output_step = "bracket_assembly.step"


# ============================================================
# 组件构造函数
# ============================================================

def make_base_plate():
    """构造底板（与 V7C 底板几何一致）。

    坐标系：以原点为底板底面中心，底板向 +Z 方向延伸。
    """
    plate = cq.Workplane("XY").box(
        base_length, base_thickness, base_width
    )

    # 2 个底板安装孔
    plate = (
        plate
        .faces(">Z")
        .workplane()
        .rect(base_hole_spacing, 0, forConstruction=True)
        .vertices()
        .hole(base_hole_diameter)
    )

    return plate


def make_vertical_plate():
    """构造立板（与 V7C 立板几何一致）。

    坐标系：与底板相对定位。
    """
    vertical = (
        cq.Workplane("XY")
        .transformed(offset=(vertical_length / 2.0, 0, base_thickness + vertical_height / 2.0))
        .box(vertical_length, vertical_thickness, vertical_height)
    )

    # 1 个立板大孔（简化：销钉孔）
    vertical = (
        vertical
        .faces(">Z")
        .workplane()
        .hole(vertical_hole_diameter)
    )

    return vertical


def make_bolt(head_diameter, head_height, shaft_diameter, shaft_length):
    """构造一个简化螺栓（教学示意）。

    螺栓结构：圆柱头 + 圆柱杆。
    注：实际工程中需要螺纹、退刀槽、扳手孔等细节。
    """
    # 头（圆柱体）
    head = cq.Workplane("XY").circle(head_diameter / 2.0).extrude(head_height)

    # 杆（圆柱体）
    shaft = (
        cq.Workplane("XY")
        .workplane(offset=head_height)
        .circle(shaft_diameter / 2.0)
        .extrude(shaft_length - head_height)
    )

    # 合并
    bolt = head.union(shaft)
    return bolt


def make_pin(diameter, length):
    """构造一个简化销钉（教学示意）。"""
    return cq.Workplane("XY").circle(diameter / 2.0).extrude(length)


# ============================================================
# 装配体构建
# ============================================================

def build_assembly():
    """构建完整的支架装配体。

    组件清单：
    - 1 × base_plate
    - 1 × vertical_plate
    - 2 × mounting_bolt
    - 1 × side_pin
    """
    # 创建装配体容器
    assembly = cq.Assembly(name="bracket_assembly")

    # 1. 添加底板（位于装配体原点）
    base = make_base_plate()
    assembly.add(
        base,
        name="base_plate",
        color=cq.Color(0.7, 0.7, 0.8, 1.0),  # 浅蓝色
    )

    # 2. 添加立板（坐标已通过 make_vertical_plate 定位）
    vertical = make_vertical_plate()
    assembly.add(
        vertical,
        name="vertical_plate",
        loc=cq.Location(cq.Vector(0, 0, 0)),
        color=cq.Color(0.7, 0.8, 0.7, 1.0),  # 浅绿色
    )

    # 3. 添加螺栓（2 个，位于底板安装孔位）
    #    螺栓头部朝上（+Y 方向），从底板上方插入
    bolt = make_bolt(
        head_diameter=bolt_head_diameter,
        head_height=bolt_head_height,
        shaft_diameter=bolt_diameter,
        shaft_length=bolt_length,
    )

    # 螺栓 1：左侧孔位
    assembly.add(
        bolt,
        name="bolt_left",
        loc=cq.Location(
            cq.Vector(
                -base_hole_spacing / 2.0,                    # X 位置
                base_thickness / 2.0,                        # Y 位置：板厚中心
                base_thickness - bolt_length,                 # Z 位置：从板底穿出
            )
        ),
        color=cq.Color(0.8, 0.7, 0.5, 1.0),  # 棕色
    )

    # 螺栓 2：右侧孔位
    assembly.add(
        bolt,
        name="bolt_right",
        loc=cq.Location(
            cq.Vector(
                base_hole_spacing / 2.0,
                base_thickness / 2.0,
                base_thickness - bolt_length,
            )
        ),
        color=cq.Color(0.8, 0.7, 0.5, 1.0),
    )

    # 4. 添加销钉（位于立板中心孔）
    pin = make_pin(pin_diameter, pin_length)
    assembly.add(
        pin,
        name="side_pin",
        loc=cq.Location(
            cq.Vector(
                vertical_length / 2.0,                      # X：立板中心
                vertical_thickness / 2.0,                   # Y：立板中心
                base_thickness + vertical_height / 2.0 - pin_length / 2.0,  # Z：立板中心
            )
        ),
        color=cq.Color(0.6, 0.6, 0.6, 1.0),  # 灰色
    )

    return assembly


# ============================================================
# 主流程
# ============================================================

def main():
    """主流程：构建 + 导出。"""
    print(f"=== CadQuery 支架装配体 (V8A) ===")
    print(f"组件清单：")
    print(f"  - 1 x base_plate ({base_length} x {base_thickness} x {base_width} mm)")
    print(f"  - 1 x vertical_plate ({vertical_length} x {vertical_thickness} x {vertical_height} mm)")
    print(f"  - {bolt_count} x mounting_bolt (M{bolt_diameter} 示意)")
    print(f"  - 1 x side_pin (Phi{pin_diameter} 示意)")
    print(f"")
    print(f"教学声明：螺栓和销钉尺寸是教学示意值，不可直接用于实际设计")

    # 构建装配体
    assembly = build_assembly()

    # 导出整个装配体为单个 STEP
    assembly.save(output_step)
    print(f"[OK] 装配体已导出: {output_step}")
    print(f"")
    print(f"提示：")
    print(f"  - 用 FreeCAD 打开 {output_step} 可以看到完整装配体")
    print(f"  - 选中单个零件可单独保存为 STEP（用于 CAM 加工）")
    print(f"  - 装配体是教学示意，不替代工业级装配设计")


if __name__ == "__main__":
    main()