/**
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Example 4:
Input nums = [4, 1, 7, 13, 9], target = 16
Output: [2, 4]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

 */

const nums1 = [2, 7, 11, 15];
const target1 = 9;
const nums2 = [3, 2, 4];
const target2 = 6;
const nums3 = [3, 3];
const target3 = 6;
const nums4 = [4, 1, 7, 13, 9];
const target4 = 16;
const nums5 = [1, 3, 5, 6, 8, 11, 13, 15];
const target5 = 24;

const twoSum = (nums, target) => {
  const map = new Map();
  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i];

    if (map.has(complement)) {
      return [map.get(complement), i];
    }
    map.set(nums[i], i);
  }
  // nums.forEach((num, i) => {
  //   if (map.has(target - num)) {
  //     return [map.get(target - num), i];
  //   }
  //   map.set(num, i);
  // });
};

const res1 = twoSum(nums1, target1);
console.log(res1);

const res2 = twoSum(nums2, target2);
console.log(res2);

const res3 = twoSum(nums3, target3);
console.log(res3);

const res4 = twoSum(nums4, target4);
console.log(res4);

const res5 = twoSum(nums5, target5);
console.log(res5);
