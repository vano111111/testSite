from flask import Flask, render_template, redirect, url_for, session
import sqlite3
import os


app = Flask(__name__)


@app.route('/')
def index():
    return "Hello loshok, what`s up?"


if __name__ == "__main__":
    app.run(debug=True)