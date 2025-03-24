const express = require('express');
const router = express.Router();
const { execFile } = require('child_process');
const path = require('path');
const flag = process.env.FLAG || 'YBN24{test_flag}';

router.get('/', (req, res) => {
    res.render('index', { title: 'CTF Challenge' });
});

router.post('/nuke', (req, res) => {
    // Call the backend script with the provided data
    const data = req.body;
    if (!data.baba || !data.nukes) {
        res.status(400).json({ error: 'Invalid data' });
        return
    }
    if (data.baba.length !== 2 || data.nukes.some(nuke => nuke.length !== 2)) {
        res.status(400).json({ error: 'Invalid data' });
        return
    }


    const {baba,nukes} = data;
    baba[0] = Number(baba[0])
    baba[1] = Number(baba[1])
    if (baba[0] < 0 || baba[0] > 20 || baba[1] < 0 || baba[1] > 20){
        res.status(400).json({ error: 'Data Out Of Range' });
        return
    }
    // add an extra nuke at baba's exact position
    nukes.push(baba)
    var number_of_nukes_hit = 0

    for (let nuke of nukes){
        let [x,y] = nuke;
        x = parseInt(x)
        y = parseInt(y)
        if (x < 0 || x > 20 || y < 0 || y > 20){
            res.status(400).json({ error: 'Data Out Of Range' });
            return
        }
        if (Math.abs(baba[0]-x) <= 5 && Math.abs(baba[1]-y) <= 5){
            number_of_nukes_hit += 1
        }
    }
    if (number_of_nukes_hit >= 1){
        res.status(200).json({result: `Good Job Comarade. Baba has been successfully nuked! He has suffered a total of ${number_of_nukes_hit} damage.`});
    }
    else {
        res.status(200).json({result: `Baba is safe. You have failed the motherland. ${flag} `});
    }
});

module.exports = router;
