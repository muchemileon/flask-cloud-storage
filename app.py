from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Simulating a file storage system
files = []

@app.route('/')
def index():
    return render_template('index.html', files=files)

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        file_name = request.form['file_name']
        if file_name:
            files.append(file_name)
    return redirect(url_for('index'))

@app.route('/update/<filename>', methods=['GET', 'POST'])
def update(filename):
    if request.method == 'POST':
        new_name = request.form['new_name']
        if new_name:
            index = files.index(filename)
            files[index] = new_name
            return redirect(url_for('index'))
    return render_template('update.html', filename=filename)

@app.route('/delete/<filename>')
def delete(filename):
    if filename in files:
        files.remove(filename)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
