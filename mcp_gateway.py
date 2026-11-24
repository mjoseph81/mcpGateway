from fastmcp.server import create_proxy

BACKEND_SERVERS = {
    "mcpServers": {
        "mattcoin": {
            "command": "/home/matt/python/mattCoin/.venv/bin/python",
            "args": ["/home/matt/python/mattCoin/mattcoin_mcp.py"],
        },
        "dice": {
            "command": "/home/matt/python/mcpGateway/.venv/bin/python",
            "args": ["/home/matt/python/diceRoller/dice_mcp.py"],
        },
    }
}

gateway = create_proxy(BACKEND_SERVERS, name="MattUnifiedGateway")

if __name__ == "__main__":
    gateway.run(show_banner=False)
