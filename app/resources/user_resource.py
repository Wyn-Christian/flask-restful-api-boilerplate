# app/resources/user_resource.py

from flask_restful import Resource, reqparse, abort
from flask_jwt_extended import jwt_required
from http_constants.status import HttpStatus

from app.models import  User
from app.extensions import db

parser = reqparse.RequestParser()
parser.add_argument("username", type=str, required=True, help="Username is required")
parser.add_argument("email", type=str, required=True, help="Email is required")
parser.add_argument("password", type=str, required=True, help="Password is required")


class UserResource(Resource):
    @jwt_required()
    def get(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return abort(
                HttpStatus.NOT_FOUND,
                error="User Not Found",
                message=f"User ID ({user_id}) not found",
            )

        return user.to_dict(), HttpStatus.OK

    @jwt_required()
    def delete(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return abort(
                HttpStatus.NOT_FOUND,
                error="User Not Found",
                message=f"User ID ({user_id}) not found",
            )

        db.session.delete(user)
        db.session.commit()

        return {}, HttpStatus.NO_CONTENT


class UserListResource(Resource):
    @jwt_required()
    def get(self):
        users = User.query.all()

        return [user.to_dict() for user in users], HttpStatus.OK

    @jwt_required()
    def post(self):
        args = parser.parse_args()
        user = User(username=args["username"], email=args["email"])
        user.set_password(args["password"])

        db.session.add(user)
        db.session.commit()

        return user.to_dict(), HttpStatus.CREATED
