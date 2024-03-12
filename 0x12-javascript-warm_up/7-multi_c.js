#!/usr/bin/node

// Convert the first argument to an integer
const num = parseInt(process.argv[2]);

// Check if the conversion was successful
if (!isNaN(num)) {
  // Loop to print "C is fun" x times
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
