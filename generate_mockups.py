#!/usr/bin/env python3
"""
Mockup screenshot generator for Part 1 educational materials
Generates SVG-based mockups and converts to PNG
"""

import os
from pathlib import Path
from xml.etree import ElementTree as ET
import subprocess

# VS Code color scheme (Dark Theme)
COLORS = {
    "bg": "#1e1e1e",
    "bg_light": "#252526",
    "bg_sidebar": "#2d2d30",
    "text": "#d4d4d4",
    "text_dim": "#858585",
    "accent": "#007acc",
    "success": "#4ec9b0",
    "warning": "#ce9178",
    "error": "#f48771",
    "border": "#3e3e42",
    "highlight": "#264f78",
}

def create_svg_base(width=1920, height=1080):
    """Create base SVG element"""
    svg = ET.Element('svg', {
        'xmlns': 'http://www.w3.org/2000/svg',
        'width': str(width),
        'height': str(height),
        'viewBox': f'0 0 {width} {height}'
    })
    return svg

def add_rect(parent, x, y, width, height, fill, **attrs):
    """Add rectangle to SVG"""
    rect_attrs = {
        'x': str(x),
        'y': str(y),
        'width': str(width),
        'height': str(height),
        'fill': fill,
    }
    rect_attrs.update(attrs)
    ET.SubElement(parent, 'rect', rect_attrs)

def add_text(parent, x, y, text, size=14, fill=COLORS["text"], **attrs):
    """Add text to SVG"""
    text_attrs = {
        'x': str(x),
        'y': str(y),
        'font-family': "'SF Mono', 'Consolas', monospace",
        'font-size': f'{size}px',
        'fill': fill,
    }
    text_attrs.update(attrs)
    text_elem = ET.SubElement(parent, 'text', text_attrs)
    text_elem.text = text
    return text_elem

def add_circle(parent, cx, cy, r, fill, **attrs):
    """Add circle to SVG"""
    circle_attrs = {
        'cx': str(cx),
        'cy': str(cy),
        'r': str(r),
        'fill': fill,
    }
    circle_attrs.update(attrs)
    ET.SubElement(parent, 'circle', circle_attrs)

def create_vscode_window_frame(svg):
    """Create VS Code window frame"""
    # Background
    add_rect(svg, 0, 0, 1920, 1080, COLORS["bg"])
    
    # Title bar
    add_rect(svg, 0, 0, 1920, 40, COLORS["bg_sidebar"])
    
    # Window controls (macOS style)
    add_circle(svg, 20, 20, 6, "#ff5f57")
    add_circle(svg, 40, 20, 6, "#febc2e")
    add_circle(svg, 60, 20, 6, "#28c840")
    
    # Title
    add_text(svg, 90, 27, "Visual Studio Code", size=13, fill=COLORS["text_dim"])
    
    # Sidebar
    add_rect(svg, 0, 40, 250, 1040, COLORS["bg_sidebar"])
    
    # Activity bar
    add_rect(svg, 0, 40, 48, 1040, COLORS["bg_light"])
    
    # Status bar
    add_rect(svg, 0, 1040, 1920, 40, COLORS["accent"])

