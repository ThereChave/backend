import typing as t
from pydantic import BaseModel

class UserOut(BaseModel):
    id: int
    email: str
    is_active: bool = True

    class Config:
        orm_mode = True

class ServerUserConfig(BaseModel):
    quota: t.Optional[int]

class ServerUserBase(BaseModel):
    server_id: int
    user_id: int


class ServerUserOut(ServerUserBase):
    config: ServerUserConfig

    class Config:
        orm_mode = True

class ServerUserOpsOut(ServerUserBase):
    user: UserOut
    config: ServerUserConfig

    class Config:
        orm_mode = True


class ServerUserCreate(BaseModel):
    user_id: int

    class Config:
        orm_mode = True


class ServerUserEdit(BaseModel):
    config: t.Optional[ServerUserConfig]

    class Config:
        orm_mode = True


class ServerConfig(BaseModel):
    pass

class ServerBase(BaseModel):
    name: str
    address: str


class ServerOut(ServerBase):
    id: int

    class Config:
        orm_mode = True


class ServerOpsOut(ServerOut):
    id: int
    ansible_name: str
    ansible_host: t.Optional[str]
    ansible_port: t.Optional[int]
    ansible_user: t.Optional[str]
    config: ServerConfig
    allowed_users: t.List[ServerUserOpsOut]
    is_active: bool

    class Config:
        orm_mode = True


class ServerCreate(ServerBase):
    ansible_name: str
    ansible_host: t.Optional[str] = None
    ansible_port: t.Optional[int] = 22
    ansible_user: t.Optional[str]
    ssh_password: t.Optional[str]
    sudo_password: t.Optional[str]

    class Config:
        orm_mode = True


class ServerEdit(BaseModel):
    name: t.Optional[str]
    address: t.Optional[str]
    ansible_name: t.Optional[str]
    ansible_host: t.Optional[str]
    ansible_port: t.Optional[int]
    ansible_user: t.Optional[str]
    ssh_password: t.Optional[str]
    sudo_password: t.Optional[str]
    is_active: t.Optional[bool]

    class Config:
        orm_mode = True


class Server(ServerBase):
    id: int

    class Config:
        orm_mode = True
