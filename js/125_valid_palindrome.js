/**
 * 
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
 */

// non optimal solution time O(n) space O(n)
const isPalindrome = (str) => {
  const regex = /[^a-zA-Z0-9]/g;
  const formatted = str.replace(regex, "").toLowerCase();

  for (let start = 0; start < formatted.length / 2; start++) {
    if (formatted[start] !== formatted[formatted.length - 1 - start]) {
      return false;
    }
  }

  return true;
};

// optimal solution time O(n) space O(1)

const inAlphaNumeric = (char) => {
  if (
    (char >= "a" && char <= "z") ||
    (char >= "A" && char <= "Z") ||
    (char >= "0" && char <= "9")
  ) {
    return true;
  }
  return false;
};
const isPalindromeOptimal = (str) => {
  let startPointer = 0;
  let endPointer = str.length - 1;

  while (startPointer < endPointer) {
    while (startPointer < endPointer && !inAlphaNumeric(str[startPointer])) {
      startPointer++;
    }
    while (startPointer < endPointer && !inAlphaNumeric(str[endPointer])) {
      endPointer--;
    }

    if (str[startPointer].toLowerCase() !== str[endPointer].toLowerCase()) {
      return false;
    }
    startPointer++;
    endPointer--;
  }

  return true;
};

const str1 = "A man, a plan, a canal: Panama";
const str2 = "raceacar";
const res1 = isPalindromeOptimal(str1);
const res2 = isPalindromeOptimal(str2);
console.log(res1); // true
console.log(res2); // false
