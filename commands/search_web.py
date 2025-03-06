import webbrowser

def run(args):
    if not args:
        print("Usage: devkit search_web <query>")
        return
    
    query = "+".join(args)
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    print(f"Searching Google for: {' '.join(args)}")
