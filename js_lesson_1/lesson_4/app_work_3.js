// вариант 2 ----------------------------------------------------------------------------------------------------------------------------

// const basket = {
//     product: getProduct('груши', 300, 1),
//     product1: getProduct('сливы', 500, 1),
//     product2: getProduct('яблоки', 600, 1),
//     getProduct(name, price, count) {
//         return {
//             name,
//             price,
//             count,
//         }
//     },
//     summBasket(basket) {
//         let total = 0
//         for (let i = 0; i < basket.length; i++) {
//             total += basket[i].price * basket[i].count
//         }
//         return `Сумма корзины ${total}`
//     },
//     run() {

//     }
// };

// console.log(basket.summBasket())


const baskett = {
    product: [
        {
            name: 'сливы',
            price: 300,
            count: 2
        },
        {
            name: 'груши',
            price: 400,
            count: 3
        },
        {
            name: 'яблоки',
            price: 500,
            count: 4
        }
    ],
    sumBasket() {
        return this.product.reduce((total, item) => total + item.price * item.count, 0);
    },
}


console.log(baskett.sumBasket())