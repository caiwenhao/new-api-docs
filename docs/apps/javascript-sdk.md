# 🌐 JavaScript SDK 使用指南

Kapon AI 完全兼容 OpenAI JavaScript SDK，您可以直接使用官方 OpenAI SDK 来调用我们的 API。

## 📦 安装

### npm 安装
```bash
npm install openai
```

### yarn 安装
```bash
yarn add openai
```

### pnpm 安装
```bash
pnpm add openai
```

## 🔧 配置

### 基础配置

```javascript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: 'your-kapon-api-key', // 替换为您的 Kapon AI API 密钥
  baseURL: 'https://models.kapon.cloud/v1', // Kapon AI API 端点
});
```

### 环境变量配置

推荐使用环境变量管理 API 密钥：

```bash
# .env 文件
OPENAI_API_KEY=your-kapon-api-key
OPENAI_BASE_URL=https://models.kapon.cloud/v1
```

```javascript
import OpenAI from 'openai';

// 自动从环境变量读取配置
const client = new OpenAI();
```

## 💬 对话 API

### 基础对话

```javascript
async function chat() {
  const completion = await client.chat.completions.create({
    model: "gpt-4",
    messages: [
      { role: "system", content: "你是一个有帮助的助手。" },
      { role: "user", content: "你好！" }
    ],
  });

  console.log(completion.choices[0].message.content);
}

chat();
```

### 流式对话

```javascript
async function streamChat() {
  const stream = await client.chat.completions.create({
    model: "gpt-4",
    messages: [
      { role: "user", content: "写一首关于春天的诗" }
    ],
    stream: true,
  });

  for await (const chunk of stream) {
    const content = chunk.choices[0]?.delta?.content || '';
    process.stdout.write(content);
  }
}

streamChat();
```

### 函数调用

```javascript
async function functionCall() {
  const functions = [
    {
      name: "get_weather",
      description: "获取指定城市的天气信息",
      parameters: {
        type: "object",
        properties: {
          city: {
            type: "string",
            description: "城市名称"
          }
        },
        required: ["city"]
      }
    }
  ];

  const completion = await client.chat.completions.create({
    model: "gpt-4",
    messages: [{ role: "user", content: "北京今天天气怎么样？" }],
    functions: functions,
    function_call: "auto"
  });

  const message = completion.choices[0].message;
  
  if (message.function_call) {
    const functionName = message.function_call.name;
    const functionArgs = JSON.parse(message.function_call.arguments);
    
    if (functionName === "get_weather") {
      const result = getWeather(functionArgs.city);
      console.log(`天气信息：${result}`);
    }
  }
}

function getWeather(city) {
  // 模拟天气查询
  return `${city}今天晴朗，温度25°C`;
}

functionCall();
```

## 🖼️ 图像生成

```javascript
async function generateImage() {
  const image = await client.images.generate({
    model: "dall-e-3",
    prompt: "一只可爱的小猫在花园里玩耍",
    size: "1024x1024",
    quality: "hd",
    n: 1,
  });

  console.log(`生成的图像URL：${image.data[0].url}`);
}

generateImage();
```

## 🔤 文本嵌入

```javascript
async function createEmbedding() {
  const embedding = await client.embeddings.create({
    model: "text-embedding-ada-002",
    input: "这是一段需要向量化的文本",
  });

  const vector = embedding.data[0].embedding;
  console.log(`嵌入向量维度：${vector.length}`);
  console.log(`前5个维度：${vector.slice(0, 5)}`);
}

createEmbedding();
```

## 🔊 音频处理

### 语音转文字

```javascript
import fs from 'fs';

async function transcribeAudio() {
  const transcription = await client.audio.transcriptions.create({
    file: fs.createReadStream("audio.mp3"),
    model: "whisper-1",
  });

  console.log(transcription.text);
}

transcribeAudio();
```

### 文字转语音

```javascript
import fs from 'fs';

async function textToSpeech() {
  const mp3 = await client.audio.speech.create({
    model: "tts-1",
    voice: "alloy",
    input: "你好，这是一段测试语音。",
  });

  const buffer = Buffer.from(await mp3.arrayBuffer());
  await fs.promises.writeFile("output.mp3", buffer);
}

textToSpeech();
```

## 🛠️ 高级功能

### 错误处理

```javascript
import { OpenAIError } from 'openai';

async function handleErrors() {
  try {
    const completion = await client.chat.completions.create({
      model: "gpt-4",
      messages: [{ role: "user", content: "Hello!" }],
    });
    
    console.log(completion.choices[0].message.content);
  } catch (error) {
    if (error instanceof OpenAIError) {
      console.error('OpenAI API 错误:', error.message);
    } else {
      console.error('其他错误:', error);
    }
  }
}

handleErrors();
```

### 并发请求

```javascript
async function concurrentRequests() {
  const messages = [
    "介绍一下人工智能",
    "什么是机器学习？",
    "深度学习的应用场景"
  ];

  const promises = messages.map(message => 
    client.chat.completions.create({
      model: "gpt-4",
      messages: [{ role: "user", content: message }],
    })
  );

  const results = await Promise.all(promises);
  
  results.forEach((result, index) => {
    console.log(`问题 ${index + 1} 的回答：${result.choices[0].message.content}\n`);
  });
}

concurrentRequests();
```

### 请求配置

```javascript
const client = new OpenAI({
  apiKey: 'your-kapon-api-key',
  baseURL: 'https://models.kapon.cloud/v1',
  timeout: 30000, // 30秒超时
  maxRetries: 3,   // 最大重试次数
});
```

## 🌐 浏览器环境

### 基础配置

```html
<!DOCTYPE html>
<html>
<head>
    <title>Kapon AI Web Demo</title>
</head>
<body>
    <script type="module">
        import OpenAI from 'https://cdn.skypack.dev/openai';
        
        const client = new OpenAI({
            apiKey: 'your-kapon-api-key',
            baseURL: 'https://models.kapon.cloud/v1',
            dangerouslyAllowBrowser: true // 仅用于演示，生产环境请使用代理
        });
        
        async function chat() {
            const completion = await client.chat.completions.create({
                model: "gpt-4",
                messages: [{ role: "user", content: "Hello!" }],
            });
            
            document.body.innerHTML = completion.choices[0].message.content;
        }
        
        chat();
    </script>
</body>
</html>
```

### 安全注意事项

⚠️ **重要提醒**：
- 不要在客户端代码中暴露 API 密钥
- 生产环境中应使用后端代理
- 考虑使用 CORS 代理或服务器端渲染

## 📊 使用统计

```javascript
async function getUsageStats() {
  const completion = await client.chat.completions.create({
    model: "gpt-4",
    messages: [{ role: "user", content: "Hello!" }],
  });

  // 打印使用统计
  const usage = completion.usage;
  console.log(`输入 tokens：${usage.prompt_tokens}`);
  console.log(`输出 tokens：${usage.completion_tokens}`);
  console.log(`总计 tokens：${usage.total_tokens}`);
}

getUsageStats();
```

## 🔗 相关资源

- [OpenAI JavaScript SDK 官方文档](https://github.com/openai/openai-node)
- [API 参考文档](../api/index.md)
- [错误处理指南](error-handling.md)
- [性能优化技巧](performance-optimization.md)
