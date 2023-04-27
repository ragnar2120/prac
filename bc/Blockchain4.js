const sha256 =require('sha256');
function Blockchain4(){
    this.chain =[];
    this.pendingTransactions = [];
};
//const Blockchain4 = require('./Blockchain4');

Blockchain4.prototype.createNewBlock = function(nonce, previousBlockHash, hash)
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

Blockchain4.prototype.getLastBlock=function(){
    return this.chain[this.chain.length-1];
};

Blockchain4.prototype.proofOfWork = function(previousBlockHash,currentBlockData) {
    let nonce =0;
    let hash = this.hashBlock(previousBlockHash,currentBlockData,nonce);
    while (hash.substring(0,4) !== '0000') {
        nonce++;
        hash =this.hashBlock(previousBlockHash,currentBlockData,nonce);
    }
    return nonce;
};

Blockchain4.prototype.getLastBlockHash=function(){
    return this.chain[this.chain.length-1].hash;
};

Blockchain4.prototype.createNewTransaction = function (a ,s ,r ) {
    const newTransaction ={
        amount:a,
        sender:s,
        recipient:r
    };
    this.pendingTransactions.push(newTransaction);
}
Blockchain4.prototype.hashBlock = function (previousBlockHash,currentBlockData,nonce){
    const dataString =previousBlockHash + nonce.toString() + JSON.stringify(currentBlockData);
    const hash =sha256(dataString);
    return hash;
}

module.exports =Blockchain4;
