#!/usr/bin/node

if (process.argv.length < 3) {
    console.log('Missing number of occurrences');
} else {
    const x = parseInt(process.argv[2]);
    if (!isNaN(x)) {
        for (let i = 0; i < x; i++) {
            console.log('C is fun');
        }
    } else {
        console.log('Invalid number of occurrences');
    }
}
