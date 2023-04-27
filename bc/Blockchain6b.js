var express = require("express");
var app =express();
var request =require("request");
var bodyparser =require("body-parser");
app.use(bodyparser.urlencoded({extended :true}));
app.use(bodyparser.json());

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
    res.sendFile("C:/Users/swaro/Desktop/Desktop/BC/test.html");
});

app.post("/wallet",function(req,res){
    var username=req.body.username
    var fav_coin=req.body.fav_coin
    var uses =req.body.uses
    console.log("Your Username : "+username)
    console.log("Your Favourite Coin : "+fav_coin)
    console.log("Uses : ")
    uses.forEach(use => console.log(use))
    res.send("Complete");

});

app.listen(3000,function(){
    console.log("hello world")
})

