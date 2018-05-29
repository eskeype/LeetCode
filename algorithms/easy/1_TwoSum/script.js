/* O(n) time and space */
function twoSum(nums, target) {
    var hash = {};
    for (var index = 0; index < nums.length; index++) {
        if (hash[target-nums[index]] !== undefined) {
            return [hash[target - nums[index]], index]; 
        }
        hash[nums[index]] = index;
    }
}