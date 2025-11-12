#!/usr/bin/env python3
"""
Generate remaining simple mockup screenshots quickly
"""

import xml.etree.ElementTree as ET
from pathlib import Path
from generate_mockups import (
    create_svg_base, add_rect, add_text, add_circle, save_svg,
    convert_svg_to_png, COLORS
)


def generate_github_education_pack():
    """Generate GitHub Education Pack page mockup"""
    svg = create_svg_base()
    
    # Browser chrome
    add_rect(svg, 0, 0, 1920, 60, "#2d2d30")
    add_text(svg, 960, 40, "🌐 education.github.com/pack", 
            size=16, fill="white", **{'text-anchor': 'middle'})
    
    # White page background
    add_rect(svg, 0, 60, 1920, 1020, "white")
    
    # Header
    add_rect(svg, 0, 60, 1920, 120, "#24292f")
    add_text(svg, 960, 130, "GitHub Student Developer Pack", 
            size=36, fill="white", **{'text-anchor': 'middle', 'font-weight': 'bold'})
    
    # Hero section
    add_rect(svg, 200, 220, 1520, 300, "#f6f8fa", rx='15', 
            stroke="#d0d7de", **{'stroke-width': '2'})
    
    add_text(svg, 960, 280, "🎓 무료로 시작하세요", 
            size=32, fill="#24292f", **{'text-anchor': 'middle', 'font-weight': 'bold'})
    add_text(svg, 960, 330, "학생 인증만 하면 $200,000 상당의 개발 도구를 무료로 사용할 수 있습니다", 
            size=18, fill="#57606a", **{'text-anchor': 'middle'})
    
    # CTA Button
    add_rect(svg, 810, 370, 300, 60, "#2da44e", rx='10')
    add_text(svg, 960, 410, "Get your pack", 
            size=20, fill="white", **{'text-anchor': 'middle', 'font-weight': 'bold'})
    
    # Benefits grid
    benefits = [
        {"icon": "🤖", "name": "GitHub Copilot Pro", "value": "$240/year"},
        {"icon": "☁️", "name": "Azure Credits", "value": "$100"},
        {"icon": "🚀", "name": "Vercel Pro", "value": "$240/year"},
        {"icon": "💾", "name": "MongoDB Atlas", "value": "$200"},
    ]
    
    y_base = 580
    for i, benefit in enumerate(benefits):
        x = 260 + (i * 380)
        add_rect(svg, x, y_base, 340, 180, "white", rx='10', 
                stroke="#d0d7de", **{'stroke-width': '2'})
        add_text(svg, x + 170, y_base + 60, benefit["icon"], 
                size=48, **{'text-anchor': 'middle'})
        add_text(svg, x + 170, y_base + 120, benefit["name"], 
                size=18, fill="#24292f", **{'text-anchor': 'middle', 'font-weight': 'bold'})
        add_text(svg, x + 170, y_base + 150, f"가치: {benefit['value']}", 
                size=14, fill="#57606a", **{'text-anchor': 'middle'})
    
    # Highlight Copilot
    add_rect(svg, 250, 570, 360, 200, "none", rx='15', 
            stroke="#ff6b6b", **{'stroke-width': '4'})
    
    return svg


def generate_login_prompt():
    """Generate Copilot login prompt mockup"""
    svg = create_svg_base()
    add_rect(svg, 0, 0, 1920, 1080, "#1e1e1e")
    
    # Dialog box
    add_rect(svg, 610, 340, 700, 400, "#252526", rx='10', 
            stroke="#3e3e42", **{'stroke-width': '2'})
    
    # GitHub logo
    add_circle(svg, 960, 420, 50, "#ffffff")
    add_text(svg, 960, 435, "GH", size=28, fill="#24292f", 
            **{'text-anchor': 'middle', 'font-weight': 'bold'})
    
    # Title
    add_text(svg, 960, 520, "Sign in to use GitHub Copilot", 
            size=22, fill="#d4d4d4", **{'text-anchor': 'middle', 'font-weight': 'bold'})
    add_text(svg, 960, 560, "GitHub 계정으로 로그인하여 Copilot을 시작하세요", 
            size=14, fill="#858585", **{'text-anchor': 'middle'})
    
    # Sign in button
    add_rect(svg, 760, 600, 400, 50, "#007acc", rx='5')
    add_text(svg, 960, 633, "Sign in with GitHub", 
            size=16, fill="white", **{'text-anchor': 'middle', 'font-weight': 'bold'})
    
    # Info text
    add_text(svg, 960, 690, "✓ 학생 계정이면 Copilot Pro를 무료로 사용할 수 있습니다", 
            size=13, fill="#4ec9b0", **{'text-anchor': 'middle'})
    
    return svg


def generate_troubleshooting_inactive():
    """Generate Copilot inactive status for troubleshooting"""
    svg = create_svg_base()
    add_rect(svg, 0, 0, 1920, 1080, "#1e1e1e")
    
    # Centered alert box
    add_rect(svg, 460, 340, 1000, 400, "#2d2d30", rx='15', 
            stroke="#f48771", **{'stroke-width': '3'})
    
    # Warning icon
    add_text(svg, 960, 440, "⚠️", size=72, **{'text-anchor': 'middle'})
    
    # Title
    add_text(svg, 960, 520, "Copilot이 비활성화되어 있습니다", 
            size=28, fill="#f48771", **{'text-anchor': 'middle', 'font-weight': 'bold'})
    
    # Troubleshooting steps
    steps = [
        "1. 인터넷 연결을 확인하세요",
        "2. GitHub 로그인 상태를 확인하세요",
        "3. VS Code를 재시작해보세요",
        "4. Copilot 확장이 활성화되어 있는지 확인하세요",
    ]
    
    y_offset = 580
    for step in steps:
        add_text(svg, 960, y_offset, step, size=16, fill="#d4d4d4", 
                **{'text-anchor': 'middle'})
        y_offset += 35
    
    # Status bar preview (inactive)
    add_rect(svg, 560, 420, 800, 40, "#007acc")
    add_text(svg, 1300, 445, "GitHub Copilot", size=14, fill="#858585")
    add_text(svg, 1240, 445, "❌", size=14)
    
    return svg


