#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && w !== undefined && h !== undefined) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i, j;
    for (i = 0; i < this.height; i++) {
      let z = '';
      for (j = 0; j < this.width; j++) {
        z += 'X';
      }
      console.log(z);
    }
  }
}
module.exports = Rectangle;
