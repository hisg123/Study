const fs = require('fs');
const stdin = (process.platform === 'linux' ?
    fs.readFileSync('/dev/stdin') :
    18
);

const input = (() => {
    return () => stdin;
})();

let SugarDeliver = function (sugar) {
    const containers = [5, 3];
    const LAST_IDX = containers.length - 1;
    let cnt = 0;
    let index = 0;

    while (sugar > 0) {
        if (sugar >= containers[index]) {
            console.log('sugar: '+sugar);
            console.log('container: ' + containers[index]);
            console.log('cnt:' + cnt);
            sugar -= containers[index];
            if (index === LAST_IDX && sugar < containers[LAST_IDX] && sugar !== 0) {
                console.log(-1)
                return -1;
            } else if (sugar < containers[index] && sugar > 0) {
                sugar += containers[index];
                index++;
            } else {
                cnt++;
            }

        } else {
            index++;
        }
    }

    console.log(cnt);
    return cnt;
}

SugarDeliver(input());