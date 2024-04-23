#!/usr/bin/node

const count = process.argv[2];
const verify = parseInt(count);
const x = 'x';

if (isNaN(verify)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < verify; i++) {
    console.log(x.repeat(verify));
  }
}
