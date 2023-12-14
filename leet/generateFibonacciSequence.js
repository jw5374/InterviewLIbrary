/**
 * @return {Generator<number>}
 */
var fibGenerator = function*() {
    let first = 0
    let second = 1
    for(let i = 0; i < 51; i++) {
        if(i < 2) {
            yield i
        }
        let temp = first + second
        first = second
        second = temp
        yield second
    }
};
