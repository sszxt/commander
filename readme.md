# Commander - Your Terminal Assistant

**Commander** is a lightweight, fully local Large Language Model (LLM)-powered terminal assistant. Designed for Unix systems, it lets you generate, explain, and run terminal commands through natural language — all from your terminal and without any need for cloud services or internet access.

> Think of it as your AI command-line co-pilot for linux commands — private, fast, and efficient.



## Features

- **Local LLM-Powered**: Works entirely offline — your data stays on your machine.
- **Interactive Shell**: Start a session where you can chat with the LLM to generate commands.
- **Quick Prompt Mode**: Run one-off prompts directly from the command line.
- **Lightweight**: Minimal dependencies and fast startup.
- **Unix-Focused**: Tailored to understand and generate Unix-based commands.



## Installation

You can install Commander locally using `pip`:

```bash
git clone https://github.com/yourusername/commander.git
cd commander
pip install .
```
## Usage 

**Interactive Mode**
```bash
commander
```
- Start an AI-powered interactive shell
- Then, start chatting with your LLM assistant to get help, generate commands, or run them directly.

Example:
```bash
> How do I find the largest file in a directory?
> find . -type f -exec du -h {} + | sort -rh | head -n 1
```

**One - Line Prompt Mode**
```bash
commander "how to list all open ports"
```
- Skips the interactive shell and get instant suggestions for a one-line prompt


Example : 

```bash 
commander "how to list all open ports"
assistant : sudo lsof -i -P -n | grep LISTEN
```

## Project Structure
```bash
commander/
├── commander/              # Source code and model
│   ├── __main__.py         # CLI entry point
│   └── model/
│       └── checkpoint-750/ # Trained Local model files
├── build/                  # Build artifacts
├── requirements.txt        # Python dependencies
├── setup.py                # Installer
└── readme.md               # You're reading this right now.
```

## Privacy
Commander runs entirely locally. No commands, prompts, or data are sent to any server. It's your assistant, and your business stays yours.

## Contribution
Commander leverages powerful open-source LLMs and tools, and we welcome your contributions — feel free to open an issue or pull request for bug reports, suggestions, or new features!
