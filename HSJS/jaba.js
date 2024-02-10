let A = [1, 2, [3, 4], 5, [6, 7], [8, 9]];
let B = [];

A.forEach(a => {
    if (Array.isArray(a)) {
        console.log(a);
        a.forEach(i => B.push(i));
    } else {
        B.push(a);
    }
});

console.log(`${A}를 평탄화하면`);
console.log(`${B}입니다`);
