function once(fn) {
    let called_yet = false
    return function (...args) {
        if (called_yet) { return undefined; }
        called_yet = true;
        return fn(...args);
    };
}