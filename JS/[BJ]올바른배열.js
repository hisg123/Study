const fs = require('fs');
const stdin = (process.platform === 'linux'
    ? fs.readFileSync('/dev/stdin').toString().trim()
    :
    `7
    6
    1
    9
    5
    7
    15
    8`
).split('\n');

const input = (() => {
    return () => stdin.map(element => {
        return Number(element.trim())
    });
})()

let ValidArray = function (n, list) {
    let result = "";
    let cntArray = [];
    list.sort((a, b) => a - b);

    for (let i = 0; i < list.length; i++) {
        let cnt = 0;
        let index = 0;
        let value = list[i];

        while (index < 4) {
            value++;
            if (value !== list[i + 1 + index - cnt]) { cnt++; }
            index++;
        }
        cntArray.push(cnt);
    }
    return Math.min(...cntArray);
}

console.log(ValidArray(input()[0], input().slice(1)));