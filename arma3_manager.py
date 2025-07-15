import argparse
import subprocess
import os
import yaml


def run_command(command):
    print(f"Running: {command}")
    result = subprocess.run(command, shell=True)
    return result.returncode == 0


def update_server(cfg):
    server_path = cfg.get('server_path', '/opt/arma3')
    cmd = f"steamcmd +login anonymous +force_install_dir {server_path} +app_update 233780 validate +quit"
    return run_command(cmd)


def download_mods(cfg):
    mods = cfg.get('mods', [])
    if not mods:
        print('No mods configured')
        return True
    user = os.environ.get('STEAM_USERNAME')
    password = os.environ.get('STEAM_PASSWORD')
    if not user or not password:
        print('STEAM_USERNAME and STEAM_PASSWORD must be set for mod downloads')
        return False
    success = True
    for mod_id in mods:
        cmd = f"steamcmd +login {user} {password} +workshop_download_item 107410 {mod_id} +quit"
        if not run_command(cmd):
            success = False
    return success


def apply_config(cfg):
    server_path = cfg.get('server_path', '/opt/arma3')
    config_file = cfg.get('server_config_path', os.path.join(server_path, 'server.cfg'))
    config_content = cfg.get('server_config')
    if not config_content:
        print('No server_config provided in config')
        return False

    os.makedirs(os.path.dirname(config_file), exist_ok=True)
    with open(config_file, 'w') as f:
        f.write(config_content)
    print(f"Wrote server config to {config_file}")
    return True


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Arma 3 Dedicated Server Manager')
    parser.add_argument('action', choices=['update-server', 'download-mods', 'apply-config', 'all'],
                        help='Action to perform')
    parser.add_argument('-c', '--config', default='config.yaml', help='Path to configuration file')
    args = parser.parse_args()

    with open(args.config) as f:
        cfg = yaml.safe_load(f)

    ok = True
    if args.action in ('update-server', 'all'):
        ok &= update_server(cfg)
    if args.action in ('download-mods', 'all'):
        ok &= download_mods(cfg)
    if args.action in ('apply-config', 'all'):
        ok &= apply_config(cfg)
    if not ok:
        exit(1)
