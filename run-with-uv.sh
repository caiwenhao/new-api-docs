#!/bin/bash

echo "🚀 使用 uv 启动 New API 文档项目"

# 检查 uv 是否已安装
if ! command -v uv &> /dev/null; then
    echo "❌ uv 未安装，请先安装 uv："
    echo "curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

echo "📦 创建虚拟环境并安装依赖..."
# 创建虚拟环境（如果不存在）
if [ ! -d ".venv" ]; then
    uv venv
fi

# 激活虚拟环境并安装依赖
source .venv/bin/activate
uv pip install mkdocs-material "mkdocs-static-i18n[material]"

echo "🌐 启动开发服务器..."
echo "📱 中文版: http://127.0.0.1:8000"
echo "📱 英文版: http://127.0.0.1:8000/en/"
echo "🛑 按 Ctrl+C 停止服务器"

# 运行 mkdocs serve
mkdocs serve
