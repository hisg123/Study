const fs = require('fs');
const stdin = (process.platform === 'linux'
  ? fs.readFileSync('/dev/stdin').toString()
  : `23 59`
).split('\n');

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let t = input();
const [a, b] = t.split(' ').map(Number);

/**
 * hour, min을 입력받아 -45 minutes 한 시간 반환
 * 
 * @param {*} hour input hour
 * @param {*} minutes input minutes
 * @returns {string} result hour, minutes
 */
let AlarmClock = function(hour, minutes) {
    minutes -= 45;
    if (minutes < 0) {
        minutes += 60;
        hour -= 1;
        if (hour < 0) {
            hour = 23;
        }
    }

    console.log(`${hour} ${minutes}`);
    return `${hour} ${minutes}`;
}

AlarmClock(a,b);
