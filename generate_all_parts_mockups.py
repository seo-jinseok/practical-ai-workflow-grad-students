#!/usr/bin/env python3
"""
Comprehensive mockup generator for Part 2, Part 3, and Context_and_Planning
Generates all necessary screenshots, diagrams, and visual aids
"""

import xml.etree.ElementTree as ET
from pathlib import Path
from generate_mockups import (
    create_svg_base, add_rect, add_text, add_circle, save_svg,
    convert_svg_to_png, COLORS, draw_arrow
)


# ============================================================
# PART 2: MCP & SpecKit Mockups
# ============================================================

def generate_mcp_terminal_install():
    """Generate MCP terminal installation mockup"""
    svg = create_svg_base()
    
    # Terminal window (dark)
    add_rect(svg, 0, 0, 1920, 1080, "#0d1117")
    
    # Terminal header
    add_rect(svg, 50, 50, 1820, 40, "#161b22")
    add_circle(svg, 70, 70, 6, "#ff5f57")
    add_circle(svg, 90, 70, 6, "#febc2e")
    add_circle(svg, 110, 70, 6, "#28c840")
    add_text(svg, 140, 77, "Terminal - Node.js 및 MCP 설치", 
            size=13, fill="#8b949e")
    
    # Terminal content
    commands = [
        ("$ node --version", "#58a6ff", 120),
        ("v20.11.0", "#7ee787", 150),
        ("", "#c9d1d9", 180),
        ("$ npm --version", "#58a6ff", 210),
        ("10.2.4", "#7ee787", 240),
        ("", "#c9d1d9", 270),
        ("$ npm install -g @modelcontextprotocol/server-filesystem", "#58a6ff", 300),
        ("npm WARN deprecated ...", "#f85149", 330),
        ("added 45 packages in 8s", "#7ee787", 360),
        ("", "#c9d1d9", 390),
        ("$ npm list -g --depth=0 | grep mcp", "#58a6ff", 420),
        ("└── @modelcontextprotocol/server-filesystem@1.0.0", "#7ee787", 450),
        ("", "#c9d1d9", 480),
        ("✅ MCP 서버 설치 완료!", "#7ee787", 510),
    ]
    
    for text, color, y in commands:
        add_text(svg, 80, y, text, size=14, fill=color, 
                **{'font-family': "'Monaco', 'Menlo', monospace"})
    
    # Info box
    add_rect(svg, 80, 600, 1760, 400, "#1c2128", rx='10', 
            stroke="#30363d", **{'stroke-width': '2'})
    add_text(svg, 960, 650, "💡 MCP 서버 설치 단계", 
            size=24, fill="#58a6ff", **{'text-anchor': 'middle', 'font-weight': 'bold'})
    
    steps = [
        "1. Node.js 20+ 버전 확인 (node --version)",
        "2. npm 패키지 매니저 확인 (npm --version)",
        "3. MCP 서버 글로벌 설치 (npm install -g)",
        "4. 설치 확인 (npm list -g --depth=0)",
        "",
        "📝 다음 단계: Claude Desktop 설정 파일 수정",
    ]
    
    y_offset = 700
    for step in steps:
        if step == "":
            y_offset += 10
        elif step.startswith("📝"):
            add_text(svg, 120, y_offset, step, size=16, fill="#f85149", 
                    **{'font-weight': 'bold'})
        else:
            add_text(svg, 120, y_offset, step, size=15, fill="#c9d1d9")
        y_offset += 35
    
    return svg


