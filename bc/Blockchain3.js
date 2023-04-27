const sha256 =require('sha256');
function Blockchain3(){
    this.chain =[];
    this.pendingTransactions = [];
};
//const Blockchain3 = require('./Blockchain3');

Blockchain3.prototype.createNewBlock = function(nonce, previousBlockHash, hash)
{
const newBlock = {
    index: this.chain.length+1,
    timestamp: Date.now(),
    transactions: this.pendingTransactions,
    nonce: nonce,
    hash: hash,
    previousBlockHash: previousBlockHash,
};
newBlock.hash =this.hashBlock(previousBlockHash,newBlock.transactions,nonce)
this.pendingTransactions = [];
this.chain.push(newBlock);
return newBlock;   
}

Blockchain3.prototype.getLastBlock=function(){
    return this.chain[this.chain.length-1];
};


Blockchain3.prototype.getLastBlockHash=function(){
    return this.chain[this.chain.length-1].hash;
};

Blockchain3.prototype.createNewTransaction = function (a ,s ,r ) {
    const newTransaction ={
        amount:a,
        sender:s,
        recipient:r
    };
    this.pendingTransactions.push(newTransaction);
}
Blockchain3.prototype.hashBlock = function (previousBlockHash,currentBlockData,nonce){
    const dataString =previousBlockHash + nonce.toString() + JSON.stringify(currentBlockData);
    const hash =sha256(dataString);
    return hash;
}

module.exports =Blockchain3;
