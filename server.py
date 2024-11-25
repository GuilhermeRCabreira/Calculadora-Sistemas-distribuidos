from flask import Flask, request, jsonify
import math

app = Flask(__name__)

# Memória para armazenar as variáveis
variables = {"x": 0.0, "y": 0.0, "z": 0.0}

# Operações disponíveis
@app.route('/wscalc/<operation>/<arg1>', methods=['GET'])
@app.route('/wscalc/<operation>/<arg1>/<arg2>', methods=['GET'])
def calculate(operation, arg1, arg2=None):
    try:
        # Converte argumentos
        val1 = resolve_argument(arg1)
        val2 = resolve_argument(arg2) if arg2 else None

        # Processa as operações
        if operation == 'add':
            result = val1 + val2
        elif operation == 'sub':
            result = val1 - val2
        elif operation == 'mul':
            result = val1 * val2
        elif operation == 'div':
            result = val1 / val2
        elif operation == 'pow':
            result = math.pow(val1, val2)
        elif operation == 'sqrt':
            result = math.sqrt(val1)
        elif operation == 'log':
            result = math.log10(val1)
        elif operation == 'ln':
            result = math.log(val1)
        elif operation == 'lg':
            result = math.log2(val1)
        elif operation == 'sin':
            result = math.sin(val1)
        elif operation == 'cos':
            result = math.cos(val1)
        elif operation == 'tan':
            result = math.tan(val1)
        elif operation == 'mod':
            result = abs(val1)
        elif operation == 'fact':
            result = math.factorial(int(val1))
        else:
            return "Operação não suportada", 400

        return jsonify(result=result)

    except Exception as e:
        return str(e), 400


@app.route('/wscalc/var/<var_name>', methods=['GET', 'POST'])
def variable(var_name):
    if request.method == 'POST':
        value = float(request.args.get('value', 0))
        if var_name in variables:
            variables[var_name] = value
            return jsonify(success=True)
        else:
            return "Variável inválida", 400

    if request.method == 'GET':
        if var_name in variables:
            return jsonify(value=variables[var_name])
        else:
            return "Variável não encontrada", 404

# Função para resolver os argumentos
def resolve_argument(arg):
    if arg in variables:
        return variables[arg]
    elif arg == "pi":
        return math.pi
    elif arg == "euler":
        return math.e
    else:
        return float(arg)

if __name__ == '__main__':
    app.run(port=8080)
