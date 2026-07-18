# 🛡️ Deception-Based Industrial Honeypot for ICS Networks

A Python-based Industrial Control System (ICS) honeypot that detects suspicious Modbus TCP traffic and transparently redirects attackers to a realistic fake PLC while allowing legitimate clients to communicate with the real PLC.

---

# 📖 Overview

Industrial Control Systems are increasingly targeted by attackers through reconnaissance, unauthorized register access, and malicious write operations.

This project implements a deception-based architecture where a gateway continuously monitors Modbus traffic, calculates a risk score, and redirects suspicious clients to a honeypot PLC without disrupting legitimate communication.

---

# ✨ Features

- 🏭 Modbus TCP PLC Simulation
- 🌡️ Realistic Industrial Process Simulation
- 🌐 Gateway Proxy
- 🔍 Protocol-aware Packet Inspection
- ⚠️ Risk-based Decision Engine
- 🎭 Transparent Traffic Redirection
- 🍯 Industrial Honeypot
- 📝 Attack Logging
- 🧠 Threat Intelligence Collection
- 📄 Attack Report Generation

---

# 🛠️ Tech Stack

- 🐍 Python 3
- 📡 pymodbus
- 🕷️ Scapy
- 🗄️ SQLite
- 🐧 Linux
- 🔥 iptables

---

# ✅ Current Progress

## 🏭 Phase 1 — PLC Development

- [x] Project setup
- [x] Git repository
- [x] Process simulator
- [x] Sensor simulation
- [x] Multi-threaded simulator
- [x] Modbus TCP Server
- [x] Register synchronization
- [x] Tested using mbpoll

---

## 🌐 Phase 2 — Gateway

- [x] TCP Proxy
- [x] Client connection handler
- [x] Forward packets to Real PLC
- [x] Receive PLC responses
- [x] Forward responses back to client
- [ ] Support multiple clients

---

## 🔍 Phase 3 — Detection Engine

- [x] Parse Modbus packets
- [ ] Detect excessive polling
- [ ] Detect register scanning
- [ ] Detect unauthorized writes
- [ ] Detect invalid function codes
- [ ] Detect malformed packets

---

## ⚠️ Phase 4 — Risk Engine

- [ ] Risk score calculation
- [ ] Per-IP tracking
- [ ] Risk threshold
- [ ] Automatic risk decay
- [ ] Blacklist support

---

## 🍯 Phase 5 — Honeypot PLC

- [ ] Fake PLC implementation
- [ ] Fake industrial process
- [ ] Fake sensor values
- [ ] Accept attacker writes
- [ ] Log every interaction

---

## 🎭 Phase 6 — Deception Engine

- [ ] Redirect suspicious clients
- [ ] Transparent forwarding
- [ ] Session persistence
- [ ] Redirect based on risk score

---

## 📝 Phase 7 — Logging

- [ ] Connection logs
- [ ] Packet logs
- [ ] Risk logs
- [ ] Attack timeline
- [ ] JSON log format

---

## 🧠 Phase 8 — Threat Intelligence

- [ ] SQLite database
- [ ] Store attacker IP
- [ ] Store function codes
- [ ] Store accessed registers
- [ ] Generate attack statistics

---

## 📄 Phase 9 — Reports

- [ ] Attack summary
- [ ] Top attackers
- [ ] Function code statistics
- [ ] Most targeted registers
- [ ] PDF report generation

---

## 🖥️ Phase 10 — Dashboard

- [ ] Live traffic monitoring
- [ ] Active clients
- [ ] Current risk scores
- [ ] Attack history
- [ ] Real PLC status
- [ ] Honeypot PLC status

---

# 🚀 Future Improvements

- 🌍 Web Dashboard
- 🍯 Multiple Honeypots
- 🔌 Modbus RTU Support
- ⚡ DNP3 Support
- 🏗️ IEC-104 Support
- 📨 MQTT Support
- 🤖 Machine Learning Based Detection
- 🌐 Threat Intelligence Feed Integration
- 🐳 Docker Deployment
- ☸️ Kubernetes Deployment

---

# 🎯 Learning Objectives

This project demonstrates:

- 🏭 Industrial Control System Security
- 📡 Modbus TCP Protocol
- 🐍 Python Networking
- 🌐 TCP Proxy Development
- 🍯 Honeypot Design
- 🎭 Deception Technology
- 🔍 Threat Detection
- ⚠️ Risk Scoring
- 🐧 Linux Networking
- 🔐 Industrial Cybersecurity

---

# 📜 License

This project is developed for educational and research purposes.