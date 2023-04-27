function Blockchain1(){
    this.chain = []
    this.newTransctions = []
};
//const Blockchain = require('./blockchain');

Blockchain1.prototype.createNewBlock = function(nonce, previousBlockHash, hash)
{

//create new block objects
const newBlock = {
    index: this.chain.length+1,
    timeStamp: Date.now(),
    transactions: this.newTransactions,
    nonce: nonce, //comes from proof work typically a number
    hash: hash,
    previousBlockHash: previousBlockHash,
};
this.newTransctions = [];
this.chain.push(newBlock);
return newBlock;
};

Blockchain1.prototype.getLastBlock = function(){
    return this.chain[this.chain.length-1];
};

Blockchain1.prototype.getLastBlockHash = function(){
    return this.chain[this.chain.length-1].hash;
};

module.exports = Blockchain1;