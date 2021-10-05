"""Program entrypoint."""
import argparse
from csq.app import App


def run() -> None:
    app = App()
    app.run()

if __name__ == '__main__':
    """
        Entry point of the program from console.
    """
    parser = argparse.ArgumentParser(
        description='Autocomplete functionality for Contestsquare'
    )

    args = parser.parse_args()
    run()
