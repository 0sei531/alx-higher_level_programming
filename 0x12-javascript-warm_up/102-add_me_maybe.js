#!/usr/bin/node

// Define a function that increments a number and calls another function
function incrementAndCall (number, theFunction) {
  // Increment the number
  number++;
  // Call theFunction with the incremented number as argument
  theFunction(number);
}

// Export the function to make it visible from outside
module.exports = incrementAndCall;
