const fs = require('fs');
const lines = fs.readFileSync('input.csv', 'utf8').trim().split('
');
console.log(lines.length);
