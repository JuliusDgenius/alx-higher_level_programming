#!/usr/bin/node
const myVar = process.argv[2];
const convertToInt = parseInt(myVar);
if (isNaN(convertToInt)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${convertToInt}`);
}
