import os
import re
import typing as t
import ansible_runner
from uuid import uuid4
from collections import defaultdict
from distutils.dir_util import copy_tree
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.db.models.port import Port
from app.db.models.user import User
from app.db.models.server import Server
from app.db.models.port_forward import PortForwardRule
from app.db.crud.port import get_port_with_num
from app.db.crud.server import get_server, get_servers
from app.db.crud.port_usage import create_port_usage, edit_port_usage
from app.db.schemas.port_usage import PortUsageCreate, PortUsageEdit

from . import celery_app
from .utils import prepare_priv_dir, iptables_finished_handler



@celery_app.task()
def traffic_runner():
    servers = get_servers(SessionLocal())
    for server in servers:
        priv_data_dir = prepare_priv_dir(server)
        ansible_runner.run_async(
            private_data_dir=priv_data_dir,
            project_dir="ansible/project",
            playbook="traffic.yml",
            extravars={"host": server.ansible_name},
            finished_callback=iptables_finished_handler(server),
        )
