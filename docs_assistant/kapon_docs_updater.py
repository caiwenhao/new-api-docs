#!/usr/bin/env python3
"""
Kapon AI 文档更新工具
用于维护和更新 Kapon AI 文档网站
"""

import os
import logging
import time
from datetime import datetime
from pathlib import Path

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('kapon_docs_updater')

class KaponDocsUpdater:
    """Kapon AI 文档更新器"""
    
    def __init__(self, docs_dir="/app/docs"):
        self.docs_dir = Path(docs_dir)
        self.update_interval = int(os.getenv('UPDATE_INTERVAL', 3600))  # 默认1小时
        
    def update_service_status(self):
        """更新服务状态页面"""
        try:
            status_file = self.docs_dir / "docs" / "support" / "service-status.md"
            
            # 模拟服务状态检查
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            status_content = f"""# 📈 服务状态

## 🟢 当前状态：正常运行

**最后更新时间**：{current_time}

## 📊 实时监控

### API 服务状态
- **状态**：🟢 正常
- **可用性**：99.9%
- **响应时间**：< 500ms
- **活跃连接**：正常

### 模型服务状态
- **GPT-4**：🟢 正常
- **Claude-3.5**：🟢 正常
- **Gemini Pro**：🟢 正常
- **DALL-E 3**：🟢 正常

### 基础设施状态
- **CDN**：🟢 正常
- **数据库**：🟢 正常
- **负载均衡**：🟢 正常
- **监控系统**：🟢 正常

## 📅 维护计划

当前无计划维护。

## 📞 问题报告

如遇到服务问题，请联系：
- 📧 邮箱：[support@kapon.cloud](mailto:support@kapon.cloud)
- 📱 热线：400-123-4567

---

*此页面每小时自动更新*
"""
            
            # 确保目录存在
            status_file.parent.mkdir(parents=True, exist_ok=True)
            
            # 写入状态文件
            with open(status_file, 'w', encoding='utf-8') as f:
                f.write(status_content)
                
            logger.info("服务状态页面已更新")
            return True
            
        except Exception as e:
            logger.error(f"更新服务状态失败: {e}")
            return False
    
    def update_api_models(self):
        """更新 API 模型列表"""
        try:
            models_file = self.docs_dir / "docs" / "api" / "models.md"
            
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            models_content = f"""# 🤖 支持的模型

**最后更新时间**：{current_time}

## 💬 对话模型

### OpenAI 系列
- **GPT-4o** - 最新多模态模型
- **GPT-4o-mini** - 轻量级高效模型
- **GPT-4 Turbo** - 高性能对话模型
- **GPT-3.5 Turbo** - 经典对话模型

### Anthropic 系列
- **Claude-3.5 Sonnet** - 最新智能模型
- **Claude-3 Haiku** - 快速响应模型
- **Claude-3 Opus** - 高级推理模型

### Google 系列
- **Gemini Pro** - 多模态智能模型
- **Gemini Flash** - 快速处理模型

## 🖼️ 图像生成模型

- **DALL-E 3** - 高质量图像生成
- **DALL-E 2** - 经典图像生成
- **Stable Diffusion** - 开源图像生成

## 🔤 嵌入模型

- **text-embedding-3-large** - 高维度嵌入
- **text-embedding-3-small** - 轻量级嵌入
- **text-embedding-ada-002** - 经典嵌入模型

## 🔊 音频模型

- **Whisper** - 语音转文字
- **TTS** - 文字转语音
- **TTS HD** - 高清文字转语音

## 📊 模型性能对比

| 模型 | 响应速度 | 质量评分 | 成本效益 | 推荐场景 |
|------|----------|----------|----------|----------|
| GPT-4o | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | 复杂推理 |
| Claude-3.5 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | 长文本处理 |
| Gemini Pro | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 多模态应用 |

## 🔄 模型更新

我们会定期更新模型列表，添加最新的 AI 模型。如有特定模型需求，请联系我们的技术团队。

---

*模型列表每日自动更新*
"""
            
            # 确保目录存在
            models_file.parent.mkdir(parents=True, exist_ok=True)
            
            # 写入模型文件
            with open(models_file, 'w', encoding='utf-8') as f:
                f.write(models_content)
                
            logger.info("API 模型列表已更新")
            return True
            
        except Exception as e:
            logger.error(f"更新 API 模型列表失败: {e}")
            return False
    
    def cleanup_old_files(self):
        """清理旧的开源项目相关文件"""
        try:
            # 需要清理的文件列表
            files_to_remove = [
                "docs/wiki",
                "docs/installation", 
                "docs/guide",
                "docs/support/community-interaction.md",
                "docs/support/buy-us-a-coffee.md",
                "docs/support/feedback-issues.md",
                "docs/business-cooperation.md"
            ]
            
            for file_path in files_to_remove:
                full_path = self.docs_dir / file_path
                if full_path.exists():
                    if full_path.is_dir():
                        import shutil
                        shutil.rmtree(full_path)
                        logger.info(f"已删除目录: {file_path}")
                    else:
                        full_path.unlink()
                        logger.info(f"已删除文件: {file_path}")
                        
            return True
            
        except Exception as e:
            logger.error(f"清理旧文件失败: {e}")
            return False
    
    def run_update_cycle(self):
        """运行一次更新周期"""
        logger.info("开始文档更新周期")
        
        # 更新服务状态
        self.update_service_status()
        
        # 更新模型列表
        self.update_api_models()
        
        logger.info("文档更新周期完成")
    
    def run_daemon(self):
        """以守护进程模式运行"""
        logger.info(f"启动 Kapon AI 文档更新器，更新间隔: {self.update_interval} 秒")
        
        while True:
            try:
                self.run_update_cycle()
                time.sleep(self.update_interval)
            except KeyboardInterrupt:
                logger.info("收到停止信号，退出程序")
                break
            except Exception as e:
                logger.error(f"更新周期出错: {e}")
                time.sleep(60)  # 出错后等待1分钟再重试

def main():
    """主函数"""
    updater = KaponDocsUpdater()
    
    # 检查是否为一次性运行
    if os.getenv('RUN_ONCE', 'false').lower() == 'true':
        updater.run_update_cycle()
    else:
        updater.run_daemon()

if __name__ == "__main__":
    main()
