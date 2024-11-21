from pathlib import Path

import qrcode


_HERE = Path(__file__).parent


def main():
    base_url = "https://irmo322.github.io/avent-maman-2024/"

    for p in _HERE.parent.glob("jour*.html"):
        full_url = base_url + p.name
        img = qrcode.make(full_url)
        img.save(_HERE.parent / "qr_codes" / ("qr_code_" + p.stem + ".png"))


if __name__ == "__main__":
    main()
