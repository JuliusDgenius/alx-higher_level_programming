#!/usr/bin/node
// a script that prints the title of a Star
// Wars movie where the episode number matches a given integer.

const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

if (!id) {
  console.log('Usage: ./3-starwars_title.js <id>');
  process.exit(1);
}

request(url, (err, response, body) => {
  if (err) {
    console.log(`Error: ${err} occurred`);
    process.exit(1);
  }
  if (response.statusCode === 200) {
    const data = JSON.parse(body);
    console.log(data.title);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
