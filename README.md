<div align="center">

# 🏛️ System Design & Architecture Masterclass
### *The Definitive Staff & Principal-Level Distributed Systems Curriculum*

[![GitHub Pages](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-0284c7?style=for-the-badge&logo=github)](https://mr-elegant.github.io/System-Design-Masterclass/)
[![Topics](https://img.shields.io/badge/Verified%20Topics-616%20Topics-10b981?style=for-the-badge)](https://mr-elegant.github.io/System-Design-Masterclass/)
[![Animations](https://img.shields.io/badge/Interactive%20SVGs-108%20Diagrams-a855f7?style=for-the-badge)](https://mr-elegant.github.io/System-Design-Masterclass/)
[![Papers](https://img.shields.io/badge/Systems%20Papers-11%20Classics-f59e0b?style=for-the-badge)](https://mr-elegant.github.io/System-Design-Masterclass/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)

<br/>

**[🌐 Launch Interactive Masterclass Website](https://mr-elegant.github.io/System-Design-Masterclass/)**

<p align="center">
  <b>A comprehensive, production-grade distributed systems curriculum designed for Senior, Staff, and Principal engineers preparing for FAANG+ system design rounds and architecting planet-scale backends.</b>
</p>

</div>

---

## 📚 Curriculum Overview

| Module | Core Domain | Topics Covered | Key Highlights |
| :--- | :--- | :---: | :--- |
| [**01. System Design Fundamentals**](./01-System-Design-Fundamentals/) | Distributed Building Blocks | **18 Chapters** | DNS Anycast, L4/L7 Load Balancing, Caching Topologies, Sharding, CAP/PACELC, Bloom Filters, Distributed Patterns, Security & LLM Attention Hardware. |
| [**02. System Design Interview & Architecture**](./02-System-Design-Interview/) | FAANG Flagships & Systems Papers | **39 Classic + 6 AI + 11 Papers** | 7-Step FAANG Framework, TinyURL, Uber H3, Ticketmaster, Figma CRDTs, Stripe Ledgers, ChatGPT, ColPali RAG, and Dynamo/Kafka/Raft Whitepapers. |
| [**03. Microservices Design Patterns**](./03-Microservices-Design-Patterns/) | Production Microservices | **14 Patterns** | Strangler Fig, API Gateway, BFF, Service Discovery, Circuit Breaker (Resilience4j), Distributed Sagas, CQRS, and Agentic Microservices. |
| [**04. Low Level Design (LLD)**](./04-Low-Level-Design-JavaScript/) | Object-Oriented & Clean Code | **10 Modules** | SOLID Principles, GoF Design Patterns, Concurrency Locks, Machine-Coding Flagships (Parking Lot, Elevator, Chess), and Node.js SDK Architecture. |

---

## 🌟 Key Highlights & Features

### 1. ⏱️ The 45-Minute 7-Step FAANG Framework
* **Step 1:** Functional & Non-Functional Requirements Decomposition (P99 latency SLAs, scale targets).
* **Step 2:** High-Level API Design (Idempotency keys, pagination, REST/gRPC/GraphQL).
* **Step 3:** Capacity Estimation & Envelope Calculations (QPS, storage over 5 years, memory sizing).
* **Step 4:** Data Modeling & Schema Design (Relational vs Document vs Key-Value vs Graph).
* **Step 5:** High-Level Architecture Diagram (Data flow through gateways, load balancers, workers, caches).
* **Step 6:** Deep Dive & Bottleneck Resolution (Replication lag, split-brain, hot-key caching).
* **Step 7:** Fault Tolerance & Operational Resiliency (Chaos engineering, circuit breaking, fallback states).

### 2. 🤖 State-of-the-Art Generative AI & LLM Systems
* **ChatGPT at 100M Scale:** Token streaming over SSE, KV-Cache memory footprint, RadixAttention tree prefix caching, and speculative decoding.
* **Multimodal Document RAG:** ColPali multi-vector late interaction patch embeddings with MaxSim token scoring and Milvus / Qdrant vector indexing.
* **Agentic Microservices:** Distributed multi-agent swarms with MCP (Model Context Protocol), asynchronous message passing, and budget-constrained semantic routing.

### 3. 📄 11 Legendary Distributed Systems Whitepapers
1. **Amazon Dynamo (2007):** Consistent Hash Rings, Virtual Nodes, Sloppy Quorums & Vector Clocks.
2. **Google Spanner (2012):** TrueTime API, GPS/Atomic Clocks, 2PC + Paxos Globally Distributed Transactions.
3. **Apache Kafka (2011):** Zero-Copy `sendfile()`, Sequential Disk Append, and Consumer Offset Groups.
4. **Google Bigtable (2006):** Sparse Multidimensional Sorted Maps, SSTables & Bloom Filters.
5. **Raft Consensus (2014):** Leader Election, Log Replication, Joint Consensus Reconfiguration.
6. **Google File System / GFS (2003):** 64MB Chunks, Single Master Metadata, Chunkserver Heartbeats.
7. **Google MapReduce (2004):** Distributed Map/Shuffle/Reduce Data Processing.
8. **Apache ZooKeeper (2010):** Zab Consensus, Ephemeral Znodes, Watchers & Distributed Locks.
9. **Lamport's Logical Clocks (1978):** Partial Ordering and Happened-Before Relation ($\rightarrow$).
10. **CAP Theorem & Brewer’s Conjecture (2000/2012):** Mathematical consistency tradeoffs during network partitions.
11. **ColPali: Efficient Document Retrieval with Vision Language Models (2024):** End-to-end multimodal retrieval.

---

## 🚀 Live Demo & Navigation

You can browse the entire curriculum with interactive animations, dark mode, and zero external dependencies:

```
👉 https://mr-elegant.github.io/System-Design-Masterclass/
```

### 📂 Repository File Tree

```
System-Design-Masterclass/
│
├── 01-System-Design-Fundamentals/             # 18 Core Building Block Chapters
├── 02-System-Design-Interview/                # 39 Classic/Architect Cases + 6 AI + 11 Papers
├── 03-Microservices-Design-Patterns/          # 14 Microservices Production Patterns
├── 04-Low-Level-Design-JavaScript/            # 10 LLD Machine-Coding Modules
│
├── LinkedIn_Posting_Vault/                    # Complete Post-by-Post LinkedIn Content Catalog
├── linkedin_post_assets/                      # 32 Autoplaying 60 FPS Animated Diagrams
├── index.html                                 # Master Interactive Hub (Protected)
└── README.md                                  # Repository Documentation
```

---

## 💻 Local Setup

To run or read the curriculum offline on your local machine:

```bash
# Clone the repository
git clone https://github.com/Mr-Elegant/System-Design-Masterclass.git

# Navigate into the project folder
cd System-Design-Masterclass

# Open the master hub in any modern browser
# On Windows:
start index.html

# On macOS:
open index.html

# On Linux:
xdg-open index.html
```

---

## 🛡️ Content Protection & Intellectual Property

All course modules include client-side protection mechanisms:
* **Context Menu Lock:** Prevents direct right-click copying.
* **DevTools Shortcut Interception:** Disables `F12`, `Ctrl+Shift+I`, `Ctrl+Shift+J`, and `Ctrl+U`.
* **Selective Text Selection:** Protects core curriculum content while keeping code blocks accessible for engineering study.

---

## 🤝 Contributing

Contributions, feedback, and architecture suggestions are always welcome!
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingArchitecture`)
3. Commit your Changes (`git commit -m 'feat: Add New Distributed Case Study'`)
4. Push to the Branch (`git push origin feature/AmazingArchitecture`)
5. Open a Pull Request

---

## 📄 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for more information.

<div align="center">
  <sub>Built with ❤️ for the global software architecture community. Star ⭐ this repository if you found it valuable!</sub>
</div>
