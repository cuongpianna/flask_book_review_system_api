from flask import request

from flask_restful import Resource, marshal_with
from flask_marshmallow import Schema

from app import ma,db
from app.models.User import  User

class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
        fields = ('id','username','email','address','avartar')

userschema = UserSchema(many=True)
userschema = UserSchema()

class UserResource(Resource):
    def get(self,id=None):
        #id = request.args.get('id')
        if id:
            user = User.query.get(id)
            return userschema.dump(user)
        return {'msg':'user does not exist'}

    def post(self,id=None):
        #json_data = request.get_json(force=True)
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user = User(username=username,email=email)
        db.session.add(user)
        db.session.commit()
        user.set_password(password)
        db.session.commit()
        return {'msg': 'ok'}




