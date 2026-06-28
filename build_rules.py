#!/usr/bin/env python3
import os
import sys

RULES_CONTENT = """# SLIVER: Token Optimization Rules
Enforce the SLIVER token-saving constraints strictly. No exceptions:
1. **YAGNI:** Decline non-essential feature requests.
2. **Native Only:** Use standard libraries. Never import new packages unless vital.
3. **Zero-Prose:** Write code or unified diffs ONLY. Never explain code, changes, or implementation steps.
4. **No Comments:** Never output comments, docstrings, or annotations unless explicitly asked.
5. **Unified Diff Format:** Return only modified lines prefixed with + or -. No surrounding context.
"""

FILES_TO_GENERATE = {
    ".agents/AGENTS.md": "Antigravity (AGY)",
    ".cursorrules": "Cursor IDE",
    ".windsurfrules": "Windsurf IDE",
    ".clinerules": "Cline (VS Code)",
    "copilot-instructions.md": "GitHub Copilot / Codex"
}

def deploy_rules(target_dir):
    print(f"[*] Deploying SLIVER rules in: {target_dir}")
    
    for filename, description in FILES_TO_GENERATE.items():
        filepath = os.path.join(target_dir, filename)
        
        # Create directories if needed
        dir_name = os.path.dirname(filepath)
        if dir_name:
            os.makedirs(os.path.join(target_dir, dir_name), exist_ok=True)
            
        try:
            with open(filepath, 'w') as f:
                f.write(RULES_CONTENT)
            print(f"  [+] Created {filename} ({description})")
        except Exception as e:
            print(f"  [!] Error writing {filename}: {e}")

if __name__ == "__main__":
    target = os.getcwd()
    if len(sys.argv) > 1:
        target = sys.argv[1]
        
    deploy_rules(target)
    print("\n[+] SLIVER Rules successfully deployed. Your active AI agents will now run in ultra-strict token-saving mode.")
