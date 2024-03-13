#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (!(w <= 0 || h <= 0) && w && h) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
    this.print(); // Update the printed representation of the rectangle
  }
};
