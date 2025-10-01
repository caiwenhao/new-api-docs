# ⚡ 性能优化指南

本文汇总在使用 Kapon AI 接口进行应用开发时的常见性能优化策略与实践建议，帮助你在稳定性的前提下获得更低的延迟与成本。

## ✅ 基础优化
- 连接复用：在服务端复用 HTTP 连接（keep-alive），避免频繁建连开销。
- 压缩传输：开启 `gzip/br` 压缩，降低大响应体带宽占用。
- 超时设置：为请求设置合理的超时，避免阻塞线程/协程。
- 并发控制：使用连接池或队列限制并发峰值，防止抖动。

## 🚀 请求层优化
- 批量请求：能批就批（如嵌入向量），减少往返次数。
- 流式响应：开启流式接口，边到边处理，缩短首包延迟。
- 结果缓存：对确定性结果做缓存（如 embeddings / rerank）。
- 退避重试：对 429/5xx 使用指数退避 + 抖动重试。

## 🧠 模型使用优化
- 合理温度：对确定性任务降低 `temperature`，降低 token 浪费。
- 控制长度：设置 `max_tokens`，避免长尾输出拖慢响应。
- 压缩上下文：对历史对话做摘要/截断，减少 prompt 体积。

## 🧪 代码片段
Python（requests + 重试）：
```python
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import requests

session = requests.Session()
retry = Retry(total=3, status_forcelist=[429,500,502,503], backoff_factor=1)
session.mount('https://', HTTPAdapter(max_retries=retry))

resp = session.post('https://models.kapon.cloud/v1/chat/completions', timeout=30, json={...})
```

Node.js（fetch + 超时控制）：
```js
const controller = new AbortController();
const timer = setTimeout(() => controller.abort(), 30000);

const resp = await fetch(url, { method: 'POST', body: JSON.stringify(body), signal: controller.signal });
clearTimeout(timer);
```

## 🔗 相关文档
- API 参考: ../api/index.md
- 错误处理: error-handling.md
- 提示词工程: prompt-engineering.md
