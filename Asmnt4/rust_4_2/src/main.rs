fn encode(input: &str) -> String {
    return input
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;");
}

fn main() {
    let msg = "Is 3 < 4 && 3 > 4?";
    println!("{} becomes: {}", msg, encode(msg));
}
