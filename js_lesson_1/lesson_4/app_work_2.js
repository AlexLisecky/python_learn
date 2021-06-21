// 2.Продолжить работу с интернет-магазином:
// 2.1. В прошлом домашнем задании вы реализовали корзину на базе массивов. Какими объектами можно заменить их элементы?
// 2.2. Реализуйте такие объекты.
// 2.3. Перенести функционал подсчета корзины на объектно-ориентированную базу.

// вариант 1
let basket = []

function getProduct(name, price, count) {
    return {
        name,
        price,
        count,
    }
};

function pushProduct(name, price, count) {
    basket.push(getProduct(name, price, count))
};

function summBasket(basket) {
    let total = 0
    for (let i = 0; i < basket.length; i++) {
        total += basket[i].price * basket[i].count
    }
    return `Сумма корзины ${total}`
};

function start() {
    let answer = parseInt(prompt('Хотите поторговать?\nВведите "1" если да\nВведите "0" если нет'))
    if (answer === 0) {
        return alert('Bye')
    }
    else {
        return true
    }
};

function middle() {
    answer = parseInt(prompt('Наш ассортимент: Груши по 300 под лотом "1"\nСливы по 500 под лотом "2"\nЯблоки по 600 под лотом "3"\n"0" для выхода'))
    switch (answer) {
        case (1):
            return pushProduct('груши', 300, 1), middle()
        case (2):
            return pushProduct('сливы', 500, 1), middle()
        case (3):
            return pushProduct('яблоки', 600, 1), middle()
        case (0):
            break
    }
};


function run() {
    if (start() == true) {
        middle()
    }
    return summBasket(basket)
};

let basketPrice = run()

alert(basketPrice)



