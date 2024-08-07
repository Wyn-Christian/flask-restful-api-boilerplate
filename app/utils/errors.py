# app/utils/errors.py

from werkzeug.exceptions import HTTPException, NotFound
from flask_jwt_extended.exceptions import NoAuthorizationError
from sqlalchemy.exc import SQLAlchemyError, IntegrityError, OperationalError
from http_constants.status import HttpStatus


def handle_error(e):
    response = {"error": "Internal Server Error", "message": str(e)}
    return response, HttpStatus.INTERNAL_SERVER_ERROR


def handle_http_error(e):
    response = {"error": e.name, "message": e.description}
    return response, e.code


def handle_not_found_error(e):
    response = {
        "error": "URL Not Found",
        "message": "The requested URL was not found on the server.",
    }
    return response, HttpStatus.NOT_FOUND


def handle_sqlalchemy_error(e):
    response = {
        "error": "Database Error",
        "message": str(e),
    }
    return response, HttpStatus.INTERNAL_SERVER_ERROR


def handle_integrity_error(e):
    response = {
        "error": "Database Integrity Error",
        "message": str(e),
    }
    return response, HttpStatus.BAD_REQUEST


def handle_operational_error(e):
    response = {
        "error": "Database Operational Error",
        "message": str(e),
    }
    return response, HttpStatus.INTERNAL_SERVER_ERROR


def handle_no_auth_error(e):
    response = {
        "error": "No Authorization Error",
        "message": "Missing JWT in cookies or headers!",
    }
    return response, HttpStatus.UNAUTHORIZED


error_handlers = [
    (Exception, handle_error),
    (HTTPException, handle_http_error),
    (NotFound, handle_not_found_error),
    (NoAuthorizationError, handle_no_auth_error),
    (SQLAlchemyError, handle_sqlalchemy_error),
    (IntegrityError, handle_integrity_error),
    (OperationalError, handle_operational_error),
]


def register_error_handlers(app):
    for exc, handler in error_handlers:
        app.register_error_handler(exc, handler)
