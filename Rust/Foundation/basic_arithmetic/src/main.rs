// use prompted::input; Crate with python like input
use std::io;

fn main() {
    println!("Please enter 2 number, to be added together");

    let mut num: u8 = 1;
    let num1 = take_int(num);
    num = 2;
    let num2 = take_int(num);

    println!("{}", num1 + num2);
}

// Function for int64 input
fn take_int(num: u8) -> i64 {
    println!("Please input number {num}: ");

    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();

    return input.trim().parse().unwrap();
}