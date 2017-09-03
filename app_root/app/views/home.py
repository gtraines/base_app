from flask import Flask


@app.route('/')
def index():
    return '<h1>Return value</h1>'
