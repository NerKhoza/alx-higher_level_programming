#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

// Make the request to the specified URL
request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  // Write the response body to the specified file
  fs.writeFile(filePath, body, { encoding: 'utf-8' }, (err) => {
    if (err) {
      console.error('Error writing file:', err);
    } else {
      console.log(`Successfully saved the response body to ${filePath}`);
    }
  });
});