def generate_claude_desktop_config():
    """Generate Claude Desktop MCP configuration mockup"""
    svg = create_svg_base()
    
    # Background
    add_rect(svg, 0, 0, 1920, 1080, "#1e1e1e")
    
    # VS Code window simulation
    add_rect(svg, 100, 50, 1720, 980, "#252526", rx='10')
    
    # File tab
    add_rect(svg, 120, 70, 200, 35, "#1e1e1e")
    add_text(svg, 140, 93, "claude_desktop_config.json", size=12, fill="#d4d4d4")
    
    # JSON content
    add_rect(svg, 120, 110, 1680, 890, "#1e1e1e")
    
    json_lines = [
        ('{', 0, "#d4d4d4"),
        ('  "mcpServers": {', 1, "#d4d4d4"),
        ('    "filesystem": {', 2, "#d4d4d4"),
        ('      "command": "npx",', 3, "#ce9178"),
        ('      "args": [', 3, "#d4d4d4"),
        ('        "-y",', 4, "#ce9178"),
        ('        "@modelcontextprotocol/server-filesystem",', 4, "#ce9178"),
        ('        "/Users/username/research"', 4, "#ce9178"),
        ('      ]', 3, "#d4d4d4"),
        ('    },', 2, "#d4d4d4"),
        ('    "task-master": {', 2, "#d4d4d4"),
        ('      "command": "npx",', 3, "#ce9178"),
        ('      "args": [', 3, "#d4d4d4"),
        ('        "-y",', 4, "#ce9178"),
        ('        "task-master-mcp"', 4, "#ce9178"),
        ('      ]', 3, "#d4d4d4"),
        ('    }', 2, "#d4d4d4"),
        ('  }', 1, "#d4d4d4"),
        ('}', 0, "#d4d4d4"),
    ]
    
    y_offset = 140
    for line, indent, color in json_lines:
        x = 150 + (indent * 30)
        add_text(svg, x, y_offset, line, size=14, fill=color,
                **{'font-family': "'Monaco', 'Menlo', monospace"})
        y_offset += 30
    
    # Annotation box
    add_rect(svg, 1000, 300, 700, 500, "#2d2d30", rx='10', 
            stroke="#007acc", **{'stroke-width': '3'})
    add_text(svg, 1350, 350, "📝 설정 파일 위치", 
            size=20, fill="#007acc", **{'text-anchor': 'middle', 'font-weight': 'bold'})
    
    locations = [
        "macOS:",
        "~/Library/Application Support/",
        "Claude/claude_desktop_config.json",
        "",
        "Windows:",
        "%APPDATA%\\Claude\\",
        "claude_desktop_config.json",
        "",
        "⚠️ 주의사항:",
        "• JSON 문법 오류 주의",
        "• 경로에 공백 없도록",
        "• 저장 후 Claude 재시작 필수",
    ]
    
    y_offset = 400
    for loc in locations:
        if loc == "":
            y_offset += 10
        elif loc.endswith(":"):
            add_text(svg, 1050, y_offset, loc, size=15, fill="#4ec9b0", 
                    **{'font-weight': 'bold'})
        elif loc.startswith("•"):
            add_text(svg, 1070, y_offset, loc, size=13, fill="#858585")
        elif loc.startswith("⚠️"):
            add_text(svg, 1050, y_offset, loc, size=15, fill="#f48771", 
                    **{'font-weight': 'bold'})
        else:
            add_text(svg, 1070, y_offset, loc, size=13, fill="#d4d4d4")
        y_offset += 28
    
    # Arrow
    draw_arrow(svg, 900, 400, 700, 300, "#007acc")
    
    return svg


def generate_speckit_workflow():
    """Generate SpecKit 7-step workflow diagram"""
    svg = create_svg_base()
    add_rect(svg, 0, 0, 1920, 1080, "#f5f5f5")
    
    # Title
    add_text(svg, 960, 80, "SpecKit 7단계 워크플로우", 
            size=32, fill="#1e1e1e", **{'text-anchor': 'middle', 'font-weight': 'bold'})
    add_text(svg, 960, 120, "연구 프로젝트에 적용하기", 
            size=18, fill="#666", **{'text-anchor': 'middle'})
    
    # Steps
    steps = [
        {"num": "1", "name": "Constitution", "desc": "프로젝트 원칙 정의", "color": "#6c5ce7"},
        {"num": "2", "name": "Specification", "desc": "연구 명세서 작성", "color": "#0984e3"},
        {"num": "3", "name": "Plan", "desc": "작업 계획 수립", "color": "#00b894"},
        {"num": "4", "name": "Implement", "desc": "연구 수행", "color": "#fdcb6e"},
        {"num": "5", "name": "Test", "desc": "검증 및 평가", "color": "#e17055"},
        {"num": "6", "name": "Review", "desc": "동료 검토", "color": "#d63031"},
        {"num": "7", "name": "Deploy", "desc": "논문 제출", "color": "#2d3436"},
    ]
    
    y_base = 200
    for i, step in enumerate(steps):
        y = y_base + (i * 110)
        
        # Step box
        add_rect(svg, 300, y, 1320, 90, step["color"], rx='10', opacity='0.9')
        
        # Step number
        add_circle(svg, 350, y + 45, 25, "white")
        add_text(svg, 350, y + 55, step["num"], size=20, fill=step["color"], 
                **{'text-anchor': 'middle', 'font-weight': 'bold'})
        
        # Step name
        add_text(svg, 410, y + 45, step["name"], size=22, fill="white", 
                **{'font-weight': 'bold'})
        
        # Step description
        add_text(svg, 410, y + 70, step["desc"], size=15, fill="white", 
                **{'font-style': 'italic'})
        
        # Arrow to next step
        if i < len(steps) - 1:
            add_text(svg, 1650, y + 100, "▼", size=30, fill="#666")
    
    return svg


