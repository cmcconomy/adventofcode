import re;

problem_num='9'
inputfile='day' + problem_num + '.txt'
inputfile='input.txt'

with open(inputfile) as f:
  lines = [line for line in f.read().split('\n') if len(line)>0]

line = lines[0]

def decompress(input_str):
  compression = [i for i,x in enumerate(input_str) if x=='(' or x=='x' or x==')']
  compress_index=0
  currlist_pos=0
  strsize_to_dupe=0
  numDupes=0

  output=''

  while currlist_pos < len(input_str):
    if input_str[currlist_pos] == '(':
      # Compression Instruction
      if len(compression) > 0:
        openParen = compression[compress_index]
        x = compression[compress_index+1]

        closeParen = compression[compress_index+2]
        strsize_to_dupe = int(input_str[openParen+1:x])
        numDupes = int(input_str[x+1:closeParen])
      else:
        closeParen = -1
        strsize_to_dupe = len(input_str)
        numDupes = 1

      segment = input_str[closeParen+1:closeParen+strsize_to_dupe+1]
      for i in range(0,numDupes):
        output += segment

      compress_index += 3
      # if compress_index >= len(compression):
      #   break

      currlist_pos = closeParen + len(segment) + 1
      while compress_index < len(compression) and compression[compress_index] < currlist_pos:
        compress_index += 1
        if compress_index >= len(compression):
          break

    else:
      # simple string print
      if len(compression) > 0 and compress_index < len(compression): 
        end_of_str = compression[compress_index]
      else:
        end_of_str = len(input_str)
      output += input_str[currlist_pos:end_of_str]
      currlist_pos = end_of_str


  return output

def part1():
#  return decompress('X(8x2)(3x3)ABCY')
  return len(decompress(line))

def part2():
  return ''

print( 'Solution for Problem ' + problem_num)
print( 'Part 1: ' + str(part1()) )
print( 'Part 2: ' + str(part2()) )


