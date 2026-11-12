/*
 * 15 - Bank Account Smart Contract
 *
 * Aim: Write a smart contract on a test network, for Bank account of a customer
 *      for following operations: Deposit money, Withdraw money, Show balance.
 *
 * Complexity:
 *   deposit / withdraw / showBalance : O(1) each -> mapping lookup is constant time
 *   Space                            : O(n)      -> one balance per user
 *
 * Key terms:
 *   Smart contract : program stored on the blockchain, runs automatically when called.
 *   Solidity       : language for writing Ethereum smart contracts.
 *   mapping        : like a dictionary -> address => balance.
 *   msg.sender     : address of whoever calls the function.
 *   msg.value      : amount of Ether sent with the call.
 *   payable        : allows a function to receive Ether.
 *   require        : checks a condition; if false the transaction is cancelled (reverted).
 *   view           : only reads data, so calling it costs no gas.
 *   Gas            : fee for running a transaction; writing data costs gas, reading is free.
 *   Wei            : smallest unit of Ether; 1 Ether = 10^18 Wei.
 *   Test network   : (e.g. Sepolia) uses fake Ether for testing.
 *
 * ---------------------------- HOW TO RUN ----------------------------
 * A) Remix VM (quick practice, no MetaMask needed)
 *   1. Open https://remix.ethereum.org in Chrome.
 *   2. File Explorer (1st icon) -> create file "15_bl_bank_account.sol" -> paste this code.
 *   3. Solidity Compiler (2nd icon) -> select version 0.8.x -> click Compile.
 *   4. Deploy & Run (3rd icon) -> Environment: "Remix VM" -> click Deploy.
 *   5. Open the contract under "Deployed Contracts":
 *        Deposit : set VALUE at the top to 1 and unit to Ether -> click deposit.
 *        Balance : click showBalance (shows Wei, 1 Ether = 1000000000000000000).
 *        Withdraw: type 500000000000000000 (0.5 Ether in Wei) -> click withdraw.
 *   6. Click a transaction line in the bottom terminal to see gas / transaction cost.
 *
 * B) On a test network (for the practical)
 *   1. Install MetaMask, enable "Show test networks", switch to Sepolia.
 *   2. Get free Sepolia ETH from a faucet (search "Sepolia faucet").
 *   3. In Remix Deploy & Run -> Environment: "Injected Provider - MetaMask" -> Connect.
 *   4. Click Deploy -> confirm in MetaMask (note the gas fee).
 *   5. Run deposit / withdraw (confirm each in MetaMask), showBalance is free.
 *   6. In MetaMask click "View on Etherscan" to see transaction details.
 * --------------------------------------------------------------------
 */

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Bank {
    mapping(address => uint) balance;      // each account's balance

    // Deposit money
    function deposit() public payable {
        require(msg.value > 0, "Send some Ether");
        balance[msg.sender] += msg.value;
    }

    // Withdraw money
    function withdraw(uint amount) public {
        require(balance[msg.sender] >= amount, "Insufficient balance");
        balance[msg.sender] -= amount;
        payable(msg.sender).transfer(amount);
    }

    // Show balance
    function showBalance() public view returns (uint) {
        return balance[msg.sender];
    }
}
