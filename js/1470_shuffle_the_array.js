/**
 * 1470. Shuffle the Array
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].

 

Example 1:

Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7] 
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
Example 2:

Input: nums = [1,2,3,4,4,3,2,1], n = 4
Output: [1,4,2,3,3,2,4,1]
Example 3:

Input: nums = [1,1,2,2], n = 2
Output: [1,2,1,2]
 

Constraints:

1 <= n <= 500
nums.length == 2n
1 <= nums[i] <= 10^3

 */

const test1 = [2,5,1,3,4,7];
const n1 = 3;

const test2 = [1,2,3,4,4,3,2,1];
const n2 = 4;

const test3 = [1, 1, 2, 2];
const n3 = 2;

const shuffle = (nums, n) => {
    for (let i = 0; i < n; i++) {
        nums[i + n] = nums[i] << 10 | nums[i + n]
    }

    let j = 0;

    for (let i = 0; i < n; i++) {
        const y = nums[i + n] & (2 ** 10 - 1);
        const x = nums[i + n] >> 10;
        nums[j] = x;
        nums[j+1] = y;
        j+= 2;
    }
    return nums;
}

console.log('test1:= ', shuffle(test1, n1));
console.log('test2:= ', shuffle(test2, n2));