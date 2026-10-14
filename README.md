# 🚀 MonoCI: Zero-Config Monorepo CI/CD CLI

Инструмент командной строки для умного запуска задач (тестов, сборки, линтинга) **только в измененных пакетах** монорепозитория. Не требует файлов конфигурации.

## ✨ Возможности
- **Zero-Config**: Автоматически обнаруживает пакеты в папках `apps/`, `packages/`, `libs/`, `services/`.
- **Multi-language**: Поддерживает Node.js (`package.json`), Python (`pyproject.toml`), Rust (`Cargo.toml`), Java (`pom.xml`), Go (`go.mod`).
- **Git-Powered**: Анализирует `git diff` для точного определения затронутых компонентов.
- **Красивый вывод**: Использует `rich` для удобного чтения в CI/CD логах.

## 📦 Установка
```bash
pip install .
```
