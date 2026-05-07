#!/usr/bin/env bash
set -e

PROJECT_NAME="mirocopy-converter-bot"
APP_DIR="$HOME/MiroCopy-Converter-Bot"

echo "🚀 Deploy start"
cd "$APP_DIR" || { echo "❌ $APP_DIR not found"; exit 1; }

echo "📥 Pull latest code"
git pull

echo "🛑 Stop old containers"
docker compose -p "$PROJECT_NAME" down --remove-orphans

echo "🔨 Build & start containers"
docker compose -p "$PROJECT_NAME" up -d --build

echo "🧹 Cleaning up unused Docker images..."
docker image prune -f

echo "✅ Deploy finished"