def generate_copilot_workbook_demo():
    """Generate Copilot Workbook exercise demo"""
    svg = create_svg_base()
    
    # VS Code window
    add_rect(svg, 0, 0, 1920, 1080, "#1e1e1e")
    
    # Title bar
    add_rect(svg, 0, 0, 1920, 40, "#2d2d30")
    add_circle(svg, 20, 20, 6, "#ff5f57")
    add_circle(svg, 40, 20, 6, "#febc2e")
    add_circle(svg, 60, 20, 6, "#28c840")
    add_text(svg, 90, 27, "Copilot Workbook - Exercise 3: 데이터 분석", 
            size=13, fill="#d4d4d4")
    
    # Split view - Code on left, Chat on right
    add_rect(svg, 20, 60, 1200, 1000, "#1e1e1e")
    
    # Code editor
    add_text(svg, 40, 90, "data_analysis.py", size=12, fill="#858585")
    
    code_lines = [
        "# 연구 데이터 분석 스크립트",
        "import pandas as pd",
        "import matplotlib.pyplot as plt",
        "",
        "# 데이터 로드",
        "df = pd.read_csv('survey_results.csv')",
        "",
        "# 기술통계",
        "print(df.describe())",
        "",
        "# 시각화",
        "df['score'].hist(bins=20)",
        "plt.title('학습 성취도 분포')",
        "plt.xlabel('점수')",
        "plt.ylabel('빈도')",
        "plt.show()",
    ]
    
    y_offset = 130
    for line in code_lines:
        if line.startswith("#"):
            color = "#6a9955"
        elif line.startswith("import"):
            color = "#c586c0"
        elif "print" in line or "plt." in line:
            color = "#dcdcaa"
        else:
            color = "#d4d4d4"
        
        add_text(svg, 40, y_offset, line, size=13, fill=color,
                **{'font-family': "'Monaco', 'Menlo', monospace"})
        y_offset += 25
    
    # Copilot suggestion (ghost text)
    add_text(svg, 40, y_offset + 30, "# Copilot 제안: 추가 분석...", 
            size=13, fill="#585858", **{'font-style': 'italic'})
    
    # Chat panel
    add_rect(svg, 1240, 60, 660, 1000, "#252526")
    add_text(svg, 1260, 90, "GitHub Copilot Chat", size=14, fill="#d4d4d4", 
            **{'font-weight': 'bold'})
    
    # Chat messages
    add_rect(svg, 1260, 120, 620, 100, "#1e1e1e", rx='5')
    add_text(svg, 1280, 145, "👤 You:", size=11, fill="#858585", **{'font-weight': 'bold'})
    add_text(svg, 1280, 170, "설문 데이터를 분석하는 Python", size=13, fill="#d4d4d4")
    add_text(svg, 1280, 195, "스크립트를 작성해줘", size=13, fill="#d4d4d4")
    
    add_rect(svg, 1260, 240, 620, 300, "#2d2d30", rx='5')
    add_text(svg, 1280, 265, "🤖 Copilot:", size=11, fill="#007acc", **{'font-weight': 'bold'})
    
    response = [
        "설문 데이터 분석 스크립트를 작성했습니다.",
        "",
        "주요 기능:",
        "• CSV 파일에서 데이터 로드",
        "• 기술통계량 출력",
        "• 히스토그램 시각화",
        "",
        "추가로 상관관계 분석이나 그룹별",
        "비교가 필요하면 말씀해주세요.",
    ]
    
    y_offset = 295
    for line in response:
        if line.startswith("•"):
            add_text(svg, 1300, y_offset, line, size=12, fill="#d4d4d4")
        elif line == "":
            y_offset -= 5
        else:
            add_text(svg, 1280, y_offset, line, size=12, fill="#d4d4d4")
        y_offset += 22
    
    return svg


# ============================================================
# PART 3: Folder Structure & Workflow Diagrams
# ============================================================

