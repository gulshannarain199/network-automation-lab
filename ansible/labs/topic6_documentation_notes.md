
# Topic 6: Ansible Documentation Reference Guide

## 1. Web Documentation (docs.ansible.com)
* Main portal for standard modules (e.g., `cisco.ios.ios_config`).
* Contains complete **Parameter Tables** (like `backup: yes`, `before`, `after`).
* Includes copy-pasteable playbook examples at the bottom of the page.

## 2. CLI Documentation (ansible-doc)
* Built-in command line utility for **offline** lookups.
* Syntax: `ansible-doc cisco.ios.ios_config`

## 3. Ansible Galaxy (galaxy.ansible.com)
* The community automation hub ("app store") for downloading third-party collections.
* Command to install vendor drivers (e.g., Cisco IOS-XR):
  `ansible-galaxy collection install cisco.iosxr`
