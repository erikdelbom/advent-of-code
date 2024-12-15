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

    for blink in 0..25 {
        let mut i = 0;
        while i < stones.len() {
            let stone = stones[i];
            let stone_str = stone.to_string();
            let stone_len = stone_str.len();
            if stone == 0 {
                stones[i] = 1;
            } else if  stone_len % 2 == 0 {
                let first_half = &stone_str[0..stone_len/2];
                let second_half = &stone_str[stone_len/2..stone_len];
                stones[i] = first_half.parse::<u64>().unwrap();
                stones.insert(i+1, second_half.parse::<u64>().unwrap());
                i += 1;
            } else {
                stones[i] = stone * 2024;
            }
            i += 1;
        }
    }
    stones.len() as u64
}

fn part_2(data: &Vec<String>) -> u64 {
    let mut stones = parse_input(&data);
    let stone_types = vec![vec![]; ];

    for blink in 0..25{
        for type in stone_types {

        }
    }
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
