#!/usr/bin/env python3
"""
scripts_ingester.py
Recursively walks a directory of .sql files, sanitizes content,
generates frontmatter, and writes .md files into the Astro content collection.

Usage:
    python extractor/scripts_ingester.py
"""

import os
import re
import json
import hashlib
from pathlib import Path

# ── Config ──────────────────────────────────────────────────────────────────
SCRIPTS_SOURCE = r"C:\Users\kedhar\Desktop\scripts"
SCRIPTS_OUTPUT = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "site", "src", "content", "scripts"
)

# ── Category mapping: folder name → Zod enum value ─────────────────────────
FOLDER_CATEGORY_MAP = {
    "always on ag":                   "high-availability",
    "clustering":                     "high-availability",
    "log shipping":                   "high-availability",
    "mirroring":                      "high-availability",
    "architecture":                   "architecture",
    "automation":                     "automation",
    "backup restore corruption":      "backup-restore",
    "database":                       "database",
    "general":                        "general",
    "others":                         "general",
    "indexing":                       "index-maintenance",
    "installation":                   "installation",
    "lock block deadlock":            "performance",
    "performance health monitoring":  "performance",
    "troubleshooting":                "troubleshooting",
    "replication":                    "replication",
    "security":                       "security-audit",
    "transparent data encryption":    "security-audit",
    "table":                          "database",
    "upgradation and migration":      "migration",
}

# ── Sanitization patterns ──────────────────────────────────────────────────
def build_sanitizer():
    """Return a function that sanitizes SQL content."""
    patterns = [
        # Windows local paths: C:\... D:\... etc.
        (re.compile(r"""['"]([A-Za-z]:\\(?:[^'"\\]+\\)*[^'"\\]*)['"]""", re.IGNORECASE),
         lambda m: f"'{os.path.basename(m.group(1))}'"),

        # Generic file paths in strings: /home/..., /tmp/...
        (re.compile(r"""['"](/[^'"]+)['"]"""),
         lambda m: f"'[path]'"),

        # IP addresses
        (re.compile(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'),
         lambda m: '[ip_address]'),

        # Passwords in SQL: PASSWORD = 'xxx'
        (re.compile(r"(PASSWORD\s*=\s*)'[^']*'", re.IGNORECASE),
         lambda m: f"{m.group(1)}'[password]'"),

        # Passwords in SQL: PASSWORD N'xxx'
        (re.compile(r"(PASSWORD\s*=\s*)N'[^']*'", re.IGNORECASE),
         lambda m: f"{m.group(1)}N'[password]'"),

        # Encrypted values: ENCRYPTED_VALUE = 0x...
        (re.compile(r"(ENCRYPTED_VALUE\s*=\s*)0x[0-9A-Fa-f]+", re.IGNORECASE),
         lambda m: f"{m.group(1)}0x[encrypted_value]"),

        # SID values: SID = 0x...
        (re.compile(r"(SID\s*=\s*)0x[0-9A-Fa-f]+", re.IGNORECASE),
         lambda m: f"{m.group(1)}0x[sid]"),

        # Instance names in brackets: [SERVER\INSTANCE]
        (re.compile(r'\[[A-Za-z0-9_-]+\\[A-Za-z0-9_-]+\]'),
         lambda m: '[instance_name]'),

        # Machine names in SERVER = 'xxx'
        (re.compile(r"(SERVER\s*=\s*)'[^']*'", re.IGNORECASE),
         lambda m: f"{m.group(1)}'[server]'"),

        # DataSource in connection strings
        (re.compile(r"(Data\s*Source\s*=\s*)[^;]+", re.IGNORECASE),
         lambda m: f"{m.group(1)}[datasource]"),

        # User ID in connection strings
        (re.compile(r"(User\s*ID\s*=\s*)[^;]+", re.IGNORECASE),
         lambda m: f"{m.group(1)}[username]"),

        # Initial Catalog in connection strings
        (re.compile(r"(Initial\s*Catalog\s*=\s*)[^;]+", re.IGNORECASE),
         lambda m: f"{m.group(1)}[database]"),
    ]

    def sanitize(text):
        for pattern, replacement in patterns:
            text = pattern.sub(replacement, text)
        # Normalize multiple blank lines
        text = re.sub(r'\n\s*\n\s*\n+', '\n\n', text)
        return text.strip()

    return sanitize


# ── Description extraction ─────────────────────────────────────────────────
def extract_description(content):
    """Extract first meaningful comment line or use fallback."""
    lines = content.strip().split('\n')
    for line in lines:
        line = line.strip()
        if line.startswith('--'):
            desc = line.lstrip('-').strip()
            if desc and len(desc) > 5 and not desc.startswith('~'):
                # Truncate at reasonable length
                return desc[:200]
        elif line and not line.startswith('SET ') and not line.startswith('GO'):
            # Fallback: figure out what the script does from the first SQL statement
            break
    return ""


def derive_tags(name, category, content):
    """Auto-derive tags from name and content."""
    tags = set()
    tags.add(category)

    # Derive from name keywords
    name_lower = name.lower()
    keyword_tags = {
        'index': 'indexing',
        'backup': 'backup',
        'restore': 'restore',
        'security': 'security',
        'permission': 'permissions',
        'login': 'login',
        'user': 'user',
        'monitor': 'monitoring',
        'session': 'session',
        'block': 'blocking',
        'deadlock': 'deadlock',
        'memory': 'memory',
        'cpu': 'cpu',
        'disk': 'disk',
        'cache': 'cache',
        'database': 'database',
        'table': 'table',
        'failover': 'failover',
        'availability': 'availability-group',
        'replication': 'replication',
        'mirror': 'mirroring',
        'log shipping': 'log-shipping',
        'encrypt': 'encryption',
        'audit': 'audit',
        'automation': 'automation',
        'job': 'agent-job',
        'configure': 'configuration',
        'diagnostic': 'diagnostics',
        'performance': 'performance',
        'wait': 'wait-statistics',
        'troubleshoot': 'troubleshooting',
        'check': 'health-check',
        'cleanup': 'cleanup',
        'health': 'health-check',
    }
    for keyword, tag in keyword_tags.items():
        if keyword in name_lower:
            tags.add(tag)

    # Limit to 5 tags
    return sorted(list(tags))[:5]


def make_slug(name):
    """Create a URL-safe slug from the script name."""
    slug = name.lower()
    slug = slug.replace('_', ' ')  # underscores to spaces first
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'[-\s]+', '-', slug)
    slug = slug.strip('-')
    # Truncate but ensure uniqueness by adding hash suffix for very long names
    if len(slug) > 80:
        suffix = hashlib.md5(slug.encode()).hexdigest()[:6]
        slug = slug[:74] + '-' + suffix
    return slug


