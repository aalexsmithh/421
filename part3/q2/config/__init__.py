import json


def get_config(fname):
    config = None
    with open(fname, 'r') as f:
        config = json.load(f)

    valid, err = verify_db_config(config)
    if not valid:
        raise KeyError(err)

    return config


def verify_db_config(config):
    if 'database' not in config:
        return False, "Database config not found"

    db_config = config['database']

    if 'database' not in db_config or db_config == '':
        return False, "Database name not in config"

    if 'hostname' not in db_config or db_config == '':
        return False, "Database hostname not in config"

    if 'password' not in db_config or db_config == '':
        return False, "Database password not in config"

    if 'username' not in db_config or db_config == '':
        return False, "Database username not in config"

    return True, None
