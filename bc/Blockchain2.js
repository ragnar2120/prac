function Blockchain2(){
    this.chain =[];
    this.pendingTransactions = [];
};
//const Blockchain2 = require('./Blockchain2');

Blockchain2.prototype.createNewBlock = function(nonce, previousBlockHash, hash)
{
const newBlock = {
    index: this.chain.length+1,
    timestamp: Date.now(),
    transactions: this.pendingTransactions,
    nonce: nonce,
    hash: hash,
    previousBlockHash: previousBlockHash,
};
this.pendingTransactions = [];
this.chain.push(newBlock);
return newBlock;   
}

Blockchain2.prototype.getLastBlock=function(){
    return this.chain[this.chain.length-1];
};


Blockchain2.prototype.getLastBlockHash=function(){
    return this.chain[this.chain.length-1].hash;
};

Blockchain2.prototype.createNewTransaction = function (a ,s ,r ) {
    const newTransaction ={
        amount:a,
        sender:s,
        recipient:r
    };
    this.pendingTransactions.push(newTransaction);
    return this.getLastBlock()['index']+1;
};
module.exports =Blockchain2;
