# 📚 Kapon AI Docs

## 🚀 本地开发步骤

### 1️⃣ 安装依赖
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install mkdocs-material "mkdocs-static-i18n[material]" \
            mkdocs-git-revision-date-localized-plugin \
            mkdocs-glightbox mkdocs-minify-plugin
```

### 2️⃣ 启动本地服务
```bash
mkdocs serve
```
启动成功后访问
中文版: http://127.0.0.1:8000
英文版: http://127.0.0.1:8000/en/

OpenAPI 参考文档页面：`/api/reference/`（内嵌 Redoc，规范文件位于 `docs/openapi/openapi.yaml`）

### 3️⃣ 可选：Docker Compose 方式
使用自定义 `Dockerfile`（已预装所需插件），首次运行建议先构建：
```bash
docker compose build mkdocs
docker compose up
```
访问: http://127.0.0.1:2004

提示：若 zsh 报 `no matches found`，请给 extras 依赖加引号或转义方括号，例如：
`pip install "mkdocs-static-i18n[material]"`
