
document.getElementById("submit").addEventListener("click", add);

var nameArray = [];
var numberArray = [];

function add() {
    console.log("in add");

    var name = document.getElementById('box1').value;
    nameArray.push(name);
    console.log(nameArray);

    var number = document.getElementById('box2').value;
    numberArray.push(number);
    console.log(numberArray);
}