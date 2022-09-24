const fs = require('fs');
const stdin = (process.platform === 'linux' ?
    fs.readFileSync('/dev/stdin'):
    4
);

const input = (() => {
    return () => stdin;
})();

let SugarDeliver = function (sugar) {
    let cnt = 0;

    while (true) {
        if (sugar % 5 === 0) {
            cnt += sugar / 5;
            return cnt;
        }

        if (sugar < 0) {
            return -1;
        }

        sugar -= 3;
        cnt++;
    }
}

console.log(SugarDeliver(input()));