import subprocess

GIT_ALIASES = {
    "st": "status",
    "co": "checkout",
    "br": "branch",
    "cm": "commit -m",
    "psh": "push",
    "pll": "pull",
}

def run(args):
    if len(args) < 1:
        print("Usage: devkit git_simplify <alias> [args]")
        return

    alias = args[0]
    if alias in GIT_ALIASES:
        command = ["git"] + GIT_ALIASES[alias].split() + args[1:]
        subprocess.run(command)
    else:
        print(f"Unknown alias: {alias}")
