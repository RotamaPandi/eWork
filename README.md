# QA Automation - Costumer Registration [Appium]

This repository contains automated UI tests using **Selenium**, **Pytest**, **Allure Report** to automate the **Company Registration** functionality.

---

## 📁 Folder Structure

```bash
eSuit_Assessment/
├── page/                  
│   ├── __init__.py
│   ├── login.py
│   └── registration.py
│
├── reports/                    
│   └── index.html
│
├── tests/                    
│   ├── __init__.py
│   └── test_company_registration.py
│
├── utils/                    
│   ├── __init__.py
│   └── driver_setup.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the test:
    ```bash
   pytest tests/test_company_registration.py --alluredir=reports/
   ```
3. Generate allure-result:
    ```bash
   allure generate reports/ -o reports/html --clean
   ```
3. Generate and Open report via server:
    ```bash
   allure serve reports/
   ```
   
## 💡 Notes
Credentials 
```bash
Site: eWork app
Company ID: 5049209
Username: qatestsalesman
Password: it.QA2025
```