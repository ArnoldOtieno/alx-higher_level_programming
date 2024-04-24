#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const letter = 'x';
    for (let i = 0; i < this.height; i++) {
      console.log(letter.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
