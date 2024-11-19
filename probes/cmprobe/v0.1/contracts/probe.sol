// SPDX-License-Identifier: MIT
// Author: omotcha
// Version: 0.0.1
// cm probe contract
pragma solidity ^0.8.0;
contract Probe{
    address private _contract_owner;
    uint256 private _nonce;
    constructor(){
        _contract_owner = msg.sender;
        _nonce = 0;
    }
    function check() public returns(uint256){
        require(msg.sender==_contract_owner, "you are not contract owner");
        _nonce += 1;
        if(_nonce >= 10000){
            _nonce -= 10000;
        }
        return _nonce;
    }
}
