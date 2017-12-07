import unittest;
import re;

problem_num='7'
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

def to_progs(lines):
  progs = []
  for line in lines:
    chunks = line.split()
    prog = {}
    prog['name'] = chunks[0]
    prog['weight'] = int(chunks[1][1:-1])

    if len(chunks) > 2:
      prog['child_names'] = line.split(' -> ')[1].split(', ')
    else:
      prog['child_names'] = []
    progs.append(prog)

  return progs

def map_progs(progs):
  progmap = {}
  for prog in progs:
    progmap[prog['name']] = prog

  return progmap

def find_root(progmap):
  root_possibilities = list(progmap.keys())

  for name in progmap.keys():
    prog = progmap[name]
    for childname in prog['child_names']:
      root_possibilities.remove(childname)

  return progmap[root_possibilities[0]]

def get_tree(progs):
  progmap = map_progs(progs)
  root = find_root(progmap)

  return (root,progmap)

def measure_accum_weights(prog, progmap):
  prog['accum_weight'] = prog['weight']

  for childname in prog['child_names']:
    prog['accum_weight'] += measure_accum_weights(progmap[childname],progmap)

  return prog['accum_weight']

def adjusted_balanced_weight(prog, progmap, imbalance_amount=None):
  weights = []
  for childname in prog['child_names']:
    weights.append(progmap[childname]['accum_weight'])

  imbalance_index=-1
  for i, childname in enumerate(prog['child_names']):
    if weights.count(progmap[childname]['accum_weight']) == 1:
      imbalance_index = i
      break

  if imbalance_index == -1:
    # all children are equal.. so we're the problem!
    return prog['weight'] - imbalance_amount
  else:
    if (imbalance_amount == None):
      # There is only one imbalance so this carries forward.. we can just calc once
      imbalanced_weight = progmap[prog['child_names'][imbalance_index]]['accum_weight'];
      weights.remove(imbalanced_weight)
      imbalance_amount = imbalanced_weight - weights[0]

    imbalanced_prog = progmap[prog['child_names'][imbalance_index]]
    return adjusted_balanced_weight(imbalanced_prog, progmap, imbalance_amount)

def part1():
  progs = to_progs(basic_split(file_input_text))
  (root,progmap) = get_tree(progs)
  return root['name']

def part2():
  progs = to_progs(basic_split(file_input_text))
  (root,progmap) = get_tree(progs)
  measure_accum_weights(root,progmap)
  return adjusted_balanced_weight(root,progmap)

#########
# Tests
#########

class TestSolution(unittest.TestCase):
  def test_Part1(self):
    test_input="""pbga (66)
                  xhth (57)
                  ebii (61)
                  havc (66)
                  ktlj (57)
                  fwft (72) -> ktlj, cntj, xhth
                  qoyq (66)
                  padx (45) -> pbga, havc, qoyq
                  tknk (41) -> ugml, padx, fwft
                  jptl (61)
                  ugml (68) -> gyxo, ebii, jptl
                  gyxo (61)
                  cntj (57)"""
    progs = to_progs(basic_split(test_input))
    (root,progmap) = get_tree(progs)
    self.assertEqual(root['name'],'tknk')

  def test_Part2(self):
    test_input="""pbga (66)
                  xhth (57)
                  ebii (61)
                  havc (66)
                  ktlj (57)
                  fwft (72) -> ktlj, cntj, xhth
                  qoyq (66)
                  padx (45) -> pbga, havc, qoyq
                  tknk (41) -> ugml, padx, fwft
                  jptl (61)
                  ugml (68) -> gyxo, ebii, jptl
                  gyxo (61)
                  cntj (57)"""
    progs = to_progs(basic_split(test_input))
    (root,progmap) = get_tree(progs)
    measure_accum_weights(root,progmap)
    self.assertEqual(adjusted_balanced_weight(root,progmap),60)

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