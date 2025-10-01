# Base on official MkDocs Material image
FROM squidfunk/mkdocs-material:latest

# Set timezone and working directory
ENV TZ=Asia/Shanghai
WORKDIR /docs

# Install extra MkDocs plugins/extensions used by this project
# - mkdocs-static-i18n[material] for multi-language support
# - mkdocs-git-revision-date-localized-plugin for last-updated stamps
# - mkdocs-glightbox for image lightbox
# - mkdocs-minify-plugin to minify HTML
RUN pip install --no-cache-dir \
      "mkdocs-static-i18n[material]" \
      mkdocs-git-revision-date-localized-plugin \
      mkdocs-glightbox \
      mkdocs-minify-plugin

# Copy repo (optional when using bind mount in docker-compose)
# Keeping this allows the image to run standalone without a mount.
COPY . /docs

# Default entrypoint delegates to our dev helper (overridable by docker-compose)
ENTRYPOINT ["/bin/sh", "-c"]
CMD ["./dev-server.sh"]

