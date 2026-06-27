# Topic 8: Using the Cisco IOS Core Command Module

## 1. Operational Command Execution
* Module used: `cisco.ios.ios_command`
* Core Function: Used to execute non-configuring operational inspection parameters (like standard `show` or `ping` commands).
* Key Rule: Never utilize this module to issue persistent state configuration changes.

## 2. Capturing Execution Output
* The `commands` argument takes an ordered structured block array list of explicit CLI target strings.
* Use the `register` keyword to capture console stream responses into an internal runtime variable (e.g., `register: command_output`).
* Output text lines are indexed within a standard array format string wrapper payload:
  * `command_output.stdout[0]` maps to the textual screen response of the first command.
  * `command_output.stdout[1]` maps to the textual screen response of the second command.