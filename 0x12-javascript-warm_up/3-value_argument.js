#!/usr/bin/node
const { argv } = require('node:process');
argv.forEach((val, index) => {
    if (val != NULL) {
        console.log(`${val}`);
    }
    else {
        console.log('No argument')
    }
});