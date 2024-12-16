from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Path to your CSV file
    formulas_file = 'formulas.xlsx'
    
    # Read the CSV with headers
    df = pd.read_excel(formulas_file)
    
    # Extract column headers and rows
    headers = df.columns.tolist()
    rows = df.to_dict(orient='records')
    
    # Pass headers and rows to the template
    return render_template('index.html', headers=headers, rows=rows)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
