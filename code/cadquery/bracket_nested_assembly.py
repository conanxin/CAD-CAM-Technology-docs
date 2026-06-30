"""
嵌套装配体 — CadQuery 教学示例 (V8C)
=====================================

本文件是 CAD-CAM-Technology-docs 项目的 V8C 教学示例，
配合 examples/cadquery-assembly-placement-mini-lab.rst 使用。

教学目的
--------
演示如何用：
1. 显式 Location 表达组件位置
2. 局部 vs 全局坐标系的区别
3. 子装配（bolt_pair）的组织
4. 教学型 placement 数据结构

注意
----
- 本文件是教学示例（teaching example）
- 不作为工业生产模型（not for industrial production）
- 不是真实干涉求解器（not a real interference solver）
- 螺栓 / 销钉尺寸是教学示意值
- 不做真实动画、不做真实约束求解

依赖
----
- cadquery >= 2.0
- 运行：python bracket_nested_assembly.py

与 V8A 区别
----------
- V8A bracket_assembly.py：所有组件直接 add 到主装配
- V8C bracket_nested_assembly.py：使用子装配（bolt_pair）组织相关组件

输出
----
bracket_nested_assembly.step
"""

import cadquery as cq


# ============================================================
# 参数集中区
# ============================================================

# 底板参数
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

# 螺栓参数
bolt_diameter = 8.0
bolt_head_diameter = 13.0
bolt_head_height = 5.0
bolt_length = 25.0

# 销钉参数
pin_diameter = 6.0
pin_length = 15.0


# ============================================================
# Placement 数据结构（教学型）
# ============================================================

PLACEMENT_TABLE = {
    "base_plate": {
        "type": "main_part",
        "location": (0.0, 0.0, 0.0),
        "rotates": False,
        "purpose": "装配体地面",
    },
    "vertical_plate": {
        "type": "main_part",
        "location": (vertical_length / 2.0, 0.0, base_thickness + vertical_height / 2.0),
        "rotates": False,
        "purpose": "装配体立面",
    },
    "bolt_left": {
        "type": "fastener",
        "location": (-base_hole_spacing / 2.0, base_thickness / 2.0, base_thickness - bolt_length),
        "rotates": False,
        "purpose": "左侧底板固定",
    },
    "bolt_right": {
        "type": "fastener",
        "location": (base_hole_spacing / 2.0, base_thickness / 2.0, base_thickness - bolt_length),
        "rotates": False,
        "purpose": "右侧底板固定",
    },
    "side_pin": {
        "type": "fastener",
        "location": (
            vertical_length / 2.0,
            vertical_thickness / 2.0,
            base_thickness + vertical_height / 2.0 - pin_length / 2.0,
        ),
        "rotates": False,
        "purpose": "立板定位",
    },
}


# ============================================================
# 组件构造函数
# ============================================================

def make_base_plate():
    """构造底板（含 2 个安装孔）。"""
    plate = cq.Workplane("XY").box(base_length, base_thickness, base_width)
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
    """构造立板（含 1 个中心孔）。"""
    vertical = (
        cq.Workplane("XY")
        .transformed(offset=(vertical_length / 2.0, 0, base_thickness + vertical_height / 2.0))
        .box(vertical_length, vertical_thickness, vertical_height)
    )
    vertical = (
        vertical
        .faces(">Z")
        .workplane()
        .hole(vertical_hole_diameter)
    )
    return vertical


def make_bolt():
    """构造简化螺栓（教学示意）。"""
    head = cq.Workplane("XY").circle(bolt_head_diameter / 2.0).extrude(bolt_head_height)
    shaft = (
        cq.Workplane("XY")
        .workplane(offset=bolt_head_height)
        .circle(bolt_diameter / 2.0)
        .extrude(bolt_length - bolt_head_height)
    )
    return head.union(shaft)


def make_pin():
    """构造简化销钉（教学示意）。"""
    return cq.Workplane("XY").circle(pin_diameter / 2.0).extrude(pin_length)


