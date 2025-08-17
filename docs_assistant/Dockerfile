FROM python:3.11-slim

WORKDIR /app

# 创建简化的 requirements.txt
RUN echo "requests>=2.31.0" > requirements.txt

# 安装Python依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制新的更新工具
COPY kapon_docs_updater.py .

# 设置环境变量
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1
ENV UPDATE_INTERVAL=3600
ENV RUN_ONCE=false

# 运行应用
CMD ["python", "kapon_docs_updater.py"]