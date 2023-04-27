function Blockchain(){
    this.chain = []
    this.newTransctions = []
};
//const Blockchain = require('./blockchain');

Blockchain.prototype.createNewBlock = function(nonce, previousBlockHash, hash)
{

//create new block objects
const newBlock = {
    index: this.chain.length+1,
    timeStamp: Date.now(),
    transactions: this.pendingTransactions,
    nonce: nonce, //comes from proof work typically a number
    hash: hash,
    previousBlockHash: previousBlockHash,
};
this.pendingTransactions = [];
this.chain.push(newBlock);
return newBlock;
};

Blockchain.prototype.getLastBlock = function(){
    return this.chain[this.chain.length-1];
};

Blockchain.prototype.getLastBlockHash = function(){
    return this.chain[this.chain.length-1].hash;
};

Blockchain.prototype.createNewTransaction = function(amount, sender, receiver)
{

//create new block objects
const newTransaction = {
    amount: amount,
    sender: sender,
    receiver: receiver
};    
    this.pendingTransactions.push(newTransaction)
    return this.getLastBlock()['index'] + 1;
};


module.exports = Blockchain;
