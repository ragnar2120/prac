const Blockchain2 = require('./Blockchain2');
const prompt = require('./node_modules/prompt-sync')({sigint:true})
var bitcoin = new Blockchain2;
var nonce = new Number;
var hash = new String;
var blocks= prompt('Enter No of blocks : ');
console.log('Initial Block Created')
bitcoin.createNewBlock(0000,'-----','00000')
for (let i = 0; i < blocks; i++) {
    console.log('Block-->',i+1);
    nonce= prompt('Enter Nonce : ');
    hash = prompt("Enter Hash: ");
    var pre_hash=bitcoin.getLastBlockHash()
    var trans =prompt('Enter No of transactions');
    for(let j=0;j<trans;j++){
        console.log('Transaction-->'+j+1);
        var a=prompt('Enter Amount');
        var s=prompt('Enter Sender');
        var r=prompt('Enter Recipient');
        bitcoin.createNewTransaction(a,s,r);
    }
    bitcoin.createNewBlock(nonce,pre_hash,hash);

    
}
console.log(bitcoin);