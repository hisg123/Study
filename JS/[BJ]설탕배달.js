const fs = require('fs');
const stdin = (process.platform === 'linux' ?
    fs.readFileSync('/dev/stdin') :
    21
);

const input = (() => {
    return () => stdin;
})();

let SugarDeliver = function (sugar) {
    const containers = [5, 3];
    const LAST_IDX = containers.length - 1;
    let temp = {
        sugar: sugar,
        cnt: 0
    };
    let cnt = 0;
    let index = 0;

    while (sugar > 0) {
        console.log(`sugar: ` + sugar);
        console.log(`container: ` + containers[index]);
        console.log(`cnt: ` + cnt);
        if (sugar >= containers[index]) {
            temp['sugar'] = sugar;
            temp['cnt'] = cnt;
            sugar -= containers[index];
            cnt++;
        } else {
            if (index === LAST_IDX) {
                cnt = -1;
                break;
            } else if (sugar % containers[index + 1] !== 0) {
                sugar = temp['sugar'];
                cnt = temp['cnt'];
                index++;
            } else {
                index++;
            }
        }
    }

    return cnt;
}

console.log(SugarDeliver(input()));