def generate_extensions_marketplace():
    """Generate Extensions Marketplace screenshot"""
    svg = create_svg_base()
    create_vscode_window_frame(svg)
    
    # Extensions panel
    add_text(svg, 60, 70, "EXTENSIONS", size=11, fill=COLORS["text_dim"], 
             **{'font-weight': 'bold'})
    
    # Search box
    add_rect(svg, 60, 90, 180, 30, COLORS["bg"], stroke=COLORS["border"], 
             **{'stroke-width': '1', 'rx': '3'})
    add_text(svg, 70, 111, "github copilot", size=13, fill=COLORS["text"])
    
    # Search results
    y_offset = 140
    extensions = [
        {
            "name": "GitHub Copilot",
            "publisher": "GitHub",
            "desc": "Your AI pair programmer",
            "installs": "50M+",
            "rating": "★★★★★"
        },
        {
            "name": "GitHub Copilot Chat",
            "publisher": "GitHub",
            "desc": "Chat with your AI pair programmer",
            "installs": "30M+",
            "rating": "★★★★★"
        }
    ]
    
    for ext in extensions:
        # Extension card
        add_rect(svg, 60, y_offset, 180, 80, COLORS["bg_light"], 
                rx='5', stroke=COLORS["border"], **{'stroke-width': '1'})
        
        # Extension icon (placeholder)
        add_rect(svg, 70, y_offset + 10, 40, 40, COLORS["accent"], rx='3')
        add_text(svg, 85, y_offset + 35, "GH", size=14, fill="white", 
                **{'font-weight': 'bold', 'text-anchor': 'middle'})
        
        # Extension info
        add_text(svg, 120, y_offset + 25, ext["name"], size=13, 
                fill=COLORS["text"], **{'font-weight': 'bold'})
        add_text(svg, 120, y_offset + 42, ext["publisher"], size=11, 
                fill=COLORS["text_dim"])
        add_text(svg, 120, y_offset + 58, ext["desc"], size=10, 
                fill=COLORS["text_dim"])
        
        # Install button (highlight first one)
        btn_color = COLORS["accent"] if y_offset == 140 else COLORS["bg"]
        add_rect(svg, 60, y_offset + 85, 80, 25, btn_color, rx='3')
        add_text(svg, 100, y_offset + 102, "Install", size=12, 
                fill="white", **{'text-anchor': 'middle'})
        
        y_offset += 120
    
    # Editor area with instructions
    add_text(svg, 300, 100, "Extensions Marketplace - GitHub Copilot 검색", 
            size=20, fill=COLORS["text"], **{'font-weight': 'bold'})
    add_text(svg, 300, 140, "1. 좌측 Extensions 아이콘 클릭 (Ctrl+Shift+X)", 
            size=14, fill=COLORS["text_dim"])
    add_text(svg, 300, 170, "2. 검색창에 'github copilot' 입력", 
            size=14, fill=COLORS["text_dim"])
    add_text(svg, 300, 200, "3. 'GitHub Copilot' 확장 선택", 
            size=14, fill=COLORS["text_dim"])
    add_text(svg, 300, 230, "4. 'Install' 버튼 클릭", 
            size=14, fill=COLORS["text_dim"])
    
    # Highlight arrow
    draw_arrow(svg, 245, 165, 60, 165, COLORS["warning"])
    
    return svg

def generate_copilot_status_bar():
    """Generate Copilot status bar screenshot"""
    svg = create_svg_base()
    create_vscode_window_frame(svg)
    
    # Focus on status bar area
    add_rect(svg, 100, 400, 1720, 400, COLORS["bg_light"], rx='10')
    
    # Enlarged status bar
    add_rect(svg, 150, 500, 1620, 80, COLORS["accent"], rx='5')
    
    # Status bar items
    status_items = [
        {"icon": "🔔", "text": "0", "x": 180},
        {"icon": "⚠️", "text": "0", "x": 250},
        {"icon": "✓", "text": "main", "x": 320},
        {"icon": "🤖", "text": "GitHub Copilot Pro", "x": 1400, "highlight": True},
    ]
    
    for item in status_items:
        x = item["x"]
        add_text(svg, x, 545, item["icon"], size=20)
        color = COLORS["warning"] if item.get("highlight") else "white"
        weight = "bold" if item.get("highlight") else "normal"
        add_text(svg, x + 30, 545, item["text"], size=16, fill=color, 
                **{'font-weight': weight})
        
        if item.get("highlight"):
            # Highlight box
            add_rect(svg, x - 10, 510, 270, 50, "none", 
                    stroke=COLORS["warning"], **{'stroke-width': '3', 'rx': '5'})
    
    # Annotation
    add_text(svg, 960, 350, "GitHub Copilot Pro 활성화 상태", 
            size=24, fill=COLORS["text"], **{'text-anchor': 'middle', 'font-weight': 'bold'})
    add_text(svg, 960, 390, "하단 상태바에서 'GitHub Copilot Pro' 표시 확인", 
            size=16, fill=COLORS["text_dim"], **{'text-anchor': 'middle'})
    
    # Arrow pointing to status
    draw_arrow(svg, 960, 420, 1535, 500, COLORS["warning"])
    
    return svg

