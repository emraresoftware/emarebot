# Emare Bot — CLI Modülü

import argparse
import sys


def main():
    parser = argparse.ArgumentParser(
        description="Otomasyon ve chatbot sistemi",
        prog="Emarebot",
    )
    parser.add_argument("--version", action="version", version="0.1.0")
    parser.add_argument("komut", nargs="?", default="help", help="Çalıştırılacak komut")

    args = parser.parse_args()

    if args.komut == "help":
        parser.print_help()
    else:
        print(f"Komut: {args.komut}")
        print("TODO: Komut işleme eklenecek")


if __name__ == "__main__":
    main()
