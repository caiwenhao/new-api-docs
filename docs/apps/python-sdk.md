# 🐍 Python SDK 使用指南

Kapon AI 完全兼容 OpenAI Python SDK，您可以直接使用官方 OpenAI SDK 来调用我们的 API。

## 📦 安装

使用 pip 安装 OpenAI Python SDK：

```bash
pip install openai
```

## 🔧 配置

### 基础配置

```python
import openai

# 配置 API 密钥和基础 URL
client = openai.OpenAI(
    api_key="your-kapon-api-key",  # 替换为您的 Kapon AI API 密钥
    base_url="https://models.kapon.cloud/v1"  # Kapon AI API 端点
)
```

### 环境变量配置

推荐使用环境变量管理 API 密钥：

```bash
# 设置环境变量
export OPENAI_API_KEY="your-kapon-api-key"
export OPENAI_BASE_URL="https://models.kapon.cloud/v1"
```

```python
import openai
import os

# 自动从环境变量读取配置
client = openai.OpenAI()
```

## 💬 对话 API

### 基础对话

```python
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "你是一个有帮助的助手。"},
        {"role": "user", "content": "你好！"}
    ]
)

print(response.choices[0].message.content)
```

### 流式对话

```python
stream = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": "写一首关于春天的诗"}
    ],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
```

### 函数调用

```python
import json

def get_weather(city):
    """获取天气信息的模拟函数"""
    return f"{city}今天晴朗，温度25°C"

# 定义函数描述
functions = [
    {
        "name": "get_weather",
        "description": "获取指定城市的天气信息",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "城市名称"
                }
            },
            "required": ["city"]
        }
    }
]

# 发送请求
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "北京今天天气怎么样？"}],
    functions=functions,
    function_call="auto"
)

# 处理函数调用
message = response.choices[0].message
if message.function_call:
    function_name = message.function_call.name
    function_args = json.loads(message.function_call.arguments)
    
    if function_name == "get_weather":
        result = get_weather(function_args["city"])
        print(f"天气信息：{result}")
```

## 🖼️ 图像生成

```python
response = client.images.generate(
    model="dall-e-3",
    prompt="一只可爱的小猫在花园里玩耍",
    size="1024x1024",
    quality="hd",
    n=1
)

image_url = response.data[0].url
print(f"生成的图像URL：{image_url}")
```

## 🔤 文本嵌入

```python
response = client.embeddings.create(
    model="text-embedding-ada-002",
    input="这是一段需要向量化的文本"
)

embedding = response.data[0].embedding
print(f"嵌入向量维度：{len(embedding)}")
print(f"前5个维度：{embedding[:5]}")
```

## 🔊 音频处理

### 语音转文字

```python
with open("audio.mp3", "rb") as audio_file:
    transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    )
    
print(transcript.text)
```

### 文字转语音

```python
response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input="你好，这是一段测试语音。"
)

# 保存音频文件
with open("output.mp3", "wb") as f:
    f.write(response.content)
```

## 🛠️ 高级功能

### 异步调用

```python
import asyncio
from openai import AsyncOpenAI

async_client = AsyncOpenAI(
    api_key="your-kapon-api-key",
    base_url="https://models.kapon.cloud/v1"
)

async def async_chat():
    response = await async_client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": "Hello!"}]
    )
    return response.choices[0].message.content

# 运行异步函数
result = asyncio.run(async_chat())
print(result)
```

### 批量处理

```python
import concurrent.futures

def process_message(message):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": message}]
    )
    return response.choices[0].message.content

messages = [
    "介绍一下人工智能",
    "什么是机器学习？",
    "深度学习的应用场景"
]

# 并发处理多个请求
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(process_message, messages))

for i, result in enumerate(results):
    print(f"问题 {i+1} 的回答：{result}\n")
```

## ⚠️ 错误处理

```python
from openai import OpenAI, OpenAIError

try:
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": "Hello!"}]
    )
    print(response.choices[0].message.content)
    
except OpenAIError as e:
    print(f"API 错误：{e}")
except Exception as e:
    print(f"其他错误：{e}")
```

## 📊 使用统计

```python
# 获取使用统计信息
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Hello!"}]
)

# 打印使用统计
usage = response.usage
print(f"输入 tokens：{usage.prompt_tokens}")
print(f"输出 tokens：{usage.completion_tokens}")
print(f"总计 tokens：{usage.total_tokens}")
```

## 🔗 相关资源

- [OpenAI Python SDK 官方文档](https://github.com/openai/openai-python)
- [API 参考文档](../api/index.md)
- [错误处理指南](error-handling.md)
- [性能优化技巧](performance-optimization.md)
