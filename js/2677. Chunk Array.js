/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    let result = []
    for (i = 0; i < arr.length; i += size) {
        const slice = arr.slice(i, i >= arr.length ? size - 1 : i + size);
        result.push(slice);
    }
    return result;
};