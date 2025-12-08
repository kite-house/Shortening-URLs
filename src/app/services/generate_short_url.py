import random
import string
from dataclasses import dataclass
from sqlalchemy.exc import NoResultFound

from db.crud import get_url

@dataclass
class UrlLength:
    MAX_LENGTH: int = 9
    MIN_LENGTH: int = 5

    @classmethod
    def get(cls) -> int:
        return random.randint(cls.MIN_LENGTH, cls.MAX_LENGTH)

def ValidOutputUrl(func):
    async def wrapper(*args, **kwargs):
        url = await func(*args, **kwargs)
        try:
            await get_url(slug = url)
        except NoResultFound:
            return url
        return await wrapper(*args, **kwargs)
    return wrapper


@ValidOutputUrl
async def create_url(length: int = None) -> str: # Url
    if not length:
        length = UrlLength.get()

    return "".join(random.choices(string.ascii_letters + string.digits, k=length))