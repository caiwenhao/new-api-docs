# 🤖 聊天机器人示例

本文展示如何使用 Kapon AI 快速搭建一个基础聊天机器人，并给出可扩展的工程化思路。

## 🚀 快速上手（Python）
```python
import openai

client = openai.OpenAI(api_key="YOUR_API_KEY", base_url="https://models.kapon.cloud/v1")

def chat(msg: str):
    resp = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": msg}],
        temperature=0.7,
    )
    return resp.choices[0].message.content

print(chat("你好！"))
```

## 🧩 能力扩展
- 上下文记忆：保存会话历史或做摘要，以降低 token 成本。
- 工具调用：为机器人绑定函数（天气、搜索、数据库等）。
- 安全防护：在返回前做脱敏/过滤、阈值判断。

## 🔗 相关文档
- 对话 API: ../api/openai-chat.md
- 错误处理: error-handling.md
- 性能优化: performance-optimization.md
