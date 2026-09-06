"""
Demonstration of genpark-json-schema-regex-grammar-constrainer-skill
"""

from client import JSONSchemaGrammarCompilerClient

def main():
    compiler = JSONSchemaGrammarCompilerClient()

    weather_tool_schema = {
        "type": "object",
        "properties": {
            "location": {"type": "string"},
            "unit": {"type": "string"},
            "forecast_days": {"type": "integer"}
        },
        "required": ["location", "forecast_days"]
    }

    gbnf_output = compiler.compile_schema_to_gbnf(weather_tool_schema)
    print("=== COMPILED GBNF GRAMMAR ===")
    print(gbnf_output)

    # Validate simulated response
    sample_payload = {"location": "San Francisco", "forecast_days": 5, "unit": "celsius"}
    val = compiler.validate_payload_against_schema(sample_payload, weather_tool_schema)
    print("\nValidation check:", val)

if __name__ == "__main__":
    main()
