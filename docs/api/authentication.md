# 🔑 API 认证方式

## 📝 概述

Kapon AI 使用 API 密钥进行身份验证。所有 API 请求都必须在请求头中包含有效的 API 密钥。

## 🔐 获取 API 密钥

1. 访问 [Kapon AI 控制台](https://models.kapon.cloud)
2. 注册账户或登录现有账户
3. 在控制台中创建新的 API 密钥
4. 妥善保存您的 API 密钥

!!! warning "安全提醒"
    - 请勿在客户端代码中暴露 API 密钥
    - 定期轮换您的 API 密钥
    - 如发现密钥泄露，请立即撤销并重新生成

## 🚀 使用方法

### HTTP 请求头认证

在所有 API 请求中添加以下请求头：

```http
Authorization: Bearer YOUR_API_KEY
```

### 示例

=== "Python"

    ```python
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_API_KEY",
        base_url="https://models.kapon.cloud/v1"
    )

    resp = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": "Hello!"}],
        temperature=0.7,
    )
    print(resp.choices[0].message.content)
    ```

=== "JavaScript"

    ```js
    import OpenAI from "openai";

    const client = new OpenAI({
      apiKey: process.env.KAPON_API_KEY,
      baseURL: "https://models.kapon.cloud/v1"
    });

    const resp = await client.chat.completions.create({
      model: "gpt-4",
      messages: [{ role: "user", content: "Hello!" }],
      temperature: 0.7
    });
    console.log(resp.choices[0].message.content);
    ```

=== "cURL"

    ```bash
    curl https://models.kapon.cloud/v1/chat/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $KAPON_API_KEY" \
      -d '{
        "model": "gpt-4",
        "messages": [{"role": "user", "content": "Hello!"}],
        "temperature": 0.7
      }'
    ```

### 环境变量设置

建议将 API 密钥设置为环境变量：

```bash
# Linux/macOS
export KAPON_API_KEY="your-api-key-here"

# Windows
set KAPON_API_KEY=your-api-key-here
```

## 🔒 安全最佳实践

### 1. 密钥管理
- 使用环境变量存储 API 密钥
- 不要将密钥硬编码在源代码中
- 使用密钥管理服务（如 AWS Secrets Manager）

### 2. 访问控制
- 为不同应用创建独立的 API 密钥
- 定期审查和轮换密钥
- 监控 API 使用情况

### 3. 网络安全
- 始终使用 HTTPS 进行 API 调用
- 在生产环境中限制 IP 访问
- 实施适当的速率限制

## ❌ 错误处理

### 认证失败响应

```json
{
  "error": {
    "message": "Invalid API key provided",
    "type": "invalid_request_error",
    "code": "invalid_api_key"
  }
}
```

### 常见错误码

| 错误码 | 描述 | 解决方案 |
|--------|------|----------|
| `invalid_api_key` | API 密钥无效 | 检查密钥是否正确 |
| `missing_api_key` | 缺少 API 密钥 | 添加 Authorization 头 |
| `api_key_expired` | API 密钥已过期 | 重新生成密钥 |
| `rate_limit_exceeded` | 超出速率限制 | 降低请求频率 |

## 📞 技术支持

如果您在 API 认证方面遇到问题，请联系我们的技术支持团队：

- 📧 邮箱：support@kapon.cloud
- 🌐 帮助中心：[https://models.kapon.cloud/support](https://models.kapon.cloud/support)
