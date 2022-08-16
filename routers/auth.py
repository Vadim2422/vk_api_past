from fastapi import status, HTTPException, Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from database.db import get_db
from database.user import get_user_by_email, create_user, get_user_by_username
from schemas.token import UserAuth, TokenSchema
from schemas.user import UserOut, User

from uuid import uuid4
from auth.deps import get_current_user
from auth.utils import get_hashed_password, create_access_token, verify_password, create_refresh_token
from schemas.user import UserCreate

router = APIRouter(tags=["auth"])


@router.post('/signup', summary="Create new user", response_model=UserOut)
def create(user: UserCreate, db: Session = Depends(get_db)):
    db_user: User = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=db_user)


@router.post('/login', summary="Create access and refresh tokens for user", response_model=TokenSchema)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    db_user1 = get_user_by_email(db, email=form_data.username)
    db_user2 = get_user_by_username(db, username=form_data.username)
    if db_user1 is None and db_user2 is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )
    if db_user1 is not None:
        db_user = db_user1
    if db_user2 is not None:
        db_user = db_user2

    hashed_pass = db_user['password']
    if not verify_password(form_data.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )

    return {
        "access_token": create_access_token(db_user['email']),
        "refresh_token": create_refresh_token(db_user['email']),
    }


@router.get('/me', summary='Get details of currently logged in user', response_model=UserOut)
async def get_me(user: UserOut = Depends(get_current_user)):
    return user
