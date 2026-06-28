# Module 3, Topic 3: Basic YAML Overview

## 1. Syntax Rules & Formatting Guidelines
YAML is a human-readable data serialization language used by Ansible to pass structured data into templates.

* **Document Start:** Every YAML file begins with three hyphens (`---`).
* **Case Sensitivity:** YAML is completely case-sensitive.
* **Indentation:** Uses spaces for structure, **never tabs**.
* **Comments:** Begin with a hash symbol (`#`).
* **Strings:** Quotation marks are optional unless they contain special characters.

---

## 2. Core Data Structures

### A. Simple Lists (Sequences)
Items listed with a leading dash (`-`).
```yaml
---
# vegetables
- asparagus
- spinach
- lettuce
- celery
...