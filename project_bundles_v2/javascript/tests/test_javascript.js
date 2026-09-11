const fs = require('fs');
const rows = fs.readFileSync('input.csv', 'utf8').trim().split('
').slice(1);
console.log(rows.length);
