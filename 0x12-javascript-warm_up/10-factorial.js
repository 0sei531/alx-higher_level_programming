#!/usr/bin/node

// Define a function to compute factorial recursively
function factorial (n) {
  // Base case: factorial of 0 or 1 is 1
  if (isNaN(n) || n === 0 || n === 1) {
    return 1;
  }
  // Recursive case: factorial of n is n times factorial of (n-1)
  return n * factorial(n - 1);
}

// Check if the argument is provided
if (process.argv[2] !== undefined) {
  // Convert argument to integer
  const num = parseInt(process.argv[2]);
  // Print the factorial
  console.log(factorial(num));
} else {
  console.log(1);
}
