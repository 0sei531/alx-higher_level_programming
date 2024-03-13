#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size); // Call the constructor of Rectangle with size as both width and height
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Square;