def generate_folder_structure(title, folders, base_y=150):
    """Generate a folder structure diagram"""
    svg = create_svg_base()
    add_rect(svg, 0, 0, 1920, 1080, "#f8f9fa")
    
    # Title
    add_text(svg, 960, 80, title, size=28, fill="#1e1e1e", 
            **{'text-anchor': 'middle', 'font-weight': 'bold'})
    
    # Folder tree
    y_offset = base_y
    for folder in folders:
        indent = folder.get("level", 0) * 40
        icon = folder.get("icon", "📁")
        name = folder["name"]
        desc = folder.get("desc", "")
        
        # Folder item
        x = 200 + indent
        add_text(svg, x, y_offset, icon, size=18)
        add_text(svg, x + 35, y_offset, name, size=16, fill="#1e1e1e", 
                **{'font-weight': 'bold' if folder.get("level", 0) == 0 else 'normal'})
        
        if desc:
            add_text(svg, x + 400, y_offset, f"  # {desc}", 
                    size=13, fill="#666", **{'font-style': 'italic'})
        
        y_offset += 35
    
    return svg


def generate_education_folder_structure():
    """Generate education research project folder structure"""
    folders = [
        {"level": 0, "icon": "📁", "name": "ai-education-research/", "desc": "교육학 석사논문 프로젝트"},
        {"level": 1, "icon": "📄", "name": "README.md", "desc": "프로젝트 개요"},
        {"level": 1, "icon": "📄", "name": "연구컨텍스트.md", "desc": "AI용 컨텍스트"},
        {"level": 1, "icon": "📄", "name": ".gitignore", "desc": "버전 관리 제외 파일"},
        {"level": 1, "icon": "📁", "name": "01_계획/", "desc": "연구 계획 단계"},
        {"level": 2, "icon": "📄", "name": "연구계획서.md"},
        {"level": 2, "icon": "📄", "name": "일정표.md"},
        {"level": 2, "icon": "📄", "name": "IRB신청서.md"},
        {"level": 1, "icon": "📁", "name": "02_문헌조사/", "desc": "선행 연구 조사"},
        {"level": 2, "icon": "📄", "name": "문헌목록.md"},
        {"level": 2, "icon": "📄", "name": "키워드.md"},
        {"level": 2, "icon": "📁", "name": "papers/"},
        {"level": 3, "icon": "📄", "name": "paper001.pdf"},
        {"level": 3, "icon": "📄", "name": "paper002.pdf"},
        {"level": 1, "icon": "📁", "name": "03_데이터수집/", "desc": "설문 및 인터뷰"},
        {"level": 2, "icon": "📄", "name": "설문지.md"},
        {"level": 2, "icon": "📄", "name": "인터뷰가이드.md"},
        {"level": 2, "icon": "📁", "name": "raw_data/"},
        {"level": 1, "icon": "📁", "name": "04_분석/", "desc": "데이터 분석"},
        {"level": 2, "icon": "📄", "name": "analysis_script.py"},
        {"level": 2, "icon": "📄", "name": "results.md"},
        {"level": 2, "icon": "📁", "name": "figures/"},
        {"level": 1, "icon": "📁", "name": "05_논문작성/", "desc": "논문 초안"},
        {"level": 2, "icon": "📄", "name": "chapter1_서론.md"},
        {"level": 2, "icon": "📄", "name": "chapter2_이론적배경.md"},
        {"level": 2, "icon": "📄", "name": "chapter3_연구방법.md"},
        {"level": 2, "icon": "📄", "name": "chapter4_결과.md"},
        {"level": 2, "icon": "📄", "name": "chapter5_논의.md"},
        {"level": 1, "icon": "📁", "name": "06_참고자료/", "desc": "기타 자료"},
        {"level": 2, "icon": "📄", "name": "용어집.md"},
        {"level": 2, "icon": "📄", "name": "참고문헌.md"},
    ]
    
    return generate_folder_structure("교육학 석사논문 프로젝트 폴더 구조", folders)