# ── Main ingestion ──────────────────────────────────────────────────────────
def get_pub_date(filepath):
    """Get file modification time as ISO date string."""
    mtime = os.path.getmtime(filepath)
    from datetime import datetime, timezone
    dt = datetime.fromtimestamp(mtime, tz=timezone.utc)
    return dt.strftime("%Y-%m-%d")


def main():
    sanitize = build_sanitizer()
    stats = {"files_found": 0, "files_written": 0, "errors": 0, "by_category": {}}

    # Ensure output directory exists
    os.makedirs(SCRIPTS_OUTPUT, exist_ok=True)

    # Walk source directory
    for root, dirs, files in os.walk(SCRIPTS_SOURCE):
        sql_files = [f for f in files if f.lower().endswith('.sql')]
        if not sql_files:
            continue

        folder_name = os.path.basename(root).lower().strip()
        category = FOLDER_CATEGORY_MAP.get(folder_name, "general")

        for filename in sorted(sql_files):
            stats["files_found"] += 1
            filepath = os.path.join(root, filename)

            try:
                with open(filepath, 'r', encoding='utf-8', errors='replace') as fh:
                    raw_content = fh.read()
            except Exception as e:
                print(f"  ERROR reading {filepath}: {e}")
                stats["errors"] += 1
                continue

            # Sanitize
            content = sanitize(raw_content)

            # Derive metadata
            name = filename.replace('.sql', '').strip()
            desc = extract_description(content)
            tags = derive_tags(name, category, content)
            slug = make_slug(name)
            pub_date = get_pub_date(filepath)

            # Build frontmatter (manual YAML — avoids json date serialization issues)
            safe_desc = (desc or f"SQL Server diagnostic script for {category} operations.")
            safe_desc = safe_desc.replace("'", "''")  # escape single quotes

            yaml_lines = [
                "---",
                f"name: '{name}'",
                f"title: '{name}'",
                f"description: '{safe_desc}'",
                f"category: {category}",
                "tags: [" + ", ".join(f'"{t}"' for t in tags) + "]",
                f"pubDate: {pub_date}",
                "---",
                "",
                "```sql",
            ]

            # Write .md file
            md_path = os.path.join(SCRIPTS_OUTPUT, f"{slug}.md")
            md_content = "\n".join(yaml_lines)
            md_content += "\n"
            md_content += content
            md_content += "\n```\n"

            with open(md_path, 'w', encoding='utf-8') as fh:
                fh.write(md_content)

            stats["files_written"] += 1
            stats["by_category"][category] = stats["by_category"].get(category, 0) + 1

    # Report
    print(f"Scripts Ingestion Complete")
    print(f"  Source:      {SCRIPTS_SOURCE}")
    print(f"  Output:      {SCRIPTS_OUTPUT}")
    print(f"  Files found: {stats['files_found']}")
    print(f"  Written:     {stats['files_written']}")
    print(f"  Errors:      {stats['errors']}")
    print(f"\nBy category:")
    for cat in sorted(stats["by_category"]):
        print(f"    {cat}: {stats['by_category'][cat]}")


if __name__ == "__main__":
    main()
