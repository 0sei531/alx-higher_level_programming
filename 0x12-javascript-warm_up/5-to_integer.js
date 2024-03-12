#!/usr/bin/node

// Convert the first argument to an integer
const num = parseInt(process.argv[2]);

// Check if the conversion was successful
if (!isNaN(num)) {
  console.log('My number:', num);
} else {
  console.log('Not a number');
}
