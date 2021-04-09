//3. Сделать генерацию корзины динамической: верстка корзины не должна находиться в HTML-структуре. Там должен быть только div, 
//в который будет вставляться корзина, сгенерированная на базе JS:
//3.1. Пустая корзина должна выводить строку «Корзина пуста»;
//3.2. Наполненная должна выводить «В корзине: n товаров на сумму m рублей»
//4*. Сделать так, чтобы товары в каталоге выводились при помощи JS:
//4.1. Создать массив товаров (сущность Product);
//4.2. При загрузке страницы на базе данного массива генерировать вывод из него. 
//HTML-код должен содержать только div id=”catalog” без вложенного кода. Весь вид каталога генерируется JS.
// //    product: [
//     {
//         name: 'сливы',
//         price: 300,
//         count: 2
//     },
//     {
//         name: 'груши',
//         price: 400,
//         count: 3
//     },
//     {
//         name: 'яблоки',
//         price: 500,
//         count: 4
//     }
// ],

const appBasket = {

    catalogs: [
        {
            name: 'сливы',
            price: 300,
            count: 3,
        },
        {
            name: 'груши',
            price: 400,
            count: 4,
        },
        {
            name: 'яблоки',
            price: 500,
            count: 5,
        },
        {
            name: 'перец',
            price: 100,
            count: 6,
        },
    ],

    total: [],

    sumBasket() {
        return this.catalogs.reduce((total, item) => total + item.price * item.count, 0);
    },

    sumCount() {
        return this.catalogs.reduce((total, item) => total + item.count, 0);
    },

    createText() {
        let text = document.createElement("div");
        text.style.width = "300px"
        text.style.height = "300px"
        text.style.backgroundColor = "grey"
        if (!this.catalogs.length == 0) {
            text.innerText = `«В корзине: ${this.sumCount()} товаров на сумму ${this.sumBasket()} рублей»`
            basket.appendChild(text)
        }
        else {
            text.innerText = `«Корзина пуста»`
            basket.appendChild(text)
        }
    },


    run() {
        this.createText()
        this.createProduct()
    },

    createProduct() {
        let catalog = document.createElement('div');
        catalog.style.width = "500px"
        catalog.style.height = "100%"
        catalog.style.backgroundColor = "blue"
        document.body.appendChild(catalog)


        for (let i = 1; i <= this.catalogs.length; i++) {
            let button = document.createElement('button');
            let product = document.createElement("div");
            button.id = 'button' + i;
            product.style.width = "500px";
            product.style.height = "100px";
            product.style.marginTop = "25px"
            product.style.backgroundColor = "red";;
            button.style.padding = "20px"
            button.style.backgroundColor = "green";
            button.innerText = "Купить";
            product.innerText = `Товар = ${this.catalogs[i - 1].name}\nЦена = ${this.catalogs[i - 1].price}`;
            catalog.appendChild(product);
            catalog.appendChild(button);
        }
    },
}


appBasket.run()
