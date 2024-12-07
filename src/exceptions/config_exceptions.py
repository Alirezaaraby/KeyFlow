class ConfigException(Exception):
    def __init__(self, message: str) -> None:
        super().__init__("Config Exception: %s" % message)


class ConfigImportException(ConfigException):
    def __init__(self, message: str) -> None:
        super().__init__("Config Import Exception: %s" % message)

class ConfigGenerateException(ConfigException):
    def __init__(self, message: str) -> None:
        super().__init__("Config Generate Exception: %s" % message)

class ConfigNotFoundException(ConfigException):
    def __init__(self) -> None:
        super().__init__("Config File Not Found")

class ConfigLoadException(ConfigException):
    def __init__(self, message: str) -> None:
        super().__init__("Config Load Exception: %s" % message)

class ConfgiSaveException(ConfigException):
    def __init__(self, message: str) -> None:
        super().__init__("Config Save Exception: %s" % message)
        
class ConfigKeyException(ConfigException):
    def __init__(self, message: str) -> None:
        super().__init__("Config Key Exception: %s" % message)

class ConfigTypeException(ConfigException):
    def __init__(self, message: str) -> None:
        super().__init__("Config Type Exception: %s" % message)

class ConfigOptionException(ConfigException):
    def __init__(self, message: str) -> None:
        super().__init__("Config Option Exception: %s" % message)
    
class ConfigValidatorException(ConfigException):
    def __init__(self, message: str) -> None:
        super().__init__("Config Validator Exception: %s" % message)