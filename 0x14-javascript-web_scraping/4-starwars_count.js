#!/usr/bin/node

// Import the request module
const request = require('request');

// Function to count movies with "Wedge Antilles"
function countMovies(apiUrl) {
    // Define the character ID for Wedge Antilles
    const characterId = 18;
    // Send a GET request to the API URL
    request(apiUrl, (error, response, body) => {
        if (error) {
            console.error('Error fetching data:', error);
            return;
        }
        if (response.statusCode !== 200) {
            console.error('Unexpected status code:', response.statusCode);
            return;
        }
        // Parse the JSON response body
        const films = JSON.parse(body).results;
        // Filter films where Wedge Antilles is present
        const filteredFilms = films.filter(film =>
            film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
        );
        // Print the number of filtered films
        console.log(filteredFilms.length);
    });
}

// Get the API URL from command line argument
const apiUrl = process.argv[2];

// Check if API URL is provided
if (!apiUrl) {
    console.error('Please provide the API URL as an argument.');
} else {
    // Call the function to count movies with Wedge Antilles
    countMovies(apiUrl);
}
