
from flask import Flask, render_template, request, redirect, url_for
import json
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dropdown', methods=['POST'])
def dropdown():
    selected_file = request.form.get('file_name')
    generate_csv(selected_file)
    return redirect(url_for('home'))

@app.route('/generate_csv')
def generate_csv():
    files = ['file1.json', 'file2.json', 'file3.json']
    for file in files:
        with open(file) as f:
            data = json.load(f)
        df = pd.DataFrame(data)
        df.to_csv(file.replace('.json', '.csv'), index=False)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
