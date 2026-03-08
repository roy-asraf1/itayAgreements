const fs = require('fs');
const pdf = require('pdf-parse');

let dataBuffer = fs.readFileSync('הסכם בין איתי למזמין.pdf');

pdf(dataBuffer).then(function(data) {
    fs.writeFileSync('output.txt', data.text);
    console.log('Extraction complete, text written to output.txt');
}).catch(function(error) {
    console.error('Error extracting text:', error);
});