def generate_folder_structure():
    """Generate VS Code folder structure screenshot"""
    svg = create_svg_base()
    create_vscode_window_frame(svg)
    
    # Explorer panel
    add_text(svg, 60, 70, "EXPLORER", size=11, fill=COLORS["text_dim"], 
             **{'font-weight': 'bold'})
    
    # Folder tree
    folders = [
        {"level": 0, "icon": "📁", "name": "my-research-project", "expanded": True},
        {"level": 1, "icon": "📄", "name": "README.md", "expanded": False},
        {"level": 1, "icon": "📄", "name": "연구컨텍스트.md", "expanded": False},
        {"level": 1, "icon": "📁", "name": "01_계획", "expanded": True},
        {"level": 2, "icon": "📄", "name": "연구계획서.md", "expanded": False},
        {"level": 2, "icon": "📄", "name": "일정표.md", "expanded": False},
        {"level": 1, "icon": "📁", "name": "02_자료수집", "expanded": True},
        {"level": 2, "icon": "📄", "name": "문헌목록.md", "expanded": False},
        {"level": 2, "icon": "📄", "name": "키워드.md", "expanded": False},
        {"level": 1, "icon": "📁", "name": "03_분석", "expanded": False},
        {"level": 1, "icon": "📁", "name": "04_작성", "expanded": False},
        {"level": 1, "icon": "📁", "name": "05_참고자료", "expanded": False},
    ]
    
    y_offset = 100
    for item in folders:
        indent = 60 + (item["level"] * 20)
        
        # Expand/collapse icon
        if item["icon"] == "📁":
            expand_icon = "▼" if item.get("expanded") else "▶"
            add_text(svg, indent, y_offset, expand_icon, size=10, fill=COLORS["text_dim"])
        
        # Item icon and name
        add_text(svg, indent + 15, y_offset, item["icon"], size=14)
        color = COLORS["text"] if item.get("expanded") or item["icon"] == "📄" else COLORS["text_dim"]
        add_text(svg, indent + 35, y_offset, item["name"], size=13, fill=color)
        
        y_offset += 25
    
    # Editor area showing README content
    add_rect(svg, 270, 60, 1630, 980, COLORS["bg"])
    add_text(svg, 290, 90, "README.md", size=13, fill=COLORS["text_dim"])
    add_rect(svg, 270, 100, 1630, 1, COLORS["border"])
    
    readme_content = [
        "# 내 연구 프로젝트",
        "",
        "## 프로젝트 개요",
        "이 프로젝트는 교육학 분야의 AI 활용 연구를 다룹니다.",
        "",
        "## 폴더 구조",
        "- `01_계획/`: 연구 계획 및 일정",
        "- `02_자료수집/`: 문헌 조사 및 자료",
        "- `03_분석/`: 데이터 분석 결과",
        "- `04_작성/`: 논문 초안 작성",
        "- `05_참고자료/`: 참고 문헌 및 자료",
    ]
    
    y_offset = 130
    for line in readme_content:
        if line.startswith("#"):
            add_text(svg, 290, y_offset, line, size=16, fill=COLORS["accent"], 
                    **{'font-weight': 'bold'})
        else:
            add_text(svg, 290, y_offset, line, size=13, fill=COLORS["text"])
        y_offset += 30
    
    return svg

def generate_model_picker():
    """Generate model picker dropdown screenshot"""
    svg = create_svg_base()
    create_vscode_window_frame(svg)
    
    # Chat panel
    add_rect(svg, 1400, 60, 500, 980, COLORS["bg_light"])
    add_text(svg, 1420, 90, "GitHub Copilot Chat", size=14, fill=COLORS["text"], 
            **{'font-weight': 'bold'})
    
    # Model picker dropdown (expanded)
    add_rect(svg, 1420, 110, 460, 40, COLORS["bg"], rx='3', 
            stroke=COLORS["border"], **{'stroke-width': '1'})
    add_text(svg, 1440, 135, "Claude Sonnet 4.5", size=13, fill=COLORS["text"])
    add_text(svg, 1850, 135, "▼", size=12, fill=COLORS["text_dim"])
    
    # Dropdown menu
    add_rect(svg, 1420, 155, 460, 400, COLORS["bg_light"], rx='5', 
            stroke=COLORS["border"], **{'stroke-width': '2'})
    
    models = [
        {"name": "GPT-5", "tag": "Latest", "premium": True},
        {"name": "Claude Sonnet 4.5", "tag": "Recommended", "selected": True, "premium": True},
        {"name": "Gemini 2.5 Pro", "tag": "Vision", "premium": True},
        {"name": "Grok", "tag": "New", "premium": True},
        {"name": "GPT-4o mini", "tag": "Fast", "premium": False},
        {"name": "Claude Haiku", "tag": "Efficient", "premium": False},
    ]
    
    y_offset = 180
    for model in models:
        # Selection highlight
        if model.get("selected"):
            add_rect(svg, 1425, y_offset - 18, 450, 35, COLORS["highlight"], rx='3')
        
        # Model name
        add_text(svg, 1440, y_offset, model["name"], size=14, fill=COLORS["text"])
        
        # Tag
        tag_color = COLORS["accent"] if model.get("premium") else COLORS["text_dim"]
        add_rect(svg, 1650, y_offset - 15, 80, 20, tag_color, rx='3', opacity='0.3')
        add_text(svg, 1690, y_offset - 1, model["tag"], size=10, 
                fill=tag_color, **{'text-anchor': 'middle'})
        
        # Premium badge
        if model.get("premium"):
            add_text(svg, 1750, y_offset, "⭐Pro", size=10, fill=COLORS["warning"])
        
        y_offset += 60
    
    # Editor area with explanation
    add_text(svg, 300, 150, "AI 모델 선택하기", size=24, fill=COLORS["text"], 
            **{'font-weight': 'bold'})
    
    explanations = [
        "Chat 패널 상단의 모델 선택 드롭다운을 클릭하면",
        "사용 가능한 모든 AI 모델을 볼 수 있습니다.",
        "",
        "🌟 Pro 모델 (Pro 플랜 필요):",
        "  • GPT-5: OpenAI의 최신 모델",
        "  • Claude Sonnet 4.5: 긴 컨텍스트에 강함",
        "  • Gemini 2.5 Pro: 이미지 분석 가능",
        "  • Grok: X.ai의 실시간 정보 모델",
        "",
        "⚡ Free 모델 (무료 플랜):",
        "  • GPT-4o mini: 빠른 응답",
        "  • Claude Haiku: 효율적인 처리",
    ]
    
    y_offset = 200
    for line in explanations:
        if line.startswith("🌟") or line.startswith("⚡"):
            add_text(svg, 300, y_offset, line, size=15, fill=COLORS["accent"], 
                    **{'font-weight': 'bold'})
        elif line.startswith("  •"):
            add_text(svg, 320, y_offset, line, size=13, fill=COLORS["text"])
        else:
            add_text(svg, 300, y_offset, line, size=14, fill=COLORS["text_dim"])
        y_offset += 30
    
    # Arrow pointing to dropdown
    draw_arrow(svg, 1200, 250, 1420, 180, COLORS["warning"])
    
    return svg

