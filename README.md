# Arma3Manager

This repository contains a simple Python based manager for the Arma 3 dedicated server on Ubuntu. It uses `steamcmd` to install or update the server and to download Workshop mods.

## Prerequisites

- Python 3
- `steamcmd` installed and available in your `PATH`
- Install Python dependencies with `pip install -r requirements.txt`
- (Optional) `STEAM_USERNAME` and `STEAM_PASSWORD` environment variables for downloading mods from the Workshop

## Setup

Run the `setup.sh` script to install SteamCMD and the Python requirements. The script requires sudo privileges on Debian/Ubuntu based systems:

```bash
./setup.sh
```

## Configuration

Modify `config.yaml` to match your setup. `server_config_path` will default to
`<server_path>/server.cfg` if not explicitly set:

```yaml
server_path: /opt/arma3            # Where to install the server
server_config_path: /opt/arma3/server.cfg
server_config: |
  hostname = "My Arma 3 Server";
  password = "";
  maxPlayers = 32;
mods:
  - 450814997
  - 463939057
```

`server_config` can contain the contents of your `server.cfg` file. Add any mod Workshop IDs under `mods`.

## Usage

Run the manager script with one of the supported actions:

```bash
python3 arma3_manager.py update-server      # install or update the server
python3 arma3_manager.py download-mods     # download mods listed in config.yaml
python3 arma3_manager.py apply-config      # write server.cfg as configured
python3 arma3_manager.py all               # perform all actions above
```

To download mods you must set the `STEAM_USERNAME` and `STEAM_PASSWORD` environment variables to a Steam account that owns Arma 3 and is subscribed to the desired mods.

You can automate updates by running the script periodically with `cron` or a systemd timer.
