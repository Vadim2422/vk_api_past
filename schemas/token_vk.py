from pydantic import BaseModel


class Token(BaseModel):
    token: str
    user_id: int
