const fs = require('fs');
const { mainModule } = require('process');
const stdin = (process.platform === 'linux' ?
    fs.readFileSync('/dev/stdin') :
    `2
    10
    15`
).split('\n');

const input = (() => {
    return () => stdin.map(element => {
        return (Number(element));
    });
})();

let GetMaxLope = function (lopes) {
    
    return lopes[0]*Math.min(...lopes.slice(1));
}


console.log(GetMaxLope(input()));