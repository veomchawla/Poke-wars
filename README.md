# 🐉 Pokémon Battle Simulation MCP Server

> A **FastAPI-based MCP (Model Context Protocol)** server that powers Pokémon battle simulations with strategy, status effects, and real-time battle logic — built for hackathons, AI integrations, and gaming experiments.

---

## 📖 Overview

This project is an **MCP-compatible server** that allows clients (like Claude Desktop or custom MCP clients) to:
- Fetch detailed Pokémon data  
- Simulate turn-by-turn Pokémon battles  
- Apply **status effects** like Burn, Poison, and Paralysis  
- Retrieve **battle strategies, status updates, and move sets** dynamically  

The backend is built with **FastAPI** and exposes REST endpoints for direct use, while the MCP server allows AI tools to query it as a resource.

---

## ✨ Features

- 🎮 **Battle Simulation**: Turn-based Pokémon battles with realistic mechanics  
- ⚡ **Status Effects**: Burn, Poison, Paralysis with impact on health and moves  
- 🧠 **Strategy Engine**: AI-assisted move recommendations  
- 🔌 **MCP Protocol Support**: Easily integrates with Claude Desktop & other MCP clients  
- 📡 **REST API Endpoints**: Accessible via HTTP for quick testing  
- 🧪 **Test Scripts**: Automated testing with `test_battle.py`  
- 🛠 **Hackathon-Ready**: Modular and easy to extend  

---

## 🛠 Tech Stack

- **Language**: Python 3.10+  
- **Framework**: FastAPI  
- **MCP Integration**: [Model Context Protocol](https://modelcontextprotocol.io/)  
- **Testing**: `pytest`, REST Client (`battle.http`)  
- **Other Tools**: `uvicorn` for ASGI serving

---

## 📂 Project Structure

├── api.py            # FastAPI app & API routes
├── mcp_tool.py       # MCP tool definitions
├── mcp_resources.py  # MCP resource definitions
├── engine.py         # Battle logic & status effect handling
├── test_battle.py    # Automated tests
├── battle.http       # REST Client test requests
├── requirements.txt  # Dependencies
└── README.md         # Project documentation


## 🚀 Getting Started

### 1️⃣ Clone the Repository

git clone https://github.com/GunjanKaur20/pokemon-battle-mcp.git
cd pokemon-battle-mcp

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Server
uvicorn api:app --reload
The API will be available at:

arduino
http://localhost:8000

4️⃣ (Optional) Run as MCP Server
python mcp_tool.py
This will start the MCP server so it can be used in tools like Claude Desktop.

 **Get the Swagger UI at http://127.0.0.1:8000/docs**
 
🔗 API Endpoints

📜 Get Pokémon Info
GET /pokemon/{name}
Example: GET /pokemon/pikachu

⚔️ Simulate Battle

POST /battle/simulate
Query Parameters:
- pokemon1 (str) — First Pokémon name
- pokemon2 (str) — Second Pokémon name
- status1  (optional) — Status effect for Pokémon 1 (burn, poison, paralysis)
- status2  (optional) — Status effect for Pokémon 2 (burn, poison, paralysis)

Example:
POST /battle/simulate?pokemon1=pikachu&pokemon2=squirtle&status1=paralysis&status2=poison

🧠 Get Battle Strategy

GET /battle/strategy/{pokemon}
Example: GET /battle/strategy/pikachu

💪 Get Status

GET /battle/status/{pokemon}

🌀 Get Available Moves

GET /battle/moves/{pokemon}

📋 Example battle.http (VS Code REST Client)

### Get Pokémon Info
GET http://localhost:8000/pokemon/pikachu
Accept: application/json

### Simulate Battle
POST http://localhost:8000/battle/simulate?pokemon1=pikachu&pokemon2=squirtle&status1=paralysis&status2=poison
Accept: application/json

### Get Battle Strategy
GET http://localhost:8000/battle/strategy/pikachu
Accept: application/json

🧪 Running Tests

pytest test_battle.py

🤝 Contributing
Contributions are welcome!
Feel free to:

Submit PRs for bug fixes or new features

Open issues for feature requests or improvements

📜 License
This project is licensed under the MIT License — see LICENSE for details.

📣 Credits
Built with ❤️ by Gunjan Kaur for learning, hackathons, and MCP experimentation.
Pokémon data and mechanics are for educational purposes only and not affiliated with Nintendo/Game Freak.
