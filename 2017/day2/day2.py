import unittest;
import re;

problem_num='2'
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

def interize(rows):
  return [[int(cell) for cell in row.split()] for row in rows]

def checksum_bigdiff(input_text):
  sum=0
  rows = interize(basic_split(input_text))
  for i,row in enumerate(rows):
    sum += max(row) - min(row)
  return sum

def checksum_divisor(input_text):
  sum=0
  rows = interize(basic_split(input_text))
  for i,row in enumerate(rows):
    row = sorted([int(cell) for cell in row])
    rows[i] = row
    for j,cell in enumerate(row):
      for k in range(j+1,len(row)):
        if row[k] % cell == 0:
          sum += int(row[k]/cell);
          break;
  return sum

def part1():
  return checksum_bigdiff(file_input_text)

def part2():
  return checksum_divisor(file_input_text)

#########
# Tests
#########

class TestSolution(unittest.TestCase):
  def test_Part1(self):
    test_arr="""5 1 9 5
                7 5 3
                2 4 6 8"""
    self.assertEqual(checksum_bigdiff(test_arr), 18)

  def test_Part2(self):
    test_arr="""5 9 2 8
                9 4 7 3
                3 8 6 5"""
    self.assertEqual(checksum_divisor(test_arr), 9)

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



