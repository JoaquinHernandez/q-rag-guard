# q-rag-guard# 🛡️ Q-RAG-Guard: Unified Quantum-Safe CBOM & LLM/RAG Injection Scanner

A dual-engine DevSecOps and AI security utility that bridges **Post-Quantum Cryptography (PQC) readiness** with **LLM & RAG Retrieval Poisoning Defense (OWASP Top 10 for LLMs)**.

---

## ⚡ What It Solves

Modern technology stacks face two major emerging security transitions:
1. **The Quantum Transition:** Classical public-key cryptography (RSA, ECC, Diffie-Hellman) is vulnerable to Shor's algorithm on Cryptographically Relevant Quantum Computers (CRQCs). Teams need automated **Cryptographic Bill of Materials (CBOM)** discovery to migrate to NIST PQC standards (FIPS 203 ML-KEM, FIPS 204 ML-DSA).
2. **The AI & RAG Security Vector:** Retrieval-Augmented Generation (RAG) knowledge bases and AI agents are susceptible to **Indirect Prompt Injection** and **Corpus Poisoning** that subvert model decision-making.

---

## ✨ Features
- **Automated CBOM Generator**: Scans codebases for classical asymmetric primitives and provides actionable NIST PQC migration targets.
- **RAG Poisoning & Jailbreak Radar**: Intercepts indirect prompt injection payloads hidden inside external retrieval corpus files and document embeddings.
- **Unified JSON Compliance Output**: Exports structured audit logs and CBOM ledgers for enterprise DevSecOps pipelines.
- **Zero Third-Party Dependencies**: Pure Python standard library implementation.

---

## 🚀 Quick Start
```bash
python3 q_rag_guard.py
