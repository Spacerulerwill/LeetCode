/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    if (nums.length == 0) {
        return init
    }
    res = init
    nums.forEach(function(value, idx){
        res = fn(res, value)
    });
};