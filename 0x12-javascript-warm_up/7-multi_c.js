#!/usr/bin/node

const multiplier = process.argv[2];

let i;

if (!Number(multiplier)) console.log('Missing number of occurrences');
else {
  for (i = 0; i < multiplier; i++) {
    console.log('C is fun');
  }
}
