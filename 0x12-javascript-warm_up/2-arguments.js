#!/usr/bin/node

const arglength = process.argv.length;

if (arglength === 2) {
  console.log('No argument');
} else if (arglength === 3) {
  console.log('Argument Found');
} else {
  console.log('Arguments found');
}
