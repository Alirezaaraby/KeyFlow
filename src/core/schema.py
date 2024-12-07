from pathlib import Path

CONFIG_VALIDATORS = {
    "path": lambda x: Path(x).exists(),
}

CONFIG_SCHEMA = {
    "storage": {
        "type": str,
        "options": ["tinydb", "json", "sqlite"],
        "default": "tinydb",
        "required": True,
    },
    "storage_connection": {
        "type": dict,
        "required": True,
        "default": {
            "path": ".",
        },
        "keys": {
            "path": {
                "type": str,
                "required": True,
                "default": ".",
            }
        }
    }
}
