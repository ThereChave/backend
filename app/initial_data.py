#!/usr/bin/env python3
from getpass import getpass

from app.db.session import get_db
from app.db.session import SessionLocal
from app.db.crud.user import create_user
from app.db.schemas.user import UserCreate


def init() -> None:
    db = SessionLocal()
    email = input("请输入管理员邮箱：")
    password = getpass("请输入密码：")
    repeated_password = getpass("请再次输入密码：")
    if password != repeated_password:
        print("两次密码不一致！")
        return

    create_user(
        db,
        UserCreate(
            email=email,
            password=password,
            is_active=True,
            is_superuser=True,
        ),
    )


if __name__ == "__main__":
    print("Creating superuser")
    init()
    print("Superuser created")
