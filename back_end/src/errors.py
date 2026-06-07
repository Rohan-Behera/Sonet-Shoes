



class SonetShoesException(Exception):
    """This is the Base class for all exceptions"""
    pass

class InvalidToken(SonetShoesException):
    """ User has provided and invalid token """
    pass

class RevokedToken(SonetShoesException):
    """ User has provided a token that has been revoked"""
    pass

class AccessTokenRequired(SonetShoesException):
    """User has provided a refresh token when an access token is needed"""
    pass

class RefreshTokenRequired(SonetShoesException):
    """User has provided an access token when a refresh token is needed"""
    pass

class UserAlreadyExists(SonetShoesException):
    """User has provided an email for a user who exists during sign up."""
    pass

class InvalidCredentials(SonetShoesException):
    """User has provided wrong email or password during log in."""

    pass


class InsufficientPermission(SonetShoesException):
    """User does not have the neccessary permissions to perform an action."""

    pass


class BookNotFound(SonetShoesException):
    """Book Not found"""

    pass


class TagNotFound(SonetShoesException):
    """Tag Not found"""

    pass


class TagAlreadyExists(SonetShoesException):
    """Tag already exists"""

    pass


class UserNotFound(SonetShoesException):
    """User Not found"""

    pass


class AccountNotVerified(Exception):
    """Account not yet verified"""
    pass