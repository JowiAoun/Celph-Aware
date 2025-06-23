GOOD_BAD_UGLY_SCHEMA = {
    "type": "object",
    "required": ["good", "bad", "ugly", "positiveness"],
    "properties": {
        "good": {
            "type": "array",
            "minItems": 0,
            "maxItems": 3,
            "items": {"type": "string"}
        },
        "bad": {
            "type": "array",
            "minItems": 0,
            "maxItems": 3,
            "items": {"type": "string"}
        },
        "ugly": {
            "type": "array",
            "minItems": 0,
            "maxItems": 3,
            "items": {"type": "string"}
        },
        "positiveness": {
            "type": "integer",
            "minimum": 1,
            "maximum": 100
        }
    },
    "additionalProperties": False
}