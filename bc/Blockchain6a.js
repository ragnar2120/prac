var express = require("express");
var app =express();
var request =require("request");

request({
    url:"https://api.blockchain.info/stats?format=json",
    json:true
},
    function(error,response,body){
        btcPrice=body.market_price_usd;
        btcBlocks=body.n_blocks_total;
        btcFees=body.total_fees_btc;
        btcMined=body.n_blocks_mined;
        btcVolume=body.estimated_transaction_volume_usd;
    }
);
app.get("/",function(req,res){
    res.send("Bitcoin Transaction Demo and current Price is "+btcPrice);
});

app.get("/blocks",function(req,res){
    res.send("\nBitcoin Transaction Demo and block Height is "+btcBlocks);
});

app.get("/fees",function(req,res){
    res.send("\nBitcoin Transaction Demo and fees is "+btcFees);
});

app.get("/mined",function(req,res){
    res.send("Bitcoin Transaction Demo and Blocks Mined is "+btcMined);
});

app.get("/volume",function(req,res){
    res.send("Bitcoin Transaction Demo and Block Volume is "+btcVolume);
});

app.listen(3000,function(){
    console.log("hello world")
})


