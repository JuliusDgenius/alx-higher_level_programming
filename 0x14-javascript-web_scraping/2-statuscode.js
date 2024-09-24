#!/usr/bin/node
// Print status code

const request = require('request');

const url = process.argv[2];

if (!url) {
  console.log('Usage: ./status_code.js <url>');
  process.exit(1);
}

request(url, (err, response) => {
  if (err) {
    console.log(`Error: ${err.message}`);
    process.exit(1);
  }
  console.log(`code: ${response.statusCode}`);
});
