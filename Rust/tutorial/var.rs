// fn main() {
//     let x: i32 = 10;
//     let y: i32 = 5;
//     {
//         println!("Inner scope value of x is {} and value of y is {}", x, y);
//     }
//     println!("Outer scope value of x is {} and value of y is {}", x, y); 
// }


fn main() {
    define_x()
}

fn define_x() {
    let x: &str = "hello";
    println!("{}, world", x); 
}