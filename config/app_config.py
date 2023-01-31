import os
import logging
import warnings

from config.definitions import ROOT_DIR

from dotenv import load_dotenv


# SETTINGS
APP_NAME = "pybulldozer"


# ENV
def load_env():
    # Load env if not already loaded and set the ENV variable
    if (os.environ.get("ENV") == None):
        load_dotenv(dotenv_path=os.path.join(ROOT_DIR, 'config', 'conf', '.env'))
load_env()
valid_envs = ['dev', 'test', 'acceptation', 'release']
ENV = os.getenv(key="ENV")
if (ENV is None):
    warnings.warn(f"Provided an invalid ENV in .env: '{ENV}'; defaulting to 'dev'. Valid environments: {valid_envs}")
    ENV = 'dev'
else:
    ENV = ENV.lower()
APP_NAME_ENV = f"{APP_NAME}{' (' + ENV + ')' if (ENV != 'release') else ''}"

# Log Levels
logleveldict:dict = {
    "debug": logging.DEBUG,
    "info": logging.INFO,
    "warning": logging.WARNING,
    "error": logging.ERROR,
    "critical": logging.CRITICAL
}
LOGLEVEL_CONSOLE = logleveldict.get(os.getenv(key="LOGLEVEL_CONSOLE", default="debug").lower())
LOGLEVEL_FILE = logleveldict.get(os.getenv(key="LOGLEVEL_FILE", default="debug").lower())
LOGLEVEL_HTTP = logleveldict.get(os.getenv(key="LOGLEVEL_HTTP", default="debug").lower())


