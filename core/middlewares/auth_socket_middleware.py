from channels.db import database_sync_to_async
from channels.middleware import BaseMiddleware
from apps.user.models import UserModel
from core.dataclass import UserDataClass

@database_sync_to_async
def get_user(device):
    user:UserDataClass = UserModel.objects.filter(username=device).first()
    if not user:
        return None
    return user


class AuthSocketMiddleware(BaseMiddleware):
    async def __call__(self, scope, receive, send):
        device = dict(
            [item.split('=') for item in scope['query_string'].decode('utf-8').split('&') if item]
        ).get('device', None)
        scope['user'] = await get_user(device) if device else None
        return await super().__call__(scope, receive, send)



