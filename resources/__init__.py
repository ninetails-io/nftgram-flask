from flask_caching import Cache
import tempfile

tokens = Cache(config={"CACHE_TYPE": "filesystem", 'CACHE_DIR': tempfile.gettempdir()})