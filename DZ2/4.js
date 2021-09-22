function sumNumbers(a, b) {
    let result = a + b;
    return result
}


function diffNumbers(a, b) {
    let result = a - b;
    return result
}

function multNumbers(a, b) {
    let result = a * b;
    return result
}

function devNumbers(a, b) {
    let result = a / b;
    return result
}

let a = Number(prompt('Введите первое число: '))
let b = Number(prompt('Введите второе число: '))
alert(sumNumbers(a, b));
alert(diffNumbers(a, b));
alert(multNumbers(a, b));
alert(devNumbers(a, b));