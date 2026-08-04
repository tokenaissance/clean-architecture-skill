# Prior-Art Research — clean-architecture

- **Researched at**: 2026-08-05
- **Runner**: `scripts/research_prior_art.py`（skills.sh + SkillsMP 双目录，GitHub 源核验）
- **Queries**:
  1. `clean architecture`
  2. `clean-arch skill`
  3. `SOLID layered architecture agent skill`
- **Candidate families**: 30（skills.sh 12 个可命名 clean-architecture 相关技能 + SkillsMP 源仓库去重）

## Metric semantics

- **skills.sh installs** = 生态安装遥测，**不是**评分或正确性。
- **SkillsMP repo stars** = 源 GitHub 仓库星数，**不是**安装量、评分或技能级质量。
- **跨目录分数不计算**：两个目录的指标语义不同，不可互相比较，也不可加总成"最佳技能分"。

## Landscape (by skills.sh installs)

| 技能 | 仓库 | 安装量 | 备注 |
|---|---|---|---|
| android-clean-architecture | affaan-m/everything-claude-code | 6.8K | Android 平台向，非通用 |
| clean-architecture | wondelai/skills | 4.5K | 评分驱动的诊断结构，最接近本技能定位 |
| clean-architecture | giuseppe-trisciuoglio/developer-kit | 1.9K | 候选参考 |
| clean-architecture | pproenca/dot-skills | 1.8K | 候选参考 |
| clean-architecture | mindrally/skills | 800 | 候选参考 |
| android-architecture-clean | krutikjain/android-agent-skills | 265 | Android 平台向 |
| code-structure | michaelshimeles/skills | 88 | 相邻领域 |
| layered-architecture | rrezartprebreza/spring-boot-skills | 57 | Spring 平台向 |
| rails-architecture | thibautbaissac/rails_ai_agents | 55 | Rails 平台向 |
| solid-java / solid-go | fusengine/agents | 37 / 33 | SOLID 平台向 |

SkillsMP 侧：`openclaw/openclaw:openclaw-secret-scanning-maintainer`（~384K 星）与 `affaan-m/ecc:*`（~233K 星）为大型源仓库家族，其 installs 指标缺失，仅 repo stars 语义，**不参与安装量排名**。

## Keep / Adapt / Reject / Invent

### keep（保留真资产）
- 本技能 `references/clean-architecture.md`（Uncle Bob 理论全集）、`references/musk-algorithm.md`（五步法）、`references/engineering-philosophy.md`（辩证平衡）——原始内容。

### adapt（改编）
- **description 收窄**：原描述"架构设计/代码分层/依赖管理/技术选型/过度设计"过宽，导致 trigger_eval 仅 60% 通过（6 漏触发 + 2 近邻误触发）。改为列真实技术词（微服务/Kafka/Redis/缓存/MongoDB→PostgreSQL/REST→GraphQL/Stripe/PayPal）+ 明确 exclusions，调优到 20/20。
- **MANDATORY/NON-NEGOTIABLE 强制术语协议 → 建议语气**：原 SKILL.md 以"必须使用四层术语、禁止 Service/Repository/Controller"的强制口吻编写，改为"默认优先四层术语，尊重用户既有约定"。
- **技术栈硬编码 → 框架无关**：原技能把 Express/Sequelize/Stripe 写死进回答模板，改为四层术语 + 用户栈映射（Express/Next.js/Go/Spring 示例）。
- **eval 非标格式 → 标准 trigger_cases.json**：原 `evals/evals.json` + `evals/system-design-evals.json`（非标准格式）改为标准 `evals/trigger_cases.json`（should/should-not/near-neighbor）。

### reject（拒绝）
- **6 个系统设计面试 eval**（Twitter 千万用户、bit.ly、sharding、Saga、多租户、微信聊天）：稀释技能定位，直接回答不触发。
- **强制协议措辞**："MANDATORY/NON-NEGOTIABLE/MUST NOT use Service/Repository/Controller" 一律降级为建议语气。

### invent（原创）
- **可执行的「反过度设计决策」流程**：输入规模/团队/并发 → 该不该上微服务/Kafka/缓存，集成马斯克五步法为固定检查步骤。
- **rubric 输出评测**：`evals/output-eval.json` + `scripts/output_eval.py`（4 场景 13 维度，行为规范级证据）。

## Missing evidence

- 各候选仓库的完整 SKILL.md 源码审查、license、维护活跃度、真实用户反馈尚未逐一展开（`requires_source_review=true`），仅基于目录元数据完成家族级判断。
- provider 实跑与人工评审证据：**missing evidence**，不在公共声明中伪装。

## Next steps

- 对 wondelai/skills:clean-architecture 与 affaan-m/everything-claude-code 做源码级 diff，提取可复用机制。
- 收集真实用户对 v1.0.0 的输出反馈，作为后续版本 output-eval 的 provider 证据来源。
