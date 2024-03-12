#!/usr/bin/node

// Define a function to add two integers
function add (a, b) {
  return a + b;
}

// Check if both arguments are provided
if (process.argv[2] !== undefined && process.argv[3] !== undefined) {
  // Convert arguments to integers and call the add function
  const num1 = parseInt(process.argv[2]);
  const num2 = parseInt(process.argv[3]);

  // Check if the arguments are valid numbers
  if (!isNaN(num1) && !isNaN(num2)) {
    console.log(add(num1, num2));
  } else {
    console.log('Invalid arguments');
  }
} else {
  console.log('Missing arguments');
}
