import unittest;
import re;

problem_num='5'
inputfile='input.txt'

#########
# Setup
#########

with open(inputfile) as f:
  file_input_text = f.read()

#########
# Funcs
#########

def array_me(str_array):
  return [int(move) for move in str_array]

def basic_split(input_text):
  return [line for line in input_text.split('\n') if len(line)>0] 

def move(array, pos, part2=False):
  new_move = array[pos]
  if part2:
    if array[pos] >= 3:
      array[pos] -= 1  
    else:
      array[pos] += 1  
  else:
    array[pos] += 1

  pos = pos + new_move
  return (array, pos)


def part1():
  num_jumps = 0
  (array, pos) = (array_me(basic_split(file_input_text)),0)
  while (pos >= 0 and pos < len(array)):
    (array,pos) = move(array,pos)
    num_jumps += 1
  return num_jumps

def part2():
  num_jumps = 0
  (array, pos) = (array_me(basic_split(file_input_text)),0)
  while (pos >= 0 and pos < len(array)):
    (array,pos) = move(array,pos,True)
    num_jumps += 1
  return num_jumps

#########
# Tests
#########

class TestSolution(unittest.TestCase):
  def test_Part1(self):
    (array, pos) = move([0,3,0,1,-3],0)
    self.assertEqual(array, [1,3,0,1,-3])

  def test_Part2(self):
    self.assertEqual(1,1)

if __name__ == '__main__':
  unittest.main(exit=False)

#########
# Main
#########

print( '----------------------------------------------------------------------' )
print( 'Solution for Problem ' + problem_num)
print( '\tPart 1: ' + str(part1()) )
print( '\tPart 2: ' + str(part2()) )
print( '----------------------------------------------------------------------' )