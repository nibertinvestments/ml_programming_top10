const values = [12, 18, 21, 9, 31];
const total = values.reduce((sum, value) => sum + value, 0);
console.log('Total:', total);
console.log('Average:', (total / values.length).toFixed(2));
