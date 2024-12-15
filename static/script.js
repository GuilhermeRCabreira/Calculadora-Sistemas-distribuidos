const display = document.querySelector('.display');
let currentInput = ""; // Para armazenar o número ou operação atual
let operation = null; // Operação escolhida
let arg1 = null; // Primeiro argumento da operação

// Função para atualizar o display
function updateDisplay(value) {
  display.textContent = value;
}

// Função para enviar requisições ao servidor Flask
async function sendRequest(operation, arg1, arg2 = null) {
  try {
    // Construir a URL para a operação
    const url = arg2 
      ? `/wscalc/${operation}/${arg1}/${arg2}` 
      : `/wscalc/${operation}/${arg1}`;
    const response = await fetch(url);
    
    if (!response.ok) {
      throw new Error(await response.text());
    }

    // Processar o resultado
    const data = await response.json();
    updateDisplay(data.result); // Atualizar o display com o resultado
  } catch (error) {
    updateDisplay("Erro");
    console.error("Erro:", error);
  }
}

// Adicionar eventos aos botões
document.querySelectorAll('button').forEach(button => {
  button.addEventListener('click', () => {
    const value = button.textContent;

    if (!isNaN(value) || value === '.') {
      // Números e ponto decimal
      currentInput += value;
      updateDisplay(currentInput);
    } else if (value === "C") {
      // Limpar tudo
      currentInput = "";
      arg1 = null;
      operation = null;
      updateDisplay(0);
    } else if (value === "CE") {
      // Limpar entrada atual
      currentInput = "";
      updateDisplay(0);
    } else if (value === "=") {
      // Calcular
      if (arg1 !== null && operation) {
        sendRequest(operation, arg1, currentInput);
        arg1 = null;
        operation = null;
        currentInput = "";
      }
    } else if (["+", "-", "×", "/", "^"].includes(value)) {
      // Operações binárias
      if (currentInput !== "") {
        arg1 = currentInput;
        currentInput = "";
        operation = {
          "+": "add",
          "-": "sub",
          "×": "mul",
          "/": "div",
          "^": "pow"
        }[value];
      }
    } else if (["sin", "cos", "tan", "log", "ln", "√x"].includes(value)) {
      // Operações unárias
      operation = {
        "sin": "sin",
        "cos": "cos",
        "tan": "tan",
        "log": "log",
        "ln": "ln",
        "√x": "sqrt"
      }[value];
      if (currentInput !== "") {
        sendRequest(operation, currentInput);
        currentInput = "";
      }
    } else if (value === "π") {
      currentInput = "pi";
      updateDisplay("π");
    } else if (value === "e") {
      currentInput = "euler";
      updateDisplay("e");
    }
    else if (value === "RX") {
        // Ler o valor da variável 'x'
        readVariable("x");
      } else if (value === "RY") {
        // Ler o valor da variável 'y'
        readVariable("y");
      } else if (value === "RZ") {
        // Ler o valor da variável 'z'
        readVariable("z");
      } else if (value === "SX") {
        // Armazenar o valor em 'x'
        storeVariable("x", currentInput);
      } else if (value === "SY") {
        // Armazenar o valor em 'y'
        storeVariable("y", currentInput);
      } else if (value === "SZ") {
        // Armazenar o valor em 'z'
        storeVariable("z", currentInput);
      } else if (value === "x²") {
        // Calcular x² (quadrado)
        if (currentInput !== "") {
          sendRequest("sq", currentInput);
          currentInput = "";
        }
      } else if (value === "1/x") {
        // Calcular 1/x (inverso)
        if (currentInput !== "") {
          sendRequest("inv", currentInput);
          currentInput = "";
        }
      }
  });
});

async function readVariable(varName) {
    try {
      const response = await fetch(`/wscalc/var/${varName}`);
      if (!response.ok) throw new Error(await response.text());
  
      const data = await response.json();
      updateDisplay(data.value); // Exibe o valor no display
    } catch (error) {
      updateDisplay("Erro");
      console.error("Erro ao ler variável:", error);
    }
  }
  
  async function storeVariable(varName, value) {
    try {
      const response = await fetch(`/wscalc/var/${varName}?value=${value}`, { method: 'POST' });
      if (!response.ok) throw new Error(await response.text());
  
      updateDisplay("Armazenado"); // Exibe mensagem temporária
    } catch (error) {
      updateDisplay("Erro");
      console.error("Erro ao armazenar variável:", error);
    }
  }

  if (value === "x²") {
    if (currentInput !== "") {
      sendRequest("sq", currentInput);
      currentInput = "";
    }
  }
  