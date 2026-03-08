const fs = require('fs');
const pdf = require('pdf-parse');

const filePath = process.argv[2] || 'הסכם באיתי ובעל הנכס.pdf';

fs.readFile(filePath, (err, dataBuffer) => {
    if (err) {
        console.error("Error reading file:", err);
        return;
    }
    pdf(dataBuffer).then(function(data) {
        console.log(data.text);
    }).catch(function(error){
        console.error("Error parsing pdf:", error);
    });
});
