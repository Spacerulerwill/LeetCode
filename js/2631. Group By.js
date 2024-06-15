/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    let res = {}
    this.forEach((val, idx) => {
        let key = fn(val)
        if (key in res) {
            res[key].push(val);
        } else {
            res[key] = [val];
        }
    });
    return res
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */