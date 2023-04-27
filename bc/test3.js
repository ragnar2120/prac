const prompt = require('./node_modules/prompt-sync')({sigint:true})
const Blockchain3 = require('./Blockchain3');
var bitcoin = new Blockchain3;

bitcoin.createNewBlock(0001,'Genesis','000000');
bitcoin.createNewTransaction(8000,'ru','ish');
bitcoin.createNewTransaction(9000,'uu','tish');
var last_block_hash =bitcoin.getLastBlockHash();
bitcoin.createNewBlock(0002,last_block_hash);
bitcoin.createNewTransaction(81000,'pam','mish');
bitcoin.createNewTransaction(92000,'ram','sam');
bitcoin.createNewTransaction(98000,'qam','tam');
var last_block_hash =bitcoin.getLastBlockHash();
bitcoin.createNewBlock(0003,last_block_hash);
bitcoin.createNewTransaction(82000,'raj','ash');
bitcoin.createNewTransaction(93000,'kaj','ram');
bitcoin.createNewTransaction(99000,'paj','pam');
var last_block_hash =bitcoin.getLastBlockHash();
bitcoin.createNewBlock(0004,last_block_hash);
bitcoin.createNewTransaction(84000,'ram','ash');
bitcoin.createNewTransaction(94000,'kaj','aam');
bitcoin.createNewTransaction(96000,'fas','sam');
var last_block_hash =bitcoin.getLastBlockHash();
bitcoin.createNewBlock(0005,last_block_hash);
bitcoin.createNewTransaction(85000,'gaj','ash');
bitcoin.createNewTransaction(95000,'mj','rdm');
bitcoin.createNewTransaction(97000,'paj','qam');

console.log(bitcoin);
console.log(bitcoin.chain[4]);
