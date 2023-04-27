const sha256 = require('sha256');

function Blockchain(){
    this.chain = [];
    this.pendingTransactions = [];
}
Blockchain.prototype.createNewBlock = function(nonce, previousBlockHash, hash)
{

//create new block objects
    const newBlock = {
        index: this.chain.length+1,
        timestamp: Date.now(),
        transactions: this.pendingTransactions,
        nonce: nonce, //comes from proof work typically a number
        hash: hash,
        previousBlockHash: previousBlockHash,
    };
    newBlock.hash = this.hashBlock(previousBlockHash, newBlock.transactions, nonce)
    this.pendingTransactions = [];
    this.chain.push(newBlock);
    return newBlock;
}

Blockchain.prototype.getPreviousHash = function(){
    return this.chain[this.chain.length - 1].hash;
}

Blockchain.prototype.getLastBlock = function(){
    return this.chain[this.chain.length-1];
};


Blockchain.prototype.createNewTransaction = function(amount, sender, receiver){
//create new block objects
    const newTransaction = {
        amount: amount,
        sender: sender,
        receiver: receiver
    }     
    this.pendingTransactions.push(newTransaction);
}

Blockchain.prototype.hashBlock = function(previousBlockHash, currentBlockData, nonce){
    const dataString = previousBlockHash + nonce.toString()+ JSON.stringify(currentBlockData);
    const hash = sha256(dataString);
    return hash;
}
Blockchain.prototype.proofOfWork = function(previousBlockHash,currentBlockData){
    let nonce = 0 ;
    let hash = this.hashBlock(previousBlockHash,currentBlockData,nonce);
    while(hash.substring(0, 4) !== '0000'){
        nonce++;
        hash = this.hashBlock(previousBlockHash,currentBlockData,nonce);
    }
    return nonce;
}

module.exports = Blockchain;