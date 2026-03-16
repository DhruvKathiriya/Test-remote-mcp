import random
from fastmcp import FastMCP
import json
mcp = FastMCP(name="Test Remote Server")

@mcp.tool
def roll_dice(n_dice:int = 1) -> list[int]:
    """Roll number of dice"""
    return [random.randint(1,6) for _ in range(n_dice)]

@mcp.tool
def add_numbers(a:float, b:float) -> float:
    """Add two number"""
    return a+b

@mcp.tool
def random_number(min_val: int=1, max_val : int=100) -> int:
    """Generate random number within a range"""
    return random.randint(min_val,max_val)

@mcp.resource("info://server")
def server_info()-> str:
    """get information about server"""
    info = {
        "name":"test server",
        "version":"1.0.0",
        "description":"A MCP server for testing",
        "tools": ["add_number","random_number","roll_dice"],
        "author":"Dhruv Kathiriya"
    }
    return json.dump(info,indent=2)



if __name__ == "__main__":
    mcp.run(transport="http",host="0.0.0.0",port=8000)
