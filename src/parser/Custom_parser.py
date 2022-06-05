import argparse
import sys

class Custom(argparse.ArgumentParser):
    def error(self, message: str):
        sys.stderr.write(f"[X_X] error: {message} \n")
        self.print_help()
        sys.exit(2)

