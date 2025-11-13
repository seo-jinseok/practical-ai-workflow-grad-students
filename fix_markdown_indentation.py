#!/usr/bin/env python3
"""
Fix markdown indentation issues in files
Changes 4-space indentation to 2-space for unordered lists
"""

import re

def fix_indentation(content):
    """Fix indentation from 4 spaces to 2 spaces for unordered lists"""
    lines = content.split('\n')
    fixed_lines = []

    for line in lines:
        # Replace 4-space indentation with 2-space for list items at all levels
        if line.startswith('    - '):
            line = '  - ' + line[6:]
        elif line.startswith('        - '):
            line = '    - ' + line[10:]
        elif line.startswith('            - '):
            line = '      - ' + line[14:]
        elif line.startswith('                - '):
            line = '        - ' + line[18:]
        # Also fix nested content under list items
        elif line.startswith('      '):
            line = '    ' + line[6:]
        elif line.startswith('        '):
            line = '      ' + line[8:]
        elif line.startswith('          '):
            line = '        ' + line[10:]

        fixed_lines.append(line)

    return '\n'.join(fixed_lines)

def fix_line_length(content):
    """Fix lines that are too long by breaking them appropriately"""
    lines = content.split('\n')
    fixed_lines = []

    for line in lines:
        if len(line) > 80:
            # Handle different types of long lines
            if line.startswith('**') and '**: ' in line:
                # Header lines like "**Status**: ✅ 완료 (2/15 완료 - MCP 웹페이지 스크린샷 생성 완료)"
                parts = line.split('**: ', 1)
                if len(parts) == 2:
                    fixed_lines.append(parts[0] + '**:')
                    fixed_lines.append('  ' + parts[1])
                    continue
            elif ': ' in line and not line.startswith('  ') and not line.startswith('- '):
                # General lines with colon
                parts = line.split(': ', 1)
                if len(parts) == 2 and len(parts[0]) < 40:
                    fixed_lines.append(parts[0] + ':')
                    fixed_lines.append('  ' + parts[1])
                    continue
            elif ' - ' in line and len(line) > 100:
                # Long list items or descriptions
                if 'http' in line:
                    # Lines with URLs - break before URL if too long
                    url_start = line.find('http')
                    if url_start > 40:
                        fixed_lines.append(line[:url_start].rstrip())
                        fixed_lines.append('  ' + line[url_start:])
                        continue
                elif ' → ' in line:
                    # Lines with arrows
                    arrow_pos = line.find(' → ')
                    if arrow_pos > 40:
                        fixed_lines.append(line[:arrow_pos])
                        fixed_lines.append('  ' + line[arrow_pos+1:])
                        continue

        fixed_lines.append(line)

    return '\n'.join(fixed_lines)

def main():
    files_to_fix = [
        'v13.0_resources/part2/12_screenshot_descriptions.md',
        'Context_and_Planning/demo-files/06-mcp-installation/screenshots-checklist.md',
        'Context_and_Planning/demo-files/06-mcp-installation/README.md',
        'Context_and_Planning/demo-files/06-mcp-installation/part2-screenshot-generation-prompts.md'
    ]

    for file_path in files_to_fix:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Fix indentation
            content = fix_indentation(content)

            # Fix line length issues
            content = fix_line_length(content)

            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)

            print(f"Fixed: {file_path}")

        except Exception as e:
            print(f"Error fixing {file_path}: {e}")

if __name__ == "__main__":
    main()
