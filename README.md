# SLIVER: Ultra-Strict Token Optimization Framework

SLIVER is an aggressive, zero-waste system prompt specification designed to minimize token usage across AI Coding Agents (AGY, Codex, Cursor, Cline, Windsurf). It extends the Ponytail framework by enforcing absolute code-only outputs and strict diff constraints.

---

## Token Savings & Performance Benchmarks

By enforcing the SLIVER rules, AI assistants operate in a highly cost-efficient manner. Based on agentic evaluations in real-world software templates (FastAPI + React), the framework achieves the following metrics:

* **Token Consumption:** **-22%** reduction in total session tokens.
* **Cost Reduction:** **-20%** cheaper per session.
* **Lines of Code (LOC):** **-54%** less generated code (reaching up to **94%** reduction on over-engineered tasks like UI components).
* **Execution Latency:** **-27%** faster response times due to shorter completions.
* **Compounding History Savings:** Because token history is resubmitted in every chat turn, reducing initial outputs by 25% compounds to save up to **35% of total context tokens** in multi-turn sessions (especially useful in AGY's TUI).

---

## The SLIVER Decision Ladder

Before generating any output, the AI agent must run the input through the SLIVER ladder:

1. **Response Prefix:** Start the response with `[SLIVER]` (followed by a newline) on the very first line to verify the framework is active.
2. **YAGNI (You Ain't Gonna Need It):** Decline non-essential requests.
3. **Standard Library Priority:** Exclude external packages if native tools solve it.
4. **Reusability Check:** Import or inherit existing functions. Do not duplicate.
5. **No Explanations (Zero-Prose):** Never explain code, changes, or logic. Return ONLY the code or diff.
6. **No Comments/Docstrings:** Remove all comments, docstrings, and type annotations unless strictly requested.
7. **Strict Diff-Only:** Return only the exact modified lines in diff format. Never output unmodified surrounding code.

---

## Installation & Configuration

### 1. Codex CLI (As a Native Plugin)
You can install SLIVER directly from this GitHub repository using the Codex CLI:

```bash
# Add the repository to your Codex marketplace list
codex plugin marketplace add https://github.com/bywarmx/sliver

# Install the sliver plugin
codex plugin add sliver@sliver
```
*Note: To verify it is loaded, run `/skills` or `/plugin list` in Codex. To invoke it explicitly in a chat thread, type `$sliver`.*

### 2. Google Antigravity (AGY) & Local IDEs
For AGY and local development tools, you can deploy the rules automatically using the included Python helper script or install them manually:

#### Option A: Automatic Installer (All IDEs & CLI)
Run any of the following commands in the root of your project workspace to deploy SLIVER rules automatically:

* **Via `curl` (Recommended):**
  ```bash
  curl -fsSL https://raw.githubusercontent.com/bywarmx/sliver/main/build_rules.py | python3
  ```
* **Via `wget`:**
  ```bash
  wget -qO- https://raw.githubusercontent.com/bywarmx/sliver/main/build_rules.py | python3
  ```
* **Via `git`:**
  ```bash
  git clone https://github.com/bywarmx/sliver.git && cd sliver && python3 build_rules.py
  ```

This will automatically create `.agents/AGENTS.md` (for AGY), `.cursorrules` (for Cursor), `.windsurfrules` (for Windsurf), `.clinerules` (for Cline), and `copilot-instructions.md` (for Copilot/Codex).

#### Option B: Manual Installation
Create the corresponding rule file at the root of your project workspace and paste the SLIVER rules inside:

* **Antigravity (AGY):** Create `.agents/AGENTS.md`. AGY automatically loads this file at startup.
* **Cursor IDE:** Create `.cursorrules`. Applies to all Chat and Composer actions.
* **Windsurf IDE:** Create `.windsurfrules`. Applies to the Cascade assistant.
* **Cline (VS Code Extension):** Create `.clinerules`. Loads as global agent constraints.
* **GitHub Copilot / Codex:** Create `copilot-instructions.md` (or `.github/copilot-instructions.md`). Copilot will respect these constraints in chat and inline completions.
