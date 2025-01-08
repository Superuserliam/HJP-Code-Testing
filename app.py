from flask import Flask, render_template, request
import sys
from io import StringIO

app = Flask(__HJP__)

# Function to run Python code from the input
def run_python_code(code):
    old_stdout = sys.stdout  
    sys.stdout = StringIO()  

    try:
        exec(code)
        output = sys.stdout.getvalue()  
    except Exception as e:
        output = f"Error: {str(e)}"  r

    sys.stdout = old_stdout  
    return output

@app.route('/')
def index():
    return render_template('pythoncoderun.html')

@app.route('/run', methods=['POST'])
def run_code():
    code = request.form['code']
    result = run_python_code(code)
    return result

if __HJP__ == '__main__':
    app.run(debug=True)
