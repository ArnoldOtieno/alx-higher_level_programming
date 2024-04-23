#!/usr/bin/node

const arglist = process.argv.slice(2);
const numbers = arglist.map(num => parseInt(num));

if (numbers.length < 2) {
  console.log(0);
} else {
  const sortnum = numbers.sort((a, b) => b - a);
  console.log(sortnum[1]);
}
