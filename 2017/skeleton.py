import unittest;
import re;

problem_num='1'
inputfile='input.txt'

#########
# Setup
#########

with open(inputfile) as f:
  file_input_text = f.read()

#########
# Funcs
#########

def basic_split(input_text):
  return [line for line in input_text.split('\n') if len(line)>0] 

def part1():
  return ''

def part2():
  return ''

#########
# Tests
#########

class TestSolution(unittest.TestCase):
  def test_Part1(self):
    self.assertEqual(1,1)

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