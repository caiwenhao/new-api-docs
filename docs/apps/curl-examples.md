# 🔧 cURL 示例集合

本页面提供了使用 cURL 调用 Kapon AI API 的完整示例集合，适合快速测试和脚本集成。

## 🔑 认证设置

首先设置环境变量：

```bash
export KAPON_API_KEY="your-api-key-here"
export KAPON_BASE_URL="https://models.kapon.cloud/v1"
```

## 💬 对话 API

### 基础对话

```bash
curl $KAPON_BASE_URL/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $KAPON_API_KEY" \
  -d '{
    "model": "gpt-4",
    "messages": [
      {
        "role": "system",
        "content": "你是一个有帮助的助手。"
      },
      {
        "role": "user",
        "content": "你好！"
      }
    ]
  }'
```

### 流式对话

```bash
curl $KAPON_BASE_URL/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $KAPON_API_KEY" \
  -d '{
    "model": "gpt-4",
    "messages": [
      {
        "role": "user",
        "content": "写一首关于春天的诗"
      }
    ],
    "stream": true
  }' \
  --no-buffer
```

### 函数调用

```bash
curl $KAPON_BASE_URL/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $KAPON_API_KEY" \
  -d '{
    "model": "gpt-4",
    "messages": [
      {
        "role": "user",
        "content": "北京今天天气怎么样？"
      }
    ],
    "functions": [
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
    ],
    "function_call": "auto"
  }'
```

### 多轮对话

```bash
curl $KAPON_BASE_URL/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $KAPON_API_KEY" \
  -d '{
    "model": "gpt-4",
    "messages": [
      {
        "role": "user",
        "content": "我想学习编程"
      },
      {
        "role": "assistant",
        "content": "很好！你想学习哪种编程语言呢？"
      },
      {
        "role": "user",
        "content": "Python"
      }
    ]
  }'
```

## 🖼️ 图像生成

### DALL-E 3 图像生成

```bash
curl $KAPON_BASE_URL/images/generations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $KAPON_API_KEY" \
  -d '{
    "model": "dall-e-3",
    "prompt": "一只可爱的小猫在花园里玩耍",
    "size": "1024x1024",
    "quality": "hd",
    "n": 1
  }'
```

### DALL-E 2 图像生成

```bash
curl $KAPON_BASE_URL/images/generations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $KAPON_API_KEY" \
  -d '{
    "model": "dall-e-2",
    "prompt": "未来城市的科幻景象",
    "size": "512x512",
    "n": 2
  }'
```

## 🔤 文本嵌入

### 创建嵌入向量

```bash
curl $KAPON_BASE_URL/embeddings \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $KAPON_API_KEY" \
  -d '{
    "model": "text-embedding-ada-002",
    "input": "这是一段需要向量化的文本"
  }'
```

### 批量嵌入

```bash
curl $KAPON_BASE_URL/embeddings \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $KAPON_API_KEY" \
  -d '{
    "model": "text-embedding-ada-002",
    "input": [
      "第一段文本",
      "第二段文本",
      "第三段文本"
    ]
  }'
```

## 🔊 音频处理

### 语音转文字

```bash
curl $KAPON_BASE_URL/audio/transcriptions \
  -H "Authorization: Bearer $KAPON_API_KEY" \
  -F file="@audio.mp3" \
  -F model="whisper-1"
```

### 语音翻译

```bash
curl $KAPON_BASE_URL/audio/translations \
  -H "Authorization: Bearer $KAPON_API_KEY" \
  -F file="@audio.mp3" \
  -F model="whisper-1"
```

### 文字转语音

```bash
curl $KAPON_BASE_URL/audio/speech \
  -H "Authorization: Bearer $KAPON_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "tts-1",
    "input": "你好，这是一段测试语音。",
    "voice": "alloy"
  }' \
  --output speech.mp3
```

## 🔄 重排序 API

### Jina AI 重排序

```bash
curl $KAPON_BASE_URL/rerank \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $KAPON_API_KEY" \
  -d '{
    "model": "jina-reranker-v1-base-en",
    "query": "人工智能的应用",
    "documents": [
      "人工智能在医疗领域的应用",
      "机器学习算法介绍",
      "深度学习在图像识别中的应用"
    ]
  }'
```

## 📊 模型列表

### 获取可用模型

```bash
curl $KAPON_BASE_URL/models \
  -H "Authorization: Bearer $KAPON_API_KEY"
```

### 获取特定模型信息

```bash
curl $KAPON_BASE_URL/models/gpt-4 \
  -H "Authorization: Bearer $KAPON_API_KEY"
```

## 🛠️ 实用脚本

### 批量测试脚本

```bash
#!/bin/bash

# 设置 API 密钥
export KAPON_API_KEY="your-api-key-here"
export KAPON_BASE_URL="https://models.kapon.cloud/v1"

# 测试问题列表
questions=(
  "什么是人工智能？"
  "机器学习的基本原理是什么？"
  "深度学习有哪些应用场景？"
)

# 批量测试
for i in "${!questions[@]}"; do
  echo "测试问题 $((i+1)): ${questions[i]}"
  
  curl -s $KAPON_BASE_URL/chat/completions \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $KAPON_API_KEY" \
    -d "{
      \"model\": \"gpt-4\",
      \"messages\": [
        {
          \"role\": \"user\",
          \"content\": \"${questions[i]}\"
        }
      ]
    }" | jq -r '.choices[0].message.content'
  
  echo -e "\n---\n"
done
```

### 性能测试脚本

```bash
#!/bin/bash

# 性能测试
echo "开始性能测试..."

start_time=$(date +%s.%N)

curl -s $KAPON_BASE_URL/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $KAPON_API_KEY" \
  -d '{
    "model": "gpt-4",
    "messages": [
      {
        "role": "user",
        "content": "Hello!"
      }
    ]
  }' > /dev/null

end_time=$(date +%s.%N)
duration=$(echo "$end_time - $start_time" | bc)

echo "响应时间: ${duration} 秒"
```

### 错误处理示例

```bash
#!/bin/bash

# 带错误处理的请求
response=$(curl -s -w "%{http_code}" $KAPON_BASE_URL/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $KAPON_API_KEY" \
  -d '{
    "model": "gpt-4",
    "messages": [
      {
        "role": "user",
        "content": "Hello!"
      }
    ]
  }')

http_code="${response: -3}"
body="${response%???}"

if [ "$http_code" -eq 200 ]; then
  echo "请求成功:"
  echo "$body" | jq -r '.choices[0].message.content'
else
  echo "请求失败，HTTP 状态码: $http_code"
  echo "错误信息: $body"
fi
```

## 📋 常用参数

### 对话参数

| 参数 | 类型 | 描述 | 默认值 |
|------|------|------|--------|
| `model` | string | 模型名称 | 必需 |
| `messages` | array | 消息列表 | 必需 |
| `temperature` | number | 随机性控制 (0-2) | 1 |
| `max_tokens` | integer | 最大输出长度 | 无限制 |
| `stream` | boolean | 是否流式输出 | false |

### 图像生成参数

| 参数 | 类型 | 描述 | 默认值 |
|------|------|------|--------|
| `model` | string | 模型名称 | 必需 |
| `prompt` | string | 图像描述 | 必需 |
| `size` | string | 图像尺寸 | "1024x1024" |
| `quality` | string | 图像质量 | "standard" |
| `n` | integer | 生成数量 | 1 |

## 🔗 相关资源

- [API 参考文档](../api/index.md)
- [Python SDK](python-sdk.md)
- [JavaScript SDK](javascript-sdk.md)
- [错误处理指南](error-handling.md)
