from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Load formulas from the file
    formulas_file = 'formulas.csv'
    df = pd.read_csv(formulas_file)
    
    # Convert the DataFrame to a dictionary for rendering
    formulas = df.to_dict(orient='records')
    return render_template('index.html', formulas=formulas)

# Main entry point
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
