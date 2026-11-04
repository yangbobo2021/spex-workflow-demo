# 四步操作说明

这里是**人工操作手册和未来变更练习**，不是当前产品规格。当前行为只以 `docs/requirements.md` 为准。四个工作流按顺序在同一测试分支链上运行。

## 0. 准备一次测试

```sh
git clone https://github.com/yangbobo2021/spex-workflow-demo.git
cd spex-workflow-demo
git switch -c test/run-01 baseline-v1
python3 -B -m unittest discover -s tests -v
```

Windows 使用 `python`。程序只需要 Python；运行 AI 工作流还需要 SPEX、可用的 Agent 登录信息，以及工作流自身需要的工具。

### SPEX 与工作流包

本说明对应本轮实际核对过的版本，不承诺后续最新版行为相同：

- SPEX App：`0.9.0-beta.27`。
- 规格提取：`merico-ai/extract-specs`，精确版本 `0.3.0`。
- 测试工作流：`yangbobo2021/app-delivery-acceptance`，精确版本 `0.4.17`。
- `decide`、`code` 和它们调用的 `review`：本轮为 `sublang/playbooks 18.1.3`；在 Playbooks 核对实际版本与就绪状态；若没有这些全局工作流，先按团队约定安装并配置该包，不能只凭名称假设可运行。

在项目的 **Packages → Add… → Registry** 安装前两个公开包。公开安装无需登录包注册表。确认相关 Playbooks 已启用、每个角色已绑定 Player，且 Agent 显示 ready；独立 reviewer 使用独立 Player。

### 如果用 GoodMe workshop

1. 在 Space 登录 `spex.sublang.xyz`。
2. 把本地项目加入可用的 workshop 群组。
3. 在群组项目菜单选择 **Open on GoodMe workshop**，等待服务器项目出现。
4. 后续步骤选择左侧 **GoodMe workshop 下的项目**。本地配置与远程配置是两份，Git 和 Agent 准备也要在实际执行的一端检查。

### 两个容易卡住的前提

- **Git 身份**：在实际执行的仓库中检查 `git config --get user.name`、`git config --get user.email` 和 `git var GIT_AUTHOR_IDENT`。前两项缺失时，即使 Git 能自动推断身份，生成的 Git 规约仍可能要求先配置。设置仓库局部身份即可，不必改全局配置。临时测试身份示例：

  ```sh
  git config --local user.name "SPEX Workflow Demo"
  git config --local user.email "spex-workflow-demo@example.invalid"
  ```

  这是合成测试身份，不是真实人员身份。若准备将结果发布，请使用自己的提交身份。

- **干净工作区**：安装后先看 `git status --short`。SPEX 可能生成 `.gitattributes`、`spex.yaml`、`spex.lock`；检查内容后只提交这些实际生成的文件。不要提交登录信息、Agent 配置、缓存或整包 `.spex/`。本仓库已经忽略常见运行目录。`extract-specs 0.3.0` 要求起步时工作树干净。

以上 Git 操作在远程场景要在服务器项目内执行；也可以把明确的准备要求交给已配置的 `/code`，完成后再开始提取。

## 1. 提取现有规格

复制到 SPEX 新任务：

```text
/extract-specs 请对当前整数加法示例提取最小、忠于现状的规格。当前行为依据 add.py、tests/test_add.py 与 docs/requirements.md；docs/workflow-checks.md 只是未来变更的操作手册，不要把 --absolute 或 ADD-05 提取成已实现行为。Setup 分支用 test/specs-01，中文，脚手架面向 Claude 与 Codex。保留现有 MIT 许可证及 LICENSE 中的声明，不从合成测试 Git 身份推断版权，不执行模板的无关补头任务。按已安装 kit 的正常步骤提取、独立审查并保留 lint 证据，不改产品或现有测试。不推送、不建 PR。人类 Gate 正常提出，不代替人类批准；不要创建真实发布流程或补做无关功能。
```

