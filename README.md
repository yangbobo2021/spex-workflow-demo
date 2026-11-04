# SPEX 四工作流轻量示例

起点 `baseline-lite-v2` 是一个只输出 `hello` 的 Python 程序，仅含一条需求 HELLO-01 和一次真实子进程测试；当前需求以 [docs/requirements.md](docs/requirements.md) 为准。它用于检查工作流能否运行完，不用于全面评测。

```sh
python3 hello.py
python3 -B -m unittest discover -s tests -v
```

Windows 把 `python3` 换成 `python`。无需安装 Python 依赖。

按 [四步操作说明](docs/workflow-checks.md) 依次执行：提取现有规格 → 设计 `--upper` → 实现 → 验收一次 `HELLO` 输出。

`demo-lite` / `baseline-lite-v2` 是这一版起点，没有 `specs/`，没有实现 `--upper`。重新测试请克隆该标签到新目录。旧加法示例仍在 `main` / `baseline-v1`，不要混用两版需求和命令。

本版减少业务范围，保留工作流原有的独立审查、人工 Gate、lint 和交接。Git、许可等模板核对若是工作流必需，仍照常执行；不保证几分钟内完成。发布轻量基线不表示四个 AI 工作流已通过。
