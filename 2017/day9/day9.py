import unittest;
import re;

problem_num='9'
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

def parse(stream):
  in_garbage=False
  ignore_next=False
  curr_group={}
  for i,char in enumerate(list(stream)):
    # Special first case
    if i == 0:
      root = {'start':i, 'level':1, 'parent': None, 'children':[], 'garbage_count': 0}
      curr_group = root
      continue

    # garbage
    if in_garbage:
      if ignore_next:
        ignore_next=False
      else:
        if char == '>':
          in_garbage=False
        elif char == '!':
          ignore_next=True
        else:
          root['garbage_count'] += 1

      continue

    # group
    if char == '{':
      new_group = {'start':i, 'level':curr_group['level']+1, 'parent':curr_group, 'children':[]}
      curr_group['children'].append(new_group)
      curr_group = new_group
    elif char == '}':
      curr_group['end'] = i
      curr_group = curr_group['parent']
    elif char == '<':
      in_garbage = True

  return root

def score_groups(groups):
  score = groups['level']
  for child in groups['children']:
    score += score_groups(child)

  return score

def part1():
  return score_groups(parse(file_input_text))

def part2():
  return parse(file_input_text)['garbage_count']

#########
# Tests
#########

class TestSolution(unittest.TestCase):
  def test_Part1(self):
    test_cases = ['{}',
                  '{{{}}}',
                  '{{},{}}',
                  '{{{},{},{{}}}}',
                  '{<a>,<a>,<a>,<a>}',
                  '{{<ab>},{<ab>},{<ab>},{<ab>}}',
                  '{{<!!>},{<!!>},{<!!>},{<!!>}}',
                  '{{<a!>},{<a!>},{<a!>},{<ab>}}']
    self.assertEqual(score_groups(parse(test_cases[0])),1)
    self.assertEqual(score_groups(parse(test_cases[1])),6)
    self.assertEqual(score_groups(parse(test_cases[2])),5)
    self.assertEqual(score_groups(parse(test_cases[3])),16)
    self.assertEqual(score_groups(parse(test_cases[4])),1)
    self.assertEqual(score_groups(parse(test_cases[5])),9)
    self.assertEqual(score_groups(parse(test_cases[6])),9)
    self.assertEqual(score_groups(parse(test_cases[7])),3)

  def test_Part2(self):
    test_cases = ['{<>}',
                  '{<random characters>}',
                  '{<<<<>}',
                  '{<{!>}>}',
                  '{<!!>}',
                  '{<!!!>>}',
                  '{<{o"i!a,<{i<a>}']
    self.assertEqual(parse(test_cases[0])['garbage_count'],0)
    self.assertEqual(parse(test_cases[1])['garbage_count'],17)
    self.assertEqual(parse(test_cases[2])['garbage_count'],3)
    self.assertEqual(parse(test_cases[3])['garbage_count'],2)
    self.assertEqual(parse(test_cases[4])['garbage_count'],0)
    self.assertEqual(parse(test_cases[5])['garbage_count'],0)
    self.assertEqual(parse(test_cases[6])['garbage_count'],10)

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