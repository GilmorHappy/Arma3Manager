#!/usr/bin/env bash
set -e

# Ensure multiverse repository is enabled and i386 architecture is available
sudo apt-get update
sudo apt-get install -y software-properties-common
sudo dpkg --add-architecture i386
sudo add-apt-repository -y multiverse
sudo apt-get update

# Install required packages including steamcmd and Python
sudo apt-get install -y python3 python3-full python3-venv python3-pip \
    steamcmd lib32gcc-s1

# Create an isolated Python virtual environment to avoid the
# "externally-managed-environment" error when installing packages
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
deactivate

cat <<'EOF'
If pip refuses to install packages due to the "externally-managed-environment"
policy on Debian-based systems, you can:

1. Install packages via apt, e.g. sudo apt install python3-xyz
2. Use a virtual environment:
     python3 -m venv /path/to/venv
     /path/to/venv/bin/pip install <package>
3. Use pipx for command-line tools:
     pipx install <package>

You may override the restriction with
    pip install --break-system-packages <package>
but this is not recommended as it can conflict with system packages.
EOF

echo "Installation complete"
