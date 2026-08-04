# Creation Handoff — clean-architecture v1.1.1

> 交付简报：本技能如何从个人级技能（2026-03-10，16.5KB 单体 SKILL.md）重建为公开 governed 发布包。

## v1.1.1 更新（2026-08-05）

- **新增可视化报告**：`reports/assets/` 加入三张图片（SVG + PNG）——升级对比信息图、四层同心圆示意图、触发/输出评测可视化。
- **版本号**：manifest.json 与 SKILL.md metadata 由 `1.1.0` 升至 `1.1.1`（已发布版本不可变，以新小版本承载新增资产）。
- 行为、触发边界、评测与 references 内容不变；本轮仅新增图片报告资产 + 版本号变更。

## v1.1.0 更新（2026-08-05）

- **多语言 README**：根 `README.md` 改为英文主版本，新增 `docs/README.zh-CN.md` 中文版，两者通过语言切换徽章互链（参照 fastagent-meta-skill 的多语言模式）。
- **版本号**：manifest.json 与 SKILL.md metadata 由 `1.0.0` 升至 `1.1.0`（已发布版本不可变，故以新小版本承载 README 多语言改动）。
- 行为、触发边界、评测与 references 内容不变；本轮仅产品页多语言 + 版本号变更。

## Reference skills studied

| 来源 | 平台 | 学习要点 |
|---|---|---|
| [wondelai/skills](https://github.com/wondelai/skills) `clean-architecture`（4.5K 安装） | skills.sh | 评分驱动的诊断结构：先问清楚场景再给结论 |
| [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) `android-clean-architecture`（6.8K 安装） | skills.sh | 平台向技能如何做触发边界；Android 特化与本技能通用定位相反 |
| [giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit) `clean-architecture`（1.9K） | skills.sh | 候选参考 |
| [pproenca/dot-skills](https://github.com/pproenca/dot-skills) `clean-architecture`（1.8K） | skills.sh | 候选参考 |
| Robert C. Martin《架构整洁之道》 | 书籍 | 四层同心圆、依赖规则、SOLID、组件原则（references/ 原始来源） |

## Candidate-specific lessons

- **wondelai**：诊断优先于模板。本技能 Workflow 第 1 步固定为"先问输入规模/团队/并发/变更频率，不先给方案"。
- **affaan-m**：平台向技能（Android）拥有强触发边界但不可复用；验证了本技能"框架无关 + 用户栈映射"方向的正确性。
- **原始个人技能（v0）**：暴露了两个问题——description 太宽导致 trigger_eval 60%（6 漏触发 + 2 近邻误触发），以及强制术语协议降低采用意愿。两者均已修复。

## Keep / Adapt / Reject / Invent

- **keep**：references/ 三份内容；Musk 五步法；既有分层/依赖/DIP 场景转为 should-trigger。
- **adapt**：description 收窄 + 真实技术词；SKILL.md 16.5KB → 4.5KB 骨架；强制术语 → 建议语气；Express 硬编码 → 框架无关；eval 非标格式 → 标准 trigger_cases.json。
- **reject**：6 个系统设计面试 eval；MANDATORY/NON-NEGOTIABLE 措辞。
- **invent**：反过度设计决策流程；rubric 输出评测（`scripts/output_eval.py` + `evals/output-eval.json`）。

## Advantages and evidence labels

| 亮点 | 类型 | 证据 |
|---|---|---|
| 触发边界 20/20（0 误触发 / 0 漏触发） | **validated advantage** | `reports/trigger-eval.json`（行为规范级） |
| SKILL.md 4.5KB，符合 production context budget（≤14KB） | **validated advantage** | `scripts/validate_skill.py` + `reports/skill-ir.json` |
| 输出契约覆盖 5 行为、4 场景 13 维度全过 | **validated advantage** | `reports/output-eval.json`（behavior_specification） |
| 四层术语 + 用户栈映射 + 最小代码示例的固定回答结构 | **design advantage** | SKILL.md Workflow / Output Contract |
| 马斯克五步法集成进任何"上复杂方案"的建议 | **design advantage** | SKILL.md Workflow 第 4 步 |
| 该描述在真实 agent 上的触发率/回答质量 | **hypothesis** | 未跑 provider/human 实跑，标记 `missing evidence` |

## Missing evidence

- provider 实跑（真实 agent 对 20 用例的触发与回答质量）
- 人工盲评（独立评审人按 rubric 打分）
- 安装验证与发布证据（发布后由 `publish_skill.py` 补齐：npx 发现、隔离安装、Release）

以上均如实保留 `missing evidence` 标签，不伪装为已验证。
