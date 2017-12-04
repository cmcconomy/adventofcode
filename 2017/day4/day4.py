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

def is_valid(passphrase, check_anagram=False):
  # maintain a hashmap as a quick lookup of what we've encountered
  word_log={}
  words = [word for word in passphrase.split()]

  for word in words:
    if check_anagram:
      # sort words by character, so that anagrams are equal to each other
      word = ''.join(sorted(list(word)))

    if word in word_log:
      return False
    else:
      word_log[word] = True

  return True;

def num_valid_passphrases(passphrases, check_anagram=False):
  count=0;
  for passphrase in passphrases:
    if is_valid(passphrase, check_anagram):
      count += 1

  return count

def part1():
  return num_valid_passphrases(basic_split(file_input_text))

def part2():
  return num_valid_passphrases(basic_split(file_input_text), True)

#########
# Tests
#########

class TestSolution(unittest.TestCase):
  def test_Part1(self):
    self.assertEqual(is_valid('aa bb cc dd ee'),True)
    self.assertEqual(is_valid('aa bb cc dd aa'),False)
    self.assertEqual(is_valid('aa bb cc dd aaa'),True)

  def test_Part2(self):
    self.assertEqual(is_valid('abcde fghij', True),True)
    self.assertEqual(is_valid('abcde xyz ecdab', True),False)
    self.assertEqual(is_valid('a ab abc abd abf abj', True),True)
    self.assertEqual(is_valid('iiii oiii ooii oooi oooo', True),True)
    self.assertEqual(is_valid('oiii ioii iioi iiio', True),False)

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