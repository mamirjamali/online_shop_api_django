from distutils.debug import DEBUG
import os
from .common import *


DEBUG = False

SECERT_KEY = os.environ['SECRET_KEY']


ALLOWED_HOSTS = []