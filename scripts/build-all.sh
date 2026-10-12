#!/usr/bin/env bash
set -e
echo "Starting build-all pipeline..."
pnpm install
pnpm build
echo "Build completed successfully."
