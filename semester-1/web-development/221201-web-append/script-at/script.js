let total = 0;
let i = 0;

do {
    [total, i] = [total+i, i+1];
    if (i === 50) break;
} while (i <= 100)

document.write(total);
