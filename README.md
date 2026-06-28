# SLIVER: Ultra-Strict Token Optimization Framework

SLIVER is an aggressive, zero-waste system prompt specification designed to minimize token usage across AI Coding Agents (AGY, Codex, Cursor, Cline, Windsurf). It extends the Ponytail framework by enforcing absolute code-only outputs and strict diff constraints.

## The SLIVER Decision Ladder

Before generating any output, the AI agent must run the input through the SLIVER ladder:

1. **YAGNI (You Ain't Gonna Need It):** Decline non-essential requests.
2. **Standard Library Priority:** Exclude external packages if native tools solve it.
3. **Reusability Check:** Import or inherit existing functions. Do not duplicate.
4. **No Explanations (Zero-Prose):** Never explain code, changes, or logic. Return ONLY the code or diff.
5. **No Comments/Docstrings:** Remove all comments, docstrings, and type annotations unless strictly requested.
6. **Strict Diff-Only:** Return only the exact modified lines in diff format. Never output unmodified surrounding code.

## Target Tool Configurations

SLIVER rules are designed to be deployed to the following files depending on the agent in use:

* **Antigravity (AGY):** `.agents/AGENTS.md`
* **Cursor:** `.cursorrules`
* **Windsurf:** `.windsurfrules`
* **Cline:** `.clinerules`
* **GitHub Copilot / Codex:** `copilot-instructions.md`

## Installation

Run the deployer script in your workspace folder to automatically configure all AI tools present:

```bash
python3 build_rules.py
```
