/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
    return new Promise((resolve, reject) => {
        const results = new Array(functions.length);
        let completed = 0;
        functions.forEach(function(fn, idx) {
            fn()
            .then(val => {
                results[idx] = val;
                completed += 1;
                if (completed == functions.length) {
                    resolve(results);
                }
            })
            .catch(reason => reject(reason));
        });
    })
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */