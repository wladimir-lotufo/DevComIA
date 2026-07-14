#!/usr/bin/env python3
"""
Session Manager - Antigravity Kit
=================================
Analyzes project state, detects tech stack, tracks file statistics, and provides
a summary of the current session.

Usage:
    python .agent/scripts/session_manager.py status [path]
    python .agent/scripts/session_manager.py info [path]
"""

import os
import json
import argparse
from pathlib import Path
from typing import Dict, Any, List

def get_project_root(path: str) -> Path:
    return Path(path).resolve()

def analyze_project(root: Path) -> Dict[str, Any]:
    stack = []
    name = root.name
    version = "0.0.0"
    scripts = []
    
    # Check for .NET
    has_sln = list(root.glob("*.sln"))
    has_csproj = list(root.rglob("*.csproj"))
    if has_sln or has_csproj:
        stack.append(".NET")
        for csproj in has_csproj:
            try:
                content = csproj.read_text(encoding='utf-8', errors='ignore')
                if "Microsoft.Maui" in content and ".NET MAUI" not in stack:
                    stack.append(".NET MAUI")
                if ("Microsoft.AspNetCore" in content or 'Sdk="Microsoft.NET.Sdk.Web"' in content) and "ASP.NET Core" not in stack:
                    stack.append("ASP.NET Core")
                if "Microsoft.EntityFrameworkCore" in content and "Entity Framework Core" not in stack:
                    stack.append("Entity Framework Core")
                if "Npgsql.EntityFrameworkCore.PostgreSQL" in content and "PostgreSQL" not in stack:
                    stack.append("PostgreSQL")
            except Exception:
                pass
                
    # Check for Node.js
    pkg_file = root / "package.json"
    if pkg_file.exists():
        try:
            with open(pkg_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            deps = data.get("dependencies", {})
            dev_deps = data.get("devDependencies", {})
            all_deps = {**deps, **dev_deps}
            
            if "next" in all_deps: stack.append("Next.js")
            elif "react" in all_deps and not "next" in all_deps: stack.append("React")
            elif "vue" in all_deps: stack.append("Vue")
            elif "svelte" in all_deps: stack.append("Svelte")
            elif "express" in all_deps: stack.append("Express")
            elif "nestjs" in all_deps or "@nestjs/core" in all_deps: stack.append("NestJS")
            
            if "tailwindcss" in all_deps: stack.append("Tailwind CSS")
            if "prisma" in all_deps: stack.append("Prisma")
            if "typescript" in all_deps: stack.append("TypeScript")
            
            name = data.get("name", name)
            version = data.get("version", version)
            scripts = list(data.get("scripts", {}).keys())
        except Exception:
            pass

    return {
        "name": name,
        "version": version,
        "stack": stack,
        "scripts": scripts
    }

def count_files(root: Path) -> Dict[str, int]:
    stats = {"created": 0, "modified": 0, "total": 0}
    # Simple count for now, comprehensive tracking would require git diff or extensive history
    exclude = {".git", "node_modules", ".next", "dist", "build", ".agent", ".gemini", "__pycache__"}
    
    for root_dir, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in exclude]
        stats["total"] += len(files)
        
    return stats

def detect_features(root: Path) -> List[str]:
    # Heuristic: look at folder names in src/
    features = []
    src = root / "src"
    if src.exists():
        possible_dirs = ["components", "modules", "features", "app", "pages", "services"]
        for d in possible_dirs:
            p = src / d
            if p.exists() and p.is_dir():
                # List subdirectories as likely features
                for child in p.iterdir():
                    if child.is_dir():
                        features.append(child.name)
    return features[:10] # Limit to top 10

def print_status(root: Path):
    info = analyze_project(root)
    stats = count_files(root)
    features = detect_features(root)
    
    print("\n=== Project Status ===")
    print(f"\n📁 Project: {info.get('name', root.name)}")
    print(f"📂 Path: {root}")
    print(f"🏷️  Type: {', '.join(info.get('stack', [])) if info.get('stack') else 'Generic'}")
    print(f"📊 Status: Active")
    
    print("\n🔧 Tech Stack:")
    for tech in info.get('stack', []):
        print(f"   • {tech}")
        
    print(f"\n✅ Detected Modules/Features ({len(features)}):")
    for feat in features:
        print(f"   • {feat}")
    if not features:
        print("   (No distinct feature modules detected)")
        
    print(f"\n📄 Files: {stats['total']} total files tracked")
    print("\n====================\n")

def main():
    parser = argparse.ArgumentParser(description="Session Manager")
    parser.add_argument("command", choices=["status", "info"], help="Command to run")
    parser.add_argument("path", nargs="?", default=".", help="Project path")
    
    args = parser.parse_args()
    root = get_project_root(args.path)
    
    if args.command == "status":
        print_status(root)
    elif args.command == "info":
        print(json.dumps(analyze_project(root), indent=2))

if __name__ == "__main__":
    main()
