/**
 * Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
 */

const isValidAnagram = (s1, s2) => {
  if (s1.length !== s2.length) {
    return false;
  }

  const charMapCounter = {};

  // Count characters in first string
  for (let char of s1) {
    if (char in charMapCounter) {
      charMapCounter[char] += 1;
    } else {
      charMapCounter[char] = 1;
    }
  }

  // Check characters in second string
  for (let char2 of s2) {
    if (!(char2 in charMapCounter)) {
      return false;
    }

    charMapCounter[char2] -= 1;

    if (charMapCounter[char2] < 0) {
      return false;
    }
  }

  // Ensure all counts are zero
  for (let char in charMapCounter) {
    if (charMapCounter[char] !== 0) {
      return false;
    }
  }

  return true;
};

const ts1 = "anagram";
const ts2 = "nagaram";

const res = isValidAnagram(ts1, ts2);
console.log(res);
