fn main() {
    let raw = ["1", "2", "", "NA", "7"];
    let count = raw.iter().filter(|v| !v.is_empty() && *v != "NA").count();
    println!("{}", count);
}
