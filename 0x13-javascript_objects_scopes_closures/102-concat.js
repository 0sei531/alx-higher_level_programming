#!/usr/bin/node

const fs = require('fs');

// Read the content of the first file
fs.readFile(process.argv[2], 'utf8', (err, data1) => {
  if (err) {
    console.error(`Error reading ${process.argv[2]}: ${err}`);
    return;
  }

  // Read the content of the second file
  fs.readFile(process.argv[3], 'utf8', (err, data2) => {
    if (err) {
      console.error(`Error reading ${process.argv[3]}: ${err}`);
      return;
    }

    // Concatenate the content of both files
    const finalData = data1 + data2;

    // Write the concatenated content to the destination file
    fs.writeFile(process.argv[4], finalData, 'utf8', (err) => {
      if (err) {
        console.error(`Error writing to ${process.argv[4]}: ${err}`);
        return;
      }
      console.log(`Concatenation successful. Result written to ${process.argv[4]}`);
    });
  });
});
