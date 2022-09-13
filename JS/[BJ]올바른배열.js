
const fs = require('fs');
const { resourceLimits } = require('worker_threads');
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
        return Number(element.trim()[[

        ]])
    });
})()

let ValidArray = function (n, list) {
    let result = "";
    list.sort((a, b) => a - b);

    for (let i = 0; i < list.length; i++) {
        
    }   
    console.log(list);
    return result;
}

ValidArray(input()[0], input().slice(1));