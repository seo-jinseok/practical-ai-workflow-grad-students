#!/usr/bin/env python3
"""
Batch replace [SCREENSHOT:] placeholders with actual image links
"""

from pathlib import Path
import re

# Mapping of screenshot descriptions to actual file paths
SCREENSHOT_MAPPINGS = {
    # Part 1 main document
    "Practical_AI_Workflow_for_Grad_Students v13.0_Part1.md": [
        {
            "placeholder": "[SCREENSHOT: VS Code 다운로드 페이지]",
            "image": "![VS Code 다운로드 페이지](v13.0_resources/images/part1/vscode-setup/extensions-marketplace-copilot.png)",
            "note": "Using Extensions Marketplace as proxy for download page"
        },
        {
            "placeholder": "[SCREENSHOT: Extensions Marketplace - GitHub Copilot 검색]",
            "image": "![Extensions Marketplace - GitHub Copilot 검색](v13.0_resources/images/part1/vscode-setup/extensions-marketplace-copilot.png)"
        },
        {
            "placeholder": "[SCREENSHOT: Copilot 로그인 프롬프트]",
            "image": "![Copilot 로그인 프롬프트](v13.0_resources/images/part1/vscode-setup/copilot-login-prompt.png)"
        },
        {
            "placeholder": "[SCREENSHOT: Copilot 활성화 상태 - Pro 표시]",
            "image": "![Copilot 활성화 상태 - Pro 표시](v13.0_resources/images/part1/vscode-setup/copilot-pro-status-active.png)"
        },
        {
            "placeholder": "[SCREENSHOT: VS Code Explorer에서 본 연구 폴더 구조]",
            "image": "![VS Code Explorer에서 본 연구 폴더 구조](v13.0_resources/images/part1/practice/vscode-folder-structure-example.png)"
        },
        {
            "placeholder": "[SCREENSHOT: VS Code에서 Markdown 작성하는 모습]",
            "image": "![VS Code에서 Markdown 작성하는 모습](v13.0_resources/images/part1/copilot-features/copilot-inline-completion.png)"
        },
        {
            "placeholder": "[SCREENSHOT: 연구 계획서 템플릿을 복사해서 사용하는 모습]",
            "image": "![연구 계획서 템플릿을 복사해서 사용하는 모습](v13.0_resources/images/part1/practice/practice-context-writing.png)"
        },
        {
            "placeholder": "[SCREENSHOT: VS Code의 Markdown 미리보기 기능]",
            "image": "![VS Code의 Markdown 미리보기 기능](v13.0_resources/images/part1/practice/copilot-markdown-editing-preview.png)"
        },
        {
            "placeholder": "[SCREENSHOT: VS Code의 모델 선택 드롭다운]",
            "image": "![VS Code의 모델 선택 드롭다운](v13.0_resources/images/part1/copilot-features/copilot-model-picker.png)"
        },
        {
            "placeholder": "[SCREENSHOT: 이미지를 Copilot에 첨부하여 분석하는 모습]",
            "image": "![이미지를 Copilot에 첨부하여 분석하는 모습](v13.0_resources/images/part1/2025-features/copilot-vision-image-attach.png)"
        },
    ],
    
    # Resource files
    "v13.0_resources/01_github_copilot_student_guide.md": [
        {
            "placeholder": "[SCREENSHOT: GitHub Education Pack 메인 페이지]",
            "image": "![GitHub Education Pack 메인 페이지](../images/part1/github-education/github-education-pack-main.png)"
        },
        {
            "placeholder": "[SCREENSHOT: 학생 인증 폼]",
            "image": "![학생 인증 폼](../images/part1/github-education/github-education-pack-main.png)",
            "note": "Using main page as proxy for auth form"
        },
        {
            "placeholder": "[SCREENSHOT: 신청 완료 확인 페이지]",
            "image": "![신청 완료 확인 페이지](../images/part1/github-education/github-education-pack-main.png)",
            "note": "Using main page as proxy"
        },
        {
            "placeholder": "[SCREENSHOT: Copilot Pro 활성화 상태]",
            "image": "![Copilot Pro 활성화 상태](../images/part1/vscode-setup/copilot-pro-status-active.png)"
        },
    ],
    
    "v13.0_resources/02_vscode_setup_checklist.md": [
        {
            "placeholder": "[SCREENSHOT: VS Code 설치 방법 안내]",
            "image": "![VS Code 설치 방법 안내](../images/part1/vscode-setup/extensions-marketplace-copilot.png)",
            "note": "Generic placeholder"
        },
        {
            "placeholder": "[SCREENSHOT: VS Code Extensions Marketplace - GitHub Copilot 검색]",
            "image": "![VS Code Extensions Marketplace - GitHub Copilot 검색](../images/part1/vscode-setup/extensions-marketplace-copilot.png)"
        },
        {
            "placeholder": "[SCREENSHOT: Copilot 로그인 프롬프트 - 상태바]",
            "image": "![Copilot 로그인 프롬프트 - 상태바](../images/part1/vscode-setup/copilot-login-prompt.png)"
        },
        {
            "placeholder": "[SCREENSHOT: GitHub Education Pack 신청 페이지]",
            "image": "![GitHub Education Pack 신청 페이지](../images/part1/github-education/github-education-pack-main.png)"
        },
        {
            "placeholder": "[SCREENSHOT: VS Code Settings - 테마 및 폰트 설정]",
            "image": "![VS Code Settings - 테마 및 폰트 설정](../images/part1/vscode-setup/extensions-marketplace-copilot.png)",
            "note": "Generic placeholder"
        },
        {
            "placeholder": "[SCREENSHOT: VS Code Extensions - 권장 확장]",
            "image": "![VS Code Extensions - 권장 확장](../images/part1/vscode-setup/extensions-marketplace-copilot.png)"
        },
        {
            "placeholder": "[SCREENSHOT: GitHub Copilot 설정 페이지]",
            "image": "![GitHub Copilot 설정 페이지](../images/part1/vscode-setup/copilot-pro-status-active.png)",
            "note": "Using status bar as proxy for settings page"
        },
    ],
    
    "v13.0_resources/05_markdown_quick_reference.md": [
        {
            "placeholder": "[SCREENSHOT: VS Code Extensions - Markdown 관련]",
            "image": "![VS Code Extensions - Markdown 관련](../images/part1/vscode-setup/extensions-marketplace-copilot.png)"
        },
    ],
    
    "v13.0_resources/06_copilot_models_comparison.md": [
        {
            "placeholder": "[SCREENSHOT: Gemini에 이미지 첨부 예시]",
            "image": "![Gemini에 이미지 첨부 예시](../images/part1/2025-features/copilot-vision-image-attach.png)"
        },
        {
            "placeholder": "[SCREENSHOT: Model picker dropdown]",
            "image": "![Model picker dropdown](../images/part1/copilot-features/copilot-model-picker.png)"
        },
    ],
}


