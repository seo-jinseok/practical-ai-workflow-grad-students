import os

def fix_markdown_indentation(file_path):
    """
    Corrects indentation in Markdown files.
    - Changes 2-space indented list items to 4-space.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        fixed_lines = []
        for i, line in enumerate(lines):
            stripped_line = line.lstrip(' ')
            indentation = len(line) - len(stripped_line)

            # Check if the previous line was a list item
            if i > 0:
                prev_line = lines[i-1].strip()
                is_prev_list = prev_line.startswith(('-', '*', '+')) or (prev_line and prev_line[0].isdigit() and '.' in prev_line)
                
                if is_prev_list and indentation == 2:
                    fixed_lines.append(' ' * 4 + stripped_line)
                    continue

            fixed_lines.append(line)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(fixed_lines)

        print(f"Fixed indentation in: {file_path}")

    except Exception as e:
        print(f"Error fixing {file_path}: {e}")

def main():
    files_to_fix = [
        '/Users/truestone/Dropbox/repo/University/Generative AI Special Lecture - Graduate School/Context_and_Planning/demo-files/06-mcp-installation/README.md',
        '/Users/truestone/Dropbox/repo/University/Generative AI Special Lecture - Graduate School/Context_and_Planning/demo-files/06-mcp-installation/screenshots-checklist.md',
        '/Users/truestone/Dropbox/repo/University/Generative AI Special Lecture - Graduate School/v13.0_resources/part2/12_screenshot_descriptions.md',
        '/Users/truestone/Dropbox/repo/University/Generative AI Special Lecture - Graduate School/Context_and_Planning/demo-files/06-mcp-installation/part2-screenshot-generation-prompts.md'
    ]

    for file_path in files_to_fix:
        fix_markdown_indentation(file_path)

if __name__ == "__main__":
    main()
