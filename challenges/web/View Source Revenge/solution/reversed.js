const grass = [39, 199, 20, 133, 19, 174, 186, 16, 102, 83, 172, 147, 207, 223, 81, 237, 78, 237, 209, 58, 38, 92, 38];

function worldInverse(a) {
    // Reverse the nibble swap
    return ((a & 0xf0) >> 4) + ((a & 0x0f) << 4);
}

function space(n) {
    let a = 0, b = 1;
    let o = [];
    for (let i = 0; i < n; i++) {
        let c = a + b;
        a = b;
        b = c;
        o.push(a % 256);
    }
    return o;
}

function recoverFlag() {
    let n = grass.length;
    let o = space(n);
    let f = [];

    for (let i = 0; i < n; i++) {
        // Reverse XOR
        let val = grass[i] ^ o[i];
        // Reverse nibble swap
        f.push(worldInverse(val));
    }

    // Convert ASCII values to characters
    return f.map(charCode => String.fromCharCode(charCode)).join('');
}

console.log(recoverFlag());
