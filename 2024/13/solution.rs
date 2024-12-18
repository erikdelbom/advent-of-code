use std::env; 
use std::process;
use std::fs::read_to_string;
use std::time::Instant;
use regex::Regex;

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

fn gcd(mut a: u64, mut b: u64) -> u64 {
    while b != 0 {
        let m = a % b;
        a = b;
        b = m;
    }
    a
}

fn part_1(data: &Vec<String>) -> i64 {
    let rex = Regex::new(r"X\+[0-9]+").unwrap();
    for line in data {
        let Some(s) = rex.captures(line);
        println!("{s}");
    }
    1
}

fn part_2(data: &Vec<String>) -> i64 {
    2
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
