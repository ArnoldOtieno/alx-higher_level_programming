#!/usr/bin/node

let x = process.argv[2];

x = parseInt(x);
if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    let store = '';
    for (let j = 0; j < x; j++) {
      store += 'x';
    }
    console.log(store + '\n');
  }
}