def draw_arrow(svg, x1, y1, x2, y2, color):
    """Draw an arrow from (x1,y1) to (x2,y2)"""
    # Line
    ET.SubElement(svg, 'line', {
        'x1': str(x1), 'y1': str(y1),
        'x2': str(x2), 'y2': str(y2),
        'stroke': color,
        'stroke-width': '3',
        'marker-end': 'url(#arrowhead)'
    })
    
    # Arrowhead marker (define once)
    if svg.find(".//marker[@id='arrowhead']") is None:
        defs = ET.SubElement(svg, 'defs')
        marker = ET.SubElement(defs, 'marker', {
            'id': 'arrowhead',
            'markerWidth': '10',
            'markerHeight': '10',
            'refX': '9',
            'refY': '3',
            'orient': 'auto'
        })
        ET.SubElement(marker, 'polygon', {
            'points': '0 0, 10 3, 0 6',
            'fill': color
        })


def generate_inline_completion():
    """Generate inline completion mockup"""
    svg = create_svg_base()
    create_vscode_window_frame(svg)
    
    # File tab
    add_rect(svg, 250, 40, 200, 35, COLORS["bg_light"])
    add_text(svg, 270, 63, "연구계획서.md", size=13, fill=COLORS["text"])
    
    # Editor content
    y_offset = 100
    lines = [
        ("# 연구 계획서", COLORS["accent"], "bold"),
        ("", COLORS["text"], "normal"),
        ("## 연구 주제", COLORS["accent"], "bold"),
        ("교육 현장에서의 AI 활용 효과 분석", COLORS["text"], "normal"),
        ("", COLORS["text"], "normal"),
        ("## 연구 방법", COLORS["accent"], "bold"),
        ("본 연구에서는 ", COLORS["text"], "normal"),
    ]
    
    for line, color, weight in lines:
        add_text(svg, 290, y_offset, line, size=14, fill=color, 
                **{'font-weight': weight})
        y_offset += 30
    
    # Copilot suggestion (gray text) - continuing after "본 연구에서는 "
    suggestion_text = "혼합 연구 방법(Mixed Methods)을 사용합니다. 정량적 데이터는"
    add_text(svg, 450, y_offset - 30, suggestion_text, size=14, 
            fill=COLORS["text_dim"], **{'font-style': 'italic'})
    
    # Cursor
    add_rect(svg, 448, y_offset - 44, 2, 20, COLORS["text"])
    
    # Tab key hint
    add_rect(svg, 700, 400, 500, 80, COLORS["bg_light"], rx='10', 
            stroke=COLORS["border"], **{'stroke-width': '2'})
    add_text(svg, 950, 445, "💡 Copilot 제안", size=18, fill=COLORS["accent"], 
            **{'text-anchor': 'middle', 'font-weight': 'bold'})
    add_text(svg, 950, 470, "Tab 키를 눌러 제안을 수락하세요", size=14, 
            fill=COLORS["text"], **{'text-anchor': 'middle'})
    
    # Arrow to suggestion
    draw_arrow(svg, 850, 450, 700, y_offset - 20, COLORS["warning"])
    
    return svg


