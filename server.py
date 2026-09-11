from fastmcp import FastMCP

mcp = FastMCP("Minimal Ping MCP Server")


@mcp.tool
def ping() -> str:
    """Return a simple health-check response."""
    return "pong"


if __name__ == "__main__":
    mcp.run()
