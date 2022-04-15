import json

def read_json(path):
    with open(path, 'r') as f:
        data = json.load(f)
        f.close()
    return data

def write_codeowners(data, path = "CODEOWNERS"):
    LangtoExt = {
        "*": "*",
        "c": "c",
        "cpp": "cpp",
        "python": "py",
        "java": "java",
        "swift": "swift",
        "rust": "rs",
        "kotlin": "kt",
        "javascript": "js",
        "go": "go"
    }
    f = open(path, 'w')
    invited = data['invited']
    data = data['auth']
    for user, langs in data.items():
        if user not in invited:
            continue
        info = [f"# {user}"]
        for lang in langs['language']:
            ext = LangtoExt[lang]
            info.append(
                f"solution/*/*.{ext} @{user}"
            )
        
        info.append('\n')
        f.write('\n'.join(info))
    
    f.close()

if __name__ == "__main__":
    data = read_json('./reviewer.json')
    write_codeowners(data)