# DevOps Automation Scripts

This repository contains a collection of DevOps automation scripts for managing EKS Helm deployments and RDS backups/restores using AWS CLI.

## 📄 Script: devops_scripts.py

### Features
- 🚀 *Helm Deployment*: Automate rolling upgrades with Helm 3
- 🛡️ *RDS Snapshot*: Create on-demand backups of your PostgreSQL RDS instance
- ♻️ *RDS Restore*: Restore your database from a given snapshot

---

### 🛠 Requirements

Ensure the following tools are installed and configured:
- Python 3.6+
- AWS CLI (configured with appropriate credentials)
- Helm 3
- boto3 (optional for advanced AWS scripting)
- subprocess and datetime (built-in)

---

### 🚀 Usage

```bash
# Make sure the script is executable
chmod +x devops_scripts.py

# Run the script
./devops_scripts.py
