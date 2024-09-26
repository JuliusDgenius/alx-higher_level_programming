#!/usr/bin/node
// a script that prints all characters of a Star Wars movie

const request = require('request');
const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
    process.exit(1);
  }
  const data = JSON.parse(body);
  for (const k of data.characters) {
    request(k, (err, response, body) => {
      if (err) {
        console.log(err);
        process.exit(1);
      }
      const character = JSON.parse(body);
      console.log(character.name);
    });
  }
});
