/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var smallestDistancePair = function(nums, k) {
    nums.sort((a, b) => a - b);
    const m = Math.max(...nums);
    const n = nums.length;
    const buckets = new Array(m + 1).fill(0);
    
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            const distance = Math.abs(nums[i] - nums[j]);
            buckets[distance]++;
        }
    }
    
    for (let distance = 0; distance <= m; distance++) {
        k -= buckets[distance];
        if (k <= 0) {
            return distance;
        }
    }
    
    return -1;
};