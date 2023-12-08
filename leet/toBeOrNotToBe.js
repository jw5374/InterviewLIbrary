/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    return {
        toBe: (x) => {
            if(x === val) {
                return true
            }
            throw new Error("Not Equal")
        },
        notToBe: (x) => {
            if(x !== val) {
                return true
            }
            throw new Error("Equal")
        }
    }
};
