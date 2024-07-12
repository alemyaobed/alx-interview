#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch movie:', response.statusCode);
    return;
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  printCharactersInOrder(characters, 0);
});

function printCharactersInOrder (characters, index) {
  if (index >= characters.length) {
    return;
  }

  request(characters[index], (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }

    if (response.statusCode !== 200) {
      console.error('Failed to fetch character:', response.statusCode);
      return;
    }

    const character = JSON.parse(body);
    console.log(character.name);

    printCharactersInOrder(characters, index + 1);
  });
}
