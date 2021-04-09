//1. Создать функцию, генерирующую шахматную доску. При этом можно использовать любые html-теги по своему желанию.
//Доска должна быть разлинована соответствующим образом, т.е. чередовать черные и белые ячейки.
// Строки должны нумероваться числами от 1 до 8, столбцы – латинскими буквами A, B, C, D, E, F, G, H.

function gameZone() {
    const div = document.createElement("div");
    div.id = "game"
    div.style.display = "flex";
    div.style.height = "800px";
    div.style.width = "800px";
    div.style.border = "solid 1px black";
    div.style.flexWrap = "wrap";
    zones.appendChild(div);
}


function renderChess() {
    makeRow()
    makeZone()
    makeString()
    gameZone()
    let j = 0;
    let color = "cell_black"
    while (j < 8) {
        let i = 0;
        while (i < 8) {
            let myDiv = document.createElement("div");
            if (color == "cell_black") {
                myDiv.className = color;
                game.appendChild(myDiv);
                color = "cell_white";
                i++
            }
            else {
                myDiv.className = color;
                game.appendChild(myDiv);
                color = "cell_black"
                i++
            }

        }
        j++
        if (color == "cell_black") {
            color = "cell_white"
        }
        else {
            color = "cell_black"
        }
    }

}

function makeString() {
    let column = document.createElement("div");
    column.style.height = "800px"
    column.style.width = "65px"
    column.style.textAlign = "center"
    column.style.paddingTop = "20px"
    zones.appendChild(column)
    for (let i = 1; i <= 8; i++) {
        let cellString = document.createElement("div")
        cellString.style.height = "100px";
        cellString.style.width = "100px";
        cellString.id = "stroke"
        cellString.innerText = `${i}`
        column.appendChild(cellString)
    }
}


function makeRow() {
    let row = document.createElement("div");
    row.style.width = "800px";
    row.style.height = "30px";
    row.style.display = "flex";
    row.style.marginLeft = "85px"
    document.body.appendChild(row)
    let arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    for (let i = 1; i <= arr.length; i++) {
        let cellRow = document.createElement("div")
        cellRow.style.height = "100px"
        cellRow.style.width = "100px"
        cellRow.innerText = arr[i - 1]
        row.appendChild(cellRow)
    }
}


function makeZone() {
    let zone = document.createElement("div");
    zone.id = "zones"
    zone.style.width = "1000px";
    zone.style.height = "1000px";
    zone.style.display = "flex"
    document.body.appendChild(zone)
}




renderChess()




