# Blockchain-Based Crowdfunding System

A decentralized crowdfunding platform that uses blockchain technology and smart contracts to provide secure, transparent, and trustless fundraising without intermediaries.

---

## Project Overview

Traditional crowdfunding platforms are centralized and often suffer from issues such as lack of transparency, high service fees, and trust problems between contributors and campaign creators. This project overcomes these limitations by implementing a blockchain-based crowdfunding system where all transactions are recorded on a distributed ledger.

---

## Objectives

- To develop a decentralized crowdfunding platform using blockchain
- To ensure transparency and security of transactions
- To eliminate intermediaries in fundraising
- To automate fund collection and release using smart contracts
- To build trust between contributors and campaign creators

---

## Technologies Used

- Blockchain: Ethereum
- Smart Contracts: Solidity
- Backend Tools: Node.js, Hardhat / Truffle
- Frontend: HTML, CSS, JavaScript / React
- Wallet: MetaMask
- Development Tool: VS Code
- Version Control: Git and GitHub

---

## System Features

- User wallet connection using MetaMask
- Campaign creation by project owners
- Secure contribution using cryptocurrency
- Smart contract-based fund management
- Transparent transaction history on blockchain
- Automatic fund release when goal is achieved
- Refund mechanism if funding goal is not met

---

## System Architecture

1. User connects wallet to the application
2. Campaign creator deploys a smart contract
3. Contributors send funds to the smart contract
4. Blockchain records all transactions securely
5. Smart contract releases funds based on predefined rules

---

## Project Structure

blockchain-based-crowdfunding-system/
├── contracts/        # Solidity smart contracts  
├── scripts/          # Deployment scripts  
├── frontend/         # User interface code  
├── migrations/       # Blockchain migration files  
├── README.md  
├── .gitignore  

---

## How to Run the Project

1. Clone the repository  
   git clone https://github.com/your-username/blockchain-based-crowdfunding-system.git

2. Install dependencies  
   npm install

3. Start local blockchain  
   npx hardhat node

4. Deploy smart contracts  
   npx hardhat run scripts/deploy.js --network localhost

5. Run the frontend  
   npm start

---

## Security Considerations

- Private keys and environment variables are not stored in the repository
- Sensitive files are excluded using .gitignore
- All transactions are immutable and verifiable on the blockchain

---

## Applications

- Startup and business fundraising
- Charity and donation platforms
- Community-driven projects
- Decentralized finance (DeFi) applications

This project is developed for academic and educational purposes only.
