/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let newArray = [];
    arr.forEach(function(item, index) {
        if (fn(item, index)) {
            newArray.push(item)
        }
    });
    return newArray;
};