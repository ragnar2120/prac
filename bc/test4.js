const prompt = require('./node_modules/prompt-sync')({sigint:true})
const Blockchain4 = require('./Blockchain4');
var bitcoin = new Blockchain4;

const previousBlockHash ='daadsfadsfadsf';
const currentBlockData = [
    {
    amount :10,
    sender : 'fdasfdasfas',
    recipient : 'tweqtqwe'
    },
    {
    amount :20,
    sender : 'fdasfdasfas',
    recipient : 'tweqtqwe'
    },
    {
    amount :30,
    sender : 'fdasfdasfas',
    recipient : 'tweqtqwe'
    },
    {
    amount :40,
    sender : 'fdasfdasfas',
    recipient : 'tweqtqwe'
    },
    {
    amount :50,
    sender : 'fdasfdasfas',
    recipient : 'tweqtqwe'
    },
];

//console.log(bitcoin.proofOfWork(previousBlockHash,currentBlockData));
console.log(bitcoin.hashBlock(previousBlockHash,currentBlockData,49701));

