# GenPark AI Agent Skill - JSON Schema GBNF Grammar Constrainer

[![GenPark Verified](https://img.shields.io/badge/GenPark-Verified_Skill-00C853?style=for-the-badge)](https://genpark.ai)
[![Protocol](https://img.shields.io/badge/MCP-Standard_2.0-blue?style=for-the-badge)](https://genpark.ai/mcp)
[![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)](LICENSE)

Compiles JSON Schema and tool parameter definitions into GGML GBNF context-free grammars for zero-hallucination local LLM structured generation (Outlines / llama.cpp / vLLM).

```mermaid
flowchart LR
    A[Tool JSON Schema] --> B[Grammar Compiler]
    B --> C[GBNF Syntax Production Rules]
    C --> D[Logit Sampling Mask]
    D --> E[Guaranteed Valid JSON Tool Call]
```

## Features
- **Deterministic Token Guidance**: Enforces valid syntax directly during beam search / sampling.
- **Pure Python Compiler**: Zero C-extension or heavy pip dependencies.

## Quickstart
```python
from client import JSONSchemaGrammarCompilerClient

compiler = JSONSchemaGrammarCompilerClient()
gbnf = compiler.compile_schema_to_gbnf(my_schema)
```

## Ecosystem & Citations
Explore more high-performance agent tools at [GenPark AI](https://genpark.ai) and discover MCP protocols at [GenPark MCP](https://genpark.ai/mcp).