def generate_research_lifecycle():
    """Generate 8-step research lifecycle diagram"""
    svg = create_svg_base()
    add_rect(svg, 0, 0, 1920, 1080, "white")
    
    # Title
    add_text(svg, 960, 80, "연구 프로젝트 8단계 라이프사이클", 
            size=32, fill="#1e1e1e", **{'text-anchor': 'middle', 'font-weight': 'bold'})
    
    # Circle layout
    center_x, center_y = 960, 580
    radius = 350
    
    steps = [
        {"name": "프로젝트\n착수", "color": "#e74c3c", "angle": 0},
        {"name": "문헌\n조사", "color": "#e67e22", "angle": 45},
        {"name": "연구\n설계", "color": "#f39c12", "angle": 90},
        {"name": "IRB\n승인", "color": "#2ecc71", "angle": 135},
        {"name": "데이터\n수집", "color": "#3498db", "angle": 180},
        {"name": "데이터\n분석", "color": "#9b59b6", "angle": 225},
        {"name": "논문\n작성", "color": "#34495e", "angle": 270},
        {"name": "제출 및\n수정", "color": "#95a5a6", "angle": 315},
    ]
    
    import math
    
    for i, step in enumerate(steps):
        angle_rad = math.radians(step["angle"])
        x = center_x + radius * math.cos(angle_rad)
        y = center_y + radius * math.sin(angle_rad)
        
        # Circle
        add_circle(svg, x, y, 80, step["color"])
        
        # Step number
        add_text(svg, x, y - 10, str(i + 1), size=32, fill="white", 
                **{'text-anchor': 'middle', 'font-weight': 'bold'})
        
        # Step name (split by \n)
        lines = step["name"].split("\n")
        for j, line in enumerate(lines):
            add_text(svg, x, y + 20 + (j * 20), line, size=16, fill="white", 
                    **{'text-anchor': 'middle'})
        
        # Arrow to next step
        if i < len(steps) - 1:
            next_angle = math.radians(steps[i + 1]["angle"])
            x2 = center_x + radius * math.cos(next_angle)
            y2 = center_y + radius * math.sin(next_angle)
            
            # Shortened arrow (not touching circles)
            dx = x2 - x
            dy = y2 - y
            length = math.sqrt(dx*dx + dy*dy)
            dx /= length
            dy /= length
            
            start_x = x + dx * 85
            start_y = y + dy * 85
            end_x = x2 - dx * 85
            end_y = y2 - dy * 85
            
            draw_arrow(svg, start_x, start_y, end_x, end_y, "#666")
    
    # Center label
    add_circle(svg, center_x, center_y, 100, "#ecf0f1")
    add_text(svg, center_x, center_y + 10, "연구", size=24, fill="#2c3e50", 
            **{'text-anchor': 'middle', 'font-weight': 'bold'})
    add_text(svg, center_x, center_y + 35, "워크플로우", size=16, fill="#2c3e50", 
            **{'text-anchor': 'middle'})
    
    return svg


def generate_tools_ecosystem():
    """Generate AI research tools ecosystem diagram"""
    svg = create_svg_base()
    add_rect(svg, 0, 0, 1920, 1080, "#f5f5f5")
    
    # Title
    add_text(svg, 960, 80, "2025 AI 연구 도구 생태계", 
            size=32, fill="#1e1e1e", **{'text-anchor': 'middle', 'font-weight': 'bold'})
    
    # Center hub
    add_rect(svg, 760, 440, 400, 200, "#007acc", rx='20')
    add_text(svg, 960, 520, "🎯", size=60, **{'text-anchor': 'middle'})
    add_text(svg, 960, 580, "GitHub Copilot", size=24, fill="white", 
            **{'text-anchor': 'middle', 'font-weight': 'bold'})
    add_text(svg, 960, 610, "+ MCP + SpecKit", size=16, fill="white", 
            **{'text-anchor': 'middle'})
    
    # Tool categories
    tools = [
        {"cat": "문헌 관리", "items": ["Zotero", "Notion", "Obsidian"], 
         "x": 200, "y": 200, "color": "#e74c3c"},
        {"cat": "데이터 분석", "items": ["Python", "R", "SPSS"], 
         "x": 1520, "y": 200, "color": "#9b59b6"},
        {"cat": "작성 도구", "items": ["Overleaf", "MS Word", "Markdown"], 
         "x": 200, "y": 680, "color": "#2ecc71"},
        {"cat": "프로젝트 관리", "items": ["GitHub", "Trello", "Notion"], 
         "x": 1520, "y": 680, "color": "#f39c12"},
    ]
    
    for tool in tools:
        # Category box
        add_rect(svg, tool["x"], tool["y"], 300, 200, tool["color"], 
                rx='15', opacity='0.9')
        add_text(svg, tool["x"] + 150, tool["y"] + 40, tool["cat"], 
                size=20, fill="white", 
                **{'text-anchor': 'middle', 'font-weight': 'bold'})
        
        # Tool items
        y_offset = tool["y"] + 80
        for item in tool["items"]:
            add_text(svg, tool["x"] + 150, y_offset, f"• {item}", 
                    size=15, fill="white", **{'text-anchor': 'middle'})
            y_offset += 30
        
        # Arrow to center
        center_x = 960
        center_y = 540
        draw_arrow(svg, tool["x"] + 150, tool["y"] + 100, 
                  center_x, center_y, "#666")
    
    return svg


