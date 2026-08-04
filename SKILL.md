---
name: clean-architecture
description: |
  整洁架构（Clean Architecture）实战指南。当用户询问四层架构、依赖方向与依赖反转、实体直接依赖外部 SDK、数据访问层（repository）设计、微服务拆分、技术选型评估、或过度设计问题时使用。处理 Express/Next.js/Go/Spring 项目中的业务逻辑组织、MongoDB→PostgreSQL 迁移、REST→GraphQL 迁移、接入第三方 Stripe/PayPal、Redis 缓存与 Kafka 消息队列选型。基于 Robert C. Martin 整洁架构、SOLID 原则与依赖规则评估架构，用马斯克五步法防止过度设计。不要触发：纯代码质量、DDD、系统设计面试、单个 DTO 微观决策、缓存库选择、依赖注入框架调试、画架构图、翻译或格式化请求——直接回答而不调用本技能。
metadata:
  author: Tokenaissance
  version: "1.1.1"
  upstream_inspiration: wondelai/skills:clean-architecture; affaan-m/everything-claude-code; giuseppe-trisciuoglio/developer-kit; pproenca/dot-skills
---

# Clean Architecture 整洁架构实战

分层、依赖方向与反过度设计的实用指南，基于 Robert C. Martin 整洁架构、SOLID 与马斯克五步法。

## Router Rules

- 先用 frontmatter `description` 路由：命中四层架构、依赖反转、数据访问层、微服务/技术选型、过度设计等真实场景才进入本技能。
- 命中后按下方工作流回答；本技能是架构指南，不是通用代码评审或调试入口。
- 对「纯代码质量、DDD、系统设计面试、单个 DTO 微观决策、缓存库选择、框架机制调试、画架构图、翻译/格式化」直接回答，不调用本技能。
- 尊重用户技术栈：用四层术语讲解，再映射到用户的真实框架（Express/Next.js/Go/Spring），不写死单一框架。
- 术语以「建议语气」给出：默认优先使用 Entities / Use Cases / Interface Adapters / Frameworks 四层术语；Service/Repository/Controller 仅作为实现模式映射，不作主层名；允许用户已有约定时沿用。
- 只读审计请求不修改任何文件。

## Use when

- 业务逻辑堆在 controller/路由里，问怎么分层重构
- 实体/用例直接依赖外部 SDK（Stripe/PayPal）或数据库驱动，问依赖方向对不对
- 问要不要上微服务 / Kafka / Redis / 缓存，或做技术选型评估
- REST→GraphQL、MongoDB→PostgreSQL 这类迁移对数据访问代码的影响
- 接入多个第三方服务，怎么设计适配层便于切换

## Do NOT use when

- 画架构图、翻译、格式化、写标题、总结文档
- 依赖注入不生效、接口 500、SQL 慢查询 这类调试
- React 组件拆分、单个 DTO 加不加 这类微观决策
- 系统设计面试题（Twitter 千万用户、bit.ly、Saga、多租户等）——直接回答不调用
- 用户明确说「不要讲架构」或「只解释」

## Workflow

1. **诊断（先问，不先给方案）**：确认输入规模、团队大小、并发与变更频率。变更原因相同、一起变的代码才需要边界；未证实的变化轴上保持简单。
2. **读理论（按需）**：`references/clean-architecture.md`（四层同心圆、依赖规则、SOLID、组件原则）、`references/musk-algorithm.md`（五步法）、`references/engineering-philosophy.md`（辩证平衡）。
3. **结构化回答**（命中架构场景时给出）：
   - 四层术语：Entities（实体）/ Use Cases（用例）/ Interface Adapters（接口适配器）/ Frameworks（框架与驱动）
   - 依赖规则：源码依赖只指向内层，画依赖方向箭头
   - 用户栈映射：把四层映射到用户实际框架与目录结构
   - 代码示例：带层标签的最小前后对比，不超过 50 行
4. **反过度设计检查**：任何「上复杂方案」的建议先跑马斯克五步——质疑需求 → 删除 → 简化 → 加速 → 自动化，顺序不可颠倒；能用单体就不要先拆微服务。

## Output Contract

- 命中场景：诊断结论 + 四层映射 + 依赖规则说明 + 用户栈映射 + 最小代码示例 + 过度设计检查结论
- 未命中场景：直接回答，不套用本技能模板
- 不输出完整目录脚手架，除非用户明确要求；默认给出贴合的目录建议

## Reference Map

- 理论与原则：`references/clean-architecture.md`
- 反过度设计：`references/musk-algorithm.md`
- 工程哲学：`references/engineering-philosophy.md`
