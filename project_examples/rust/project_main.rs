fn main() {
    let items = [12, 18, 21, 9, 31];
    let total: i32 = items.iter().sum();
    println!("Total: {}", total);
    println!("Average: {:.2}", total as f64 / items.len() as f64);
}
