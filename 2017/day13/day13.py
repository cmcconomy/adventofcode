import unittest;
import re;
import copy

problem_num='13'
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

def to_firewalls(lines):
  firewalls = {}
  for line in lines:
    parts = line.split(': ')
    firewall = {'depth': int(parts[1]), 'scanner_pos': 0, 'move_down': True}
    firewalls[int(parts[0])] = firewall

  return firewalls

def debug_print(firewalls, packet_pos):
  if False:
    for pos in range(0,max(firewalls.keys())+1):
      if pos in firewalls.keys(): 
        fwstr = ''
        if firewalls[pos]['scanner_pos'] == 0:
          fwstr = 'S'
        else:
          fwstr = ' '

        if pos == packet_pos:
          if( fwstr == 'S'):
            fwstr = '(' + fwstr + ':' + str(packet_pos * firewalls[packet_pos]['depth']) + ') '
          else:
            fwstr = '(' + fwstr + ') '
        else:
          fwstr = '[' + fwstr + '] '

        fwstr = str(pos) + ': ' + fwstr

        for i in range(1,firewalls[pos]['depth']):
          if i == firewalls[pos]['scanner_pos']:
            fwstr += '[S] '
          else:
            fwstr += '[ ] '

        print(fwstr)

      else:
        if pos == packet_pos:
          print(str(pos) + ': (.)')
        else:
          print(str(pos) + ': ...')


def move_scanners(firewalls, packet_pos):
  # Scanners move forward
  for pos in firewalls.keys():
    if firewalls[pos]['move_down']:
      if firewalls[pos]['scanner_pos'] < firewalls[pos]['depth']-1:
        firewalls[pos]['scanner_pos'] += 1
      else:
        firewalls[pos]['move_down'] = False
        firewalls[pos]['scanner_pos'] -= 1
    else:
      if firewalls[pos]['scanner_pos'] > 0:
        firewalls[pos]['scanner_pos'] -= 1
      else:
        firewalls[pos]['move_down'] = True
        firewalls[pos]['scanner_pos'] += 1

def iterate(firewalls, next_packet_pos, current_severity=0, delay=0):
  this_packet_pos = next_packet_pos

  caught_this_round = False

  if next_packet_pos == 0 and delay > 0:
    for i in range(1,delay+1):
      move_scanners(firewalls,0)

  # Did we get caught?
  if( this_packet_pos not in firewalls ):
    # unmonitored layer
#    print('moved to pos ' + str(this_packet_pos) + ', no firewall here!')
    pass
  else:
    if( firewalls[this_packet_pos]['scanner_pos'] == 0 ):
      caught_this_round = True
      # print('moved to pos ' + str(this_packet_pos) + ', firewall here of depth ' + str(firewalls[this_packet_pos]['depth']) + ' and the scanner is at pos ' + str(firewalls[this_packet_pos]['scanner_pos']))
      # print('uh oh.. cost us ' + str(this_packet_pos * firewalls[this_packet_pos]['depth']))
      current_severity += this_packet_pos * firewalls[this_packet_pos]['depth']

  move_scanners(firewalls, this_packet_pos)

  if( this_packet_pos == max(firewalls.keys()) or (delay != 0 and caught_this_round)):
    # We made it to the end! No more iterations.. or we are breaking because this is a test of delay for stealth.
    return (firewalls, this_packet_pos+1, current_severity, caught_this_round)
  else:
    return iterate(firewalls, this_packet_pos+1, current_severity, delay)

def dont_get_caught(firewalls):
  delay = 0
  # run the first no-recurse iteration -- meaning we move all the firewalls forward
  while( True ):
    delay += 1
    iter_firewalls = copy.deepcopy(firewalls) # deep copy allows us to return an independently modified firewalls dict
    (iter_firewalls, this_packet_pos, severity, caught_this_round) = iterate(iter_firewalls, 0, delay=delay)
    if (not caught_this_round):
      return delay

def part1():
  firewalls = to_firewalls(basic_split(file_input_text))
  (firewalls, next_packet_pos, severity, caught_this_round) = iterate(firewalls,0)
  return severity

def part2():
  firewalls = to_firewalls(basic_split(file_input_text))
  return(dont_get_caught(firewalls))

#########
# Tests
#########

class TestSolution(unittest.TestCase):
  def test_Part1(self):
    test_input="""0: 3
1: 2
4: 4
6: 4"""
    firewalls = to_firewalls(basic_split(test_input))
    (firewalls, next_packet_pos, severity, caught_this_round) = iterate(firewalls,0)
    self.assertEqual(severity,24)

  def test_Part2(self):
    test_input="""0: 3
1: 2
4: 4
6: 4"""
    firewalls = to_firewalls(basic_split(test_input))
    self.assertEqual(dont_get_caught(firewalls),10)

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