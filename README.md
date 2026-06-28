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

## Quick Installation (One-Liners)

To install and activate SLIVER in your current project workspace, run any of the following commands in your terminal:

### Option A: Via `curl` (Recommended)
```bash
curl -fsSL https://raw.githubusercontent.com/bywarmx/sliver/main/build_rules.py | python3
```

### Option B: Via `wget`
```bash
wget -qO- https://raw.githubusercontent.com/bywarmx/sliver/main/build_rules.py | python3
```

### Option C: Via `git`
```bash
git clone https://github.com/bywarmx/sliver.git && cd sliver && python3 build_rules.py
```

---

## Manual Installation (Per Agent)

If you prefer to configure the rules manually, create the corresponding file at the root of your project workspace and paste the SLIVER rules inside:

#### 1. Google Antigravity (AGY)
* **File:** `.agents/AGENTS.md`
* AGY automatically loads this file at startup.

#### 2. Cursor IDE
* **File:** `.cursorrules`
* Applies to all Chat and Composer actions.

#### 3. Windsurf IDE
* **File:** `.windsurfrules`
* Applies to the Cascade assistant.

#### 4. Cline (VS Code Extension)
* **File:** `.clinerules`
* Loads as global agent constraints.

#### 5. GitHub Copilot / Codex
* **File:** `copilot-instructions.md` (or `.github/copilot-instructions.md`)
* Copilot will respect these constraints in chat and inline completions.
