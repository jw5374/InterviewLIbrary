/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let start = init
    return {
        increment: () => {
            init++
            return init
        },
        decrement: () => {
            init--
            return init
        },
        reset: () => {
            init = start
            return init
        },
    }
};