**核对**：有真实 `specs/`、证据账本及审查结果；人类计划 Gate 和样例包校准需要本人审阅。它们是流程的一部分，等待回复不能记成失败；只有走到最终报告才记作本次提取执行完成。不要为赶进度跳过 Gate，也不要把 lint 通过当成产品验收通过。

## 2. 决定一个小变更

这是**新增功能**：`--absolute` 默认关闭；开启时输出两数和的绝对值，仍为精确整数。示例：`-2 -3 --absolute` 输出 `5`；不开启仍输出 `-5`。

```text
/decide 为当前加法 CLI 设计可选的 --absolute 开关：默认行为不变；开启时只把最终和取绝对值，不是先对两个输入各自取绝对值。保持精确整数和现有错误语义。请让 Coder、Reviewer 独立提案后合成最小规格，更新相关 specs 与 docs/requirements.md：保留 ADD-01 至 ADD-04 的 ID 和默认行为，新增 ADD-05 记录可选绝对值行为，删除“尚无 ADD-05/--absolute”的过时说明。不实现代码，不扩展范围，不推送、不建 PR。完成真实设计提交和嵌套独立 review，报告 design commit、evaluated revision、未解决 findings 后停止。
```

**核对**：有独立提案、设计提交和完成的 review；此时没有提前实现 `--absolute`。需求和规格会先于代码更新，阶段间暂时未实现新需求是正常状态。

## 3. 实现这个小变更

```text
/code 按当前已经审定的 ADD-05 和对应 specs 实现 add.py 的 --absolute，并补充真实 CLI 子进程测试。至少验证：默认 -2 -3 仍输出 -5；-2 -3 --absolute 输出 5；-2 3 --absolute 输出 1；零输出 0；大整数保持精确，原有错误行为不变。只改本功能所需实现、测试及必要规格引用。保留原始测试，不降低断言，不推送、不建 PR。完成 code 的正常独立 review 循环，报告真实测试命令与结果、code-owned commit、最终 evaluated revision 和未解决 findings 后停止。
```

**核对**：`python3 add.py -2 -3 --absolute` 输出 `5`，测试通过，review 完成。编码者说“已提交，等待 review”还不算结束。

## 4. 执行一个验收场景

这一步在上一步完成后运行，目标需求 ADD-05 应当已经存在。只跑一个场景，避免小练习变成全量验收。

```text
/acceptance-orchestrate 当前是这个简单加法示例的仓库根目录。读取 README.md、docs/requirements.md 和实际启动方式。本轮仅针对 ADD-05 依据原文生成测试场景，选一个“负数相加后取绝对值且结果超过 32 位整数范围”的正常场景，实际执行、独立复审并导出最终报告及证据。不需要覆盖率，其他场景保留未执行。可用区分输入为 add.py -2147483648 -1 --absolute，预期 stdout 为 2147483649 加换行、退出码 0、stderr 空。允许准备隔离执行目录和用例，不修改产品源码或原始需求；发现缺陷如实报告，不为通过而修复产品。不推送、不建 PR。直接完成完整流程，不只给计划，报告摘要保持简短并优先给报告和证据路径。
```

**核对**：有实际运行证据、独立 reviewer 的结论、报告文件和路径。清楚区分“产品通过/产品缺陷”与“工作流执行完成/中断”。本轮成功只代表这个选中场景，不代表其他场景或所有工作流组合已被验证。

## 记录与重来

每项记下：执行机器、SPEX/包版本、源提交、会话、生成提交、复审版本、真实测试结果、报告路径、未完成项。不要只截一张“done”。

本轮发现长结果在 Captain 交接时可能被截断；必要时在原会话要求只读续查已有结果，摘要控制在约 350 字符，优先给报告路径；不要为了显示报告重跑测试。

下一轮用新目录重新克隆 `baseline-v1`。已有测试分支、会话和证据保留，不通过强制 reset 或删锁来复位。
