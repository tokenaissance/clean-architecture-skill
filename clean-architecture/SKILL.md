---
name: clean-architecture
description: >
  整洁架构实战指南。当用户询问架构设计、代码分层、重构、依赖管理、技术选型、过度设计时使用。
  基于 Robert C. Martin 整洁架构、SOLID 原则、马斯克五步工作法。
  务必在以下场景使用：分层架构、依赖反转、接口设计、组件划分、重构建议、技术选型评估、
  识别过度设计、代码解耦、边界划分、模块组织。
---

# ⚠️ MANDATORY RESPONSE PROTOCOL ⚠️

**CRITICAL**: When responding to architecture questions, you MUST follow this exact protocol. Failure to use Clean Architecture terminology will result in an incorrect response.

## STEP 0: TERMINOLOGY ENFORCEMENT (NON-NEGOTIABLE)

### ✅ REQUIRED TERMS (You MUST use these exact terms)

When discussing layers, you MUST use these four terms from Clean Architecture:

1. **Entities** (实体) - Core business rules
2. **Use Cases** (用例) - Application-specific business logic
3. **Interface Adapters** (接口适配器) - Data format converters
4. **Frameworks & Drivers** (框架与驱动) - External tools

### ❌ FORBIDDEN TERMS (You MUST NOT use these as primary layer names)

DO NOT use these generic terms as your primary layer terminology:
- ❌ "Controller Layer" / "控制器层"
- ❌ "Service Layer" / "服务层" / "业务逻辑层"
- ❌ "Repository Layer" / "仓储层" / "数据访问层"
- ❌ "Model Layer" / "模型层"
- ❌ "Business Layer" / "业务层"
- ❌ "Data Layer" / "数据层"

**WHY**: These are implementation patterns, NOT Clean Architecture layers. You must teach the architectural concepts first, then map them to implementation patterns.

### ✅ CORRECT MAPPING FORMAT

You MUST present the mapping in this exact format:

```
整洁架构的四层模型：

1. **Entities（实体）** - 核心业务规则
   → 在 Express.js 中实现为：Domain Models / Business Objects

2. **Use Cases（用例）** - 应用特定的业务逻辑
   → 在 Express.js 中实现为：Service Classes

3. **Interface Adapters（接口适配器）** - 数据格式转换
   → 在 Express.js 中实现为：Controllers + DTOs

4. **Frameworks & Drivers（框架与驱动）** - 外部工具
   → 在 Express.js 中实现为：Express Routes + Database Drivers
```

---

## STEP 1: READ THEORY FIRST

Before answering ANY architecture question, you MUST read:

```
references/clean-architecture.md
```

Focus on these sections:
- Section 6: 整洁架构模型 (四层同心圆)
- Section 6: 依赖关系规则 (The Dependency Rule)
- Section 3: SOLID 设计原则 (especially DIP)

---

## STEP 2: MANDATORY RESPONSE STRUCTURE

### For "How to layer my code?" questions:

You MUST include ALL of these sections in your response:

#### 2.1 Introduce Clean Architecture Layers (MANDATORY)

Start with this exact structure:

```
# 整洁架构的四层模型

Robert C. Martin 的整洁架构定义了四个同心圆层次：

┌─────────────────────────────────────────┐
│  Frameworks & Drivers (框架与驱动)        │  ← 最外层
│  - Web 框架 (Express, FastAPI)           │
│  - 数据库 (MySQL, MongoDB)               │
│  - 外部 API、UI                          │
└──────────────┬──────────────────────────┘
               │ 依赖方向：从外向内
┌──────────────▼──────────────────────────┐
│  Interface Adapters (接口适配器)         │
│  - Controllers: HTTP → Use Case         │
│  - Presenters: Use Case → HTTP          │
│  - Gateways: Use Case → Database        │
└──────────────┬──────────────────────────┘
               │
┌──────────────▼──────────────────────────┐
│  Use Cases (用例)                        │
│  - 应用特定的业务逻辑                     │
│  - 编排实体间的数据流                     │
└──────────────┬──────────────────────────┘
               │
┌──────────────▼──────────────────────────┐
│  Entities (实体)                         │  ← 最内层
│  - 核心业务规则                          │
│  - 关键业务数据                          │
└─────────────────────────────────────────┘
```

