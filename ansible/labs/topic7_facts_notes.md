# Topic 7: Gathering Cisco IOS Device Facts

## 1. Playbook Rule of Thumb
* Always specify `gather_facts: no` at the playbook level for network endpoints to prevent standard Linux setup scripts from crashing the execution against target switches/routers.

## 2. Fact Retrieval Module
* Legacy module: `ios_facts`
* Modern collection module: `cisco.ios.ios_facts`
* Parameter used to optimize collection speed and lower CPU overhead: `gather_subset`
* Common Subsets:
  * `min`: Core hardware model, serial key, and code system version string.
    * `interfaces`: Comprehensive line-state mapping table and configuration values per port.
      * `config`: Pulls down the active running-config.

      ## 3. Core Exported Properties
      * `ansible_facts['net_hostname']` -> Device name identifier.
      * `ansible_facts['net_model']` -> Chassis hardware architecture footprint.
      * `ansible_facts['net_version']` -> Operating system release tag.
      