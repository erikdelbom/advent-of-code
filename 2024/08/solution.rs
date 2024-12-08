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

fn parse_input(data: &Vec<String>) -> Vec<Vec<char>> {
    data.iter()
        .map(|s| s.chars().collect())
        .collect()
}

fn vec_same_shape(vec: &Vec<Vec<char>>) -> Vec<Vec<u8>> {
    vec.iter()
       .map(|row| vec![0; row.len()])
       .collect()
}

fn find_matches(antennas: &Vec<Vec<char>>, origin: (usize, usize)) -> Vec<(i32, i32)> {
    let n: usize = antennas.len();
    let m: usize = antennas[0].len();
    let y = origin.0;
    let x = origin.1;
    let c = antennas[y][x];
    let mut matches: Vec<(i32, i32)> = Vec::new();

    for i in 0..n {
        for j in 0..m {
            if i == y && j == x {
                continue
            }

            if antennas[i][j] == c {
                matches.push((i as i32, j as i32));
            }
        }
    }

    matches
}

fn offset(a: (i32, i32), b: (i32, i32)) -> (i32, i32) {
    let y = b.0 - a.0;
    let x = b.1 - a.1;

    (y, x)
}

fn part_1(data: &Vec<String>) -> i64 {
    let antennas = parse_input(&data);
    let mut anti = vec_same_shape(&antennas);

    let n = antennas.len();
    let m = antennas[0].len();
  
    for i in 0..n {
        for j in 0..m {
            let c = antennas[i][j];
            if !(c.is_numeric() || c.is_alphabetic()) {
                continue
            }
            
            let matches = find_matches(&antennas, (i, j));
            for ma in matches {
                let (dy, dx) = offset((i as i32, j as i32), (ma.0,ma.1));
                let y = ma.0+dy;
                let x = ma.1+dx;
                if y < (n as i32) && y >= 0 && x < (m as i32) && x >= 0 {
                    anti[y as usize][x as usize] = 1;
                }
            }
        }
    } 
    
    anti.iter()
        .flat_map(|row| row.iter())
        .map(|&x| x as i64)
        .sum()
}

fn part_2(data: &Vec<String>) -> i64 {
    let antennas = parse_input(&data);
    let mut anti = vec_same_shape(&antennas);

    let n = antennas.len();
    let m = antennas[0].len();
    
    for i in 0..n {
        for j in 0..m {
            let c = antennas[i as usize][j as usize];
            if !(c.is_numeric() || c.is_alphabetic()) {
                continue
            }
            anti[i as usize][j as usize] = 1; 
            let matches = find_matches(&antennas, (i, j));
            for (y, x) in matches {
                let (dy,dx) = offset((i as i32, j as i32), (y,x));
                let mut y = y+dy;
                let mut x = x+dx;
                while y < (n as i32) && y >= 0 && x < (m as i32) && x >= 0 {
                    anti[y as usize][x as usize] = 1;
                    y += dy;
                    x += dx;
                }
            }
        }
    } 
    
    anti.iter()
        .flat_map(|row| row.iter())
        .map(|&x| x as i64)
        .sum()

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
