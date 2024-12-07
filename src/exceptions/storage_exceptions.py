class StorageException(Exception):
    def __init__(self, message: str) -> None:
        super().__init__("Storage Exception: %s" % message)


class StoragePermissionException(StorageException):
    def __init__(self, message: str) -> None:
        super().__init__("Storage Permission Exception: %s" % message)


class StorageNotFoundException(StorageException):
    def __init__(self, message: str) -> None:
        super().__init__("Storage Not Found Exception: %s" % message)


class StorageParserException(StorageException):
    def __init__(self, message: str) -> None:
        super().__init__("Storage Parser Exception: %s" % message)


class StorageOSException(StorageException):
    def __init__(self, message: str) -> None:
        super().__init__("Storage OS Exception: %s" % message)


class StorageIOErrorException(StorageException):
    def __init__(self, message: str) -> None:
        super().__init__("Storage IO Error Exception: %s" % message)
