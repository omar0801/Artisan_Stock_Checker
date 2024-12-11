from configparser import ConfigParser
import time
import hashlib
import traceback
import error_logger
import os
from dotenv import load_dotenv

DEFAULT_CONFIG_FILE = "config.cfg"

load_dotenv()

def config_info(config_file=DEFAULT_CONFIG_FILE):
    config = ConfigParser()
    config.read(config_file)
    return config


def backup_bad_config(config_file=DEFAULT_CONFIG_FILE):
    try:
        with open(config_file, "rb") as hashfile:
            bytes = hashfile.read()
            hash_value = hashlib.md5(bytes).hexdigest()
        backup_file = config_file + ".bak" + hash_value
        with open(config_file, "r") as conf, open(backup_file, "w") as backup:
            for line in conf:
                backup.write(line)
    except Exception:
        pass


def default_config(config_file=DEFAULT_CONFIG_FILE):
    backup_bad_config(config_file)

    defaults = ConfigParser()
    defaults["stock"] = {
        "stock_delay": os.getenv("STOCK_DELAY", ""),
        "cart_delay": os.getenv("CART_DELAY", ""),
        "batch_delay": os.getenv("BATCH_DELAY", ""),
        "request_fail_delay": os.getenv("REQUEST_FAIL_DELAY", ""),
    }

    defaults["webhook"] = {
        "fallback_url": os.getenv("FALLBACK_URL", ""),
        "S_url": os.getenv("S_URL", ""),
        "M_url": os.getenv("M_URL", ""),
        "L_url": os.getenv("L_URL", ""),
        "XL_url": os.getenv("XL_URL", ""),
        "XXL_url": os.getenv("XXL_URL", ""),
        "content": os.getenv(
            "WEBHOOK_CONTENT",
            "{Role Ping} In Stock!\\nModel: {Model}, Hardness: {Hardness}, Size: {Size}, Color: {Color}\\nLink: {Link}"
        ),
        "uptime_url": os.getenv("UPTIME_URL", ""),
    }

    defaults["webhook_role_pings"] = {
        "role_CS_Zero": os.getenv("ROLE_CS_ZERO", "<@&>"),
        "role_CS_Raiden": os.getenv("ROLE_CS_RAIDEN", "<@&>"),
        "role_FX_Hayate_Otsu": os.getenv("ROLE_FX_HAYATE_OTSU", "<@&>"),
        "role_FX_Hayate_Kou": os.getenv("ROLE_FX_HAYATE_KOU", "<@&>"),
        "role_FX_Hien": os.getenv("ROLE_FX_HIEN", "<@&>"),
        "role_FX_Zero": os.getenv("ROLE_FX_ZERO", "<@&>"),
        "role_FX_Raiden": os.getenv("ROLE_FX_RAIDEN", "<@&>"),
        "role_FX_Shidenkai": os.getenv("ROLE_FX_SHIDENKAI", "<@&>"),
        "role_FX_TYPE99": os.getenv("ROLE_FX_TYPE99", "<@&>"),
        "role_FX_KEY83": os.getenv("ROLE_FX_KEY83", "<@&>"),
    }

    with open(config_file, "w") as conf:
        defaults.write(conf)


def read(config_file, section, name):
    function_success = False
    while not function_success:
        try:
            config = config_info(config_file)
            return config.get(section, name)
            function_success = True

        except Exception:
            error_logger.error_log(
                "Config corrupted. Reverting to default:", traceback.format_exc()
            )
            default_config(config_file)
            time.sleep(1)


def write(config_file, section, name, value):
    function_success = False
    while not function_success:
        try:
            config = config_info(config_file)
            if not config.has_section(section):
                config.add_section(section)
            config[section][name] = value
            with open(config_file, "w") as conf:
                config.write(conf)
            function_success = True
        except Exception:
            error_logger.error_log(
                "Config corrupted. Reverting to default:", traceback.format_exc()
            )
            default_config(config_file)
            time.sleep(1)