def generate_chat_panel():
    """Generate Copilot Chat panel mockup"""
    svg = create_svg_base()
    create_vscode_window_frame(svg)
    
    # Chat panel on right side
    add_rect(svg, 1300, 60, 600, 980, COLORS["bg_light"])
    
    # Chat header
    add_text(svg, 1320, 90, "GitHub Copilot Chat", size=14, fill=COLORS["text"], 
            **{'font-weight': 'bold'})
    
    # Model picker (compact)
    add_rect(svg, 1320, 100, 280, 30, COLORS["bg"], rx='3')
    add_text(svg, 1330, 121, "Claude Sonnet 4.5", size=12, fill=COLORS["text"])
    add_text(svg, 1590, 121, "▼", size=10, fill=COLORS["text_dim"])
    
    # Chat messages
    messages = [
        {
            "role": "user",
            "text": "교육학 연구에서 혼합 연구 방법의\n장점을 설명해줘",
            "y": 160
        },
        {
            "role": "assistant",
            "text": "혼합 연구 방법(Mixed Methods)의 주요 장점:\n\n1. **포괄적 이해**: 정량적 + 정성적 데이터\n   통합으로 현상을 다각도로 분석\n\n2. **상호보완**: 한 방법의 약점을 다른\n   방법이 보완\n\n3. **타당도 향상**: 다양한 자료원으로\n   연구 결과의 신뢰성 증대",
            "y": 250
        }
    ]
    
    for msg in messages:
        if msg["role"] == "user":
            # User message (right-aligned bubble)
            add_rect(svg, 1500, msg["y"], 380, 70, COLORS["accent"], 
                    rx='10', opacity='0.3')
            add_text(svg, 1520, msg["y"] + 25, "👤 You:", size=11, 
                    fill=COLORS["text_dim"], **{'font-weight': 'bold'})
            
            y_text = msg["y"] + 45
            for line in msg["text"].split("\n"):
                add_text(svg, 1520, y_text, line, size=12, fill=COLORS["text"])
                y_text += 18
        else:
            # Assistant message (left-aligned)
            add_rect(svg, 1320, msg["y"], 560, 280, COLORS["bg"], 
                    rx='10', stroke=COLORS["border"], **{'stroke-width': '1'})
            add_text(svg, 1340, msg["y"] + 25, "🤖 Copilot:", size=11, 
                    fill=COLORS["accent"], **{'font-weight': 'bold'})
            
            y_text = msg["y"] + 50
            for line in msg["text"].split("\n"):
                if line.startswith("1.") or line.startswith("2.") or line.startswith("3."):
                    add_text(svg, 1340, y_text, line, size=12, 
                            fill=COLORS["text"], **{'font-weight': 'bold'})
                elif line.startswith("   "):
                    add_text(svg, 1360, y_text, line.strip(), size=11, 
                            fill=COLORS["text_dim"])
                else:
                    add_text(svg, 1340, y_text, line, size=12, fill=COLORS["text"])
                y_text += 22
    
    # Input box at bottom
    add_rect(svg, 1320, 950, 560, 60, COLORS["bg"], rx='5', 
            stroke=COLORS["border"], **{'stroke-width': '1'})
    add_text(svg, 1340, 985, "메시지를 입력하세요...", size=12, 
            fill=COLORS["text_dim"])
    
    # Editor area with instructions
    add_text(svg, 300, 150, "Copilot Chat 사용하기", size=24, 
            fill=COLORS["text"], **{'font-weight': 'bold'})
    add_text(svg, 300, 200, "📌 Chat 패널 열기: Ctrl+Shift+I", size=14, 
            fill=COLORS["text_dim"])
    add_text(svg, 300, 230, "📌 질문을 입력하면 AI가 응답합니다", size=14, 
            fill=COLORS["text_dim"])
    add_text(svg, 300, 260, "📌 코드나 문서 작성을 도와줍니다", size=14, 
            fill=COLORS["text_dim"])
    
    return svg


