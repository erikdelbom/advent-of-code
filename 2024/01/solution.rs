use std::env; 
use std::process;
use std::fs::read_to_string;
use std::time::Instant;

fn get_filename() -> String {
    match env::args().nth(1) {
        Some(filename) => filename,
        None =>  {
            eprintln!("No input file provided. Exiting");
            process::exit(1)
        }
    }    
}

fn read_input(filename: &str) -> Vec<String> {
    match read_to_string(filename) {
        Ok(content) => {
            content
                .lines()
                .map(String::from)
                .collect()
        }
        Err(e) => {
            eprintln!("Error reading file '{}': {}", filename, e);
            process::exit(1)
        }
    } 
}

fn parse_lists(data: &Vec<String>) -> (Vec<i32>, Vec<i32>) {
    let mut left: Vec<i32> = Vec::new(); 
    let mut right: Vec<i32> = Vec::new(); 
    for line in data.iter() {
        let parts: Vec<&str> = line.split_whitespace().collect();
        let l: i32 = parts[0].parse().unwrap();
        let r: i32 = parts[1].parse().unwrap();
        left.push(l);
        right.push(r);
    }
    left.sort();
    right.sort();

    (left, right)
}

fn part_1(data: &Vec<String>) -> i64 {
    let (left, right) = parse_lists(data);
    let mut sum: i64 = 0; 

    for i in 0..left.len() {
        sum += (left[i] - right[i]).abs() as i64;
    }

    sum
}

fn part_2(data: &Vec<String>) -> i64 {
    let (left, right) = parse_lists(data);
    let mut sum: i64 = 0;

    for num in left {
        let count: i32 = right.iter().filter(|&&x| x == num).count() as i32;
        sum += (num * count) as i64;
    }

    sum
}

fn main() {
    let filename: String = get_filename();
    let data: Vec<String> =  read_input(&filename);
    
    let mut timer = Instant::now();
    let mut result = part_1(&data); 
    let mut duration = timer.elapsed();
    println!("Part 1: {} - {:.3} s", result, duration.as_secs_f64());

    timer = Instant::now();
    result = part_2(&data);
    duration = timer.elapsed();
    println!("Part 2: {} - {:.3} s", result, duration.as_secs_f64());
}
