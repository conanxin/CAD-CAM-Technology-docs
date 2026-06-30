# scripts/cadquery/ — CadQuery 辅助脚本

## 脚本列表

| 脚本 | 用途 | 运行前提 |
|------|------|---------|
| `smoke_test_cadquery.py` | 最小环境验证（import + box + export） | Python 3.11+ + cadquery |
| `run_plate_export.py` | 导出 plate_with_hole 到 local-exports/ | Python 3.11+ + cadquery |
| `verify_exports.py` | 验证导出的 STEP/STL 文件格式 | 无（标准库 only） |

## 快速开始

```bash
# 1. 确认环境
python scripts/cadquery/smoke_test_cadquery.py

# 2. 导出 plate
python scripts/cadquery/run_plate_export.py

# 3. 验证导出
python scripts/cadquery/verify_exports.py
```

## 推荐 Python 版本

- **Python 3.11+**（CadQuery 2.8 要求）
- Python 3.10 可用 CadQuery 2.3（但需要手动处理 OCP）

## 输出目录

导出的文件默认写入 `local-exports/`：

```
local-exports/
├── plate_with_hole.step
├── plate_with_hole.stl
└── ...
```

`local-exports/` 已加入 `.gitignore`，默认不提交。

## 本仓库默认不提交生成的 STEP/STL

- 教学示例导出文件**不**提交到仓库
- 如需提交小型教学文件（< 100KB），使用 `git add -f`
- 大型文件不建议提交

## 相关文档

- [CadQuery 本地环境指南](../../examples/cadquery-local-environment-guide.rst)
- [CadQuery 运行试点（V9B）](../../examples/cadquery-runtime-export-pilot.rst)
- [CadQuery 参数化建模（V7A）](../../examples/cadquery-parametric-modeling.rst)

## 教学声明

这些脚本是**教学辅助工具**，不是生产工具：

- 不保证在所有环境下可用
- 不替代 CadQuery 官方文档
- 不适合真实工程或生产环境
