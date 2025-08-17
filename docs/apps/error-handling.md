# 🛡️ 错误处理指南

本指南将帮助您优雅地处理 Kapon AI API 调用中可能遇到的各种错误情况。

## 📋 错误类型概览

### HTTP 状态码

| 状态码 | 错误类型 | 描述 |
|--------|----------|------|
| 400 | Bad Request | 请求格式错误 |
| 401 | Unauthorized | 认证失败 |
| 403 | Forbidden | 权限不足 |
| 404 | Not Found | 资源不存在 |
| 429 | Too Many Requests | 请求过于频繁 |
| 500 | Internal Server Error | 服务器内部错误 |
| 502 | Bad Gateway | 网关错误 |
| 503 | Service Unavailable | 服务不可用 |

### 错误响应格式

```json
{
  "error": {
    "message": "错误描述信息",
    "type": "error_type",
    "code": "error_code",
    "param": "parameter_name"
  }
}
```

## 🔑 认证错误

### 401 - API 密钥无效

**错误示例：**
```json
{
  "error": {
    "message": "Invalid API key provided",
    "type": "invalid_request_error",
    "code": "invalid_api_key"
  }
}
```

**解决方案：**
```python
import openai

try:
    client = openai.OpenAI(
        api_key="your-kapon-api-key",
        base_url="https://models.kapon.cloud/v1"
    )
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": "Hello!"}]
    )
except openai.AuthenticationError as e:
    print(f"认证失败: {e}")
    # 检查 API 密钥是否正确
    # 确认密钥是否已过期
    # 验证密钥权限设置
```

### 403 - 权限不足

**常见原因：**
- API 密钥权限不足
- 账户余额不足
- 模型访问权限受限

**处理方式：**
```python
try:
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": "Hello!"}]
    )
except openai.PermissionDeniedError as e:
    print(f"权限不足: {e}")
    # 检查账户余额
    # 确认模型访问权限
    # 联系技术支持
```

## 🚦 请求限制错误

### 429 - 请求过于频繁

**错误示例：**
```json
{
  "error": {
    "message": "Rate limit exceeded",
    "type": "rate_limit_error",
    "code": "rate_limit_exceeded"
  }
}
```

**指数退避重试策略：**
```python
import time
import random
from openai import RateLimitError

def make_request_with_retry(client, max_retries=5):
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": "Hello!"}]
            )
            return response
        except RateLimitError as e:
            if attempt == max_retries - 1:
                raise e
            
            # 指数退避 + 随机抖动
            wait_time = (2 ** attempt) + random.uniform(0, 1)
            print(f"请求限制，等待 {wait_time:.2f} 秒后重试...")
            time.sleep(wait_time)
    
    raise Exception("重试次数已用完")
```

**JavaScript 版本：**
```javascript
async function makeRequestWithRetry(client, maxRetries = 5) {
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      const response = await client.chat.completions.create({
        model: "gpt-4",
        messages: [{ role: "user", content: "Hello!" }],
      });
      return response;
    } catch (error) {
      if (error.status === 429 && attempt < maxRetries - 1) {
        const waitTime = Math.pow(2, attempt) * 1000 + Math.random() * 1000;
        console.log(`请求限制，等待 ${waitTime/1000:.2f} 秒后重试...`);
        await new Promise(resolve => setTimeout(resolve, waitTime));
      } else {
        throw error;
      }
    }
  }
}
```

## 📝 请求格式错误

### 400 - 请求参数错误

**常见错误：**

1. **缺少必需参数**
```json
{
  "error": {
    "message": "Missing required parameter: 'messages'",
    "type": "invalid_request_error",
    "code": "missing_parameter",
    "param": "messages"
  }
}
```

2. **参数类型错误**
```json
{
  "error": {
    "message": "Invalid type for parameter 'temperature': expected number, got string",
    "type": "invalid_request_error",
    "code": "invalid_parameter_type",
    "param": "temperature"
  }
}
```

**参数验证函数：**
```python
def validate_chat_params(model, messages, **kwargs):
    """验证聊天 API 参数"""
    errors = []
    
    # 验证必需参数
    if not model:
        errors.append("model 参数不能为空")
    if not messages or not isinstance(messages, list):
        errors.append("messages 必须是非空列表")
    
    # 验证可选参数
    if 'temperature' in kwargs:
        temp = kwargs['temperature']
        if not isinstance(temp, (int, float)) or temp < 0 or temp > 2:
            errors.append("temperature 必须是 0-2 之间的数字")
    
    if 'max_tokens' in kwargs:
        max_tokens = kwargs['max_tokens']
        if not isinstance(max_tokens, int) or max_tokens <= 0:
            errors.append("max_tokens 必须是正整数")
    
    if errors:
        raise ValueError(f"参数验证失败: {'; '.join(errors)}")

# 使用示例
try:
    validate_chat_params(
        model="gpt-4",
        messages=[{"role": "user", "content": "Hello!"}],
        temperature=0.7,
        max_tokens=1000
    )
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": "Hello!"}],
        temperature=0.7,
        max_tokens=1000
    )
except ValueError as e:
    print(f"参数错误: {e}")
except Exception as e:
    print(f"API 调用失败: {e}")
```