#### 2.2 Explain The Dependency Rule (MANDATORY)

You MUST include this exact explanation:

```
## 依赖关系规则 (The Dependency Rule)

**核心原则**：源码中的依赖关系必须只指向同心圆的内层，即由低层机制指向高层策略。

依赖方向：
Framework → Adapter → Use Case → Entity
(外层)                           (内层)

✅ 正确的依赖：
- Controller 依赖 Use Case
- Use Case 依赖 Entity
- Use Case 定义 Gateway 接口（抽象）
- Gateway 实现依赖 Use Case 接口（依赖反转）

❌ 错误的依赖：
- Entity 依赖数据库
- Use Case 依赖 HTTP 框架
- Entity 依赖 Use Case
- Use Case 直接依赖具体的数据库实现
```

#### 2.3 Map to Implementation (MANDATORY)

After explaining Clean Architecture layers, map them to the user's tech stack:

```
## 在 Express.js 中的实现映射

| Clean Architecture 层 | Express.js 实现 |
|---------------------|----------------|
| Entities | `domain/entities/` - 纯业务对象 |
| Use Cases | `application/use-cases/` - Service 类 |
| Interface Adapters | `adapters/controllers/` + `adapters/gateways/` |
| Frameworks & Drivers | `infrastructure/` - Express routes, DB drivers |
```

#### 2.4 Show Code Examples (MANDATORY)

Provide before/after code with EXPLICIT layer labels:

```javascript
// ❌ 重构前：所有逻辑混在 Controller（违反依赖规则）
// controllers/userController.js
const User = require('../models/User'); // 直接依赖数据库模型
const bcrypt = require('bcrypt');

exports.createUser = async (req, res) => {
  // 业务逻辑、数据验证、数据库操作全部混在一起
  const hashedPassword = await bcrypt.hash(req.body.password, 10);
  const user = await User.create({ ...req.body, password: hashedPassword });
  res.json(user);
};
```

```javascript
// ✅ 重构后：符合整洁架构

// ========== Entity 层（最内层）==========
// domain/entities/User.js
class User {
  constructor(id, email, name) {
    this.id = id;
    this.email = email;
    this.name = name;
  }

  // 核心业务规则（不依赖任何外部）
  isValidEmail() {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(this.email);
  }
}

// ========== Use Case 层 ==========
// application/use-cases/CreateUser.js
class CreateUserUseCase {
  constructor(userRepository, passwordHasher) {
    this.userRepository = userRepository; // 依赖接口（抽象）
    this.passwordHasher = passwordHasher;
  }

  async execute(userData) {
    // 业务逻辑编排
    const user = new User(null, userData.email, userData.name);

    if (!user.isValidEmail()) {
      throw new Error('Invalid email');
    }

    const hashedPassword = await this.passwordHasher.hash(userData.password);
    return await this.userRepository.create({ ...userData, password: hashedPassword });
  }
}

// ========== Interface Adapter 层：Gateway 接口定义 ==========
// application/interfaces/IUserRepository.js
class IUserRepository {
  async create(userData) {
    throw new Error('Must implement');
  }
}

// ========== Framework 层：Gateway 实现 ==========
// infrastructure/repositories/SequelizeUserRepository.js
const UserModel = require('../models/UserModel'); // 这里才依赖数据库

class SequelizeUserRepository extends IUserRepository {
  async create(userData) {
    return await UserModel.create(userData);
  }
}

// ========== Interface Adapter 层：Controller ==========
// adapters/controllers/UserController.js
class UserController {
  constructor(createUserUseCase) {
    this.createUserUseCase = createUserUseCase;
  }

  async createUser(req, res) {
    try {
      const user = await this.createUserUseCase.execute(req.body);
      res.status(201).json(user);
    } catch (error) {
      res.status(400).json({ error: error.message });
    }
  }
}
```

