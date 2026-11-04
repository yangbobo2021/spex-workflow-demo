# SPEX 四工作流最小示例

一个十几行的 Python 整数加法程序，用来验证 SPEX 的四个工作流是否真正执行：

| 工作流 | 本仓库的练习 | 看什么结果 |
| --- | --- | --- |
| `extract-specs` | 从已有加法程序提取规格 | `specs/`、审查记录、lint 结果、人类 Gate |
| `decide` | 设计可选的 `--absolute` 功能 | 两方独立提案、设计提交、独立复审 |
| `code` | 按审定规格实现该功能 | 实现提交、真实 CLI 测试、独立复审 |
| `acceptance-orchestrate` | 验收一个大整数绝对值场景 | 真实执行、独立结论、报告与证据 |

**只有一个产品文件，没有数据库、服务或第三方 Python 依赖。** 这个仓库是工作流冒烟示例，不是性能或全面能力评测。

## 先运行程序

需要 Python 3.10+。macOS / Linux：

```sh
python3 add.py 2 3
# 5
python3 add.py 2147483647 1
# 2147483648
python3 -B -m unittest discover -s tests -v
```

Windows 把上面的 `python3` 换成 `python`；测试通过 `sys.executable` 启动子进程，不依赖 shell 语法。

## 然后验证工作流

按 [四步操作说明](docs/workflow-checks.md) 安装包、准备干净工作区，再逐条复制请求。当前需求在 [docs/requirements.md](docs/requirements.md)。

`main` / `baseline-v1` 故意不带 `specs/`，也没有实现 `--absolute`，这样第一个工作流有规格可提取，后两个工作流有一个真实的小功能可做。操作说明中的后续变更不是当前产品行为。

重复测试时重新克隆 `baseline-v1` 到新目录，并从该基线建测试分支；不要把第一次生成的规格和功能带进下一轮，也不要覆盖旧结果。这个标签是固定测试起点，不代表四个 AI 工作流已在本仓库通过验收。

本仓库只在测试分支执行本地提交；四步请求均不要求推送、创建 PR 或合并。
