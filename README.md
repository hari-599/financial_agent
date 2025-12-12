# 🚀 Financial Agent Pro

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-Llama3-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Live-green?style=for-the-badge)

**[View Live Demo](https://financial-agent-c2io.onrender.com)**

Financial Agent Pro is a production-ready **Agentic AI Application** that provides real-time stock market insights and financial analysis. It leverages **Llama 3 (70B)** via the **Groq LPU** for sub-second inference, grounded in real-time data using **PhiData** tools.

## ⚡ Key Features
* **🗣️ Natural Language Interface:** Ask complex financial queries (e.g., *"Compare AAPL and MSFT fundamentals"*).
* **📉 Real-Time RAG Pipeline:** Fetches live stock prices, analyst ratings, and P/E ratios using **YFinance** tools to prevent hallucinations.
* **📰 News Integration:** Aggregates latest market news via **DuckDuckGo** search tools.
* **🚀 High-Performance Inference:** Powered by **Groq API**, delivering responses 10x faster than standard GPT-4 implementations.
* **🐳 Containerized:** Fully Dockerized architecture deployed on **Render**.

## 🛠️ Tech Stack
* **LLM:** Llama 3 (70B) via Groq Cloud
* **Orchestration:** PhiData (Agentic Workflow)
* **Backend:** Flask (Python)
* **Tools:** YFinance, DuckDuckGo Search
* **Deployment:** Docker, Render

## 💻 Local Installation
To run this project locally, follow these steps:

1. **Clone the repository**
   ```bash
   git clone [https://github.com/hari-599/financial_agent.git](https://github.com/hari-599/financial_agent.git)
   cd financial_agent
