#!/usr/bin/node
// Script displays the status code of a get request
const request = require('request');

// Extract the URL from command-line arguments
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  console.log('Status code:', response.statusCode);
});
