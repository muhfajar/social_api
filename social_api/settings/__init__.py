from .base import *
from .modules import *

try:
    from .private import *
except ImportError:
    import random
    raise ImportError("""
    Please create private.py file
    with contain configuration for 
    ====================================
    SECRET_KEY = '{}'
    ALLOWED_HOSTS = []
    ====================================
    """.format(''.join([random.SystemRandom().
                       choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])))

try:
    from .production import *
except ImportError:
    pass
