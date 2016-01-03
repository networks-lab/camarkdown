class AddingException(Exception):
    pass

class CodeParserException(Exception):
    pass

class UninitializedDirectory(Exception):
    pass

class ProjectException(Exception):
    pass

class ProjectTypeError(ProjectException):
    pass

class ProjectDirectoryMissing(ProjectException):
    pass

class ProjectMissingFiles(ProjectException):
    pass

class ProjectFileError(ProjectException):
    pass

class ProjectCodeError(ProjectException):
    pass

class CodeBookException(Exception):
    pass

class TestError(Exception):
    pass
