FROM python:3.11-slim

WORKDIR /app
RUN apt-get update && apt-get install -y curl
COPY . .
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

ENV PATH="/root/.local/bin:${PATH}"

RUN uv venv .venv && uv pip install -r pyproject.toml

EXPOSE 3000
EXPOSE 5173

ENTRYPOINT ["uv", "run", "mcp", "run", "src/server.py:mcp"]