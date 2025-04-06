class BaseUrlNotSetException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class BucketNameNotSetException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class BucketDoesNotExist(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class PostFileError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class BucketIdNotSetException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class FileDownloadError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class FileOperationError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
class IdentifierNotSetException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class PatchRequestFailedException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class ItemNotFoundException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)