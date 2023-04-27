const Blockchian = require('./blockchain');
const prompt = require('./node_modules/prompt-sync')({sigint:true})
var bitcoin = new Blockchian;
var nonce = new Number;
var hash = new String;

bitcoin.createNewBlock(2345,'JayRathod','0000000');

for (let i=0; i<=10; i++){
    var last_block_hash = bitcoin.getLastBlockHash();
    nonce = prompt("Enter Nonce: ");
    hash = prompt("Enter Hash: ");

    bitcoin.createNewBlock(nonce, last_block_hash, hash);
}



console.log(bitcoin)
