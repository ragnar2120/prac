const prompt = require('prompt-sync')();
const Blockchain = require('./blockchain');


var bitcoin = new Blockchain;
const previousBlockHash = 'AJSHAHFEUHFUEHHFEW';
const currentBlockData = [
    {
        amount : 10,
        sender : 'LASJDOADOJDOJEOJE',
        receipient : 'KGAIUGSD'
    },
    {
        amount : 30,
        sender : 'LASKJSDNJSAHDJDOADOJDOJEOJE',
        receipient : 'KGAKNSKNFAIUGSD'
    },
    {
        amount : 40,
        sender : 'LASJDIDJSFIHOADOJDOJEOJE',
        receipient : 'KGAIUGSDHDLJAFH'
    },

];
const nonce = 100;
console.log(bitcoin.hashBlock(previousBlockHash,currentBlockData,220536));
// console.log(bitcoin.proofOfWork(previousBlockHash,currentBlockData));