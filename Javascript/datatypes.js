let firstName = "Balaji"; // string
let age = 25;        // number
let gpa = 9.8        // number
let isGood = true   // boolean
let isBad = false  // boolean
let x = 20>10;      // boolean

let statusNow; // undefined
let isNull = null; // null


console.log(typeof firstName);
console.log(typeof age);
console.log(typeof isGood);
console.log(typeof x);
console.log(typeof statusNow);
console.log(null == undefined);



let student = {
    name: 'Balaji',
    age: 25,
    status: 'single'
};

console.log(student);
console.log(typeof student);


let arr = ['a', 'b', 'c'];
console.log(arr);
console.log(typeof arr);


function greet() {
    console.log(`Welcome, ${firstName}`);
}
greet();

console.log(greet);
console.log(typeof greet);