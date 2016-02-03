'''
--- Day 5: Doesn't He Have Intern-Elves For This? ---

Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
For example:

ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
jchzalrnumimnmhp is naughty because it has no double letter.
haegwjzuvuyypxyu is naughty because it contains the string xy.
dvszwmarrgswjxmb is naughty because it contains only one vowel.

How many strings are nice?
'''

from sys import argv
'''OPEN THE FILE'''
script, file = argv
text = open(file)
i = text.read().split('\n')
#print('\n'.join('{}: {}'.format(*k) for k in enumerate(strings)))
#PART ONE
tot = 0
for line in i:
  # vowel
  vowel = filter(lambda d: d in "aeiou", line)
  # double
  double = False
  last = ""
  for char in line:
    if last:
      if char == last:
        double = True
        break
    last = char
  # bad words
  bad = any((sub in line) for sub in ["ab", "cd", "pq", "xy"])
  # finally
  if len(list(vowel)) >= 3 and double and not bad:
    tot += 1
    print("{} is nice ({})".format(line, tot))
  else:
    print("{} is naughty({}{}{})".format(line, "y" if len(list(vowel)) >= 3 else "n", "y" if double else "n", "y" if not bad else "n"))
print("Part 1: {}".format(tot))

'''
--- Part Two ---

Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
For example:

qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.

How many strings are nice under these new rules?
'''

#PART 2
tot = 0
for line in i:
  rule1 = False
  rule2 = False
  for x,char in enumerate(line):
    try:
      if line.count(char + line[x+1]) > 1:
        rule1 = True
    except IndexError:
      pass
    try:
      if char == line[x+2]:
        rule2 = True
    except IndexError:
      pass
  if rule1 and rule2:
    tot += 1
  #  print("{} is nice ({})".format(line, tot) + (" " + overlap if overlap else ""))else:
    #print("{} is naughty({}{})".format(line, "y" if rule1 else "n", "y" if rule2 else "n") + (" " + overlap if overlap else ""))
print("Part 2: {}".format(tot))
