
function xorEncryptDecrypt(input, key) {
    let output = '';
    for (let i = 0; i < input.length; i++) {
        let charCode = input.charCodeAt(i) ^ key.charCodeAt(i % key.length);
        charCode = charCode ^ 0x7;
        output += String.fromCharCode(charCode);
    }
    return output;
}
async function getEncryptedPayload() {
    const response = await fetch('encryptedFlag.txt');
    return await response.text();
}

async function main(){
    const key = "IAMINSOMUCHPAIN"; 
    const encrypted = await getEncryptedPayload();
    const decrypted = xorEncryptDecrypt(encrypted, key);
    const secretEle = document.getElementById('secret');
    secretEle.innerHTML = decrypted;
    window.main = () => {};
}

