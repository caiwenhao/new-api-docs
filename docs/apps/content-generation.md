# 📝 内容生成器示例

通过 Kapon AI 搭建一个可控的内容生成器（文章、摘要、标题等）。

## 示例：文章大纲生成（Python）
```python
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY", base_url="https://models.kapon.cloud/v1")

prompt = "为《AI 在教育中的应用》生成 5 条有层次的大纲"
resp = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.6
)
print(resp.choices[0].message.content)
```

## 实践建议
- 模板化提示词，减少风格漂移。
- 控制长度（`max_tokens`）、设置温度与惩罚项。
- 增加质量检查与重试机制。

## 🔗 相关文档
- 提示词工程: prompt-engineering.md
- 错误处理: error-handling.md
- 性能优化: performance-optimization.md
