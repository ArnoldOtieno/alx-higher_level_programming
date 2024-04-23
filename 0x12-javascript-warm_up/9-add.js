#!/usr/bin/node

const firstArg = process.argv[2];
const secondArg = process.argv[3];
const a = parseInt(firstArg);
const b = parseInt(secondArg);

function add (a, b) {
  a += b;
  console.log(a);
}
if (isNaN(a) || isNaN(b)) {
  console.log('NaN');
} else {
  add(a, b);
}
