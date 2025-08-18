---
hide:
  - footer
---

<style>
  .md-typeset .grid.cards > ul {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(16rem, 1fr));
    gap: 1rem;
    margin: 1em 0;
  }
  
  .md-typeset .grid.cards > ul > li {
    border: none;
    border-radius: 0.8rem;
    box-shadow: var(--md-shadow-z2);
    padding: 1.5rem;
    transition: transform 0.25s, box-shadow 0.25s;
    background: linear-gradient(135deg, var(--md-primary-fg-color), var(--md-accent-fg-color));
    color: var(--md-primary-bg-color);
  }

  .md-typeset .grid.cards > ul > li:hover {
    transform: scale(1.02);
    box-shadow: var(--md-shadow-z3);
  }

  .md-typeset .grid.cards > ul > li > hr {
    margin: 0.8rem 0;
    border: none;
    border-bottom: 2px solid var(--md-primary-bg-color);
    opacity: 0.2;
  }

  .md-typeset .grid.cards > ul > li > p {
    margin: 0.5rem 0;
  }

  .md-typeset .grid.cards > ul > li > p > em {
    color: var(--md-primary-bg-color);
    opacity: 0.8;
    font-style: normal;
  }

  .md-typeset .grid.cards > ul > li > p > .twemoji {
    font-size: 2.5rem;
    display: block;
    margin: 0.5rem auto;
  }

  /* 新增：美化介绍部分 */
  .interface-intro {
    margin: 2rem 0;
    padding: 1.5rem;
    border-radius: 0.8rem;
    background-color: var(--md-primary-fg-color--light);
    color: var(--md-primary-bg-color);
  }

  /* 新增：优化卡片链接样式 */
  .md-typeset .grid.cards > ul > li a {
    display: inline-flex;
    align-items: center;
    margin-top: 1.2em;
    padding: 0.5em 1.2em;
    color: white;
    background-color: rgba(255, 255, 255, 0.15);
    border-radius: 2em;
    transition: all 0.3s ease;
    font-weight: 500;
    font-size: 0.9em;
    letter-spacing: 0.03em;
    box-shadow: 0 3px 6px rgba(0, 0, 0, 0.1);
    position: relative;
    overflow: hidden;
    text-decoration: none;
  }

  .md-typeset .grid.cards > ul > li a:hover {
    background-color: rgba(255, 255, 255, 0.25);
    text-decoration: none;
    box-shadow: 0 5px 12px rgba(0, 0, 0, 0.2);
    transform: translateX(5px);
  }

  .md-typeset .grid.cards > ul > li a:after {
    content: "→";
    opacity: 0;
    margin-left: -15px;
    transition: all 0.2s ease;
  }

  .md-typeset .grid.cards > ul > li a:hover:after {
    opacity: 1;
    margin-left: 5px;
  }
</style>

# 接口总览

## 💫 中继接口

<div class="grid cards" markdown>

-   :material-chat:{ .twemoji }

    **聊天（Chat）**

    ---

    支持多种主流聊天模型格式：
    
    [OpenAI Chat →](openai-chat.md)
    [OpenAI Responses →](openai-responses.md)
    [Anthropic Chat →](anthropic-chat.md)
    [Deepseek Chat →](deepseek-reasoning-chat.md)
    [Google Chat →](google-gemini-chat.md)

-   :material-alphabetical:{ .twemoji }

    **嵌入（Embeddings）**

    ---

    文本向量嵌入服务：
    
    [OpenAI Embeddings →](openai-embedding.md)

-   :material-swap-vertical:{ .twemoji }

    **重排序（Rerank）**

    ---

    搜索结果重排序服务：
    
    [Jina AI Rerank →](jinaai-rerank.md)
    [Cohere Rerank →](cohere-rerank.md)
    [Xinference Rerank →](xinference-rerank.md)

-   :material-lightning-bolt:{ .twemoji }

    **实时对话（Realtime）**

    ---

    支持流式实时对话：
    
    [OpenAI Realtime →](openai-realtime.md)

-   :material-image:{ .twemoji }

    **图像（Image）**

    ---

    AI 图像生成服务：
    
    [OpenAI Image →](openai-image.md)
    [Midjourney Proxy →](midjourney-proxy-image.md)

-   :material-volume-high:{ .twemoji }

    **音频（Audio）**

    ---

    语音相关服务：
    
    [OpenAI Audio →](openai-audio.md)

-   :material-music:{ .twemoji }

    **音乐（Music）**

    ---

    AI 音乐生成服务：
    
    [Suno API →](suno-music.md)

-   :material-video:{ .twemoji }

    **视频（Video）**

    ---

    AI 视频生成和查询服务：
    
    [生成视频 →](generate-video.md)
    [查询视频 →](query-video.md)

</div>

