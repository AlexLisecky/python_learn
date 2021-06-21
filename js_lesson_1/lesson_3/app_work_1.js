// 1. С помощью цикла while вывести все простые числа в промежутке от 0 до 100.

let list = []
let max = 100

function allert() {
    let i = 2
    while (i < max) {
        if (isPrime(i) == true) {
            list.push(i);
            i++;
        }
        else {
            i++
        }
    }
}


function isPrime(number) {
    let d = 2
    while (d * d <= number && number % d != 0) {
        d++
    }
    if ((d * d) > number) {
        return true
    }

}
allert()
console.log(list)