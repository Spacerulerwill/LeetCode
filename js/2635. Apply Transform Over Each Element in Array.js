/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    let newArr = new Array(arr.length);
    arr.forEach((item, idx) => newArr[idx] = fn(item, idx));
    return newArr;
};