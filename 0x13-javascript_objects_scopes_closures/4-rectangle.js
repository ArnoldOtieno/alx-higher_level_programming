#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const letter = 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(letter.repeat(this.width));
    }
  }

  rotate () {
    [this.height, this.width] = [this.width, this.height];
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
