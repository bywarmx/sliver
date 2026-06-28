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

---

## Installation & Configuration Instructions

You can configure SLIVER manually or automatically for each AI assistant:

### Method 1: Automatic Installation (Recommended)
Copy the `build_rules.py` script to the root of your project directory and run it:
```bash
python3 build_rules.py
```
This script will automatically detect and generate the correct rules file for all supported AI agents present in your workspace.

### Method 2: Manual Installation (Per Agent)

#### 1. Google Antigravity (AGY)
Create a file named `.agents/AGENTS.md` in the root of your project workspace and paste the SLIVER rules inside. AGY automatically loads this file at startup.

#### 2. Cursor IDE
Create a file named `.cursorrules` in the root of your project workspace and paste the SLIVER rules inside. Cursor applies these instructions to all Chat and Composer actions.

#### 3. Windsurf IDE
Create a file named `.windsurfrules` in the root of your project workspace and paste the SLIVER rules. Windsurf will apply them to the Cascade assistant.

#### 4. Cline (VS Code Extension)
Create a file named `.clinerules` in the root of your project workspace and paste the rules. Cline will load them as global agent constraints.

#### 5. GitHub Copilot / Codex
Create a file named `copilot-instructions.md` at the root of your repository (or inside `.github/copilot-instructions.md`) and paste the rules. Copilot will respect these constraints in chat and inline completions.