## 🔧 服务器错误

### 500/502/503 - 服务器错误

**重试策略：**
```python
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def create_resilient_session():
    """创建具有重试机制的会话"""
    session = requests.Session()
    
    retry_strategy = Retry(
        total=3,  # 总重试次数
        status_forcelist=[429, 500, 502, 503, 504],  # 需要重试的状态码
        backoff_factor=1,  # 退避因子
        allowed_methods=["HEAD", "GET", "POST"]  # 允许重试的方法
    )
    
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    
    return session

# 使用示例
session = create_resilient_session()

try:
    response = session.post(
        "https://models.kapon.cloud/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        json={
            "model": "gpt-4",
            "messages": [{"role": "user", "content": "Hello!"}]
        },
        timeout=30
    )
    response.raise_for_status()
    result = response.json()
except requests.exceptions.RequestException as e:
    print(f"请求失败: {e}")
```

## 🕐 超时处理

### 设置合理的超时时间

```python
import asyncio
from openai import AsyncOpenAI

async def chat_with_timeout(client, timeout=30):
    """带超时的聊天请求"""
    try:
        response = await asyncio.wait_for(
            client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": "Hello!"}]
            ),
            timeout=timeout
        )
        return response
    except asyncio.TimeoutError:
        print(f"请求超时 ({timeout} 秒)")
        return None
    except Exception as e:
        print(f"请求失败: {e}")
        return None

# 使用示例
async def main():
    client = AsyncOpenAI(
        api_key="your-kapon-api-key",
        base_url="https://models.kapon.cloud/v1"
    )
    
    response = await chat_with_timeout(client, timeout=30)
    if response:
        print(response.choices[0].message.content)

asyncio.run(main())
```

## 📊 错误监控和日志

### 完整的错误处理类

```python
import logging
import time
from typing import Optional, Dict, Any
from openai import OpenAI, OpenAIError

class KaponAIClient:
    """带完整错误处理的 Kapon AI 客户端"""
    
    def __init__(self, api_key: str, base_url: str = "https://models.kapon.cloud/v1"):
        self.client = OpenAI(api_key=api_key, base_url=base_url)
        self.logger = logging.getLogger(__name__)
        
        # 配置日志
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
    
    def chat_completion(
        self, 
        model: str, 
        messages: list, 
        max_retries: int = 3,
        **kwargs
    ) -> Optional[Dict[Any, Any]]:
        """带重试和错误处理的聊天完成"""
        
        for attempt in range(max_retries):
            try:
                self.logger.info(f"发起聊天请求 (尝试 {attempt + 1}/{max_retries})")
                
                response = self.client.chat.completions.create(
                    model=model,
                    messages=messages,
                    **kwargs
                )
                
                self.logger.info("请求成功")
                return response.model_dump()
                
            except OpenAIError as e:
                self.logger.error(f"OpenAI API 错误: {e}")
                
                # 根据错误类型决定是否重试
                if hasattr(e, 'status_code'):
                    if e.status_code == 429:  # 速率限制
                        if attempt < max_retries - 1:
                            wait_time = 2 ** attempt
                            self.logger.info(f"速率限制，等待 {wait_time} 秒")
                            time.sleep(wait_time)
                            continue
                    elif e.status_code in [500, 502, 503]:  # 服务器错误
                        if attempt < max_retries - 1:
                            wait_time = 2 ** attempt
                            self.logger.info(f"服务器错误，等待 {wait_time} 秒")
                            time.sleep(wait_time)
                            continue
                
                # 不可重试的错误
                self.logger.error(f"不可重试的错误: {e}")
                return None
                
            except Exception as e:
                self.logger.error(f"未知错误: {e}")
                if attempt < max_retries - 1:
                    time.sleep(1)
                    continue
                return None
        
        self.logger.error("所有重试尝试都失败了")
        return None

# 使用示例
client = KaponAIClient("your-kapon-api-key")

response = client.chat_completion(
    model="gpt-4",
    messages=[{"role": "user", "content": "Hello!"}],
    temperature=0.7
)

if response:
    print(response['choices'][0]['message']['content'])
else:
    print("请求失败")
```

## 🔗 相关资源

- [API 参考文档](../api/index.md)
- [Python SDK](python-sdk.md)
- [JavaScript SDK](javascript-sdk.md)
- [性能优化指南](performance-optimization.md)
- [技术支持](../support/contact.md)