def generate_context_writing_practice():
    """Generate research context writing practice example"""
    svg = create_svg_base()
    
    # VS Code window
    add_rect(svg, 0, 0, 1920, 1080, "#1e1e1e")
    
    # Title bar
    add_rect(svg, 0, 0, 1920, 40, "#2d2d30")
    add_circle(svg, 20, 20, 6, "#ff5f57")
    add_circle(svg, 40, 20, 6, "#febc2e")
    add_circle(svg, 60, 20, 6, "#28c840")
    add_text(svg, 90, 27, "연구컨텍스트.md", size=13, fill="#d4d4d4")
    
    # Editor content
    content = [
        ("# 연구 컨텍스트", 20, "#007acc", "bold", 100),
        ("", 16, "#d4d4d4", "normal", 140),
        ("## 연구 분야", 18, "#007acc", "bold", 170),
        ("교육학 > 교육공학 > AI 활용 교육", 14, "#d4d4d4", "normal", 200),
        ("", 14, "#d4d4d4", "normal", 230),
        ("## 연구 목적", 18, "#007acc", "bold", 260),
        ("고등학교 수학 수업에서 AI 도구(ChatGPT, Copilot)를", 14, "#d4d4d4", "normal", 290),
        ("활용한 개별화 학습의 효과를 분석하고, 교사를 위한", 14, "#d4d4d4", "normal", 315),
        ("실천적 가이드라인을 개발합니다.", 14, "#d4d4d4", "normal", 340),
        ("", 14, "#d4d4d4", "normal", 370),
        ("## 핵심 연구 질문", 18, "#007acc", "bold", 400),
        ("1. AI 도구가 학습 성취도에 미치는 영향은?", 14, "#d4d4d4", "normal", 430),
        ("2. 학생들의 AI 활용 패턴은 어떠한가?", 14, "#d4d4d4", "normal", 455),
        ("3. 교사는 어떤 역할을 해야 하는가?", 14, "#d4d4d4", "normal", 480),
    ]
    
    for text, size, color, weight, y in content:
        add_text(svg, 50, y, text, size=size, fill=color, **{'font-weight': weight})
    
    # Copilot suggestion indicator
    add_rect(svg, 900, 400, 900, 600, "#252526", rx='10', 
            stroke="#007acc", **{'stroke-width': '2'})
    add_text(svg, 1350, 450, "💡 컨텍스트 작성 Tip", 
            size=22, fill="#007acc", **{'text-anchor': 'middle', 'font-weight': 'bold'})
    
    tips = [
        "✓ 구체적인 분야를 명시하세요",
        "  (예: 교육학 > 교육공학)",
        "",
        "✓ 연구 목적을 명확히 서술하세요",
        "  (대상, 방법, 기대효과)",
        "",
        "✓ 핵심 질문을 3-5개 작성하세요",
        "",
        "✓ Copilot에게 이 파일을 참조하게 하면",
        "  더 정확한 답변을 받을 수 있습니다",
    ]
    
    y_offset = 500
    for tip in tips:
        if tip.startswith("✓"):
            add_text(svg, 950, y_offset, tip, size=16, fill="#4ec9b0", 
                    **{'font-weight': 'bold'})
        elif tip.startswith("  "):
            add_text(svg, 970, y_offset, tip.strip(), size=14, fill="#858585")
        else:
            add_text(svg, 950, y_offset, tip, size=14, fill="#d4d4d4")
        y_offset += 30
    
    return svg


def main():
    """Generate additional mockups"""
    base_dir = Path(__file__).parent
    images_dir = base_dir / "v13.0_resources" / "images" / "part1"
    
    mockups = [
        {
            "generator": generate_github_education_pack,
            "name": "GitHub Education Pack Page",
            "category": "github-education",
            "filename": "github-education-pack-main.svg"
        },
        {
            "generator": generate_login_prompt,
            "name": "Login Prompt",
            "category": "vscode-setup",
            "filename": "copilot-login-prompt.svg"
        },
        {
            "generator": generate_troubleshooting_inactive,
            "name": "Copilot Inactive (Troubleshooting)",
            "category": "troubleshooting",
            "filename": "copilot-inactive-status.svg"
        },
        {
            "generator": generate_context_writing_practice,
            "name": "Context Writing Practice",
            "category": "practice",
            "filename": "practice-context-writing.svg"
        },
    ]
    
    print("🎨 Generating additional mockups...\n")
    
    generated = 0
    converted = 0
    
    for mockup in mockups:
        print(f"🎨 Generating: {mockup['name']}")
        svg = mockup["generator"]()
        
        svg_path = images_dir / mockup["category"] / mockup["filename"]
        save_svg(svg, svg_path)
        generated += 1
        
        png_path = svg_path.with_suffix('.png')
        if convert_svg_to_png(svg_path, png_path):
            converted += 1
    
    print("\n" + "="*60)
    print(f"✅ Generated {generated} additional mockups")
    print(f"✅ Converted {converted} to PNG")
    print("="*60)


if __name__ == "__main__":
    main()
