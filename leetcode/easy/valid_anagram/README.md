# Objective
Determine if two given strings are anagrams by comparing their character compositions.

# Definition
An anagram is a word formed by rearranging letters of another word.

# Problem
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input:
```
s = "anagram", t = "nagaram"
```

Output:
```
true
```

Example 2:

Input:
```
s = "rat", t = "car"
```

Output:
```
false
```

# Answer
See the attached code screenshots.

Since an anagram is just the characters of one word rearranged to make another word, I wasn't concerned about validating whether it was an actual word for this particular problem.

Instead, I approached the answer to this problem by focusing and validating only a few sets of criteria.

1. Are both provided arguments the same length?
    1. Since an anagram rearranges characters without subtracting any of them, we can quickly rule out if the provided arguments are suitable to be an anagram.
    1. If they are the same length, we do nothing. Otherwise, we return False.
1. When extracting unique characters of each provided argument, does the set of unique characters from both equal the same length?
    1. The check we did in step 1 isn't sufficient to determine if the provided arguments are anagrams. There could be a test case that provides arguments that are the same length but may contain different characters.
    1. This step extracts the unique characters from each argument using the set() method, then we check their lengths to ensure that each provided argument has the same length of unique characters.
    1. If they both contain the same length of unique characters, then we do nothing. Otherwise, we return False.
1. Does each unique characters from one set exists in the other?
    1. The unique characters from the first provided argument should exist in the second provided argument. If they don't, then we know that there's a character mismatch between the two provided arguments. This validates that this could not be an anagram.
    1. If the unique characters from the first provided argument exist in the second provided argument, we do nothing. Otherwise, we return False.
1. Are the unique character counts from the first provided argument equal to the unique character counts from the second provided argument?
    1. Anagrams are a rearrangement of characters from one word meaning both provided arguments should have the same unique character counts. For example, if the first argument has a count of 3 for the letter 'a' and the second argument provided has a count of 2 for the letter 'a' then we know they cannot be an anagram because of this discrepancy.
    1. If the each unique character count from the first provided argument equals the same count from the second provided argument, we do nothing. Otherwise, return False.

The above four scenarios are sufficient to determine if two provided arguments are anagrams.

For better time complexity, I leveraged dictionary and list comprehensions which perform great compared to a multi-line for-loop.