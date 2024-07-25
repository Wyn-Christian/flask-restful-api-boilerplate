import os
from datetime import timedelta


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess-eme"

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///app.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_COOKIE_SECURE = False
    JWT_TOKEN_LOCATION = ["cookies", "headers"]
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY") or "super-secret"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=8)
    JWT_COOKIE_NAME = "access_token_cookie"
    JWT_REFRESH_TOKEN_COOKIE_NAME = "refresh_token_cookie"
    JWT_COOKIE_CSRF_PROTECT = False