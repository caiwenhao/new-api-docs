#!/bin/sh

# Development server script after switching to mkdocs-static-i18n

# Ensure required MkDocs plugins are installed inside container
ensure_pkg() {
  pkg="$1"; shift
  if ! pip show "$pkg" >/dev/null 2>&1; then
    echo "📦 Installing $pkg ..."
    pip install --no-cache-dir "$@"
  fi
}

ensure_pkg mkdocs-static-i18n mkdocs-static-i18n[material]
ensure_pkg mkdocs-git-revision-date-localized-plugin mkdocs-git-revision-date-localized-plugin
ensure_pkg mkdocs-glightbox mkdocs-glightbox
ensure_pkg mkdocs-minify-plugin mkdocs-minify-plugin

echo "🚀 Starting development server with i18n (hot-reload)..."

echo "📱 Chinese version: http://0.0.0.0:8000"
echo "📱 English version: http://0.0.0.0:8000/en/"
echo "🛑 Press Ctrl+C to stop the server"

# Start mkdocs with hot reload on single port
mkdocs serve --dev-addr 0.0.0.0:8000 