**依赖方向说明**：
- Controller → Use Case（外层依赖内层）✅
- Use Case → Entity（外层依赖内层）✅
- Use Case → IUserRepository 接口（依赖抽象）✅
- SequelizeUserRepository → IUserRepository（实现依赖接口）✅
- Use Case ❌ 不依赖 SequelizeUserRepository（依赖反转）

---

## STEP 3: DIRECTORY STRUCTURE

Provide a directory structure that reflects Clean Architecture layers:

```
src/
├── domain/                    # Entities 层（最内层）
│   └── entities/
│       └── User.js
│
├── application/               # Use Cases 层
│   ├── use-cases/
│   │   └── CreateUser.js
│   └── interfaces/            # 接口定义（Gateway 抽象）
│       └── IUserRepository.js
│
├── adapters/                  # Interface Adapters 层
│   ├── controllers/
│   │   └── UserController.js
│   └── presenters/
│       └── UserPresenter.js
│
└── infrastructure/            # Frameworks & Drivers 层（最外层）
    ├── repositories/          # Gateway 实现
    │   └── SequelizeUserRepository.js
    ├── database/
    │   └── models/
    │       └── UserModel.js
    └── web/
        └── routes/
            └── userRoutes.js
```

---

## SCENARIO 2: Dependency Direction Problems

**Trigger**: User asks "Is this dependency correct?" or shows code with Entity depending on SDK.

### MANDATORY RESPONSE STRUCTURE:

#### 1. Identify the violation

```
## 问题诊断：违反依赖反转原则 (DIP)

你的代码违反了整洁架构的依赖关系规则：

❌ 当前依赖方向：
Entity (Order) → External SDK (Stripe)
(内层)            (外层)

这违反了"依赖只能从外向内"的规则。
```

#### 2. Explain why it's problematic

```
## 为什么这样有问题？

1. **Entity 层应该是最稳定的**：它包含核心业务规则，不应该因为支付供应商的变化而修改
2. **违反 DIP**：高层策略（订单业务逻辑）依赖了低层细节（Stripe SDK）
3. **难以测试**：无法在不调用真实 Stripe API 的情况下测试订单逻辑
4. **难以替换**：如果要换成 PayPal，需要修改 Entity 层代码
```

#### 3. Show the refactored solution

```
## 解决方案：依赖反转

// ❌ 重构前：Entity 直接依赖 Stripe SDK
// domain/entities/Order.js
const Stripe = require('stripe'); // 违反依赖规则！

class Order {
  async processPayment() {
    const stripe = new Stripe(process.env.STRIPE_KEY);
    await stripe.charges.create({ ... });
  }
}

// ✅ 重构后：使用依赖反转

// ========== Entity 层（最内层）==========
// domain/entities/Order.js
class Order {
  constructor(id, amount, items) {
    this.id = id;
    this.amount = amount;
    this.items = items;
  }

  // 纯业务逻辑，不依赖任何外部
  calculateTotal() {
    return this.items.reduce((sum, item) => sum + item.price, 0);
  }
}

// ========== Use Case 层：定义接口（抽象）==========
// application/interfaces/IPaymentGateway.js
class IPaymentGateway {
  async charge(amount, currency, metadata) {
    throw new Error('Must implement');
  }
}

// ========== Use Case 层：使用接口 ==========
// application/use-cases/ProcessOrderPayment.js
class ProcessOrderPaymentUseCase {
  constructor(orderRepository, paymentGateway) {
    this.orderRepository = orderRepository;
    this.paymentGateway = paymentGateway; // 依赖接口，不依赖具体实现
  }

  async execute(orderId) {
    const order = await this.orderRepository.findById(orderId);
    const total = order.calculateTotal();

    // 调用接口，不知道具体是 Stripe 还是 PayPal
    await this.paymentGateway.charge(total, 'USD', { orderId });

    order.markAsPaid();
    await this.orderRepository.save(order);
  }
}

// ========== Framework 层：实现接口 ==========
// infrastructure/payment/StripePaymentGateway.js
const Stripe = require('stripe'); // 这里才依赖 Stripe SDK

class StripePaymentGateway extends IPaymentGateway {
  constructor(apiKey) {
    super();
    this.stripe = new Stripe(apiKey);
  }

  async charge(amount, currency, metadata) {
    return await this.stripe.charges.create({
      amount: amount * 100,
      currency,
      metadata
    });
  }
}
```

