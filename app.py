"""Aplicación web Python para publicar la página de Mi Koalita."""
import os
from pathlib import Path

from flask import Flask, abort, send_from_directory


BASE_DIR = Path(__file__).resolve().parent
PHOTOS_DIR = BASE_DIR / "fotos"
app = Flask(__name__)


@app.get("/")
def home():
    return send_from_directory(BASE_DIR, "index.html")


@app.get("/styles.css")
def styles():
    return send_from_directory(BASE_DIR, "styles.css")


@app.get("/fotos/<path:filename>")
def photo(filename):
    if Path(filename).name != filename:
        abort(404)
    return send_from_directory(PHOTOS_DIR, filename)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    app.run(host="0.0.0.0", port=port)
