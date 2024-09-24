#!/usr/bin/node
// Script to read and prints the content of a file

const fs = require('fs');

const file = process.argv[2];

if (!file) {
  console.log('File does not exit');
  process.exit(1);
}

fs.readFile(file, 'utf8', (err, data) => {
  if (err) {
    console.log(`Error reading file: ${err.message}`);
  } else {
    console.log(data);
  }
});
