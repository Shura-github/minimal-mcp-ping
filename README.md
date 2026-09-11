# Minimal MCP Ping

A tiny Python MCP server built with UV and FastMCP. It exposes one tool:

- `ping` returns `pong`

## Run locally

```bash
uv sync
uv run fastmcp run server.py:mcp
```

The server uses the default stdio transport, so it can be launched by an MCP client such as VS Code.

## Configure in VS Code

```json
{
  "servers": {
    "minimal-mcp-ping": {
      "type": "stdio",
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "/absolute/path/to/minimal-mcp-ping",
        "fastmcp",
        "run",
        "server.py:mcp"
      ]
    }
  }
}
```
