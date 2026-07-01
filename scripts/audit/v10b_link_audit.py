#!/usr/bin/env python3
"""V10B full-site link audit.
Scans _build/html/ for internal links (HTML, SVG, CSS, JPG/PNG) and reports broken ones.
"""
import os
import re
import json
import sys
from pathlib import Path

BUILD_DIR = Path('_build/html')

def scan_html_files():
    """Yield (filepath, content) for all .html files in build dir."""
    for p in BUILD_DIR.rglob('*.html'):
        yield p

def extract_references(content, base_url_path):
    """Extract all internal hrefs and srcs."""
    # Find href="..." (no external scheme)
    refs = []
    # href="..."
    for m in re.finditer(r'href="([^"#?]+)(?:[#?][^"]*)?"', content):
        href = m.group(1)
        if not href.startswith(('http://', 'https://', 'mailto:', '//', 'javascript:')):
            refs.append(('href', href))
    # src="..."
    for m in re.finditer(r'src="([^"#?]+)(?:[#?][^"]*)?"', content):
        src = m.group(1)
        if not src.startswith(('http://', 'https://', '//', 'data:')):
            refs.append(('src', src))
    return refs

def resolve_local(ref, source_path):
    """Resolve a relative ref to an absolute path within build dir."""
    # Relative to the source file's directory
    src_dir = source_path.parent
    # URL -> filesystem: replace leading / with build_dir
    if ref.startswith('/'):
        target = BUILD_DIR / ref.lstrip('/')
    else:
        target = (src_dir / ref).resolve()
    return target

def main():
    broken = []
    total_refs = 0
    total_html = 0
    for html_file in scan_html_files():
        total_html += 1
        content = html_file.read_text(encoding='utf-8', errors='ignore')
        for kind, ref in extract_references(content, str(html_file)):
            total_refs += 1
            target = resolve_local(ref, html_file)
            # Skip non-file targets (e.g. anchors only)
            ref_stripped = ref.split('?')[0].split('#')[0]
            if not ref_stripped:
                continue
            target2 = resolve_local(ref_stripped, html_file)
            if not target2.exists():
                broken.append({
                    'source': str(html_file.relative_to(BUILD_DIR)),
                    'kind': kind,
                    'ref': ref,
                    'resolved': str(target2.relative_to(BUILD_DIR)),
                })
    return {
        'total_html_files': total_html,
        'total_refs': total_refs,
        'broken_count': len(broken),
        'broken': broken[:200],  # limit
    }

if __name__ == '__main__':
    result = main()
    print(json.dumps(result, ensure_ascii=False, indent=2))