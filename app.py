from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # Load formulas from the file
    formulas_file = 'formulas.csv'
    df = pd.read_csv(formulas_file)
    
    # Convert the DataFrame to a dictionary for rendering
    formulas = df.to_dict(orient='records')
    return render_template('index.html', formulas=formulas)

if __name__ == '__main__':
    app.run(debug=True)
