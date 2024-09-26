#!/usr/bin/node
// A script that prints the number of movies where the character “Wedge Antilles” is present.

// const request = require('request');

// const url = process.argv[2];

// request(url, (err, response, body) => {
//   if (err) {
//     console.log(`Error: ${err.message}`);
//     process.exit(1);
//   }

//   if (response.statusCode === 200) {
//     const data = JSON.parse(body);
//     let wedgeMoviesCount = 0;

//     // Loop through each film and check for "Wedge Antilles"
//     data.results.forEach(film => {
//       if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
//         wedgeMoviesCount++;
//       }
//     });

//     console.log(wedgeMoviesCount);
//   }
// });

const request = require('request');
const url = process.argv[2];
const characterId = '18';
let count = 0;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    data.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(characterId)) {
          count += 1;
        }
      });
    });
    console.log(count);
  }
});
