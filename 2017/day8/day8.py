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

def parse_commands(lines):
  cmds = []
  for line in lines:
    words = line.split()
    cmd = {}
    cmd['register'] = words[0]
    cmd['action'] = words[1]
    cmd['amt'] = int(words[2])
    cmd['test_register'] = words[4]
    cmd['test'] = words[5]
    cmd['test_value'] = int(words[6])
    cmds.append(cmd)
  return cmds

def do_test(register,test,value,register_values):
  if register not in register_values:
    register_values[register] = 0

  if test == '<':
    return register_values[register] < value
  elif test == '<=':
    return register_values[register] <= value
  elif test == '==':
    return register_values[register] == value
  elif test == '>=':
    return register_values[register] >= value
  elif test == '>':
    return register_values[register] > value
  elif test == '!=':
    return register_values[register] != value

def process_commands(cmds):
  register_values = {}
  register_values['highest_ever'] = None
  for cmd in cmds:
    reg = cmd['register']
    if reg not in register_values:
      register_values[reg] = 0

    if do_test(cmd['test_register'], cmd['test'], cmd['test_value'], register_values):
      if cmd['action'] == 'inc':
        register_values[reg] += cmd['amt']
      elif cmd['action'] == 'dec':
        register_values[reg] -= cmd['amt']

    if register_values['highest_ever'] == None or register_values[reg] > register_values['highest_ever']:
      register_values['highest_ever'] = register_values[reg]

  return register_values

def get_biggest_register(register_values):
  biggest_register = None
  for register_name in list(register_values.keys()):
    if register_name == 'highest_ever':
      continue
    if biggest_register == None or register_values[register_name] > biggest_register:
      biggest_register = register_values[register_name]

  return biggest_register

def part1():
  register_values = process_commands(parse_commands(basic_split(file_input_text)))
  return get_biggest_register(register_values)

def part2():
  register_values = process_commands(parse_commands(basic_split(file_input_text)))
  return register_values['highest_ever']

#########
# Tests
#########

class TestSolution(unittest.TestCase):
  def test_Part1(self):
    test_input = """b inc 5 if a > 1
                    a inc 1 if b < 5
                    c dec -10 if a >= 1
                    c inc -20 if c == 10"""
    register_values = process_commands(parse_commands(basic_split(test_input)))
    self.assertEqual(get_biggest_register(register_values),1)

  def test_Part2(self):
    test_input = """b inc 5 if a > 1
                    a inc 1 if b < 5
                    c dec -10 if a >= 1
                    c inc -20 if c == 10"""
    register_values = process_commands(parse_commands(basic_split(test_input)))
    self.assertEqual(register_values['highest_ever'],10)

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
