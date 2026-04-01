import os
import re

# 敏感詞與高風險函式
SENSITIVE_PATTERNS = {
    'Hardcoded Secrets': [r'API_KEY\s*=\s*["\']\w+["\']', r'PASSWORD\s*=\s*["\']\w+["\']', r'SECRET\s*=\s*["\']\w+["\']'],
    'Command Injection': [r'\bos\.system\(', r'\bsubprocess\.run\(', r'\beval\(', r'\bexec\('],
    'Suspicious Network': [r'requests\.post\(', r'http\.client\.HTTPSConnection\(', r'\baxios\.post\('],
    'Sensitive File Access': [r'\bos\.remove\(', r'\bshutil\.rmtree\(', r'\bfs\.unlink\(']
}

def audit_file(filepath):
    findings = []
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
            for line_num, line in enumerate(lines, 1):
                for category, patterns in SENSITIVE_PATTERNS.items():
                    for pattern in patterns:
                        if re.search(pattern, line):
                            findings.append({
                                'category': category,
                                'line': line_num,
                                'content': line.strip()
                            })
    except Exception as e:
        pass
    return findings

def audit_project(directory='.'):
    all_findings = {}
    for root, dirs, files in os.walk(directory):
        skip_dirs = ['venv', '.venv', '__pycache__', 'node_modules', '.git']
        if any(d in root.split(os.sep) for d in skip_dirs):
            continue
            
        for filename in files:
            if filename.endswith(('.py', '.js', '.ts', '.java')):
                filepath = os.path.join(root, filename)
                file_findings = audit_file(filepath)
                if file_findings:
                    all_findings[os.path.relpath(filepath, directory)] = file_findings
    return all_findings

if __name__ == '__main__':
    print("Running Mandatory Behavioral Code Scan & Security Audit...")
    findings = audit_project()
    if not findings:
        print("I have audited the source code and found no malicious patterns.")
    else:
        print("⚠️ Security Audit Summary:")
        for file, items in findings.items():
            print(f"\nFile: {file}")
            for item in items:
                print(f"  - [{item['category']}] Line {item['line']}: {item['content']}")
        print("\nDO NOT launch if these findings are unexpected.")
