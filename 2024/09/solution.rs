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

fn parse_input(data: &Vec<String>) -> Vec<i64> {
    data[0].chars()
           .filter_map(|c| c.to_digit(10))
           .map(|d| d as i64)
           .collect()
}

fn create_disk(data: &Vec<i64>) -> Vec<i64> {
    let mut result = Vec::new();
    let mut id = 0;
    for i in 0..data.len() {
        if i % 2 == 0 {
           for _ in 0..data[i] {
                result.push(id);
            } 
            id += 1;
        } else {
            for _ in 0..data[i] {
                result.push(-1);
            }
        }
    }
    result
}

fn format_disk(disk: &mut Vec<i64>) {
    let mut front = 0;
    let mut back = disk.len()-1;

    while front < back {
        let f = disk[front];
        println!("Front: {} {}, Back: {} {}", front, disk[front], back, disk[back]);
        if f == -1 {
            let mut b = disk[back];
            while b == -1 {
                back -= 1;
                b = disk[back];
            }
            disk.swap(front, back);
            back -= 1;
        }
        front += 1;
    }
}

fn checksum(disk: &Vec<i64>) -> u64{
    let mut sum = 0;
    let mut i = 0;
    let mut f = disk[i];

    while f != -1 {
        sum += (i as u64) * (f as u64);
        i += 1;
        f = disk[i];
    }
    sum
}

fn part_1(data: &Vec<String>) -> u64 {
    let parsed_data = parse_input(&data);
    let mut disk = create_disk(&parsed_data);
    //println!("{:?}", disk);
    format_disk(&mut disk);
    println!("{:?}", &disk[50000..50010]);
    checksum(&disk)
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
