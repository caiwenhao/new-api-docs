# 🏠 帮助中心

欢迎来到 Kapon AI 帮助中心！我们致力于为您提供最优质的技术支持和服务。

## 🚀 快速导航

### 📖 文档资源
- [API 文档](../api/index.md) - 完整的 API 接口文档
- [应用指南](../apps/index.md) - 开发最佳实践和示例
- [控制台](https://models.kapon.cloud/) - 管理您的 API 密钥和使用情况

### 🛠️ 开发工具
- [Python SDK](../apps/python-sdk.md) - Python 开发工具包
- [JavaScript SDK](../apps/javascript-sdk.md) - JavaScript 开发工具包
- [API 测试工具](../apps/api-testing.md) - 在线测试工具

## 📞 联系我们

### 技术支持
我们的技术支持团队随时为您提供帮助：

- **📧 邮箱支持**：[support@kapon.cloud](mailto:support@kapon.cloud)
- **⏰ 响应时间**：工作日 24 小时内回复
- **🌐 在线客服**：[https://models.kapon.cloud/support](https://models.kapon.cloud/support)

### 商务合作
如需商务合作或企业级服务，请联系：

- **📧 商务邮箱**：[business@kapon.cloud](mailto:business@kapon.cloud)
- **📱 商务热线**：400-123-4567
- **💼 企业服务**：提供定制化解决方案

## ❓ 常见问题

### API 使用相关

**Q: 如何获取 API 密钥？**
A: 访问 [Kapon AI 控制台](https://models.kapon.cloud)，注册账户后在控制台中创建 API 密钥。

**Q: API 有使用限制吗？**
A: 不同套餐有不同的使用限制，详情请查看 [定价方案](pricing.md)。

**Q: 支持哪些编程语言？**
A: 我们提供 Python、JavaScript 等主流语言的 SDK，也支持任何能发送 HTTP 请求的语言。

### 计费相关

**Q: 如何计费？**
A: 按实际使用的 tokens 数量计费，不同模型价格不同。详情请查看定价页面。

**Q: 支持哪些支付方式？**
A: 支持支付宝、微信支付、银行卡等多种支付方式。

**Q: 可以申请发票吗？**
A: 可以，企业用户可在控制台申请增值税发票。

### 技术问题

**Q: API 响应慢怎么办？**
A: 请检查网络连接，或尝试使用不同的模型。如问题持续，请联系技术支持。

**Q: 如何处理 API 错误？**
A: 请参考 [错误处理指南](../apps/error-handling.md) 了解常见错误的解决方法。

**Q: 支持流式响应吗？**
A: 是的，我们支持流式响应，可以实时获取模型输出。

---

**感谢您选择 Kapon AI！** 我们将持续为您提供优质的 AI API 服务。如有任何问题，请随时联系我们的支持团队。
    border: none;
    border-bottom: 2px solid var(--md-primary-bg-color);
    opacity: 0.2;
  }

  .md-typeset .grid.cards > ul > li > p {
    margin: 0.5rem 0;
  }

  .md-typeset .grid.cards > ul > li > p > em {
    color: var(--md-primary-bg-color);
    opacity: 0.8;
    font-style: normal;
  }

  .md-typeset .grid.cards > ul > li > p > .twemoji {
    font-size: 2.5rem;
    display: block;
    margin: 0.5rem auto;
  }

  .md-typeset .grid.cards > ul > li a {
    display: inline-flex;
    align-items: center;
    margin-top: 1.2em;
    padding: 0.5em 1.2em;
    color: white;
    background-color: rgba(255, 255, 255, 0.15);
    border-radius: 2em;
    transition: all 0.3s ease;
    font-weight: 500;
    font-size: 0.9em;
    letter-spacing: 0.03em;
    box-shadow: 0 3px 6px rgba(0, 0, 0, 0.1);
    position: relative;
    overflow: hidden;
    text-decoration: none;
  }

  .md-typeset .grid.cards > ul > li a:hover {
    background-color: rgba(255, 255, 255, 0.25);
    text-decoration: none;
    box-shadow: 0 5px 12px rgba(0, 0, 0, 0.2);
    transform: translateX(5px);
  }

  .md-typeset .grid.cards > ul > li a:after {
    content: "→";
    opacity: 0;
    margin-left: -15px;
    transition: all 0.2s ease;
  }

  .md-typeset .grid.cards > ul > li a:hover:after {
    opacity: 1;
    margin-left: 5px;
  }
</style>

# 帮助支持

## 💫 支持服务

<div class="grid cards" markdown>

-   :material-chat-question:{ .twemoji }

    **常见问题**

    ---

    查看常见问题解答，快速解决您的疑惑：
    
    [问题解答 →](faq.md)

-   :material-account-group:{ .twemoji }

    **社区交流**

    ---

    加入我们的社区，与其他用户交流：
    
    [QQ交流群 →](community-interaction.md)

-   :material-bug:{ .twemoji }

    **问题反馈**

    ---

    遇到问题？向我们反馈：
    
    [提交问题 →](feedback-issues.md)

-   :material-coffee:{ .twemoji }

    **支持我们**

    ---

    如果您觉得项目对您有帮助：
    
    [请我们喝咖啡 →](buy-us-a-coffee.md)

</div>

## 📖 支持说明

!!! tip "获取帮助"
    我们提供多种方式帮助您解决问题：

    1. **查看文档**：大多数问题都可以在文档中找到答案
    2. **常见问题**：浏览常见问题解答，快速找到解决方案
    3. **社区交流**：加入QQ群，与其他用户交流经验
    4. **问题反馈**：在GitHub上提交issue，我们会及时处理

!!! info "关于赞助"
    New API 是一个完全免费的开源项目，我们不强制要求任何形式的赞助。
    但如果您觉得项目对您有帮助，欢迎给我们买杯咖啡，这将帮助我们：

    - 维护和升级服务器
    - 开发新功能
    - 提供更好的文档
    - 建设更好的社区

!!! warning "注意事项"
    在寻求帮助时，请注意：

    - 提问前请先查看文档和常见问题
    - 提供足够的信息以便我们理解和复现问题
    - 遵守社区规则，保持友善的交流氛围
    - 耐心等待回复，我们会尽快处理您的问题 