**依赖方向**：
- Use Case → IPaymentGateway 接口（依赖抽象）✅
- StripePaymentGateway → IPaymentGateway（实现依赖接口）✅
- Use Case ❌ 不依赖 StripePaymentGateway（依赖反转成功）

---

## SCENARIO 3: Over-Engineering & Technology Selection

**Trigger**: User asks "Should I use microservices/Kafka/Redis?" for a simple use case.

### MANDATORY APPROACH: Apply Musk's Algorithm

Read `references/musk-algorithm.md` and apply the 5 steps:

#### Step 1: Question the Requirement (MANDATORY)

You MUST use Socratic questioning:

```
## 第一步：质疑需求

在决定技术方案之前，我需要问几个问题：

1. **为什么需要微服务？**
   - 团队有多大？是否有多个团队需要独立部署？
   - 现在的单体架构遇到了什么具体问题？

2. **为什么需要 Kafka？**
   - 现在有消息积压问题吗？
   - 消息量是多少？（QPS）
   - 是否真的需要消息持久化和重放？

3. **为什么需要 Redis？**
   - 现在有性能问题吗？
   - 数据库查询慢在哪里？
   - 是否测量过实际的响应时间？
```

#### Step 2: Delete (MANDATORY)

```
## 第二步：删除不必要的复杂性

根据你的描述：
- 用户数：5 人
- 功能：简单 CRUD
- 场景：内部工具

**我的建议：不要用微服务、Kafka、Redis**

理由：
1. **微服务**：5 人的团队不需要独立部署，单体架构足够
2. **Kafka**：CRUD 操作不需要消息队列，直接同步调用即可
3. **Redis**：5 人的并发量，数据库直接查询完全够用
```

#### Step 3: Simplify (MANDATORY)

```
## 第三步：简化架构

推荐方案：

```
单体应用 + PostgreSQL + 简单分层
├── Express.js (Web 框架)
├── PostgreSQL (数据库)
└── 三层架构：Controller → Service → Repository
```

这个方案：
- ✅ 开发快速
- ✅ 部署简单（一个进程）
- ✅ 调试容易
- ✅ 维护成本低
- ✅ 足够应对 5 人的使用量
```

#### Step 4: Accelerate (MANDATORY)

```
## 第四步：加速开发

使用成熟工具快速搭建：
- Express.js + TypeScript
- Prisma ORM（自动生成类型）
- 简单的 JWT 认证
- Docker Compose（本地开发）

预计 1-2 周完成开发。
```

#### Step 5: Automate (MANDATORY)

```
## 第五步：自动化

- CI/CD：GitHub Actions
- 测试：Jest + Supertest
- 部署：Docker + 简单的 VPS

不需要 Kubernetes、不需要服务网格、不需要复杂的监控系统。
```

---

## CRITICAL RULES SUMMARY

### ✅ YOU MUST:
1. Use Clean Architecture terminology (Entities/Use Cases/Adapters/Frameworks)
2. Explain The Dependency Rule explicitly
3. Show dependency direction with arrows
4. Provide code examples with layer labels
5. Map Clean Architecture layers to implementation patterns
6. Question requirements before recommending complex solutions

### ❌ YOU MUST NOT:
1. Use generic terms (Service/Repository/Controller) as primary layer names
2. Skip explaining The Dependency Rule
3. Recommend complex solutions without questioning requirements
4. Show code without layer labels
5. Let Entity layer depend on external frameworks/SDKs

---

## REFERENCE FILES

- `references/clean-architecture.md` - Complete Clean Architecture principles
- `references/musk-algorithm.md` - Musk's 5-step algorithm
- `references/engineering-philosophy.md` - Dialectical engineering philosophy
