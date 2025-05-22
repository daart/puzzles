/**
 * @description
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Input: prices = [7,2,6,8,3,14]
Output: 12
 */

const maxProfit = function (prices) {
  let maxProfit = 0;
  let currentMin = prices[0];

  for (let i = 0; i < prices.length; i++) {
    if (prices[i] < currentMin) {
      currentMin = prices[i];
    }

    if (prices[i] - currentMin > maxProfit) {
      maxProfit = prices[i] - currentMin;
    }

    // OR use Math for it
    // for (let i = 0; i < prices.length; i++) {
    //   currentMin = Math.min(prices[i], currentMin);
    //   currentMax = Math.max(prices[i] - currentMin, currentMax);
    // }
  }

  return maxProfit;
};

const prices1 = [7, 1, 5, 3, 6, 4];
const prices2 = [7, 6, 4, 3, 1];
const prices3 = [2, 4, 1];
const prices4 = [1, 2, 3, 4, 5];
const prices5 = [5, 4, 3, 2, 1];
const prices6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15];
console.log(maxProfit(prices1)); // 5
console.log(maxProfit(prices2)); // 0
console.log(maxProfit(prices3)); // 2
console.log(maxProfit(prices4)); // 4
console.log(maxProfit(prices5)); // 0
console.log(maxProfit(prices6)); // 14
