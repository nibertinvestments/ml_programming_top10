const items = [12, 18, 21, 9, 31];
const total = items.reduce((sum, value) => sum + value, 0);
console.log('Total:', total);
console.log('Average:', (total / items.length).toFixed(2));
