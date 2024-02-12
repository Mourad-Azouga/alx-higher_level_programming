#!/usr/bin/node
let max, smax;
if (process.argv.length < 4) {
  smax = 0;
} else {
  let i;
  max = smax = process.argv[2];
  for (i = 2; i < process.argv.length; i++) {
    if (process.argv[i] > max) {
      smax = max;
      max = process.argv[i];
    }
  }
}
console.log(smax);
