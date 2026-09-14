from __future__ import annotations
from dotenv import load_dotenv
from .graph import app

load_dotenv()

if __name__ == "__main__":
    print(app)