const nunjucks = require('nunjucks');
const express = require('express');
const app = express();
const path = require('path');
const fs = require('fs');
const crypto = require('crypto');

nunjucks.configure('views',
    {
    autoescape: false, //Baba made you hacker's lives so much easier
    express: app 
});

app.use(express.static(path.join(__dirname, 'public')));
app.use(express.json());
app.set('view engine', 'njk'); 

app.get('/', (req, res) => {
    res.render('index.html');
})
app.get('/view_file/:fileName', (req, res) => {
    // I heard rendering files from user input is a bad idea, so I'll just send over the plain old file!
    const fileName = req.params.fileName;
    const filePath = path.join('views/user_compliments', `${fileName}`);
    fs.readFile(filePath, 'utf8', (err, data) => {
        if (err) {
            res.status(404).send('File Not Found');
            return
        }
        res.send(data);
    })
})

app.post('/submit', (req, res) => {
    const pickup = req.body.pickup;
    const pickupNum = req.body.pickupNum;
    nunjucks.render(`default_compliments/compliment${pickupNum}.njk`, {message: pickup}, (err, html) => {
        if (err || !html) {
            console.error(err);
            res.status(500).send('Internal Server Error');
            return;
        }
        const fileHash = crypto.createHash('md5').update(pickup).digest('hex');
        const fileName = `${fileHash}_${pickup.substring(0, 10)}`;
        const filePath = path.join(__dirname, 'views/user_compliments', `${fileName}`);
        fs.writeFile(filePath, html, (err) => {
            if (err) {
                res.status(500).send('Internal Server Error');
                return
            }
            res.send(`/view_file/${fileName}`);
            // delete file after 1 minute
            setTimeout(() => {
                fs.unlink(filePath, (err) => {
                    if (err) {
                        console.log(err);
                    }
                })
            }, 60000)
        })
    })
    
})
app.listen(3000, () => {
    console.log('Server is running on port 3000');
})