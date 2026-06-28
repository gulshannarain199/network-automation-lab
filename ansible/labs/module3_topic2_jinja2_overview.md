# Module 3, Topic 2: Jinja2 Templating Overview

Jinja2 is a powerful text templating engine written for Python. In network automation, it is used to decouple static device configurations from unique network data, allowing engineers to generate thousands of configuration files programmatically using a single template block.

---

## 1. Core Architecture Concepts

Network automation using templates breaks down into a simple combination:

$$\text{Template (Jinja2)} + \text{Variables (YAML/JSON)} = \text{Rendered Configuration (Plain Text CLI)}$$

* **The Problem:** Writing hardcoded flat text configurations requires editing dozens of individual network node files when changes occur.
* **The Solution:** Creating a "cookie-cutter" layout where changing network components are designated as dynamic variables.

---

## 2. Basic Syntax Indicators

Jinja2 parses plain text configuration files by hunting for special curly-brace delimiters:

* `{{ variable }}`: **Expressions / Placeholders** — Used to print out the literal value of an assigned data variable directly onto the line.
* `{% control %}`: **Statements / Logic** — Used to handle operational programming logic like loops (`for`) and conditional tests (`if`).
* `{# comment #}`: **Comments** — Internal engineering notes that are stripped out completely during the compiling process.

> **Whitespace Control Hint:** Adding a hyphen to a statement tag (`{%-` or `-%}`) instructs the engine to strip out trailing or leading whitespaces and carriage return newlines, ensuring a tight, well-formatted device config.

---

## 3. Practical Code Examples

### A. Dynamic Loop Rendering (VLAN Generation)
**Jinja2 Template (`vlan.j2`):**
```jinja
{% for vlan in vlans -%}
{{ vlan }}
{% endfor -%}