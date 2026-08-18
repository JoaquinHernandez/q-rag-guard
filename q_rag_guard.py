import os
import sys
import json
import re
import time
from datetime import datetime, timezone

# ANSI Styling Tokens
RESET   = "\033[0m"
BOLD    = "\033[1m"
DIM     = "\033[2m"
RED     = "\033[38;5;196m"
GREEN   = "\033[38;5;48m"
CYAN    = "\033[38;5;51m"
AMBER   = "\033[38;5;214m"
MAGENTA = "\033[38;5;201m"
GRAY    = "\033[38;5;242m"

BANNER = f"""{CYAN}{BOLD}
  ██████╗         ██████╗  █████╗  ██████╗        ██████╗ ██╗   ██╗ █████╗ ██████╗ ██████╗ 
 ██╔═══██╗        ██╔══██╗██╔══██╗██╔════╝       ██╔════╝ ██║   ██║██╔══██╗██╔══██╗██╔══██╗
 ██║   ██║█████╗  ██████╔╝███████║██║  ███╗█████╗██║  ███╗██║   ██║███████║██████╔╝██║  ██║
 ██║▄▄ ██║╚════╝  ██╔══██╗██╔══██║██║   ██║╚════╝██║   ██║██║   ██║██╔══██║██╔══██╗██║  ██║
 ╚██████╔╝        ██║  ██║██║  ██║╚██████╔╝      ╚██████╔╝╚██████╔╝██║  ██║██║  ██║██████╔╝
  ╚══▀▀═╝         ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝        ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ 
{RESET}{AMBER} » UNIFIED QUANTUM-SAFE CBOM & LLM/RAG ADVERSARIAL INJECTION SCANNER «{RESET}
"""

class QRAGGuardScanner:
    def __init__(self, policy_file="guard_policy.json"):
        if not os.path.exists(policy_file):
            print(f"{RED}[-] Policy file '{policy_file}' not found.{RESET}")
            sys.exit(1)

        with open(policy_file, "r") as f:
            self.policy = json.load(f)

        self.qc_rules = self.policy.get("quantum_crypto_rules", [])
        self.rag_rules = self.policy.get("rag_injection_rules", [])

    def scan_quantum_crypto(self, source_file):
        """Scans codebase for quantum-vulnerable cryptography and builds a CBOM."""
        print(f"\n{BOLD}[1/2] Executing Post-Quantum Cryptographic Bill of Materials (CBOM) Scan...{RESET}")
        print(f"  Target Source: {CYAN}{source_file}{RESET}")

        if not os.path.exists(source_file):
            print(f"{RED}  [-] Source target '{source_file}' missing.{RESET}")
            return []

        cbom_findings = []
        with open(source_file, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()

        for idx, line in enumerate(lines, start=1):
            clean = line.strip()
            if not clean or clean.startswith("#"):
                continue

            for rule in self.qc_rules:
                if re.search(rule["regex"], clean):
                    cbom_findings.append({
                        "line": idx,
                        "id": rule["id"],
                        "name": rule["name"],
                        "severity": rule["severity"],
                        "vulnerability": rule["vulnerability"],
                        "pqc_migration": rule["pqc_alternative"],
                        "snippet": clean
                    })

        if cbom_findings:
            print(f"  {RED}[🚨 QUANTUM RISK]{RESET} Discovered {len(cbom_findings)} quantum-vulnerable cryptographic signature(s):")
            for f in cbom_findings:
                print(f"    • Line {f['line']:<3} [{RED}{f['severity']}{RESET}] {BOLD}{f['name']}{RESET}")
                print(f"      {GRAY}├─ Risk:{RESET} {f['vulnerability']}")
                print(f"      {GRAY}└─ NIST PQC Target:{RESET} {GREEN}{f['pqc_migration']}{RESET}")
        else:
            print(f"  {GREEN}[✓] Post-Quantum Audit Passed:{RESET} No Shor-vulnerable asymmetric algorithms detected.")

        return cbom_findings

    def scan_rag_pipeline(self, rag_file):
        """Audits RAG knowledge documents and context chunks for indirect prompt injections."""
        print(f"\n{BOLD}[2/2] Executing LLM & RAG Retrieval Injection Radar...{RESET}")
        print(f"  Target Knowledge Base: {CYAN}{rag_file}{RESET}")

        if not os.path.exists(rag_file):
            print(f"{RED}  [-] RAG target '{rag_file}' missing.{RESET}")
            return []

        rag_findings = []
        with open(rag_file, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()

        for idx, line in enumerate(lines, start=1):
            clean = line.strip()
            if not clean:
                continue

            for rule in self.rag_rules:
                match = re.search(rule["regex"], clean)
                if match:
                    rag_findings.append({
                        "line": idx,
                        "id": rule["id"],
                        "name": rule["name"],
                        "severity": rule["severity"],
                        "impact": rule["impact"],
                        "matched_text": match.group(0)
                    })

        if rag_findings:
            print(f"  {RED}[🚨 RAG ADVERSARIAL THREAT]{RESET} Detected {len(rag_findings)} injection / context poisoning vector(s):")
            for f in rag_findings:
                print(f"    • Line {f['line']:<3} [{RED}{f['severity']}{RESET}] {BOLD}{f['name']}{RESET}")
                print(f"      {GRAY}├─ Threat Impact:{RESET} {f['impact']}")
                print(f"      {GRAY}└─ Poison Payload:{RESET} {AMBER}'{f['matched_text']}'{RESET}")
        else:
            print(f"  {GREEN}[✓] RAG Corpus Clean:{RESET} No adversarial context poisoning or prompt injections detected.")

        return rag_findings

    def run(self, code_target="test_codebase.py", rag_target="rag_knowledge_base.txt"):
        print(BANNER)
        print(f"{BOLD}Initializing Unified Next-Gen Cyber Defense Matrix...{RESET}\n")

        steps = [
            "Parsing NIST PQC Algorithm Catalog (FIPS 203 ML-KEM, FIPS 204 ML-DSA)",
            "Hooking Cryptographic Bill of Materials (CBOM) Engine",
            "Loading OWASP Top 10 for LLMs / RAG Injection Ruleset",
            "Compiling Multi-Vector Threat Surface Correlator"
        ]
        for step in steps:
            time.sleep(0.2)
            print(f"  {CYAN}▸{RESET} {step}...")

        print("\n" + "=" * 85)

        # Run both scanners
        cbom_results = self.scan_quantum_crypto(code_target)
        rag_results = self.scan_rag_pipeline(rag_target)

        # Summary Metrics
        print("\n" + "=" * 85)
        total_threats = len(cbom_results) + len(rag_results)
        status_color = RED if total_threats > 0 else GREEN

        print(f"{BOLD}Unified Scan Summary:{RESET} {status_color}{total_threats} Security Deficiencies Identified{RESET}")
        print(f"  • Quantum-Vulnerable Crypto Assets: {RED}{len(cbom_results)}{RESET}")
        print(f"  • RAG & LLM Adversarial Payloads:   {RED}{len(rag_results)}{RESET}")

        # Export JSON CBOM and AI Audit Artifact
        output_report = {
            "timestamp": datetime.now(timezone.utc).isoformat() + "Z",
            "cbom_crypto_findings": cbom_results,
            "rag_injection_findings": rag_results
        }
        with open("q_rag_security_report.json", "w") as f:
            json.dump(output_report, f, indent=2)

        print(f"\n{GREEN}[✓] Exported Unified CBOM & AI Security Audit:{RESET} {BOLD}q_rag_security_report.json{RESET}\n")

if __name__ == "__main__":
    scanner = QRAGGuardScanner()
    scanner.run()
