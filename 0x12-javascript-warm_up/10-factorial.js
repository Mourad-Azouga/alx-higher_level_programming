#!/usr/bin/node
function fac (a) {
  if (a === 0) {
    return (1);
  }
  return (a * fac(a - 1));
}
if (isNaN(parseInt(process.argv[2]))) {
  console.log(fac(1));
} else {
  console.log(fac(parseInt(process.argv[2])));
}
