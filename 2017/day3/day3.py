import unittest;
import re;

problem_num='3'
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

def spiral_out(target):
  square_size=1
  x=0 # right is positive
  y=0 # up is positive
  dir=0 #0=right, 1=up, 2=left, 3=down
  for i in range(2,target+1):
    if dir == 0:
      if x < square_size:
        x += 1
      else:
        dir = 1
        y += 1
    elif dir == 1:
      if y < square_size:
        y += 1
      else:
        dir = 2
        x -= 1
    elif dir == 2:
      if x > -square_size:
        x -= 1
      else:
        dir = 3
        y -= 1
    elif dir == 3:
      if y > -square_size:
        y -= 1
      else:
        dir = 0
        x += 1
        square_size += 1

  return abs(x) + abs(y)

def spiral_trail(ceiling):
  square_size=1
  x=0 # right is positive
  y=0 # up is positive
  dir=0 #0=right, 1=up, 2=left, 3=down
  i=1
  grid={}
  grid[0,0] = 1


  while (True):
    # move
    if dir == 0:
      if x < square_size:
        x += 1
      else:
        dir = 1
        y += 1
    elif dir == 1:
      if y < square_size:
        y += 1
      else:
        dir = 2
        x -= 1
    elif dir == 2:
      if x > -square_size:
        x -= 1
      else:
        dir = 3
        y -= 1
    elif dir == 3:
      if y > -square_size:
        y -= 1
      else:
        dir = 0
        x += 1
        square_size += 1

    # get around-you sum
    grid[x,y] = 0
    if (x-1,y-1) in grid:
      grid[x,y] += grid[x-1,y-1]

    if (x-1,y) in grid:
      grid[x,y] += grid[x-1,y]   
    
    if (x-1,y+1) in grid:
      grid[x,y] += grid[x-1,y+1] 

    if (x,y-1) in grid:
      grid[x,y] += grid[x,y-1]   

    if (x,y+1) in grid:
      grid[x,y] += grid[x,y+1]   

    if (x+1,y-1) in grid:
      grid[x,y] += grid[x+1,y-1]   
    
    if (x+1,y) in grid:
      grid[x,y] += grid[x+1,y]

    if (x+1,y+1) in grid:
      grid[x,y] += grid[x+1,y+1] 

    # return if greater
    if grid[x,y] > ceiling:
      return grid[x,y]

    i += 1



def part1():
  return spiral_out(int(file_input_text))

def part2():
  return spiral_trail(int(file_input_text))

#########
# Tests
#########

class TestSolution(unittest.TestCase):
  def test_Part1(self):
    self.assertEqual(spiral_out(1),0)
    self.assertEqual(spiral_out(12),3)
    self.assertEqual(spiral_out(23),2)
    self.assertEqual(spiral_out(1024),31)

  def test_Part2(self):
    self.assertEqual(spiral_trail(100),122)

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