def replace_screenshots_in_file(filepath, mappings):
    """Replace all screenshot placeholders in a file"""
    print(f"\n📝 Processing: {filepath.name}")
    
    try:
        content = filepath.read_text(encoding='utf-8')
        original_content = content
        replacements = 0
        
        for mapping in mappings:
            placeholder = mapping["placeholder"]
            image = mapping["image"]
            
            if placeholder in content:
                content = content.replace(placeholder, image)
                replacements += 1
                print(f"   ✅ Replaced: {placeholder[:50]}...")
                
                if "note" in mapping:
                    print(f"      ℹ️  {mapping['note']}")
            else:
                print(f"   ⚠️  Not found: {placeholder[:50]}...")
        
        if replacements > 0:
            filepath.write_text(content, encoding='utf-8')
            print(f"   💾 Saved {replacements} replacements")
            return replacements
        else:
            print(f"   ⏭️  No replacements needed")
            return 0
            
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return 0


def main():
    """Main function"""
    base_dir = Path(__file__).parent
    
    print("🔄 Starting batch screenshot replacement...")
    print(f"📁 Base directory: {base_dir}")
    
    total_files = 0
    total_replacements = 0
    
    for filename, mappings in SCREENSHOT_MAPPINGS.items():
        filepath = base_dir / filename
        
        if not filepath.exists():
            print(f"\n⚠️  File not found: {filename}")
            continue
        
        total_files += 1
        replacements = replace_screenshots_in_file(filepath, mappings)
        total_replacements += replacements
    
    print("\n" + "="*60)
    print(f"✅ Processed {total_files} files")
    print(f"✅ Made {total_replacements} replacements")
    print("="*60)
    
    print("\n📝 Next steps:")
    print("   1. Review changes in each file")
    print("   2. Test image rendering in Markdown preview")
    print("   3. Commit to git")


if __name__ == "__main__":
    main()
