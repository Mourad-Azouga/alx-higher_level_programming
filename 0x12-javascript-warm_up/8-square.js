#!/usr/bin/node
let x, y, r;
const z = parseInt(process.argv[2]);
if (isNaN(z)) {
  console.log('Missing size');
} else {
  for (x = 0; x < z; x++) {
    r = '';
    for (y = 0; y < z; y++) {
      r += 'X';
    }
    console.log(r);
  }
}
