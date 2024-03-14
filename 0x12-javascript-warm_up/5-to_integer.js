#!/usr/bin/node

const arg = process.argv[2];

if (!isNaN(parseInt(arg))) {
	console.log(`My Number:`, parseInt(arg));
}
else {
	console.log(`Not a number`);
}
