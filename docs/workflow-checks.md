# 四步操作说明：轻量版

这是未来变更的操作手册；当前产品契约只有 `docs/requirements.md` 的 HELLO-01。

## 0. 准备

```sh
git clone --branch baseline-lite-v1 https://github.com/yangbobo2021/spex-workflow-demo.git spex-demo-lite
cd spex-demo-lite
git switch -c test/lite-run-01
python3 -B -m unittest discover -s tests -v
```

在 SPEX 中把项目加入 `spex.sublang.xyz` 的 workshop 群组，然后 **Open on GoodMe workshop**，后续只操作 GoodMe workshop 下的项目。

沿用本轮版本：SPEX `0.9.0-beta.27`，`merico-ai/extract-specs 0.3.0`，`sublang/playbooks 18.1.3`（decide/code/review），`yangbobo2021/app-delivery-acceptance 0.4.17`。在远程项目安装包，确认角色和 Agent ready，独立 reviewer 使用独立 Player。

实际执行端需要有效 Git 身份；临时测试可用仓库局部身份 `SPEX Workflow Demo <spex-workflow-demo@example.invalid>`，不改全局配置。安装生成的 `.gitattributes`、`spex.yaml`、`spex.lock` 经检查后单独提交，保持提取起步时工作区干净。准备工作可交给 `/code`，但不计作下面的正式功能实现测试。

## 1. 提取规格

```text
/extract-specs 为 hello.py 提取最小规格，当前契约仅 docs/requirements.md 的 HELLO-01，测试仅 tests/test_hello.py。只设一个业务包 hello，不提取操作手册中的未来 --upper/HELLO-02；不扩展参数、错误、部署或环境兼容需求，不研究解释器内部行为。没有证据的重要设计选择不编造 DR；Git/许可种子按原工作流核对，保留根目录 MIT LICENSE，不从测试身份推断版权、不执行无关补头任务。Setup 分支 test/lite-specs-01，中文，Claude 与 Codex。正常完成独立审查、人工 Gate、lint 和交接，不改工作流或产品/测试，不推送不建 PR。报告保持简短，优先列提交与证据路径。
```

只有一个业务包，不意味着可以跳过工作流必需的种子核对。规格比一行程序长是可预期的；在实际 Gate 中由人类决定篇幅例外，本命令不代替批准。审查仅按已定契约判断完整性，范围外行为保持无约定。

## 2. 决定一个变更

```text
/decide 仅新增 HELLO-02：恰好传入 --upper 时 stdout 为 HELLO 加换行、stderr 空、退出码0；无参数的 HELLO-01 不变。其他参数组合不在范围内。按正常独立提案、合成及 review 更新 hello 规格和 docs/requirements.md，删除“当前没有 --upper/HELLO-02”的过时说明；不实现，不新增其他功能，不推送不建 PR。报告设计提交、复审版本和未解决问题，简短即可。
```

## 3. 实现

```text
/code 按已审定 HELLO-02 实现 --upper，保留 HELLO-01；用真实子进程各验证一次无参数 hello 和单独 --upper 的 HELLO，断言 stdout/stderr/退出码，保留原测试。其他参数组合不新增约定。完成正常独立 review 和必要修订，不扩展功能，不推送不建 PR。简报测试结果、实现提交、复审版本和未解决问题。
```

## 4. 验收

```text
/acceptance-orchestrate 读取 docs/requirements.md，仅针对 HELLO-02 生成并选中一个场景：实际执行 python3 hello.py --upper，预期 stdout 为 HELLO 加换行、stderr 空、退出码0。只执行这一个场景，不收集覆盖率，其他场景保留未执行。正常完成独立复审并导出报告和证据；允许隔离执行目录和用例，不改产品或原始需求，不推送不建 PR。直接完成流程，摘要简短，优先列报告和证据路径。
```

## 完成判据

四项各保留实际执行机器、包版本、提交/复审版本、结果和证据路径。人工 Gate 等待不算失败，lint 通过不代表产品验收通过；只有工作流走到最终报告才算完成。长结果被截断时，在原会话只读续查已有报告，不为显示结果重新执行。

轻量版尚需在 GoodMe 上实际验证；旧加法示例的审批和运行结果不能算作本版证据。
