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

def to_banklist(input_text):
  banklist = []
  banklist.append([int(bank) for bank in input_text.split() if len(bank)>0])
  return banklist

def redistribute(banklist):
  lastbank = banklist[-1]
  newbank = list(lastbank) #clone

  maxval = max(newbank)
  pos = newbank.index(maxval)
  newbank[pos] = 0

  for i in range(0,maxval):
    pos = (pos+1)%len(newbank)
    newbank[pos] += 1

  banklist.append(newbank)

  return banklist

def redistribute_until_repeat(banklist):
  while banklist.index(banklist[-1]) == len(banklist)-1:
    banklist = redistribute(banklist)

  return banklist

def part1():
  return len(redistribute_until_repeat(to_banklist(file_input_text)))-1

def part2():
  repeat_banklist = redistribute_until_repeat(to_banklist(file_input_text))
  return len(repeat_banklist) - repeat_banklist.index(repeat_banklist[-1]) -1

#########
# Tests
#########

class TestSolution(unittest.TestCase):
  def test_Part1(self):
    self.assertEqual(len(redistribute_until_repeat([[0,2,7,0]]))-1,5)

  def test_Part2(self):
    repeat_banklist = redistribute_until_repeat([[0,2,7,0]])
    self.assertEqual(len(repeat_banklist) - repeat_banklist.index(repeat_banklist[-1])-1,4)

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