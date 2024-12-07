from core.schema import CONFIG_SCHEMA, CONFIG_VALIDATORS
from exceptions.config_exceptions import ConfgiSaveException, ConfigException, ConfigGenerateException, ConfigKeyException, ConfigLoadException, ConfigNotFoundException, ConfigOptionException, ConfigTypeException, ConfigValidatorException
from pathlib import Path
import yaml
import os

class Config:
    config: dict
    path: Path

    def __init__(self, path: Path) -> None:
        self.path = path
        self.config = {}
        try:
            self.load()
        except Exception as e:
            raise ConfigException(f"Failed to load config: {e}")

    def generate_config(self, schema: dict):
        try:
            for key, value in schema.items():
                self.config[key] = value.get("default")
            self.save()
        except Exception as e:
            raise ConfigGenerateException(e)

    def exist(self) -> bool:
        return self.path.is_file()

    def load(self):
        try:
            if not self.exist():
                self.generate_config(CONFIG_SCHEMA)
            with open(self.path, 'r') as file:
                self.config = yaml.safe_load(file) or {}
            self.validate()
        except FileNotFoundError:
            raise ConfigNotFoundException()
        except Exception as e:
            raise ConfigLoadException(e)

    def save(self):

        try:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.path, 'w') as file:
                yaml.dump(self.config, file, default_flow_style=False)
        except Exception as e:
            raise ConfgiSaveException(f"Failed to save config: {e}")

    def update(self):
        self.save()

    def validate(self):
        for key, schema in CONFIG_SCHEMA.items():
            if "required" in schema and schema["required"] and key not in self.config:
                raise ConfigKeyException(f"Required key '{key}' is missing in the config.")
                        
            value = self.config.get(key, None)
            
            if not isinstance(value, schema["type"]):
                raise ConfigTypeException(f"Type mismatch for key '{key}': Expected {schema['type']}, got {type(value)}.")

            if "options" in schema and value not in schema["options"]:
                raise ConfigOptionException(f"Invalid option for key '{key}': '{value}' is not in {schema['options']}.")

            if "validator" in schema:
                validator_func = CONFIG_VALIDATORS.get(schema["validator"])
                if validator_func and not validator_func(value):
                    raise ConfigValidatorException(f"Validation failed for key '{key}'.")

            if isinstance(value, dict) and "keys" in schema:
                for sub_key, sub_schema in schema["keys"].items():
                    sub_value = value.get(sub_key, None)
                    if sub_key not in value:
                        raise ConfigKeyException(f"Subkey '{sub_key}' is missing under '{key}'.")
                    else:
                        if not isinstance(sub_value, sub_schema["type"]):
                            raise ConfigTypeException(f"Type mismatch for subkey '{sub_key}' under '{key}': Expected {sub_schema['type']}, got {type(sub_value)}.")
                        
                        if "options" in sub_schema and sub_value not in sub_schema["options"]:
                            raise ConfigOptionException(f"Invalid option for subkey '{sub_key}' under '{key}': '{sub_value}' is not in {sub_schema['options']}.")

                        if "validator" in sub_schema:
                            validator_func = CONFIG_VALIDATORS.get(sub_schema["validator"])
                            if validator_func and not validator_func(sub_value):
                                raise ConfigValidatorException(f"Validation failed for subkey '{sub_key}' under '{key}'.")
