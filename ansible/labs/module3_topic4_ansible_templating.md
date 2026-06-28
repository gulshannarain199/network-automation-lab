# Module 3, Topic 4: Configuration Templating with Ansible

## 1. Overview of the Automation Architecture
To cleanly automate configurations, responsibilities are completely separated into a three-tier architecture:

* **The Template Logic (Jinja2):** Found inside the `templates/` directory (e.g., `interface.j2`). It lays out the raw Cisco IOS syntax structure combined with logical operations (`for` loops or `if` conditions).
* **The Variables Data (YAML):** Stored cleanly within files matching host inventory configurations (e.g., `host_vars/csr1kv1.yml`). It defines the raw network properties data distinct from structural logic.
* **The Core Orchestrator (Ansible):** The execution engine that binds templates and variables together, compiles clean plain text `.cfg` files, and deploys them onto production hardware.

---

## 2. Directory Structure Blueprint
Before running a playbook, directories are structured predictably so Ansible automatically tracks inheritance parameters:

```text
.
├── build_config.yml       # The primary Ansible Playbook
├── configs/               # Destination folder for compiled engine outputs
├── host_vars/             # Host-specific variable overrides
│   ├── csr1kv1.yml        # Variables mapped only to router 1
│   ├── csr1kv2.yml        # Variables mapped only to router 2
│   └── csr1kv3.yml        # Variables mapped only to router 3
├── inventory              # List of targets grouped under names (e.g., [iosxe])
└── templates/             # Directory housing template files
    └── interface.j2       # Master configuration layout engine