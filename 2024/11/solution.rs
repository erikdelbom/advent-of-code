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

fn parse_input(data: &Vec<String>) -> Vec<u64> {
    data[0].split_whitespace()
            .map(|num| num.parse::<u64>().expect("Invalid integer"))
            .collect()
}

fn part_1(data: &Vec<String>) -> u64 {
    let mut stones = parse_input(&data);
    println!("{:?}", stones);

    for blink in 0..6 {
        for i in range 0..stones.len() {
            let stone = stones[i];
            if stone == 0 {
                stones[i] = 1;
            }
            else if ((stone.abs() as f64).log10().floor() as u32 + 1) % 2 == 0 {

            }
        }
    }
    2 
}

fn part_2(data: &Vec<String>) -> u64 {
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
