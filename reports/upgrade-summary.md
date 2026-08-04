# Upgrade Summary — clean-architecture v0 → v1.0.0

> 面向发布的 before/after 差异报告。旧技能：个人级 `~/.agents/skills/clean-architecture/`（2026-03-10，16.5KB 单体 SKILL.md）。新技能：公开包 `tokenaissance/clean-architecture-skill` v1.0.0（governed 发布）。

## v1.1.0 补充（2026-08-05）

- **多语言 README**：根 `README.md` 改为英文主版本，新增 `docs/README.zh-CN.md` 中文版，语言切换徽章互链。行为、触发边界、评测与 references 不变。
- 版本由 `1.0.0` 升至 `1.1.0`（已发布版本不可变，以新小版本承载本轮改动）。发布引用文案中的版本号以最新 Release 为准。

## v1.1.1 补充（2026-08-05）

- **新增可视化报告**：`reports/assets/` 加入升级对比信息图、四层同心圆示意图、触发/输出评测可视化（SVG + PNG）。行为与评测内容不变。
- 版本由 `1.1.0` 升至 `1.1.1`。

## 差异总表

| 维度 | v0（旧） | v1.0.0（新） | 改进 |
|---|---|---|---|
| **触发精度** | trigger_eval 60%（20 例中 8 失败：6 漏触发 + 2 近邻误触发） | trigger_eval **20/20**（0 误触发 / 0 漏触发） | description 收窄 + 真实技术词 + 明确 exclusions |
| **上下文预算** | 16.5KB 单体 SKILL.md（远超 production 预算） | 4.5KB 骨架 SKILL.md（≤14KB 预算内） | 路由/边界/工作流骨架化，判断下沉到 references/ |
| **结构** | 无 manifest/README/interface/trigger_cases；2 个非标 eval 文件 | 标准 governed 包：manifest.json + agents/interface.yaml + README + evals/trigger_cases.json + reports/ | 完整可验证、可发布 |
| **技术栈** | 写死 Express/Sequelize/Stripe 进回答模板 | 框架无关：四层术语 + 用户栈映射（Express/Next.js/Go/Spring 示例） | 跨框架可复用 |
| **术语协议** | MANDATORY/NON-NEGOTIABLE 强制四层术语，禁 Service/Repository/Controller | 建议语气：默认四层术语，尊重用户既有约定 | 降低采用阻力 |
| **反过度设计** | 无独立流程 | 马斯克五步法集成进任何"上复杂方案"的建议（Workflow 第 4 步） | 新增可执行决策闸门 |
| **评测** | 6 个系统设计面试 eval 稀释定位；无输出评测 | 标准 trigger_cases.json（20 例）+ rubric 输出评测（4 场景 13 维度） | 定位清晰，输出有行为规范约束 |
| **打包** | 个人目录，无版本/授权 | manifest v1.0.0、MIT LICENSE、README 产品页、Skill IR | 团队可复用、可安装 |
| **发布** | 未发布 | 公开仓库 + feature branch → PR → merge → v1.0.0 Release → `npx skills add` 发现 + 隔离安装 | 完整 governed 发布 |

## 数据证据

- 触发边界：`reports/trigger-eval.json` — `ok: true`，`summary.passed == total == 20`，`pass_rate 1.0`。
- 输出契约：`reports/output-eval.json` — `evidence_kind: behavior_specification`，4 场景 13/13 维度通过。
- 结构校验：`scripts/validate_skill.py` — 0 failures；SKILL.md 4.5KB ≤ 14KB；`reports/skill-ir.json` 与 manifest 的 name/version 一致。
- 单元测试：5/5 通过（`tests/test_output_eval.py`）。

## 保留 / 删除 / 新增

- **保留**：references/ 三份真资产（clean-architecture / musk-algorithm / engineering-philosophy）；Musk 五步法；分层/依赖/DIP 场景。
- **删除**：6 个系统设计面试 eval；强制术语协议；Express/Sequelize/Stripe 硬编码模板；非标 eval 格式。
- **新增**：标准 trigger_cases.json；rubric 输出评测；反过度设计决策流程；governed 包结构（manifest/interface/README/reports）；公开发布流水线。

## 发布引用建议

> clean-architecture v1.0.0：从个人笔记级技能升级为公开 governed 包。触发边界 20/20，SKILL.md 从 16.5KB 精简到 4.5KB，写死 Express 改为框架无关 + 用户栈映射，强制术语改为建议语气，新增马斯克五步法反过度设计闸门与 rubric 输出评测。安装：`npx skills add tokenaissance/clean-architecture-skill`。
