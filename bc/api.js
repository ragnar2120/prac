var express = require('express')
var app = express();
var request = require("request");

request({
    url:"https://api.blockchain.info/stats?format=json",
    json: true
},function(error,response,body){
    btcPrice = body.market_price_usd;
    btcBlocks = body.n_blocks_total;
    btcFees = body.total_fees_btc;
    btcMined = body.n_blocks_mined;
    btcVolume = body.estimated_transaction_volume_usd;
})
app.get('/',function(req,res){
    res.send("Bitcoin Transaction Demo and current Price is"+btcPrice);
});
app.post('/blocks',function(req,res){
    res.send("\nBitcoin Transaction Demo and current Height is"+btcBlocks);
});
app.get('/fees',function(req,res){ //create new block
    res.send("\nBitcoin Transaction Demo and current Fees is"+btcFees);
});
app.get('/mined',function(req,res){ //create new block
    res.send("\nBitcoin Transaction Demo and current mined is"+btcMined);
});
app.get('/volume',function(req,res){ //create new block
    res.send("\nBitcoin Transaction Demo and current volume is"+btcVolume);
});
app.listen(3000 , function(){
    console.log('listening at port 3000');
});