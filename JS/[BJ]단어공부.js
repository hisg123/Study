const fs = require('fs');
const stdin = (process.platform === 'linux'
  ? fs.readFileSync('/dev/stdin').toString().trim()
  : `zZa`
);

const input = (() => {
  return () => stdin;
})();

let WordStudy = function(word) {
    let dict = {};

    for(let i =0; i< word.length; i++) {
        let upper = word[i].toUpperCase();
        if (upper in dict) {
            dict[upper] += 1; 
        } else {
            dict[upper] = 1;
        }
    }

    let keys = Object.keys(dict);
    let maxKey = Object.keys(dict)[0];
    let maxValue = dict[maxKey];
    
    for (let i = 0; i < keys.length; i++) {
        let element = keys[i];
        if (maxValue < dict[element]) { 
            maxValue = dict[element];
            maxKey = element;
        } else if (maxKey!== element && maxValue === dict[element]) {
            maxKey = '?';
        }
    }

    console.log(maxKey);
    return maxKey;
}

WordStudy(input())