from werkzeug.exceptions import HTTPException


class InternalServerError(HTTPException):
    pass


class SchemaValidationError(HTTPException):
    pass


class EventAlreadyExistsError(HTTPException):
    pass


class UpdatingEventError(HTTPException):
    pass


class DeletingEventError(HTTPException):
    pass


class EventNotExistsError(HTTPException):
    pass


class EmailAlreadyExistsError(HTTPException):
    pass


class UnauthorizedError(HTTPException):
    pass


class BadTokenError(HTTPException):
    pass


class EmailDoesnotExistsError(HTTPException):
    pass


class ExpiredTokenError(HTTPException):
    pass


errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
    "SchemaValidationError": {
        "message": "Request is missing required fields",
        "status": 400
    },
    "EventAlreadyExistsError": {
        "message": "Event with given name already exists",
        "status": 400
    },
    "UpdatingEventError": {
        "message": "Updating event added by other is forbidden",
        "status": 403
    },
    "DeletingEventError": {
        "message": "Deleting event added by other is forbidden",
        "status": 403
    },
    "EventNotExistsError": {
        "message": "Event with given id doesn't exists",
        "status": 400
    },
    "EmailAlreadyExistsError": {
        "message": "User with given email address already exists",
        "status": 400
    },
    "UnauthorizedError": {
        "message": "Invalid username or password",
        "status": 401
    },
    "BadTokenError": {
        "message": "Invalid Token",
        "status": 403
    },
    "EmailDoesnotExistsError": {
        "message": "Coundn't find the user with given email address",
        "status": 400
    },
    "ExpiredTokenError": {
        "message": "Expired Token",
        "status": 400
    }
}
