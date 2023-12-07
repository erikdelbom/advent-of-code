use std::fs;
use std::env;

fn get_filename() -> String 
{
    let args: Vec<String> = env::args().collect();
    let filename: String = args[1].clone();

    return filename;
}

fn read_input(filename: &str) -> String
{
    let contents = fs::read_to_string(filename)
                    .expect("Could not read file");
    return contents;
}

fn parse_input(input: &String) 
{

}

fn part_1(input: String) 
{
    
}

fn part_2(input: String) 
{

}

fn main() 
{
    let filename: String = get_filename();
    let input = read_input(&filename);
    
    //part_1_result = part_1(input);
    //println!("Part 1: {part_1_result}");
    
    //part_2_result = part_2(input);
    //println("Part 2: {part_2_result}");

}