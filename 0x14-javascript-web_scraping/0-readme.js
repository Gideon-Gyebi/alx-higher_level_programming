#!/usr/bin/node
// A script that reads and prints the content of a given file.
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', function (error, content) {
  console.log(error || content);
});
