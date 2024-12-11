use std::env; 
use std::process;
use std::fs::read_to_string;
use std::time::Instant;
use std::collections::VecDeque;

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

fn parse_input(data: &Vec<String>) -> Vec<Vec<i64>> {
    data.iter()
        .map(|s| {
            s.chars()
             .map(|c| c.to_digit(10).expect("Invalid digit") as i64)
             .collect::<Vec<i64>>()
        })
        .collect::<Vec<Vec<i64>>>()
}

fn find_heads(map: &Vec<Vec<i64>>) -> Vec<(usize, usize)> {
    let mut res = Vec::new();
    for row in 0..map.len() {
        for col in 0..map[0].len() {
            if map[row][col] == 0 {
                res.push((row, col));
            }
        }
    }
    res
}

fn find_neighbors(map: &Vec<Vec<i64>>, pos: (usize, usize)) -> Vec<(usize, usize)> {
    let n = map.len();
    let m = map[0].len();
    let mut neighbors = Vec::new();
    
    if pos.0 > 0 {
        neighbors.push((pos.0-1, pos.1));
    }
    if pos.0 < n-1 {
        neighbors.push((pos.0+1, pos.1));
    }
    if pos.1 > 0 {
        neighbors.push((pos.0, pos.1-1));
    }
    if pos.1 < m-1 {
        neighbors.push((pos.0, pos.1+1));
    }

    neighbors
}

fn find_trails(map: &Vec<Vec<i64>>, head: (usize, usize), distinct: bool) -> i64 {
    let mut count = 0;
    let mut visited = vec![vec![0; map[0].len()]; map.len()];
    let mut queue: VecDeque<(usize, usize)> = VecDeque::new();

    queue.push_back(head);

    while !queue.is_empty() {
        let current = queue.pop_front().unwrap();
        visited[current.0][current.1] = 1;
        //println!("{:?}", current);
        if map[current.0][current.1] == 9 {
            count += 1;
        } else {
            let neighbors = find_neighbors(map, current);
            //println!("{:?}", neighbors);
            for n in neighbors {
                let diff = (map[n.0][n.1] - map[current.0][current.1]);
                if visited[n.0][n.1] == 0 && diff == 1 {
                    if distinct {
                        queue.push_back(n);
                    } else {
                        queue.push_front(n);
                    }
                }
            }
        }
    }
    //println!("{count}");
    count
}

fn part_1(data: &Vec<String>) -> i64 {
    let map = parse_input(&data);
    let heads = find_heads(&map);
    let mut sum = 0; 
    for head in heads {
        sum += find_trails(&map, head, false);
    }
    sum
}

fn part_2(data: &Vec<String>) -> i64 {
    let map = parse_input(&data);
    let heads = find_heads(&map);
    let mut sum = 0; 
    for head in heads {
        sum += find_trails(&map, head, true);
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
