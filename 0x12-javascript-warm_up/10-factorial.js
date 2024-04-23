#!/usr/bin/node

function factorial (par1) {
  if (isNaN(par1)) {
    return 1;
  } else if (par1 === 0) {
    return 1;
  } else {
    return par1 * factorial(par1 - 1);
  }
}

const arg = parseInt(process.argv[2]);
const mreturn = factorial(arg);
console.log(mreturn);
