"""Inicializador multiplataforma: execute com o Python do computador."""
import argparse
import hashlib
import os
from pathlib import Path
import subprocess
import sys
import venv

ROOT = Path(__file__).resolve().parent
ENV = ROOT / ".venv"
PYTHON = ENV / ("Scripts/python.exe" if os.name == "nt" else "bin/python")


def executar(*args):
    subprocess.run([str(PYTHON), *map(str, args)], cwd=ROOT, check=True)


def main():
    parser = argparse.ArgumentParser(description="Prepare e execute o Festival SONORA")
    parser.add_argument("--test", action="store_true", help="executa os testes em um banco temporário")
    parser.add_argument("--port", type=int, default=8000, help="porta do servidor local")
    args = parser.parse_args()
    if not  (1 <= args.port <= 65535):
        parser.error("porta inválida")
    if not ((3, 10) <= sys.version_info[:2] <= (3, 14)):
        raise SystemExit("Use Python 3.10 a 3.14 (recomendado: 3.12 ou 3.13).")
    if not PYTHON.exists():
        print("Criando ambiente virtual em .venv...", flush=True)
        venv.EnvBuilder(with_pip=True).create(ENV)
    requirements = ROOT / "requirements.txt"
    fingerprint = hashlib.sha256(requirements.read_bytes()).hexdigest()
    marker = ENV / ".requirements_hash"
    installed = subprocess.run([str(PYTHON), "-c", "import django, pytest, pytest_django"], cwd=ROOT,
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0
    if not installed or not marker.exists() or marker.read_text() != fingerprint:
        print("Instalando dependências (internet necessária na primeira execução)...", flush=True)
        executar("-m", "pip", "install", "--disable-pip-version-check", "-r", requirements)
        marker.write_text(fingerprint)
    if args.test:
        executar("-m", "pytest")
        return
    print("Preparando o banco SQLite...", flush=True)
    executar("manage.py", "migrate", "--noinput")
    executar("manage.py", "migrate", "--database=legacy", "--noinput")
    executar("manage.py", "seed_demo")
    print(f"\nAbra no navegador: http://127.0.0.1:{args.port}/\nPara encerrar, pressione Ctrl+C.\n", flush=True)
    executar("manage.py", "runserver", f"127.0.0.1:{args.port}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nServidor encerrado.")
    except (OSError, subprocess.CalledProcessError) as exc:
        print(f"\nNão foi possível concluir: {exc}\nConfira a mensagem acima. Se a instalação falhou, verifique a internet e o Python/venv.", file=sys.stderr)
        sys.exit(1)
