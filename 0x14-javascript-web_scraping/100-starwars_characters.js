#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID as the first argument.');
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Unexpected status code:', response.statusCode);
    process.exit(1);
  }

  const movieData = JSON.parse(body);
  const charactersUrls = movieData.characters;

  charactersUrls.forEach((characterUrl) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        process.exit(1);
      }

      if (response.statusCode !== 200) {
        console.error('Unexpected status code:', response.statusCode);
        process.exit(1);
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});

