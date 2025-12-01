from typing import Type
from core.exceptions.jwt_exception import JwtException
from core.enums.action_token_enum import ActionTokenEnum
from rest_framework_simplejwt.tokens import BlacklistMixin, Token

from django.contrib.auth import get_user_model

from rest_framework.generics import get_object_or_404

UserModel = get_user_model()


class ActionToken(BlacklistMixin, Token):
    pass

class SocketToken(ActionToken):
    token_type = ActionTokenEnum.SOCKET.token_type
    lifetime = ActionTokenEnum.SOCKET.life_time


class JWTService:
    @staticmethod
    def create_token(user, token_class):
        return token_class.for_user(user)

    @staticmethod
    def validate_token(token, token_class):
        try:
            token_res = token_class(token)
            token_res.check_blacklist()
        except Exception:
            raise JwtException

        token_res.blacklist()
        user_id = token_res.payload.get('user_id')
        return get_object_or_404(UserModel, pk=user_id)
