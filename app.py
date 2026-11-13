"""Simple calculator web application using Flask."""

from flask import Flask, request
from calculator import Calculator

app = Flask(__name__)

@app.route('/')
def landing():
    """Landing page."""
    return """Welcome to the simple calculator flask application!<br>
    Use the <b>/calculate</b> endpoint with parameters <b>op</b>, <b>arg1</b>, and <b>arg2</b><br> 
    Calculator operations: <b>sum</b>, <b>subtract</b>, <b>multiply</b>, <b>divide</b>.<br>
    Example: /calculate?op=<b>sum</b>&arg1=<b>2</b>&arg2=<b>5</b>"""
@app.route('/calculate')
def calculate():
    """Calculate endpoint."""
    op = request.args.get('op', type=str)
    arg1 = request.args.get('arg1', type=int)
    arg2 = request.args.get('arg2', type=int)

    calc = Calculator(arg1, arg2)
    if op == 'sum':
        result = calc.sum()
        sign = '+'
    elif op == 'subtract':
        result = calc.subtract()
        sign = '-'
    elif op == 'multiply':
        result = calc.multiply()
        sign = '*'
    elif op == 'divide':
        if arg2 == 0:
            return "error: division by zero"
        result = calc.divide()
        sign = '/'
    else:
        return "error: invalid operation"
    return f"{arg1} {sign} {arg2} = {result}"

if __name__ == '__main__':
    app.run(debug=True)
