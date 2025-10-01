# ❓ 常见问题

## 💰 额度相关问题

??? tip "额度是什么？怎么计算的？"
    
    额度计算公式如下：
    
    额度 = 分组倍率 * 模型倍率 * （提示 token 数 + 补全 token 数 * 补全倍率）

    补全倍率说明：
    
    - GPT3.5：固定为 1.33
    
    - GPT4：固定为 2（与官方保持一致）

    注意事项：
    
    - 非流模式下，官方接口会返回消耗的总 token，但提示和补全的消耗倍率不同
    
    - 本平台的默认倍率与官方倍率一致，已经过调整

??? tip "账户额度足够为什么提示额度不足？"
    
    这是因为令牌额度和账户额度是分开的：
    
    - 令牌额度仅用于设置最大使用量限制
    - 用户可以自由设置令牌额度
    - 请检查您的令牌额度是否充足

## 🔐 认证与接入

??? tip "如何获取并配置 API Key？"
    
    在 Kapon AI 控制台生成 API Key，并在请求头中以 Bearer 方式携带：
    
    - Header：`Authorization: Bearer <YOUR_API_KEY>`
    - Base URL：`https://models.kapon.cloud/v1`
    
    SDK 示例（Python）：
    
    ```python
    from openai import OpenAI
    client = OpenAI(api_key="YOUR_API_KEY", base_url="https://models.kapon.cloud/v1")
    ```

??? tip "SDK 有版本要求吗？如何安装？"
    
    推荐使用官方 OpenAI SDK 的较新版本（Python/JavaScript 均可）。
    
    - Python：`pip install openai`
    - Node.js：`npm i openai` 或 `pnpm add openai`
    
    若因网络或镜像源导致安装缓慢，建议配置国内镜像或使用代理。

## 🔧 调用与错误排查

??? tip "出现 401/403 该如何处理？"
    
    - 401（Unauthorized）：检查 API Key 是否正确、是否传入了 `Authorization` 头；确认 Base URL 无误。
    - 403（Forbidden）：多为权限或配额限制，检查账户余额、模型授权、令牌额度设置是否足够。

??? tip "遇到 429（限流）怎么做重试？"
    
    对 429/5xx 建议使用指数退避并加入随机抖动。示例（伪代码）：
    
    ```python
    for attempt in range(max_retries):
        try:
            call_api()
            break
        except RateLimitError:
            sleep((2 ** attempt) + random())
    ```

??? tip "如何设置请求超时？"
    
    - Python `requests`：`timeout=30`
    - OpenAI Python SDK（异步）：可结合 `asyncio.wait_for` 做超时控制
    - Node.js `fetch/axios`：通过 `AbortController` 或客户端配置超时

??? tip "如何使用流式响应（stream）？"
    
    在对话接口中开启 `stream` 以缩短首包延迟，边到边处理：
    
    - Python：`client.chat.completions.create(..., stream=True)`
    - Node.js：使用 SDK 的流式接口或解析 SSE 流

## 📊 模型与计费

??? tip "支持哪些模型？如何查看？"
    
    可在控制台查看已开通模型；不同模型的可用性与倍率可能不同。文档中的各 API 页面也会列出示例与注意事项。

??? tip "Embeddings 的额度如何计算？"
    
    Embeddings 消耗通常只与输入 token 数相关，不存在补全；因此建议对输入做去重与合并，提升吞吐与降低开销。

## 🌐 前端与部署

??? tip "浏览器直接请求报 CORS，怎么办？"
    
    为安全与密钥保护，强烈建议在业务服务端转发请求，不要在浏览器中直接携带密钥。也可在受控网关中做域名白名单与鉴权。

??? tip "如何切换中英文文档？"
    
    文档站点提供多语言版本：
    
    - 中文：`/`
    - English：`/en/`
    
    本地开发时同样生效（如 `http://127.0.0.1:8000/en/`）。
