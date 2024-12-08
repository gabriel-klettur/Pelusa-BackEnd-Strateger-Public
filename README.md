# 📈 Pelusa BackEnd Strateger - Public

## 🗂️ Table of Contents
1. [General Overview](#1-general-overview)
2. [Key Features](#2-key-features)
3. [Technologies Used](#3-technologies-used)
4. [Directory Structure](#4-directory-structure)
5. [API Structure](#5-api-structure)
6. [Development Cycle](#6-development-cycle)
7. [Installation & Setup](#7-installation--setup)
8. [Usage](#8-usage)
9. [Testing](#9-testing)
10. [Contributing](#10-contributing)
11. [License](#11-license)
12. [Contact](#12-contact)

---

## 🧭 1. General Overview
**Project Name:** Pelusa BackEnd Strateger - Public

**Description:**  
The **Pelusa BackEnd Strateger** is a core part of the **Pelusa Trading System**, a backend built with FastAPI to automate trading operations based on signals (alarms) received from **TradingView**. The system processes these alarms and interacts with the **BingX Exchange** to execute trades. This backend is designed to be modular, secure, and scalable, supporting multiple databases, security layers (IP filtering, exception handling), and advanced logging using **Loguru**.

The backend supports alarm management, order execution, data storage, and API endpoints for account balances, trading positions, and strategy creation. It integrates with other key components like **AlarmHugger** and **SiteGround**-hosted databases to provide a seamless, real-time trading experience.

---

## 🚀 2. Key Features
- **API-Driven:** RESTful API endpoints for alarms, orders, positions, strategies, and more.
- **Modular Design:** Logic separated into controllers, routes, services, and models.
- **Multi-Database Support:** Interacts with multiple databases for alarms, orders, strategies, and positions.
- **Alarm Processing:** Receives TradingView alerts via a webhook and processes them into actionable trades.
- **BingX Integration:** Executes trade operations on BingX for USDT-M, Coin-M, Spot, and Standard accounts.
- **Error Handling & Logging:** Centralized logging with **Loguru** and structured error handling for consistent API responses.
- **Security:** Whitelists IP addresses, monitors server requests, and gracefully handles invalid requests.
- **Backtesting & Strategy Management:** Offers CRUD endpoints for managing strategies, orders, and diary entries.
- **Server Health Checks:** Monitors the server's health and database connections with `/status-server`.

---

## 🛠️ 3. Technologies Used
### **Core Technologies**
- **Language:** Python 3+
- **Framework:** FastAPI
- **Web Server:** Uvicorn (development) + Gunicorn (production)
- **Database:** MySQL (multiple databases)
- **ORM:** SQLAlchemy
- **Security:** IP whitelisting, centralized error handling, SSL certificates for HTTPS

### **Libraries & Tools**
- **aiomysql:** Asynchronous MySQL connections for high performance.
- **Loguru:** Advanced logging for tracking requests, responses, and errors.
- **Pydantic:** Data validation and serialization for API request and response models.
- **SQLAlchemy:** ORM for database schema definitions and query building.
- **Uvicorn:** High-performance ASGI server used for development.
- **Gunicorn:** WSGI server for production deployments.

---

## 📂 4. Directory Structure
```bash
Pelusa-BackEnd-Strateger-Public/ 
├── pytest.ini 
├── requirements.txt 
├── run.py 
├── app/ 
│ ├── config.py 
│ ├── main.py 
│ ├── alarms/ 
│ ├── bingx/ 
│ ├── interactiveBrokers/ 
│ ├── klinedata/ 
│ ├── server/ 
│ ├── siteground/ 
│ ├── strateger/ 
│ ├── utils/ 
│ └── init.py 
├── Docs/ 
├── logs/ 
└── tests/
```

### **Key Folders**
- **alarms/**: Handles alarms from TradingView.  
- **bingx/**: BingX controllers, routes, and services for interacting with BingX accounts (USDT-M, Coin-M, Spot, etc.).  
- **klinedata/**: Handles fetching and saving K-line (candlestick) data from BingX.  
- **server/**: Middlewares for logging, IP filtering, and health check routes.  
- **strateger/**: CRUD operations for accounts, backtesting, diary, orders, positions, and strategies.  

---

## 📡 5. API Structure
| **Endpoint**      | **Method** | **Description**                  |
|-------------------|------------|-----------------------------------|
| `/alarms/`        | GET        | List all alarms (supports filters, pagination) |
| `/alarms/{id}`    | GET        | Get alarm details by ID           |
| `/alarms/`        | POST       | Create a new alarm                |
| `/orders/`        | GET        | List all orders                   |
| `/orders/{id}`    | GET        | Get order details by ID           |
| `/orders/`        | POST       | Create a new order                |
| `/status-server/` | GET        | Health check and DB status        |
| `/strategies/`    | GET        | List all trading strategies       |
| `/strategies/`    | POST       | Create a new trading strategy     |

---

## 📐 6. Development Cycle
### **Building Cycle**
1. **Requirements Specification:** Define API purpose, models, and endpoints.  
2. **Logic Design:** Plan routes, controllers, and services.  
3. **Data Design:** Define models and schemas for validation.  
4. **Implementation:** Write logic for controllers, routes, and services.  
5. **Testing:** Write unit and integration tests using **pytest**.  

### **Consolidate Cycle**
1. **Documentation:** Create OpenAPI docs for all endpoints.  
2. **Code Review & Refactoring:** Optimize query performance, logging, and security.  
3. **Integration & Deployment:** Deploy to AWS EC2 and link it with SiteGround databases.  

---

## ⚙️ 7. Installation & Setup
1. **Clone the Repository**
   ```bash
   git clone https://github.com/username/backend-strateger.git
   cd backend-strateger
   ```

2. **Install Dependencies**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```
3. **Environment Variables**

Create a .env file with the following:

```bash
DB_URL_DESARROLLO=your_database_url
API_KEY=your_api_key
```

4. **Run the Server**
```bash
uvicorn app.main:app --reload
```

---

## 🚀 8. Usage
- **API Docs**: Available at /docs for a Swagger-based interface.
- **Server Health Check**: Call /status-server to check server status and DB connections.

## 🧪 9. Testing
1. **Run Tests**
```bash
pytest tests/
```

2. **Testing Key Areas**
- Controllers: Test request validation, route logic, and responses.
- Services: Test business logic, transformations, and API calls.
- Models: Test schema validation and database interactions.

---

## 🤝 10. Contributing
How to Contribute
1. Fork the repository.
2. Create a branch
```bash
git checkout -b feature-name
```
3. Commit your changes
```bash
git commit -m "feat: description of the feature"
```
4. Push to the branch
```bash
git push origin feature-name
```
5. Open a pull request.


## Commit Guidelines
We follow **Conventional Commits**:

```bash
<type>(<scope>): <description>
```

**Examples:**
- feat(alarms): add filter to alarms endpoint
- fix(server): handle 500 errors in health check


---

## 📜 11. License
This project is licensed under the MIT License. See the LICENSE file for more details.

## 💬 **12. Contact**

If you have any questions, issues, or feedback, feel free to contact **Gabriel** through:

- **GitHub Issues**: Open an issue in this repository.
- **Email**: [gabriel.astudillo.roca@gmail.com](mailto:your-email@example.com)
