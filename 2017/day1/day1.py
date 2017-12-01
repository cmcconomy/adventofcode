import re;

problem_num='1'
inputfile='input.txt'

with open(inputfile) as f:
  lines = [line for line in f.read().split('\n') if len(line)>0]

line = lines[0]

def conga_line_add(input_str):
  value=0;
  for i,this_char in enumerate(input_str):

    if i == len(input_str)-1:
      # loop around as the list is circular
      i = -1;
    next_char=input_str [i+1]

    if this_char == next_char:
      # Good - this matches the next number
      value += int(this_char)

  return value

def conga_jump_add(input_str):
  value=0;
  for i,this_char in enumerate(input_str):

    jump_pos = int((i+len(input_str)/2) % len(input_str))
    jump_char=input_str[jump_pos]

    if this_char == jump_char:
      # Good - this matches the jump number
      value += int(this_char)

  return value

def part1():
  return conga_line_add(line)

def part2():
  return conga_jump_add(line)

print( 'Solution for Problem ' + problem_num)
print( 'Part 1: ' + str(part1()) )
print( 'Part 2: ' + str(part2()) )


