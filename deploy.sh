#!/usr/bin/env bash
set -e

PROJECT_NAME="mirocopy-converterbot"
APP_DIR="$HOME/MiroCopy-ConverterBot"

echo "🚀 Deploy ConverterBot ($PROJECT_NAME)"

cd "$APP_DIR"

echo "📥 Pull latest code"
git pull

echo "🛑 Stop old ConverterBot containers"
docker compose -p "$PROJECT_NAME" down --remove-orphans

echo "🔨 Build & start ConverterBot containers"
docker compose -p "$PROJECT_NAME" up -d --build

echo "🧹 Cleaning up unused Docker images..."
docker image prune -f

echo "✅ ConverterBot deploy finished"
