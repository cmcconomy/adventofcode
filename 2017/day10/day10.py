import unittest;
import re;

problem_num='10'
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

def intify(items):
  return [int(item) for item in items]

def asciify(items):
  asciilist = [ord(item) for item in items]
  asciilist.append(17)
  asciilist.append(31)
  asciilist.append(73)
  asciilist.append(47)
  asciilist.append(23)
  return asciilist

def print_twist(knot, currpos, skip, length):
  end_range = (currpos+(length-1))%len(knot)
  out = '{ '
  for i in range(0,len(knot)):
    if i == currpos:
      out += '(['

    out += str(knot[i])

    if i == currpos:
      out += ']'

    if i == end_range:
      out += ')'

    out += ' '

  out += ' }'
  print(out)

def twist(knot, currpos, skip, length):
  if (length > len(knot)):
    print('Invalid length!! ' + str(length) + " is greater than the list size, " + str(len(knot)))
    return None

  for i in range(0,int(length/2)):
    a = (currpos+i)%len(knot)
    b = (currpos+(length-i-1))%len(knot)
    if (a != b):
      temp = knot[a]
      knot[a] = knot[b]
      knot[b] = temp

  currpos += length + skip
  currpos %= len(knot)
  skip += 1

  return (knot,currpos,skip)

def create_sequential_knot_data(num_items=256):
  return list(range(0,num_items))

def process_twist_list(twistlist, knot, skip=0, currpos=0):
  for length in twistlist:
    (knot,currpos,skip) = twist(knot,currpos,skip,length)

  return (knot, currpos, skip)

def process_64_twists(twistlist, knot):
  skip=0
  currpos=0
  for i in range(0,64):
    (newknot,currpos,skip) = process_twist_list(twistlist, knot, skip=skip, currpos=currpos )

  return knot

def convert_to_dense(knot):
  dense_knot = []
  for i in range(0,16):
    startpos = i*16
    dense_element = knot[startpos]
    for j in range(startpos+1, startpos+16):
      dense_element ^= knot[j]
    dense_knot.append(dense_element)

  return dense_knot

def denseknot_to_hex(dense_knot):
  hexknot = ["%0.2X" % dense_element for dense_element in dense_knot]
  return ''.join(hexknot).lower()

def knot_checksum(knot):
  return knot[0]*knot[1]

def part1():
  (knot,currpos,skip) = process_twist_list(intify(file_input_text.split(',')), create_sequential_knot_data())
  return(knot_checksum(knot))

def part2():
  return denseknot_to_hex(convert_to_dense(process_64_twists(asciify(file_input_text),create_sequential_knot_data())))

#########
# Tests
#########

class TestSolution(unittest.TestCase):
  def test_Part1(self):
    test_input = '3,4,1,5'
    (knot,currpos,skip) = process_twist_list(intify(test_input.split(',')), create_sequential_knot_data(5))
    self.assertEqual(knot_checksum(knot),12)

  def test_Part2(self):
    test_input = '1,2,3'
    self.assertEqual(asciify(test_input),[49,44,50,44,51,17,31,73,47,23])

    test_input = [64, 7, 255]
    self.assertEqual(denseknot_to_hex(test_input),'4007ff')

    test_input = ''
    self.assertEqual(denseknot_to_hex(convert_to_dense(process_64_twists(asciify(test_input),create_sequential_knot_data()))), 'a2582a3a0e66e6e86e3812dcb672a272')
    test_input = 'AoC 2017'
    self.assertEqual(denseknot_to_hex(convert_to_dense(process_64_twists(asciify(test_input),create_sequential_knot_data()))), '33efeb34ea91902bb2f59c9920caa6cd')
    test_input = '1,2,3'
    self.assertEqual(denseknot_to_hex(convert_to_dense(process_64_twists(asciify(test_input),create_sequential_knot_data()))), '3efbe78a8d82f29979031a4aa0b16a9d')
    test_input = '1,2,4'
    self.assertEqual(denseknot_to_hex(convert_to_dense(process_64_twists(asciify(test_input),create_sequential_knot_data()))), '63960835bcdc130f0b66d7ff4f6a5a8e')


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