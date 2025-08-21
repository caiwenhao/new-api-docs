# 基于官方 MkDocs Material 镜像
FROM squidfunk/mkdocs-material:latest

# 设置工作目录
WORKDIR /docs

# 安装项目所需的额外依赖
RUN pip install --no-cache-dir \
    mkdocs-static-i18n[material]

# 复制项目文件
COPY . /docs

# 确保脚本有执行权限
RUN chmod +x /docs/dev-server.sh

# 暴露端口
EXPOSE 8000

# 默认命令
CMD ["./dev-server.sh"]
