//1. Доработать модуль корзины.
//a. Добавлять в объект корзины выбранные товары по клику на кнопке «Купить» без перезагрузки страницы
//b. Привязать к событию покупки товара пересчет корзины и обновление ее внешнего вида

const basket = {
    basketDiv: document.querySelector(`.basket`),
    basketSumDiv: document.querySelector(`.basketSum`),
    clrBtn: document.querySelector(`.clrBtn`),
    item: [
        {
            id: 1,
            name: "Сливы",
            price: 300,
            count: 1,
        },
    ],

    renderBasket() {
        this.basketDiv.innerHTML = '';
        this.item.forEach(item => {
            this.basketDiv.insertAdjacentHTML('beforeend', this.createBasketGood(item))
        });
    },

    createBasketGood(item) {
        return `<div class = "good">
                <h3>${item.name}</h3>
                <p>${item.price} руб.</p>
                <p>${item.count} шт.</p>
            </div>`;
    },
    pushToBasket(product) {
        if (product) {
            const findInBasket = this.item.find(({ id }) => product.id === id);
            if (findInBasket) {
                findInBasket.count++;
            } else {
                this.item.push(Object.assign({ count: 1 }, product));
            }
            this.renderBasket();
            this.createBasketSum();
        } else {
            alert('Ошибка добавления!');
        }
    },

    createBasketSum() {
        this.basketSumDiv.innerHTML = (`<h3>Сумма товаров = ${this.sumItem()}</h3>`)
    },

    sumItem() {
        return this.item.reduce((total, item) => total + item.price * item.count, 0);
    },

    addClrBasket() {
        this.clrBtn.addEventListener('click', () => this.clrBasket())
    },

    clrBasket() {
        this.item = []

        this.renderBasket()

        this.createBasketSum()
    },

    init() {
        this.renderBasket()
        this.createBasketSum()
        this.addClrBasket()
    }


};


const catalog = {
    catalogDiv: document.querySelector(".catalog"),
    buyBtn: buyBtn = document.querySelector(".buyBtn"),
    basket: basket,
    good: [
        {
            id: 1,
            name: "Сливы",
            price: 300
        },
        {
            id: 2,
            name: "Яблоки",
            price: 300
        },
        {
            id: 3,
            name: "Груши",
            price: 300
        },
    ],

    createGood() {
        this.good.forEach(item => {
            this.catalogDiv.insertAdjacentHTML('beforeend', this.createCatalogGood(item))
        })
    },

    createCatalogGood(item) {
        return `<div class = "good">
                <h3>${item.name}</h3>
                <p>${item.price} руб.</p>
                <button class = "buyBtn"
                data-id_product="${item.id}"
                >Купить</button>
            </div>`;
    },
    buyGood() {
        this.catalogDiv.addEventListener('click', (event) => this.pushToBasket(event))
    },

    pushToBasket(event) {
        const idProduct = +event.target.dataset.id_product;
        const productToAdd = this.good.find((product) => product.id === idProduct);
        this.basket.pushToBasket(productToAdd);
    },

    init() {
        this.createGood()
        this.buyGood()
    }



};



catalog.init()
basket.init()