# ============================================================
# Main execution
# ============================================================

def main():
    """Generate all Part 2, Part 3, and planning mockups"""
    base_dir = Path(__file__).parent
    
    # Create output directories
    part2_images = base_dir / "v13.0_resources" / "part2" / "images"
    part3_images = base_dir / "v13.0_resources" / "part3" / "images"
    planning_images = base_dir / "Context_and_Planning" / "images"
    
    for dir in [part2_images, part3_images, planning_images]:
        dir.mkdir(parents=True, exist_ok=True)
    
    print("🎨 Generating comprehensive mockups for all parts...\n")
    
    # Part 2 mockups
    part2_mockups = [
        {
            "generator": generate_mcp_terminal_install,
            "name": "MCP Terminal Installation",
            "dir": part2_images,
            "filename": "mcp-terminal-install.svg"
        },
        {
            "generator": generate_claude_desktop_config,
            "name": "Claude Desktop Config",
            "dir": part2_images,
            "filename": "claude-desktop-config.svg"
        },
        {
            "generator": generate_speckit_workflow,
            "name": "SpecKit Workflow",
            "dir": part2_images,
            "filename": "speckit-7step-workflow.svg"
        },
        {
            "generator": generate_copilot_workbook_demo,
            "name": "Copilot Workbook Demo",
            "dir": part2_images,
            "filename": "copilot-workbook-exercise.svg"
        },
    ]
    
    # Part 3 mockups
    part3_mockups = [
        {
            "generator": generate_education_folder_structure,
            "name": "Education Project Folder Structure",
            "dir": part3_images,
            "filename": "education-project-folders.svg"
        },
        {
            "generator": generate_research_lifecycle,
            "name": "Research Lifecycle",
            "dir": part3_images,
            "filename": "research-8step-lifecycle.svg"
        },
        {
            "generator": generate_tools_ecosystem,
            "name": "AI Tools Ecosystem",
            "dir": part3_images,
            "filename": "ai-tools-ecosystem.svg"
        },
    ]
    
    all_mockups = [
        ("Part 2", part2_mockups),
        ("Part 3", part3_mockups),
    ]
    
    total_generated = 0
    total_converted = 0
    
    for part_name, mockups in all_mockups:
        print(f"\n{'='*60}")
        print(f"📋 {part_name} Mockups")
        print(f"{'='*60}\n")
        
        for mockup in mockups:
            print(f"🎨 Generating: {mockup['name']}")
            svg = mockup["generator"]()
            
            svg_path = mockup["dir"] / mockup["filename"]
            save_svg(svg, svg_path)
            total_generated += 1
            
            png_path = svg_path.with_suffix('.png')
            if convert_svg_to_png(svg_path, png_path):
                total_converted += 1
    
    # Summary
    print("\n" + "="*60)
    print(f"✅ Generated {total_generated} SVG mockups")
    print(f"✅ Converted {total_converted} to PNG")
    print("="*60)
    
    print("\n📁 Files saved to:")
    print(f"   • Part 2: {part2_images}")
    print(f"   • Part 3: {part3_images}")
    
    print("\n📝 Next steps:")
    print("   1. Review generated images")
    print("   2. Update documentation references")
    print("   3. Commit to git")


