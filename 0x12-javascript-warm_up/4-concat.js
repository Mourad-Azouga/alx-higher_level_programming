#!/usr/bin/node
let exp1;
let exp2;
if (process.argv[2] === undefined) {
  exp1 = 'undefined';
} else {
  exp1 = process.argv[2];
}
if (process.argv[3] === undefined) {
  exp2 = 'undefined';
} else {
  exp2 = process.argv[2];
}
console.log(exp1 + ' is ' + exp2);
