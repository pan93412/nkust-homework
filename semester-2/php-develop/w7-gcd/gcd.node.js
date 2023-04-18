function gcdLoop(x, y) {
  while (x != 0 && y != 0) {
    console.log({ x, y });
    if (x >= y) {
      x %= y;
    } else {
      y %= x;
    }
  }

  return Math.max(x, y);
}

gcdLoop(12, 4);
