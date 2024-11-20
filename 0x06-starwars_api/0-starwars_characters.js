#!/usr/bin/node

const request = require('request');

const movieID = process.argv[2];
const apiURL = 'https://swapi-api.hbtn.io/api/films/' + movieID;
let characterURLs = [];
const characterNames = [];

const fetchCharacterURLs = async () => {
  await new Promise(resolve => request(apiURL, (error, response, body) => {
    if (error || response.statusCode !== 200) {
      console.error('Error: ', error, '| StatusCode: ', response.statusCode);
    } else {
      const parsedBody = JSON.parse(body);
      characterURLs = parsedBody.characters;
      resolve();
    }
  }));
};

const fetchCharacterNames = async () => {
  if (characterURLs.length > 0) {
    for (const url of characterURLs) {
      await new Promise(resolve => request(url, (error, response, body) => {
        if (error || response.statusCode !== 200) {
          console.error('Error: ', error, '| StatusCode: ', response.statusCode);
        } else {
          const parsedBody = JSON.parse(body);
          characterNames.push(parsedBody.name);
          resolve();
        }
      }));
    }
  } else {
    console.error('Error: No characters found');
  }
};

const printCharacterNames = async () => {
  await fetchCharacterURLs();
  await fetchCharacterNames();

  for (const name of characterNames) {
    if (name === characterNames[characterNames.length - 1]) {
      process.stdout.write(name);
    } else {
      process.stdout.write(name + '\n');
    }
  }
};

printCharacterNames();
