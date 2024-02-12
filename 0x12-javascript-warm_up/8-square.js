#!/usr/bin/node

const squareSize = process.argv[2];

if (!Number(squareSize)) console.log('Missing size');
else {
  for (let i = 0; i < squareSize; i++) {
    console.log('x'.repeat(squareSize));
  }
}
