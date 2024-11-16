#!/usr/bin/env node

const request = require('request');

// Check for the correct number of arguments
if (process.argv.length !== 3) {
    console.error("Usage: ./0-starwars_characters.js <movie_id>");
    process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Fetch the movie data
request(apiUrl, (error, response, body) => {
    if (error) {
        console.error("Error:", error);
        process.exit(1);
    }

    if (response.statusCode === 404) {
        console.error("Error: Movie not found");
        process.exit(1);
    }

    if (response.statusCode !== 200) {
        console.error("Error:", `Status code ${response.statusCode}`);
        process.exit(1);
    }

    // Parse the JSON response
    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    // Fetch and print each character's name
    characters.forEach((url) => {
        request(url, (err, res, charBody) => {
            if (err) {
                console.error("Error:", err);
                return;
            }
            if (res.statusCode !== 200) {
                console.error("Error:", `Status code ${res.statusCode}`);
                return;
            }

            const character = JSON.parse(charBody);
            console.log(character.name);
        });
    });
});
