"""
MCP Server for genpark-json-schema-regex-grammar-constrainer-skill
Standard JSON-RPC 2.0 protocol over stdio.
"""

import sys
import json
from client import JSONSchemaGrammarCompilerClient

client = JSONSchemaGrammarCompilerClient()

def handle_request(req):
    req_id = req.get("id")
    method = req.get("method")
    params = req.get("params", {})

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "compile_schema_to_gbnf",
                        "description": "Compile JSON Schema to GBNF grammar.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "schema": {"type": "object"}
                            },
                            "required": ["schema"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        tool_name = params.get("name")
        args = params.get("arguments", {})
        if tool_name == "compile_schema_to_gbnf":
            res = client.compile_schema_to_gbnf(args.get("schema", {}))
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": res}]}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_request(req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": str(e)}}
            sys.stdout.write(json.dumps(err) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
