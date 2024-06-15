/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    let k = n - 1
    return function() {
        k += 1
        return k;
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */