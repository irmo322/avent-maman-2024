from pathlib import Path


_HERE = Path(__file__).parent


def main():
    base_url = "https://irmo322.github.io/avent-maman-2024/"

    for p in _HERE.parent.glob("jour*.html"):
        full_url = base_url + p.name
        print("- " + full_url)


if __name__ == "__main__":
    main()
