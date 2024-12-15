use std::env; 
use std::process;
use std::fs::read_to_string;
use std::time::Instant;
use std::collections::VecDeque;

type Coord = (usize, usize);

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


fn find_neighbors(map: &Vec<Vec<char>>, pos: Coord) -> Vec<Coord> {
    let (y, x) = pos;
    let n = map.len();
    let m = map.len();
    let mut neighbors = Vec::new();

    if y > 0 {
        neighbors.push((y-1, x));
    }
    if y < n-1 {
        neighbors.push((y+1, x));
    }
    if x > 0 {
        neighbors.push((y, x-1));
    }
    if x < m-1 {
        neighbors.push((y, x+1));
    } 
    
    neighbors 
}

fn find_area(map: &Vec<Vec<char>>, visited: &mut Vec<Vec<i32>>, start: Coord) -> (i64, i64, Vec<Coord>) {
    let (y, x) = start;  
    if visited[y][x] != 0 {
        return (0, 0, Vec::new());
    } 
    let area_code = map[y][x];
    let mut frontier: VecDeque<Coord> = VecDeque::new(); 
    frontier.push_back(start);
    visited[y][x] = 1;
    
    let mut border = Vec::new();
    let mut area = 0;
    let mut per = 0;
    while !frontier.is_empty() {
        let current = frontier.pop_front().unwrap();
        area += 1;
        let neighbors = find_neighbors(map, current);
        let mut per_update = 4 - neighbors.len() as i64;
        for n in neighbors {
            if map[n.0][n.1] != area_code {
                per_update += 1;
                continue
            }
            if visited[n.0][n.1] == 0 {
                visited[n.0][n.1] = 1;
                frontier.push_back(n);
            }
        }
        if per_update != 0 {
            border.push(current);
        }
        per += per_update;
    }

    (area, per, border)
}

fn find_sides(map: &Vec<Vec<char>>, border: &Vec<Coord>) -> i64 {
    let ymin = border.iter().map(|a| a.0).min().unwrap(); 
    let ymax = border.iter().map(|a| a.0).max().unwrap(); 
    let xmin = border.iter().map(|a| a.1).min().unwrap(); 
    let xmax = border.iter().map(|a| a.1).max().unwrap();

    let area_code = map[border[0].0][border[0].1];
    let mut sides = 0;

    let mut active = false;
    for i in ymin..ymax+1 {
        active = false;
        for j in xmin..xmax+1 {
            let c = map[i][j];
            if c == area_code {
                if (i == 0 || map[i-1][j] != area_code) && !active {
                    if border.contains(&(i,j)) {
                        sides += 1;
                        active = true;
                    }
                } else if i > 0 && map[i-1][j] == area_code {
                    active = false;
                }
            } else {
                active = false;
            }              
        }
    }
    for i in ymin..ymax+1 {
        active = false;
        for j in xmin..xmax+1 {
            let c = map[i][j];
            if c == area_code {
                if (i == map.len()-1 || map[i+1][j] != area_code) && !active {
                    if border.contains(&(i,j)) {
                        sides += 1;
                        active = true;
                    }
                }  else if i < map.len()-1 && map[i+1][j] == area_code {
                    active = false;
                }
            } else {
                active = false;
            }              
        }
    }
    for j in xmin..xmax+1 {
        active = false;
        for i in ymin..ymax+1 {
            let c = map[i][j];
            if c == area_code {
                if (j == 0 || map[i][j-1] != area_code) && !active {
                    if border.contains(&(i,j)) {
                        sides += 1;
                        active = true;
                    }
                } else if j > 0 && map[i][j-1] == area_code {
                    active = false;
                }
            } else {
                active = false;
            }              
        }
    }
    for j in xmin..xmax+1 {
        active = false;
        for i in ymin..ymax+1 {
            let c = map[i][j];
            if c == area_code {
                if (j == map.len()-1 || map[i][j+1] != area_code) && !active {
                    if border.contains(&(i,j)) {
                        sides += 1;
                        active = true;
                    }
                } else if j < map[0].len()-1 && map[i][j+1] == area_code {
                    active = false;
                }
            } else {
                active = false;
            }              
        }
    }
    sides
}

fn part_1(data: &Vec<String>) -> i64 {
    let mut sum = 0;
    let map = parse_input(&data);
    let mut visited = vec![vec![0; map[0].len()]; map.len()];
    for i in 0..map.len() {
        for j in 0..map[0].len() {
            let (area, per, _) = find_area(&map, &mut visited, (i, j));
            sum += area * per;
        }
    }
    sum
}

fn part_2(data: &Vec<String>) -> i64 {
    let mut sum = 0;
    let map = parse_input(&data);
    let mut visited = vec![vec![0; map[0].len()]; map.len()];
    for i in 0..map.len() {
        for j in 0..map[0].len() {
            let (area, _, border) = find_area(&map, &mut visited, (i, j));
            if area > 0 {
                let sides = find_sides(&map, &border);
                sum += area * sides;
            }
        }
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
