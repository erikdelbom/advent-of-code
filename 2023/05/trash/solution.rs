use std::fs;
use std::env;

fn get_filename() -> String 
{
    let args: Vec<String> = env::args().collect();
    let filename: String = args[1].clone();

    return filename;
}

fn read_input(filename: &str) -> Vec<String>
{
    let contents = fs::read_to_string(filename)
                    .expect("Could not read file");
    let lines = contents.split("\n").clone();
    let collection: Vec<String> = lines.collect();
    
    return collection;
    //return contents.split("\n").collect::<Vec<Sttr>>();
}

fn parse_input(input: &String) 
{
    let mut vector_of_converts: Vec<Vec< [u64; 3]>>; 
 
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

    dbg!(input);
    
    //part_1_result = part_1(input);
    //println!("Part 1: {part_1_result}");
    
    //part_2_result = part_2(input);
    //println("Part 2: {part_2_result}");

}