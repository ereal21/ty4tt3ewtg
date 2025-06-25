import importlib
import subprocess
import sys

REQUIRED_MODULES = [
    "flask",
]


def ensure_requirements() -> None:
    missing = []
    for module in REQUIRED_MODULES:
        try:
            importlib.import_module(module)
        except Exception:
            missing.append(module)
    if missing:
        subprocess.check_call([
            sys.executable,
            "-m",
            "pip",
            "install",
            "-r",
            "requirements.txt",
        ])


if __name__ == "__main__":
    ensure_requirements()
    from bot.ipn_server import app

from bot.ipn_server import app

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)
