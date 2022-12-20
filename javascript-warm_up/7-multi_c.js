#!/usr/bin/node
const MyVar = process.argv[2];
if (isNaN(MyVar) === true) {
  console.log('Missing number of occurrences');
} else {
  for (let x = 0; x < MyVar; x++) {
    console.log('C is fun');
  }
}
