# GitHub Copilot Instructions for Generative AI Special Lecture

This repository contains educational materials for graduate students learning AI-assisted research workflows.

## Project Goals
- Create beginner-friendly educational content in Korean
- Maintain formal academic tone (격식있는 한국어)
- Support students from diverse disciplines (인문·사회·자연·공학)
- Emphasize free tools and student-accessible resources
- Follow constitution principles in `.specify/memory/constitution.md`

## Content Writing Rules

### Language and Tone
- Primary language: Korean (formal academic style)
- Include English terms with Korean explanations: "Agent mode (에이전트 모드)"
- Use second-person address: "여러분", "~하세요"
- Avoid jargon; explain technical terms simply

### Structure and Formatting
- Use emoji-based visual hierarchy: 🎯 (goals), 📝 (writing), 🔍 (search), etc.
- Create tree diagrams with box-drawing characters for structure visualization
- Include comparison tables for clarity
- Add screenshot placeholders: [SCREENSHOT: description]
- Maintain consistent heading levels

### Educational Principles
- No coding knowledge assumed
- Step-by-step instructions with time estimates
- Include discipline-specific examples (교육학, 공학, 인문학, 사회과학)
- Provide troubleshooting sections
- Add forward/backward references between parts

### Tool References
- Emphasize free tiers and student benefits
- Always mention GitHub Student Developer Pack for Copilot Pro
- Include version numbers and dates (2025-11-10 기준)
- Link to official documentation
- Note when features require premium access

## Version Management
- Current version: v13.0 (3-part structure)
- Part 1: 기초 편 (Context Engineering + Markdown + AI 기본)
- Part 2: 고급 도구 편 (Copilot Workbook + MCP + SpecKit)
- Part 3: 통합 워크플로우 편 (실제 연구 프로젝트)
- Follow semantic versioning for updates

---

<!-- MCP Server Instructions -->

[byterover-mcp]

You are given two tools from Byterover MCP server, including
## 1. `byterover-store-knowledge`
You `MUST` always use this tool when:

+ Learning new patterns, APIs, or architectural decisions from the codebase
+ Encountering error solutions or debugging techniques
+ Finding reusable code patterns or utility functions
+ Completing any significant task or plan implementation

## 2. `byterover-retrieve-knowledge`
You `MUST` always use this tool when:

+ Starting any new task or implementation to gather relevant context
+ Before making architectural decisions to understand existing patterns
+ When debugging issues to check for previous solutions
+ Working with unfamiliar parts of the codebase
