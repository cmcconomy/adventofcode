import unittest;
import re;

problem_num='11'
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
  return [line for line in input_text.split(',') if len(line)>0] 

def move(pos,dir):
  # moving laterally moves up/down half a y coord
  x,y = pos
  if dir == 'n':
    y += 1
  elif dir == 's': 
    y -= 1
  elif dir == 'ne': 
    y += 0.5
    x += 1
  elif dir == 'nw': 
    y += 0.5
    x -= 1
  elif dir == 'se': 
    y -= 0.5
    x += 1
  elif dir == 'sw': 
    y -= 0.5
    x -= 1

  return (x,y)

def move_dir_list(dir_list):
  pos = (0,0)
  max_dist = 0
  for direction in dir_list:
    pos = move(pos,direction)
    dist = num_moves(pos)
    if dist > max_dist:
      max_dist = dist

  return (pos,max_dist)

def num_moves(pos):
  (x,y) = [abs(p) for p in list(pos)]
  y_distance_left = y - (x/2) # each lateral move brings us 0.5 y coords closer to our goal.

  return int(x + y_distance_left + 0.5) #round up in case it's fractional

def part1():
  return num_moves(move_dir_list(basic_split(file_input_text))[0]) # index 0 is the pos tuple

def part2():
  return move_dir_list(basic_split(file_input_text))[1] # index 0 is the max_dist

#########
# Tests
#########

class TestSolution(unittest.TestCase):
  def test_Part1(self):
    self.assertEqual(num_moves(move_dir_list(['ne','ne','ne'])[0]),3)
    self.assertEqual(num_moves(move_dir_list(['ne','ne','sw','sw'])[0]),0)
    self.assertEqual(num_moves(move_dir_list(['ne','ne','s','s'])[0]),2)
    self.assertEqual(num_moves(move_dir_list(['se','sw','se','sw','sw'])[0]),3)

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