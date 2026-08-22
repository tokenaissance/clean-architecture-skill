# clean-architecture 中文介绍

> 分层、依赖方向与反过度设计的实用指南：用四层模型回答架构设计、代码重构、技术选型与过度设计问题。

[![English](https://img.shields.io/badge/Docs-English-black)](../README.md)
[![中文](https://img.shields.io/badge/Docs-%E4%B8%AD%E6%96%87-red)](README.zh-CN.md)
[![GitHub Release](https://img.shields.io/github/v/release/tokenaissance/clean-architecture?display_name=tag&sort=semver)](https://github.com/tokenaissance/clean-architecture/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-black.svg)](../LICENSE)

`clean-architecture` 不是一个「生成目录脚手架」的技能，而是一套**决策方法**：先诊断，再分层，最后用马斯克五步法拦住过度设计。

当一个项目里业务逻辑堆在 controller 里、实体直接依赖外部 SDK、或者团队在纠结要不要上微服务时，这个技能会给你：四层术语的清晰解释、依赖规则的判定、映射到你真实技术栈（Express/Next.js/Go/Spring）的落地路径，以及一段带层标签的最小代码示例。

```text
Use the clean-architecture skill to review this layered-code proposal,
explain the dependency direction, and tell me whether microservices are over-engineering.
```

它处理：**分层重构 → 依赖反转（DIP）→ 数据访问层（repository）→ 技术选型与迁移 → 反过度设计检查**。

**v1.2.0** 新增 GEB 分形文档纪律、reference 文件 L3 头部自举、框架无关的违规检测模式。发布证据见 [Releases](https://github.com/tokenaissance/clean-architecture/releases)。

## 为什么值得用

- **触发边界精确**：description 收窄并写入真实技术词（微服务/Kafka/Redis/缓存/MongoDB→PostgreSQL/REST→GraphQL/Stripe/PayPal），trigger eval 20/20 通过，误触发与漏触发均为 0。
- **技术栈无关**：不再写死 Express/Sequelize/Stripe，而是把四层术语映射到用户的实际框架。
- **自带反过度设计闸门**：任何「上复杂方案」的建议都会先跑马斯克五步法（质疑→删除→简化→加速→自动化）。
- **架构决策可留存**（v1.2.0）：GEB 分形文档纪律。重大架构决策附带 L2/L3 文档骨架。L3 `[INPUT]` 字段比测试更早暴露依赖方向违规——Use Case 的 INPUT 里出现 HTTP 请求对象，不看 import，头部第一行就暴露了。
- **框架无关的违规检测**（v1.2.0）：违规表检测的是模式（"ORM 驱动在 Entity 里"），不是具体框架。Node、Go、Spring 任意技术栈通用。
- **自举**（v1.2.0）：4 个 reference 文件全部携带 L3 `[INPUT]/[OUTPUT]/[POS]` 头部。讲文档纪律的 skill 自己先遵守纪律。
- **轻量输出**：context budget 为 production 级（SKILL.md ~5KB，远低于 14KB 上限），只给判断与最小示例，不给大段模板。输出边界已量化：目录建议 ≤5 个目录且不含具体文件名。

## 你可以直接这样说

- "业务逻辑都写在 controller 里，数据库查询也直接调用，怎么分层重构？"
- "Order 实体直接 import 了 Stripe SDK 处理支付，这样设计有什么问题？"
- "5 个人用的内部 CRUD 工具，同事建议微服务 + Kafka + Redis，有必要吗？"
- "要从 REST 迁移到 GraphQL，数据访问代码真的要全部重写吗？"
- "接入 Stripe/PayPal 等多个第三方，怎么设计适配层方便切换？"

## 什么时候不该用

- 画架构图、翻译、格式化、写标题、总结文档
- 依赖注入不生效、接口 500、SQL 慢查询这类调试
- React 组件拆分、单个 DTO 加不加这类微观决策
- 系统设计面试题（Twitter 千万用户、bit.ly、Saga 等）

## Installation

```bash
npx skills add tokenaissance/clean-architecture
```

Install only this skill:

```bash
npx skills add tokenaissance/clean-architecture --skill clean-architecture
```

Verify:

```bash
test -f ~/.agents/skills/clean-architecture/SKILL.md
python3 ~/.agents/skills/clean-architecture/scripts/validate_skill.py \
  ~/.agents/skills/clean-architecture
```

## Prerequisites

- [ ] Node.js 18+：`node --version`
- [ ] npx 可用：`npx --version`
- [ ] Python 3.11+（PyYAML）：`python3 --version && python3 -c "import yaml"`
- [ ] GitHub CLI 已认证（如需发布）：`gh auth status`

## Output

安装后得到完整 Skill 包：

```text
clean-architecture/
├── SKILL.md                    # 路由 + 触发边界 + 工作流 + Reference Map
├── README.md                   # 产品页（英文，本文件为中文版）
├── LICENSE                     # MIT
├── manifest.json               # 版本、作者、平台与发布门禁
├── agents/interface.yaml       # 跨 Agent 接口
├── references/                 # clean-architecture / musk-algorithm / engineering-philosophy / geb-fractal-docs
├── scripts/output_eval.py      # rubric 输出评测
├── evals/                      # trigger_cases.json + output-eval.json
└── reports/                    # Skill IR、trigger-eval、output-eval、prior-art、handoff、upgrade-summary
```

## Local quality checks

```bash
python3 scripts/validate_skill.py .
python3 scripts/export_skill_ir.py . --output reports/skill-ir.json
python3 scripts/trigger_eval.py . --cases evals/trigger_cases.json --output reports/trigger-eval.json
python3 scripts/output_eval.py . --output reports/output-eval.json
python3 -m unittest discover -s tests -p 'test_*.py'
```

> 注意：`validate_skill.py` 需要 PyYAML。本仓库脚本在 `conda run -n google python` 下验证通过（Python 3.13 + PyYAML）。

## Troubleshooting

| 问题 | 常见原因 | 解决 |
|---|---|---|
| Skill 从未触发 | description 缺少真实技术词 | 把用户真实问法加入 description 并重跑 `trigger_eval.py` |
| Skill 到处误触发 | description 太宽或缺少 near-neighbor 用例 | 收敛描述，检查 `evals/trigger_cases.json` 的 should-not/near-neighbor |
| 输出变成模板长篇 | 把本技能当目录生成器 | 本技能只输出诊断 + 映射 + 最小示例，完整脚手架需用户明确要求 |
| 验证脚本失败 | 证据文件缺失或 Python 版本不含 PyYAML | 按报错补齐 `reports/` 证据，用 3.11+ 解释器重跑 |
| 用户装不上 | 只做了本地验证没有公开发布 | 走完整 publisher（feature branch → PR → Release → 干净安装） |

## Credits and sources

- [`wondelai/skills`](https://github.com/wondelai/skills)：clean-architecture 的评分驱动诊断结构启发。
- [`affaan-m/everything-claude-code`](https://github.com/affaan-m/everything-claude-code)：android-clean-architecture（skills.sh 6.8K 安装）的候选参考。
- [`giuseppe-trisciuoglio/developer-kit`](https://github.com/giuseppe-trisciuoglio/developer-kit)：clean-architecture 候选参考。
- [`pproenca/dot-skills`](https://github.com/pproenca/dot-skills)：clean-architecture 候选参考。
- **Robert C. Martin（Uncle Bob）《架构整洁之道》**：四层同心圆、依赖规则与 SOLID 的原始来源；本技能 references/ 基于其方法重写。
- **GEB 分形文档协议** by @chunxiang：代码-文档同构与三层分形结构（L1/L2/L3），为本技能 v1.2.0 的文档纪律提供理论基础。

Upstream ideas are adopted semantically with attribution, not mirrored wholesale; search popularity is never passed off as quality. 详见 `reports/prior-art-research.md`。

Upstream inspiration: wondelai/skills:clean-architecture; affaan-m/everything-claude-code; giuseppe-trisciuoglio/developer-kit; pproenca/dot-skills

## Security and evidence boundary

- 本技能不执行网络操作；references/ 与 scripts/ 均为本地只读资产。
- 发布前检查公开文件不含密钥、Cookie、私有路径或未验证的结果声明。
- 触发/输出评测是行为规范证据（behavior_specification），provider 实跑与人工评审证据如实标注 `missing evidence`，不伪装。

## License

MIT (see LICENSE for copyright holders).
