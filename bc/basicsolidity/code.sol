## SOLIDITY DATATYPES

pragma solidity ^0.5;
contract MyContract{
    bool public valid = false;

    uint32 public uidata = 5012019;
    int32 public intdata = -6012019;

    string public str = "This is a string";
}
-----------------------------------------------------------
## SOLIDITY DATAFUNCTIONS 

pragma solidity ^0.5;
contract MyContract{
    enum State {waiting, ready, active}
    State public state;
    constructor() public {
        state = State.waiting;
    }    
    function ready() public {
        state = State.ready;
    }
    function activate() public {
        state = State.active;
    }
    function isActive() public view returns (bool) {
    return state == State.active;   
}
}
---------------------------------------------------------------
## Struct mapping with onlyOwner modifier

pragma solidity ^0.5;
contract MyContract{
    
    uint256 public peoplecount = 0;
    address public owner;

    modifier onlyowner (){
        require (msg.sender == owner);
        _;
    }    
    
    mapping (uint=>Person) public people;
    
    constructor() public {
        owner = msg. sender;
    
    }

    struct Person {
        uint _id;
        string _firstName;
        string _lastName;
    }
    function addPerson(string memory _firstName, string memory _lastName) public onlyowner {
        incrementCount () ;
        people [peoplecount] = Person (peoplecount, _firstName, _lastName);
    }

    function incrementCount () internal {
        peoplecount += 1;
    }
}
-----------------------------------------------------------------------------------------
## Struct mapping with Time modifier

pragma solidity ^0.5;
contract MyContract{
    uint256 public peoplecount = 0;
    uint256 startTime;
    
    modifier onlywhileOpen (){
        require (block.timestamp >= startTime);
        _;
    }
    
    mapping (uint=>Person) public people;

    constructor() public {
        startTime = 1544668513;
    }
    
    struct Person {
    uint id;
    string _firstName;
    string _lastName;
    }
    
    function addPerson(string memory _firstName, string memory _lastName) public onlywhileOpen {
        incrementCount ();
        people [peoplecount] = Person(peoplecount, _firstName, _lastName);
    }

    function incrementCount () internal {
        peoplecount += 1;    
    }
}
