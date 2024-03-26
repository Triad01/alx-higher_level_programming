#!/usr/bin/node
// Script reads and print the content of a file

const fs = require('fs');

const filePath = process.argv[2];

fs.readFile(filePath, 'utf8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
