class UserNotFoundException(Exception):

    def __init__(self, value='User not found.'):
        self.value = value

    def __str__(self):
        return repr(self.value)

class PasswordTooShortException(Exception):

    def __init__(self, value='Password too short.'):
        self.value = value

    def __str__(self):
        return repr(self.value)

class UserAlreadyExistsException(Exception):

    def __init__(self, value='Could not upload file.'):
        self.value = value

    def __str__(self):
        return repr(self.value)


class PostNotFoundException(Exception):

    def __init__(self, value='Post not found.'):
        self.value = value

    def __str__(self):
        return repr(self.value)

class InvalidUserException(Exception):

    def __init__(self, value='User not valid.'):
        self.value = value

    def __str__(self):
        return repr(self.value)


class InvalidTokenException(Exception):

    def __init__(self, value='External token not valid.'):
        self.value = value

    def __str__(self):
        return repr(self.value)

class InvalidTypeException(Exception):

    def __init__(self, value='Invalid URL.'):
        self.value = value

    def __str__(self):
        return repr(self.value)


class PasswordMismatchException(Exception):

    def __init__(self, value='Credentials not matched.'):
        self.value = value

    def __str__(self):
        return repr(self.value)


class NoPermissionException(Exception):

    def __init__(self, value='Credentials not matched.'):
        self.value = value

    def __str__(self):
        return repr(self.value)

class UnameUnavailableException(Exception):

    def __init__(self, value='Username Unavailable'):
        self.value = value

    def __str__(self):
        return repr(self.value)

class ObjectNotFoundException(Exception):

    def __init__(self, value='Object not found'):
        self.value = value

    def __str__(self):
        return repr(self.value)

class ObjectAlreadyExists(Exception):

    def __init__(self, value='Cant create because already exists'):
        self.value = value

    def __str__(self):
        return repr(self.value)