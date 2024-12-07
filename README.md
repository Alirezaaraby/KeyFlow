> [!WARNING]  
> This Project Is Under Heavy Construction and Not Ready for Production Use.
# KeyFlow - Keyboard Logger & Analyzer ⌨

KeyFlow is an advanced tool designed to log and analyze your keyboard usage. It helps you gather precise statistics about your keyboard activity and provides insightful visualizations, such as heatmaps, to improve your productivity and typing efficiency.


✨ Features until now (constantly updating):
- **Keyboard Logger**: Log every key you press on your keyboard.
- **Flexible Storage Options**: Save data in multiple formats like TinyDB, JSON, and SQLite.
- **Modular and Flexible**: Designed with a modular architecture for easy customization and scalability.

🚀 Upcoming Features:
- **Keyboard Heatmap**: Visualize your keyboard usage with a heatmap.

## Project Structure
```plaintext
KeyFlow/
│
├── main.py                     # Main program entry point
├── adapters/                   # Storage adapters
│   └── storage/
│       ├── json_adapter.py     # JSON-based storage
│       ├── tinydb_adapter.py   # TinyDB-based storage
│       └── sqlite_adapter.py   # SQLite-based storage
│
├── core/                       # Core components
│   ├── adapters.py             # Adapter management
│   ├── config.py               # Configuration handling
│   ├── db.py                   # Abstract database class
│   └── keylogger/
│       ├── keylogger.py        # Keylogger implementation
│       └── __init__.py
│
├── exceptions/                 # Exception handling
│   ├── config_exceptions.py
|   ├── keylogger_exceptions.py
│   └── storage_exceptions.py
| README.md                     # Project documentation
```

## How To Use

- Clone the repository:  
```bash
git clone https://github.com/Alirezaarabi/keyflow.git
```

- Install the required dependencies:  
```bash
pip install -r requirements.txt
```

- Run the main program:  
```bash
cd keyflow
python main.py
```

## ❤️ Contributing  

Contributions are welcome! To contribute:  
1. Fork the repository.  
2. Add new features or fix bugs.  
3. Submit a pull request.  

## 📜 License  

This project is licensed under the [MIT License](LICENSE).  

---

> **KeyFlow**: Unlock the power of keyboard analytics! ⌨️