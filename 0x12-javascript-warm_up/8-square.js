#!/usr/bin/node

// Convert the first argument to an integer
const size = parseInt(process.argv[2]);

// Check if the conversion was successful
if (!isNaN(size)) {
  // Loop to print square
  for (let i = 0; i < size; i++) {
    let line = '';
    for (let j = 0; j < size; j++) {
      line += 'X';
    }
    console.log(line);
  }
} else {
  console.log('Missing size');
}
