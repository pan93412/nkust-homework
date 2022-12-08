#!/usr/bin/env node

/**
 * @param {int} n
 * @returns {string}
 */
function triangle(n) {
    const buf = [];

    for (let i = 1; i <= n; i++) {
        buf.push("*".repeat(i));
    }

    return buf.join("\n");
}

/**
 *
 * @param {int} n
 * @returns {string}
 */
function middleTriangle(n) {
    const buf = [];
    const middle = Math.floor((2 * n - 1) / 2);

    for (let i = 0; i < n; i++) {
        const spaceCount = middle - i;

        const space = " ".repeat(Math.max(spaceCount, 0));
        const star = "*".repeat(2 * i + 1)
        buf.push(space + star);
    }

    return buf.join("\n");
}

/**
 *
 * @param {int} n
 * @returns {string}
 */
function tree(n) {
    const middle = Math.floor((2 * n - 1) / 2);
    return middleTriangle(n) + `\n${" ".repeat(middle)}|`.repeat(n);
}

/**
 * Fib
 */
function fib(n) {
    if (n < 1) return 1;
    return n + fib(n-1);
}

console.log(triangle(10))
console.log(tree(10))
console.log(fib(10))
