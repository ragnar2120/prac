const prompt = require('prompt-sync')();
const Blockchain = require('./blockchain');


var bitcoin = new Blockchain;

bitcoin.createNewBlock(1001,'genesis', 'test_hash 1');
bitcoin.createNewTransaction(5000,'Bojack','Carolyn')
bitcoin.createNewTransaction(2000,'Bojack','Todd')
bitcoin.createNewBlock(10002, bitcoin.getPreviousHash());

console.log("Before changing the data")
console.log(bitcoin.chain[1].transactions)
console.log("Hash : "+ bitcoin.chain[1].hash)


console.log("After changing the data")
bitcoin.chain[1].transactions[0].amount = 2000;
bitcoin.chain[1].transactions[1].amount = 5000;
bitcoin.chain[1].hash = bitcoin.hashBlock(bitcoin.chain[1].previousBlockHash,bitcoin.chain[1].transactions,bitcoin.chain[1].nonce);

console.log(bitcoin.chain[1].transactions)
console.log("Hash : "+bitcoin.chain[1].hash)
