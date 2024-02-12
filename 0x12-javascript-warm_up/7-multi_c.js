#!/usr/bin/node
let x;
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing number of occurences');
} else {
  for (x = 0; x < parseInt(process.argv[2]); x++) {
    console.log('C is fun');
  }
}
