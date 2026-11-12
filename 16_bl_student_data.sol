/*
 * 16 - Student Data Smart Contract (Structures, Arrays, Fallback)
 *
 * Aim: Write a program in Solidity to create Student data. Use the following
 *      constructs: Structures, Arrays, Fallback. Deploy this as smart contract on
 *      Ethereum and observe the transaction fee and Gas values.
 *
 * Complexity:
 *   addStudent : O(1) -> push adds at the end of the array
 *   getStudent : O(1) -> direct access by index
 *   Space      : O(n) -> one entry per student
 *
 * Key terms:
 *   struct          : groups related data (roll, name, marks) into one type.
 *   Array           : list of items; Student[] is a dynamic array of students.
 *   fallback()      : runs when a function that does not exist is called.
 *   receive()       : runs when plain Ether is sent with no data.
 *   memory          : temporary data, exists only during the function call.
 *   storage         : permanent data saved on the blockchain.
 *   Gas             : units of computation a transaction needs.
 *   Gas price       : cost per unit of gas (in Gwei).
 *   Transaction fee : Gas used x Gas price. Writing to storage costs the most; reading is free.
 *
 * ---------------------------- HOW TO RUN ----------------------------
 * A) Remix VM (quick practice)
 *   1. Open https://remix.ethereum.org in Chrome.
 *   2. File Explorer -> create "16_bl_student_data.sol" -> paste this code.
 *   3. Solidity Compiler -> version 0.8.x -> Compile.
 *   4. Deploy & Run -> Environment: "Remix VM" -> Deploy.
 *   5. Under "Deployed Contracts":
 *        addStudent    : enter  1,"Ayush",85   (string in double quotes) -> transact
 *        getStudent    : enter  0  -> shows 1, Ayush, 85
 *        totalStudents : click -> shows 1
 *   6. Test fallback: scroll to "Low level interactions" at the bottom of the
 *      deployed contract -> put 0x1234 in CALLDATA -> click Transact.
 *   7. Observe gas: click each transaction in the bottom terminal and note
 *      gas, transaction cost and execution cost.
 *
 * B) On Ethereum test network (Sepolia) to observe real fee
 *   1. MetaMask -> enable test networks -> Sepolia -> get test ETH from a faucet.
 *   2. Remix Deploy & Run -> Environment: "Injected Provider - MetaMask" -> Connect.
 *   3. Deploy and run addStudent -> MetaMask popup shows the gas fee -> Confirm.
 *   4. "View on Etherscan" shows Gas Used, Gas Price and Transaction Fee.
 *      Note these values (deploy costs the most, view functions cost nothing).
 * --------------------------------------------------------------------
 */

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentData {
    // Structure
    struct Student {
        uint roll;
        string name;
        uint marks;
    }

    // Array of structures
    Student[] students;

    // Add a student
    function addStudent(uint _roll, string memory _name, uint _marks) public {
        students.push(Student(_roll, _name, _marks));
    }

    // Get a student by index
    function getStudent(uint i) public view returns (uint, string memory, uint) {
        Student memory s = students[i];
        return (s.roll, s.name, s.marks);
    }

    // Total number of students
    function totalStudents() public view returns (uint) {
        return students.length;
    }

    // Fallback: runs when a non-existing function is called
    fallback() external payable {}

    // Receive: runs when plain Ether is sent with no data
    receive() external payable {}
}
