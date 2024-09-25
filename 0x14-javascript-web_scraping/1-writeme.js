#!/usr/bin/node
// write a string to a file

const fs = require('fs');

const filePath = process.argv[2];
const content = process.argv[3];

if (!filePath || !content) {
  console.log('Usage: ./write_to_file.js <file_path> <string_to_write>');
  process.exit(1);
}

fs.writeFile(filePath, content, 'utf8', (err) => {
  if (err) {
    console.log(`Error writing to: ${err.message}`);
    process.exit(1);
  }
  // console.log(`Successfully written to ${filePath}`);
});