def generate_life_science_folders():
    """Generate life science project folder structure"""
    svg = create_svg_base()
    add_rect(svg, 0, 0, 1920, 1080, COLORS['bg'])
    
    add_text(svg, 960, 80, '생명과학 연구 프로젝트 구조', 48, 'white', 
            **{'text-anchor': 'middle', 'font-weight': 'bold'})
    add_text(svg, 960, 140, '세포 신호전달 경로 연구', 28, '#888', 
            **{'text-anchor': 'middle'})
    add_rect(svg, 200, 220, 1520, 760, '#252526', 
            stroke='#3e3e42', **{'stroke-width': '2', 'rx': '8'})
    
    folders = [
        ('📁', 0, 'cell_signaling/', ''), ('📁', 1, '01_실험계획/', ''),
        ('📄', 2, 'proposal.md', '제안서'), ('📄', 2, 'protocol.md', '프로토콜'),
        ('📁', 1, '02_실험데이터/', ''), ('📁', 2, 'raw_data/', '원시'),
        ('📄', 3, 'western_blot.tif', '블롯'), ('📁', 1, '03_분석/', ''),
        ('📄', 2, 'analysis.py', 'Python'), ('📁', 1, '04_논문/', ''),
        ('📄', 2, 'manuscript.md', '초안'), ('📄', 1, 'README.md', '개요')
    ]
    
    y = 260
    for icon, indent, name, desc in folders:
        x = 240 + indent * 40
        add_text(svg, x, y, icon, 20, 'white')
        c = '#4ec9b0' if icon == '📁' else '#ce9178'
        add_text(svg, x+35, y, name, 18, c, **{'font-family': 'Monaco'})
        if desc:
            add_text(svg, x+35+len(name)*10, y, f'  # {desc}', 16, '#6a9955')
        y += 50
    
    add_text(svg, 960, 1010, '💡 생명과학: 실험 데이터 관리와 재현성이 핵심', 
            20, '#858585', **{'text-anchor': 'middle'})
    return svg


def generate_cs_folders():
    """Generate CS project folder structure"""
    svg = create_svg_base()
    add_rect(svg, 0, 0, 1920, 1080, COLORS['bg'])
    
    add_text(svg, 960, 80, '컴퓨터공학 연구 프로젝트 구조', 48, 'white',
            **{'text-anchor': 'middle', 'font-weight': 'bold'})
    add_text(svg, 960, 140, '추천 시스템 개발', 28, '#888', **{'text-anchor': 'middle'})
    add_rect(svg, 200, 220, 1520, 760, '#252526', 
            stroke='#3e3e42', **{'stroke-width': '2', 'rx': '8'})
    
    folders = [
        ('📁', 0, 'recommendation_system/', ''), ('📁', 1, '01_design/', ''),
        ('📄', 2, 'architecture.md', '설계'), ('📄', 2, 'api_spec.yaml', 'API'),
        ('📁', 1, '02_dataset/', ''), ('📁', 2, 'raw/', '원시'),
        ('📄', 3, 'interactions.csv', '로그'), ('📁', 1, '03_models/', ''),
        ('📄', 2, 'neural_cf.py', '딥러닝'), ('📁', 1, '04_evaluation/', ''),
        ('📄', 2, 'metrics.py', '평가'), ('📁', 1, '05_deploy/', ''),
        ('📄', 2, 'Dockerfile', '컨테이너'), ('📄', 1, 'README.md', '문서')
    ]
    
    y = 260
    for icon, indent, name, desc in folders:
        x = 240 + indent * 40
        add_text(svg, x, y, icon, 20, 'white')
        c = '#4ec9b0' if icon == '📁' else '#ce9178'
        add_text(svg, x+35, y, name, 18, c, **{'font-family': 'Monaco'})
        if desc:
            add_text(svg, x+35+len(name)*10, y, f'  # {desc}', 16, '#6a9955')
        y += 48
    
    add_text(svg, 960, 1010, '💡 컴퓨터공학: 코드 버전 관리와 재현 가능한 실험', 
            20, '#858585', **{'text-anchor': 'middle'})
    return svg


