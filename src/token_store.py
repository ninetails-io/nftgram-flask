from datetime import datetime, timedelta
from flask import jsonify, current_app, request
from flask_caching import Cache
import jwt
from resources import tokens

# TODO: compare jwt, flask_jwt_extended


def jwt_current_token(user_id):
    try:
        token = tokens.get(user_id)
        return token
    except Exception as e:
        print(repr(e))
        return None


def jwt_encode_token(user_id):
    try:
        jwt_payload_headers = {
            "typ": "JWT",
            "alg": "HS256"}
        jwt_payload = {
            "iss": "nftgram",
            "sub": user_id,
            "role": "user" if user_id != "admin" else "admin",
            'exp': datetime.utcnow() + timedelta(days=1),
            'iat': datetime.utcnow(),
        }
        token = jwt.encode(
            jwt_payload,
            current_app.config.get('SECRET_KEY'),
            headers=jwt_payload_headers,
            algorithm='HS256'
        )
        tokens.set(user_id, token)
        return token

    except Exception as e:
        print(e.args)
        raise e


def jwt_decode_token(token):
    # decode the token using SECRET_KEY from config.py
    key = current_app.config.get('SECRET_KEY')

    # exceptions will pass back to caller
    jwt_payload = jwt.decode(token, key, algorithms=['HS256'], issuer='nftgram', verify=True)
    return jwt_payload


def jwt_token_from_request(req):
    try:
        token = None
        auth = req.headers.get('Authorization')
        if auth is None: return None
        if auth.startswith("Bearer "):
            token = auth[7:]
        return token

    except Exception as e:
        print(repr(e))
        return None


def jwt_user_from_request(req):
    try:
        token = jwt_token_from_request(req)
        if token is None: return None
        payload = jwt_decode_token(token)
        user_id = payload["sub"]
        if tokens.get(user_id) != token:
            raise jwt.exceptions.InvalidTokenError
        return user_id

    except Exception as e:
        print(repr(e))
        return None
