# 🌐 智能翻译示例

使用 Kapon AI 构建一个简洁高效的多语言翻译工具。

## 快速上手（Python）
```python
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY", base_url="https://models.kapon.cloud/v1")

def translate(text: str, target_lang: str = "en"):
    prompt = f"将以下文本翻译为{target_lang}：\n" + text
    resp = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return resp.choices[0].message.content

print(translate("你好，世界！", "en"))
```

## 进阶实践
- 领域术语表：对特定词汇做替换/锁定，提升一致性。
- 批量翻译：合并请求降低延迟与成本。
- 质量评估：引入参考译文、BLEU/Comet 等指标（可选）。

## 🔗 相关文档
- 对话 API: ../api/openai-chat.md
- 性能优化: performance-optimization.md
