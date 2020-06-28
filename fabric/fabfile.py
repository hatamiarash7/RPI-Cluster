from __future__ import with_statement
from fabric.api import env, parallel, sudo
import os
from dotenv import load_dotenv

load_dotenv('.env')

env.hosts = [
    'pi@192.168.1.50',
    'pi@192.168.1.51',
    'pi@192.168.1.52',
    'pi@192.168.1.53'
]

env.password = os.getenv("SSH_PASS")


@parallel
def cmd(command='hostname'):
    sudo(command)
