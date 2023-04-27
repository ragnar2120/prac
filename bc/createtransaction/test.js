const Blockchian = require('./blockchain');
const prompt = require('./node_modules/prompt-sync')({sigint:true})
var bitcoin = new Blockchian;
var nonce = new Number;
var hash = new String;
var amount = new Float32Array;
var sender = new String;
var receiver = new String;

// Creating new Block
bitcoin.createNewBlock(2345,'Sathyaprakash','0000000');
console.log(bitcoin)



for (let i=1; i<=5; i++){



    for (let j=0; j<3; j++){

        amount = prompt("Enter Amount: ");
        sender = prompt("Enter Sender: ");
        receiver = prompt("Enter Receiver: ");

        bitcoin.createNewTransaction(amount,sender,receiver);
    };

    console.log(bitcoin)
    
    var last_block_hash = bitcoin.getLastBlockHash();
    nonce = prompt("Enter Nonce: ");
    hash = prompt("Enter Hash: ");

    bitcoin.createNewBlock(nonce, last_block_hash, hash);

    console.log(bitcoin.chain)
}