def generate_markdown_editing():
    """Generate Markdown editing with preview mockup"""
    svg = create_svg_base()
    create_vscode_window_frame(svg)
    
    # Split view - Editor on left, Preview on right
    # Editor side
    add_text(svg, 270, 70, "연구계획서.md", size=12, fill=COLORS["text_dim"])
    add_rect(svg, 250, 80, 835, 1, COLORS["border"])
    
    markdown_content = [
        "# 연구 계획서",
        "",
        "## 1. 연구 배경",
        "교육 현장에서 AI 도구의 활용이 증가하고 있습니다.",
        "",
        "## 2. 연구 목적",
        "- 교사의 AI 활용 역량 분석",
        "- 학생 학습 효과 측정",
        "- 윤리적 가이드라인 제안",
        "",
        "## 3. 연구 방법",
        "| 구분 | 방법 | 대상 |",
        "|------|------|------|",
        "| 정량 | 설문 | 교사 200명 |",
        "| 정성 | 인터뷰 | 교사 20명 |",
    ]
    
    y_offset = 110
    for line in markdown_content:
        if line.startswith("#"):
            color = COLORS["accent"]
            weight = "bold"
        elif line.startswith("|"):
            color = COLORS["success"]
            weight = "normal"
        elif line.startswith("-"):
            color = COLORS["text"]
            weight = "normal"
        else:
            color = COLORS["text"]
            weight = "normal"
        
        add_text(svg, 270, y_offset, line, size=13, fill=color, 
                **{'font-weight': weight})
        y_offset += 25
    
    # Vertical divider
    add_rect(svg, 1085, 80, 2, 960, COLORS["border"])
    
    # Preview side
    add_text(svg, 1120, 70, "미리보기", size=12, fill=COLORS["text_dim"])
    add_rect(svg, 1090, 80, 810, 1, COLORS["border"])
    
    # Rendered preview
    preview_content = [
        ("연구 계획서", 28, "bold", COLORS["text"]),
        ("1. 연구 배경", 20, "bold", COLORS["text"]),
        ("교육 현장에서 AI 도구의 활용이 증가하고 있습니다.", 14, "normal", COLORS["text"]),
        ("2. 연구 목적", 20, "bold", COLORS["text"]),
        ("• 교사의 AI 활용 역량 분석", 14, "normal", COLORS["text"]),
        ("• 학생 학습 효과 측정", 14, "normal", COLORS["text"]),
        ("• 윤리적 가이드라인 제안", 14, "normal", COLORS["text"]),
        ("3. 연구 방법", 20, "bold", COLORS["text"]),
    ]
    
    y_offset = 120
    for text, size, weight, color in preview_content:
        add_text(svg, 1120, y_offset, text, size=size, fill=color, 
                **{'font-weight': weight})
        y_offset += size + 15
    
    # Table in preview
    add_rect(svg, 1120, y_offset, 600, 80, COLORS["bg_light"], 
            stroke=COLORS["border"], **{'stroke-width': '1'})
    table_rows = [
        ["구분", "방법", "대상"],
        ["정량", "설문", "교사 200명"],
        ["정성", "인터뷰", "교사 20명"],
    ]
    
    row_y = y_offset + 25
    for row in table_rows:
        for i, cell in enumerate(row):
            add_text(svg, 1140 + (i * 180), row_y, cell, size=13, 
                    fill=COLORS["text"])
        row_y += 25
    
    return svg


def generate_vision_feature():
    """Generate Vision feature (image analysis) mockup"""
    svg = create_svg_base()
    create_vscode_window_frame(svg)
    
    # Chat panel with image attached
    add_rect(svg, 1300, 60, 600, 980, COLORS["bg_light"])
    add_text(svg, 1320, 90, "GitHub Copilot Chat", size=14, 
            fill=COLORS["text"], **{'font-weight': 'bold'})
    
    # Model indicator (Gemini for Vision)
    add_rect(svg, 1320, 100, 280, 30, COLORS["bg"], rx='3')
    add_text(svg, 1330, 121, "Gemini 2.5 Pro", size=12, fill=COLORS["text"])
    add_text(svg, 1470, 121, "👁️ Vision", size=11, fill=COLORS["success"])
    
    # User message with image
    add_rect(svg, 1320, 150, 560, 400, COLORS["bg"], rx='10')
    add_text(svg, 1340, 180, "👤 You:", size=11, fill=COLORS["text_dim"], 
            **{'font-weight': 'bold'})
    add_text(svg, 1340, 210, "이 그래프를 분석해줘", size=13, fill=COLORS["text"])
    
    # Image thumbnail placeholder
    add_rect(svg, 1340, 230, 520, 300, COLORS["bg_sidebar"], rx='5', 
            stroke=COLORS["border"], **{'stroke-width': '2'})
    add_text(svg, 1600, 380, "📊 chart-data.png", size=14, 
            fill=COLORS["text_dim"], **{'text-anchor': 'middle'})
    add_text(svg, 1600, 410, "1920x1080", size=11, fill=COLORS["text_dim"], 
            **{'text-anchor': 'middle'})
    
    # Response
    add_rect(svg, 1320, 570, 560, 200, COLORS["bg"], rx='10', 
            stroke=COLORS["accent"], **{'stroke-width': '2'})
    add_text(svg, 1340, 600, "🤖 Copilot:", size=11, fill=COLORS["accent"], 
            **{'font-weight': 'bold'})
    
    response_lines = [
        "이 막대 그래프는 다음을 보여줍니다:",
        "",
        "• X축: 연도별 데이터 (2020-2024)",
        "• Y축: 사용자 수 (단위: 천 명)",
        "• 추세: 지속적인 증가세 (연평균 25%)",
        "",
        "특이점: 2023년에 급격한 성장 관찰됨"
    ]
    
    y_offset = 630
    for line in response_lines:
        if line.startswith("•"):
            add_text(svg, 1360, y_offset, line, size=12, fill=COLORS["text"])
        elif line == "":
            y_offset -= 5
        else:
            add_text(svg, 1340, y_offset, line, size=12, fill=COLORS["text"], 
                    **{'font-weight': 'bold'})
        y_offset += 22
    
    # Instructions on left
    add_text(svg, 300, 150, "Vision 기능으로 이미지 분석", size=24, 
            fill=COLORS["text"], **{'font-weight': 'bold'})
    
    instructions = [
        "📌 이미지를 Chat에 드래그 앤 드롭",
        "📌 또는 '클립' 아이콘 클릭하여 첨부",
        "📌 Gemini 2.5 Pro 모델 선택",
        "📌 차트, 다이어그램, 스크린샷 분석 가능",
    ]
    
    y_offset = 200
    for instruction in instructions:
        add_text(svg, 300, y_offset, instruction, size=14, fill=COLORS["text_dim"])
        y_offset += 40
    
    # Example images that can be analyzed
    add_text(svg, 300, 380, "분석 가능한 이미지:", size=16, 
            fill=COLORS["accent"], **{'font-weight': 'bold'})
    
    examples = [
        "• 📊 데이터 차트 및 그래프",
        "• 📐 다이어그램 및 플로우차트",
        "• 📄 스캔된 문서 및 표",
        "• 🖼️ 연구 자료 스크린샷",
    ]
    
    y_offset = 420
    for example in examples:
        add_text(svg, 310, y_offset, example, size=14, fill=COLORS["text"])
        y_offset += 35
    
    return svg


