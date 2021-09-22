function mathNumbers(first, second, sign) {
    let result = "";
    switch (sign) {
        case "+":
            result = first + second;
            return result;
        case "-":
            result = first - second;
            return result;
        case "*":
            result = first * second;
            return result
        case "/":
            result = first / second;
            return result;
    }
}

let a = Number(prompt('Введите первое число: '))
let b = Number(prompt('Введите второе число: '))
let mathSymbol = prompt('Введите символ операции: +, -, * или /')

alert(mathNumbers(a, b, mathSymbol));