# ============================================================
# 子装配：bolt_pair
# ============================================================

def build_bolt_pair_subassembly():
    """构造螺栓对子装配。

    子装配 = 2 个螺栓 + 共享定位参考。
    """
    subasm = cq.Assembly(name="bolt_pair")

    bolt = make_bolt()

    # 螺栓 1：相对子装配的局部坐标
    subasm.add(
        bolt,
        name="bolt_left",
        loc=cq.Location(cq.Vector(-base_hole_spacing / 2.0, 0, 0)),
        color=cq.Color(0.8, 0.7, 0.5, 1.0),
    )

    # 螺栓 2：相对子装配的局部坐标
    subasm.add(
        bolt,
        name="bolt_right",
        loc=cq.Location(cq.Vector(base_hole_spacing / 2.0, 0, 0)),
        color=cq.Color(0.8, 0.7, 0.5, 1.0),
    )

    return subasm


# ============================================================
# 主装配
# ============================================================

def build_nested_assembly():
    """构建完整的支架装配体（带子装配）。

    结构：
    bracket_nested_assembly (主装配)
    ├── base_plate
    ├── vertical_plate
    ├── bolt_pair (子装配)
    │   ├── bolt_left
    │   └── bolt_right
    └── side_pin
    """
    assembly = cq.Assembly(name="bracket_nested_assembly")

    # 1. 底板
    base = make_base_plate()
    assembly.add(
        base,
        name="base_plate",
        loc=cq.Location(cq.Vector(0, 0, 0)),
        color=cq.Color(0.7, 0.7, 0.8, 1.0),
    )

    # 2. 立板
    vertical = make_vertical_plate()
    assembly.add(
        vertical,
        name="vertical_plate",
        loc=cq.Location(cq.Vector(0, 0, 0)),
        color=cq.Color(0.7, 0.8, 0.7, 1.0),
    )

    # 3. 螺栓对子装配（作为整体加入主装配）
    bolt_pair = build_bolt_pair_subassembly()
    assembly.add(
        bolt_pair,
        name="bolt_pair",
        loc=cq.Location(
            cq.Vector(0, base_thickness / 2.0, base_thickness - bolt_length)
        ),
        color=cq.Color(1.0, 0.0, 0.0, 1.0),  # 红色 - 子装配标记
    )

    # 4. 销钉
    pin = make_pin()
    assembly.add(
        pin,
        name="side_pin",
        loc=cq.Location(
            cq.Vector(
                vertical_length / 2.0,
                vertical_thickness / 2.0,
                base_thickness + vertical_height / 2.0 - pin_length / 2.0,
            )
        ),
        color=cq.Color(0.6, 0.6, 0.6, 1.0),
    )

    return assembly


# ============================================================
# 主流程
# ============================================================

def main():
    """主流程：构建 + 导出。"""
    print("=== CadQuery 嵌套装配体 (V8C) ===")
    print("组件结构：")
    print("  bracket_nested_assembly (主装配)")
    print("  |-- base_plate")
    print("  |-- vertical_plate")
    print("  |-- bolt_pair (子装配)")
    print("  |   |-- bolt_left")
    print("  |   `-- bolt_right")
    print("  `-- side_pin")
    print()
    print("Placement 数据：")
    for name, info in PLACEMENT_TABLE.items():
        print(f"  {name}: {info['location']} ({info['purpose']})")
    print()

    assembly = build_nested_assembly()
    assembly.save("bracket_nested_assembly.step")
    print("[OK] 嵌套装配体已导出: bracket_nested_assembly.step")
    print()
    print("教学说明：")
    print("- 本示例是教学型，不替代商业 CAD 装配设计工具")
    print("- 螺栓 / 销钉尺寸是教学示意值")
    print("- 教学型干涉检查用 checklist，不做真实 OCKT 仿真")


if __name__ == "__main__":
    main()