def generate_mcp_architecture():
    """Generate MCP architecture diagram"""
    svg = create_svg_base()
    add_rect(svg, 0, 0, 1920, 1080, "#f5f5f5")  # Light background
    
    # Title
    add_text(svg, 960, 100, "Model Context Protocol (MCP) 아키텍처", 
            size=32, fill="#1e1e1e", **{'text-anchor': 'middle', 'font-weight': 'bold'})
    
    # Host Application box
    add_rect(svg, 200, 250, 400, 200, COLORS["accent"], rx='15', 
            stroke="#005a9e", **{'stroke-width': '3'})
    add_text(svg, 400, 320, "Host Application", size=20, fill="white", 
            **{'text-anchor': 'middle', 'font-weight': 'bold'})
    add_text(svg, 400, 360, "VS Code / Claude Desktop", size=16, 
            fill="white", **{'text-anchor': 'middle'})
    add_text(svg, 400, 390, "Zed / IDX", size=16, fill="white", 
            **{'text-anchor': 'middle'})
    
    # Bidirectional arrows
    for i in range(3):
        y_pos = 300 + (i * 70)
        # Right arrow
        draw_arrow(svg, 600, y_pos, 800, y_pos + (i * 30), "#ff6b6b")
        # Left arrow
        draw_arrow(svg, 800, y_pos + (i * 30) + 30, 600, y_pos + 30, "#4ecdc4")
    
    # MCP Protocol label
    add_rect(svg, 850, 200, 220, 60, "#ffd93d", rx='10')
    add_text(svg, 960, 240, "MCP Protocol", size=18, fill="#1e1e1e", 
            **{'text-anchor': 'middle', 'font-weight': 'bold'})
    
    # MCP Servers (3 boxes)
    servers = [
        {"name": "File System", "icon": "📁", "y": 250},
        {"name": "Database", "icon": "🗄️", "y": 420},
        {"name": "Web Search", "icon": "🔍", "y": 590},
    ]
    
    for server in servers:
        add_rect(svg, 1320, server["y"], 380, 140, "#6c5ce7", rx='15', 
                stroke="#5f27cd", **{'stroke-width': '3'})
        add_text(svg, 1420, server["y"] + 50, server["icon"], size=40)
        add_text(svg, 1510, server["y"] + 70, f"{server['name']} Server", 
                size=18, fill="white", **{'font-weight': 'bold'})
        add_text(svg, 1510, server["y"] + 100, "MCP-compatible", 
                size=14, fill="white", **{'font-style': 'italic'})
    
    # Benefits box
    add_rect(svg, 200, 650, 1500, 350, "#e8f5e9", rx='15', 
            stroke="#4caf50", **{'stroke-width': '3'})
    add_text(svg, 950, 710, "MCP의 장점", size=24, fill="#1e1e1e", 
            **{'text-anchor': 'middle', 'font-weight': 'bold'})
    
    benefits = [
        "✅ 표준화된 프로토콜: 모든 AI 앱에서 동일한 서버 사용",
        "✅ 확장성: 새로운 도구를 서버로 추가하면 모든 앱에서 접근 가능",
        "✅ 보안성: 샌드박스 환경에서 안전하게 실행",
        "✅ 재사용성: 한 번 설정하면 여러 앱에서 활용",
    ]
    
    y_offset = 760
    for benefit in benefits:
        add_text(svg, 250, y_offset, benefit, size=18, fill="#1e1e1e")
        y_offset += 60
    
    return svg

