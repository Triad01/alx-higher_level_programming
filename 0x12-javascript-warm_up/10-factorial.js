#!/usr/bin/node

const arg = process.argv[2];

function factorial (num) {
  if (num === 0 || !Number(num)) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

console.log(factorial(arg));
