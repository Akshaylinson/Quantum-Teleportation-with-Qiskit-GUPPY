🛰️ Quantum Teleportation with Qiskit

A hands-on implementation of **Quantum Teleportation**, one of the most fascinating protocols in quantum information science.  
This project demonstrates how an arbitrary quantum state can be transferred from one qubit (Alice) to another distant qubit (Bob) — without physically moving the particle — using **quantum entanglement** and **classical communication**.

Built with [Qiskit](https://qiskit.org/) and simulated using [Qiskit Aer](https://qiskit.org/documentation/apidoc/aer.html).  
Includes **raw simulation results**, **post-processed teleportation corrections**, and professional **visualizations (circuit diagrams and histograms)**.

---

## ✨ Features
- ✅ Implements the full **quantum teleportation protocol**.
- ✅ Runs on **Qiskit AerSimulator** (no quantum hardware required).
- ✅ Separates circuit design (`circuits/teleport.py`) from execution (`main.py`).
- ✅ Produces **raw counts** (3-bit measurement results) and **corrected teleportation results**.
- ✅ Auto-saves results:
  - 📄 `results/teleport_results.txt` – raw & corrected counts  
  - 📊 `results/teleport_hist.png` – side-by-side histogram plots
- ✅ Professional **project structure** and reproducible environment.

---

## 📂 Project Structure
quantum-teleportation-guppy/
│── .venv/ # Virtual environment (Python 3.10+ recommended)
│── circuits/
│ └── teleport.py # Defines the teleportation circuit
│── results/
│ ├── teleport_results.txt # Simulation results (raw + corrected counts)
│ └── teleport_hist.png # Histogram plot (auto-generated)
│── main.py # Entry point (runs the teleportation simulation)
│── requirements.txt # Dependencies (Qiskit, Qiskit-Aer, Matplotlib)
│── README.md # Project documentation (this file)

yaml
Copy code

---

## ⚙️ Setup Instructions

### 1️⃣ Install Python (>=3.10 recommended)
Download from [python.org](https://www.python.org/downloads/).

### 2️⃣ Create and activate a virtual environment
```bash
python -m venv .venv
# On Windows (PowerShell):
.venv\Scripts\Activate.ps1
# On macOS/Linux:
source .venv/bin/activate
3️⃣ Install dependencies
bash
Copy code
python -m pip install --upgrade pip setuptools wheel
python -m pip install qiskit qiskit-aer matplotlib
4️⃣ Run the project
bash
Copy code
python main.py
📊 Outputs
After running, you will see:

Teleportation Circuit printed in the terminal.

Raw measurement counts (3 classical bits).

Corrected results showing Bob’s recovered qubit.

Histograms auto-saved and displayed.

Example saved files:

results/teleport_results.txt

results/teleport_hist.png

🔬 Quantum Protocol Explained
State Preparation – Alice prepares a qubit in an unknown state |ψ⟩.

Entanglement – Alice and Bob share an entangled Bell pair.

Bell Measurement – Alice performs joint measurements on her qubits.

Classical Communication – Alice sends two classical bits to Bob.

Correction – Bob applies conditional X/Z gates to recover |ψ⟩.

👉 The magic: The quantum state is destroyed on Alice’s side and reconstructed on Bob’s side — no faster-than-light communication occurs, but entanglement enables perfect state transfer.

📈 Example Results
Raw outcomes (3 classical bits):

bash
Copy code
{'000': 258, '011': 240, '101': 268, '110': 258}
Corrected teleportation results (Bob’s qubit):

arduino
Copy code
{'0': 502, '1': 522}
Histogram (auto-saved to results/teleport_hist.png):


🛠️ Tech Stack
Python 3.10+

Qiskit – Quantum SDK

Qiskit Aer – High-performance simulator

Matplotlib – Visualization

📌 Future Improvements
Support for real quantum hardware backends (e.g., IBM Quantum).

Extend to multi-qubit teleportation.

Integrate with Mojo / Guppy quantum DSL when stable.

Web-based visualization dashboard.

👨‍💻 Author
Developed with ❤️ using Qiskit.
This project is for educational & research purposes, demonstrating core principles of quantum information science.

📜 License
MIT License – free to use, modify, and share with attribution.

yaml
Copy code

---

⚡ This README makes your project look like a **serious professional repo**.  

👉 Do you want me to also **generate a `requirements.txt`** file with pinned versions (e.g., `qiskit==1.2.4`, `qiskit-aer==0.17.1`, etc.) so it’s fully reproducible?





Ask ChatGPT
