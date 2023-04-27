// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
contract ReceiveEther {
    /*
    Which function is called, fallback() or receive()?
           send Ether
               |
         msg.data is empty?
              / \
            yes  noa
            /     \
receive() exists?  fallback()
         /   \
        yes   no
        /      \
    receive()   fallback()
    */

    // Function to receive Ether. msg.data must be empty
    receive() external payable {}
    // Fallback function is called when msg.data is not empty
    fallback() external payable {}
    function getBalance() public view returns (uint) {
        return address(this).balance;
    }
}
contract SendEther {
    function sendViaTransfer(address payable to) public payable {
        // This function is no longer recommended for sending Ether.
        to.transfer(msg.value);
    }

    function sendViaSend(address payable to) public payable {
        // Send returns a boolean value indicating success or failure.
        // This function is not recommended for sending Ether.
        bool sent = to.send(msg.value);
        require(sent, "Failed to send Ether");
    }

    function sendViaCall(address payable to) public payable {
    // Call returns a boolean value indicating success or failure.
    // This is the current recommended method to use.
    (bool sent, ) = to.call{value: msg.value}("");
    require(sent, "Failed to send Ether");
}

} 