def generate_sociology_folders():
    """Generate sociology project folder structure"""
    svg = create_svg_base()
    add_rect(svg, 0, 0, 1920, 1080, COLORS['bg'])
    
    add_text(svg, 960, 80, '사회학 연구 프로젝트 구조', 48, 'white',
            **{'text-anchor': 'middle', 'font-weight': 'bold'})
    add_text(svg, 960, 140, '노동자 정체성 질적 연구', 28, '#888', **{'text-anchor': 'middle'})
    add_rect(svg, 200, 220, 1520, 760, '#252526', 
            stroke='#3e3e42', **{'stroke-width': '2', 'rx': '8'})
    
    folders = [
        ('📁', 0, 'labor_identity/', ''), ('📁', 1, '01_설계/', ''),
        ('📄', 2, 'research_question.md', '질문'), ('📄', 2, 'sampling.md', '표집'),
        ('📁', 1, '02_현장조사/', ''), ('📁', 2, 'fieldnotes/', '현장'),
        ('📄', 3, 'factory_visit.md', '공장'), ('📁', 2, 'interviews/', '인터뷰'),
        ('📄', 3, 'interview_01.md', '참여자A'), ('📁', 1, '03_분석/', ''),
        ('📁', 2, 'coding/', '코딩'), ('📄', 3, 'open_coding.md', '개방'),
        ('📁', 1, '04_논문/', ''), ('📄', 2, 'manuscript.md', '초안'),
        ('📁', 1, '05_윤리/', ''), ('📄', 2, 'irb.pdf', 'IRB'),
        ('📄', 1, 'README.md', '개요')
    ]
    
    y = 260
    for icon, indent, name, desc in folders:
        x = 240 + indent * 40
        add_text(svg, x, y, icon, 20, 'white')
        c = '#4ec9b0' if icon == '📁' else '#ce9178'
        add_text(svg, x+35, y, name, 18, c, **{'font-family': 'Monaco'})
        if desc:
            add_text(svg, x+35+len(name)*10, y, f'  # {desc}', 16, '#6a9955')
        y += 42
    
    add_text(svg, 960, 1010, '💡 사회학: 연구 윤리와 데이터 익명화가 필수', 
            20, '#858585', **{'text-anchor': 'middle'})
    return svg


def generate_music_folders():
    """Generate music project folder structure"""
    svg = create_svg_base()
    add_rect(svg, 0, 0, 1920, 1080, COLORS['bg'])
    
    add_text(svg, 960, 80, '음악학 연구 프로젝트 구조', 48, 'white',
            **{'text-anchor': 'middle', 'font-weight': 'bold'})
    add_text(svg, 960, 140, '바로크 오페라 분석 연구', 28, '#888', **{'text-anchor': 'middle'})
    add_rect(svg, 200, 220, 1520, 760, '#252526', 
            stroke='#3e3e42', **{'stroke-width': '2', 'rx': '8'})
    
    folders = [
        ('📁', 0, 'baroque_opera/', ''), ('📁', 1, '01_악보/', ''),
        ('📁', 2, 'original_scores/', '원본'), ('📄', 3, 'handel.mscz', 'MuseScore'),
        ('📁', 1, '02_음원/', ''), ('📁', 2, 'recordings/', '녹음'),
        ('📄', 3, '1980_gardiner.flac', '역사적'), ('📄', 3, '2020_modern.mp3', '현대'),
        ('📁', 1, '03_분석/', ''), ('📄', 2, 'harmonic.md', '화성'),
        ('📄', 2, 'form.md', '형식'), ('📁', 2, 'viz/', '시각화'),
        ('📁', 1, '04_역사맥락/', ''), ('📄', 2, 'libretto.pdf', '대본'),
        ('📁', 1, '05_논문/', ''), ('📄', 2, 'thesis.md', '초안'),
        ('📄', 2, 'bibliography.bib', '참고문헌'), ('📄', 1, 'README.md', '개요')
    ]
    
    y = 260
    for icon, indent, name, desc in folders:
        x = 240 + indent * 40
        add_text(svg, x, y, icon, 20, 'white')
        c = '#4ec9b0' if icon == '📁' else '#ce9178'
        add_text(svg, x+35, y, name, 18, c, **{'font-family': 'Monaco'})
        if desc:
            add_text(svg, x+35+len(name)*10, y, f'  # {desc}', 16, '#6a9955')
        y += 40
    
    add_text(svg, 960, 1010, '💡 음악학: 악보와 음원 파일 형식 관리가 핵심', 
            20, '#858585', **{'text-anchor': 'middle'})
    return svg


if __name__ == "__main__":
    main()
    
    # Generate additional discipline-specific folders
    print("\n" + "="*60)
    print("📋 Additional Discipline Folders")
    print("="*60 + "\n")
    
    part3_images = Path("v13.0_resources/part3/images")
    additional = [
        ('Life Science', 'life-science-project-folders', generate_life_science_folders),
        ('Computer Science', 'cs-project-folders', generate_cs_folders),
        ('Sociology', 'sociology-project-folders', generate_sociology_folders),
        ('Music', 'music-project-folders', generate_music_folders),
    ]
    
    for name, filename, func in additional:
        print(f"🎨 Generating: {name}")
        svg = func()
        svg_path = part3_images / f"{filename}.svg"
        save_svg(svg, svg_path)
        convert_svg_to_png(svg_path, part3_images / f"{filename}.png")
    
    print(f"\n✅ Generated {len(additional)} additional folder structures")
