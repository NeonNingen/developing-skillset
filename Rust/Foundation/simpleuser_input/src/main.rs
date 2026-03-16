use std::io;

fn main() {
    println!("Please provide me your name");

    let mut userinput = String::new();
    io::stdin().read_line(&mut userinput)
               .expect("Incorrect value");

    println!("Your name is: {}", userinput);
}
