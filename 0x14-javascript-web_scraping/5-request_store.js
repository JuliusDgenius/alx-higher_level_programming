#!/usr/bin/node
// a script that gets the contents of a webpage and stores it in a file.
// The first argument is the URL to request
// The second argument the file path to store the body response
// The file must be UTF-8 encoded
// You must use the module request

const request = require('request');
const fs = require('fs');
const cheerio = require('cheerio');

const url = process.argv[2];
const filePath = process.argv[3];


if (!url || !filePath) {
	console.log("Usage: ./5-request_store.js <url> <filePath>");
	process.exit(1);
}

request(url, filePath, (err, response, body) => {
	if (err) {
		console.log(`${err} occurred.`);
		process.exit(1);
	}

	fs.writeFile(filePath, body, 'utf8', (err) => {
		if (err) {
			console.log(`Error: ${err} occurred while writing file.`);
			process.exit(1);
		}
		 // console.log(`The content of ${url}${filePath} has been successfully written to ${filePath}.`);
	});
});