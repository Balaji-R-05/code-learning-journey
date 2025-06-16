// let and cost is block scoped
// var is function scoped
// let can be reassigned but const can't be reassigned

let x = 10;
const y = "Hello";

if (x>0) {
    let y = 5;
    console.log(y);
}

console.log(x);
console.log(y);