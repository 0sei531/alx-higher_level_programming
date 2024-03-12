#!/usr/bin/node

// Check if there are arguments provided
if (process.argv.length <= 2) {
  console.log(0);
} else if (process.argv.length === 3) {
  console.log(0);
} else {
  // Convert arguments to integers and remove duplicates
  const numbers = process.argv.slice(2).map(Number).filter(num => !isNaN(num));
  // Sort the numbers in descending order
  numbers.sort((a, b) => b - a);
  // Print the second largest number, if available
  console.log(numbers[1] !== undefined ? numbers[1] : 0);
}