def save_svg(svg, filepath):
    """Save SVG to file"""
    tree = ET.ElementTree(svg)
    ET.indent(tree, space="  ")
    tree.write(filepath, encoding='utf-8', xml_declaration=True)
    print(f"✅ Generated: {filepath}")

def convert_svg_to_png(svg_path, png_path, width=1920, height=1080):
    """Convert SVG to PNG using cairosvg or rsvg-convert"""
    try:
        # Try cairosvg first
        import cairosvg
        cairosvg.svg2png(
            url=str(svg_path),
            write_to=str(png_path),
            output_width=width,
            output_height=height
        )
        print(f"✅ Converted to PNG: {png_path}")
        return True
    except ImportError:
        print("⚠️  cairosvg not installed, trying rsvg-convert...")
        try:
            subprocess.run([
                'rsvg-convert',
                '-w', str(width),
                '-h', str(height),
                '-o', str(png_path),
                str(svg_path)
            ], check=True)
            print(f"✅ Converted to PNG: {png_path}")
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            print(f"⚠️  Could not convert {svg_path} to PNG")
            print("   Install cairosvg: pip install cairosvg")
            print("   Or install librsvg: brew install librsvg (macOS)")
            return False

def main():
    """Generate all mockup screenshots"""
    base_dir = Path(__file__).parent
    images_dir = base_dir / "v13.0_resources" / "images" / "part1"
    
    # Ensure all subdirectories exist
    categories = [
        "github-education",
        "vscode-setup",
        "copilot-features",
        "2025-features",
        "mcp",
        "troubleshooting",
        "practice"
    ]
    
    for category in categories:
        (images_dir / category).mkdir(parents=True, exist_ok=True)
    
    print("🎨 Generating mockup screenshots...")
    print(f"📁 Output directory: {images_dir}\n")
    
    # Generate mockups
    mockups = [
        {
            "generator": generate_extensions_marketplace,
            "name": "Extensions Marketplace",
            "category": "vscode-setup",
            "filename": "extensions-marketplace-copilot.svg"
        },
        {
            "generator": generate_copilot_status_bar,
            "name": "Copilot Status Bar",
            "category": "vscode-setup",
            "filename": "copilot-pro-status-active.svg"
        },
        {
            "generator": generate_folder_structure,
            "name": "Folder Structure",
            "category": "practice",
            "filename": "vscode-folder-structure-example.svg"
        },
        {
            "generator": generate_model_picker,
            "name": "Model Picker",
            "category": "copilot-features",
            "filename": "copilot-model-picker.svg"
        },
        {
            "generator": generate_inline_completion,
            "name": "Inline Completion",
            "category": "copilot-features",
            "filename": "copilot-inline-completion.svg"
        },
        {
            "generator": generate_chat_panel,
            "name": "Chat Panel",
            "category": "copilot-features",
            "filename": "copilot-chat-panel.svg"
        },
        {
            "generator": generate_markdown_editing,
            "name": "Markdown Editing with Preview",
            "category": "practice",
            "filename": "copilot-markdown-editing-preview.svg"
        },
        {
            "generator": generate_vision_feature,
            "name": "Vision Feature",
            "category": "2025-features",
            "filename": "copilot-vision-image-attach.svg"
        },
        {
            "generator": generate_mcp_architecture,
            "name": "MCP Architecture Diagram",
            "category": "mcp",
            "filename": "mcp-architecture-diagram.svg"
        },
    ]
    
    generated_count = 0
    converted_count = 0
    
    for mockup in mockups:
        print(f"\n🎨 Generating: {mockup['name']}")
        svg = mockup["generator"]()
        
        # Save SVG
        svg_path = images_dir / mockup["category"] / mockup["filename"]
        save_svg(svg, svg_path)
        generated_count += 1
        
        # Convert to PNG
        png_path = svg_path.with_suffix('.png')
        if convert_svg_to_png(svg_path, png_path):
            converted_count += 1
    
    # Summary
    print("\n" + "="*60)
    print(f"✅ Generated {generated_count} SVG mockups")
    print(f"✅ Converted {converted_count} to PNG")
    print("="*60)
    
    if converted_count < generated_count:
        print("\n⚠️  Some SVGs were not converted to PNG")
        print("   Install cairosvg: python -m pip install cairosvg")
        print("   SVG files can still be used in documentation")
    
    print("\n📝 Next steps:")
    print("   1. Review generated images")
    print("   2. Replace [SCREENSHOT:] placeholders in MD files")
    print("   3. Commit to git")

if __name__ == "__main__":
    main()
