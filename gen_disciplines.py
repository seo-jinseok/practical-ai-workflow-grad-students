#!/usr/bin/env python3
"""4개 전공별 폴더 구조 생성"""
from generate_mockups import *
import os

W, H = 1920, 1080
OUT = 'v13.0_resources/part3/images'

def gen_life():
    svg = create_svg_base(W, H)
    add_rect(svg, 0, 0, W, H, fill=COLORS['bg'])
    add_text(svg, W/2, 80, '생명과학 연구 프로젝트 구조', size=48, fill='white', **{'text-anchor': 'middle', 'font-weight': 'bold'})
    add_text(svg, W/2, 140, '세포 신호전달 경로 연구', size=28, fill='#888', **{'text-anchor': 'middle'})
    add_rect(svg, 200, 220, 1520, 760, fill='#252526', stroke='#3e3e42', stroke_width=2, rx=8)
    
    fs = [
        ('📁',0,'cell_signaling/',''),('📁',1,'01_실험계획/',''),('📄',2,'proposal.md','연구 제안서'),
        ('📄',2,'protocol.md','실험 프로토콜'),('📄',2,'irb.pdf','IRB 승인'),('📁',1,'02_실험데이터/',''),
        ('📁',2,'raw_data/','원시 데이터'),('📄',3,'western_blot.tif','웨스턴 블롯'),('📄',3,'pcr_results.csv','PCR 결과'),
        ('📁',2,'microscopy/','현미경'),('📄',3,'confocal_001.nd2','공초점 데이터'),('📁',1,'03_분석/',''),
        ('📁',2,'scripts/','분석 코드'),('📄',3,'image_analysis.py','이미지 분석'),('📄',3,'statistics.R','통계 분석'),
        ('📁',2,'processed/','처리됨'),('📄',3,'results.xlsx','정량화 결과'),('📁',1,'04_논문/',''),
        ('📄',2,'manuscript.md','논문 초안'),('📁',2,'figures/','그림'),('📄',3,'pathway.ai','경로도'),
        ('📄',1,'lab_notebook.md','실험 노트'),('📄',1,'README.md','프로젝트 개요')
    ]
    
    y = 260
    for icon, indent, name, desc in fs:
        x = 240 + indent * 40
        add_text(svg, x, y, icon, size=20, fill='white')
        c = '#4ec9b0' if icon == '📁' else '#ce9178'
        add_text(svg, x+35, y, name, size=18, fill=c, family='Monaco')
        if desc:
            add_text(svg, x+35+len(name)*10, y, f'  # {desc}', size=16, fill='#6a9955')
        y += 30
    
    add_text(svg, W/2, 1010, '💡 생명과학: 실험 데이터 관리와 재현성이 핵심', size=20, fill='#858585', anchor='middle')
    return svg

def gen_cs():
    svg, r = create_svg_base(W, H)
    add_rect(svg, 0, 0, W, H, fill=COLORS['bg'])
    add_text(svg, W/2, 80, '컴퓨터공학 연구 프로젝트 구조', size=48, fill='white', weight='bold', anchor='middle')
    add_text(svg, W/2, 140, '추천 시스템 개발 및 평가', size=28, fill='#888', anchor='middle')
    add_rect(svg, 200, 220, 1520, 760, fill='#252526', stroke='#3e3e42', stroke_width=2, rx=8)
    
    fs = [
        ('📁',0,'recommendation_system/',''),('📁',1,'01_design/',''),('📄',2,'architecture.md','시스템 설계'),
        ('📄',2,'api_spec.yaml','API 스펙'),('📄',2,'schema.sql','DB 스키마'),('📁',1,'02_dataset/',''),
        ('📁',2,'raw/','원시'),('📄',3,'user_interactions.csv','사용자 로그'),('📄',3,'items.json','아이템'),
        ('📁',2,'processed/','전처리'),('📄',3,'train_set.parquet','학습 데이터'),('📄',3,'test_set.parquet','테스트'),
        ('📁',1,'03_models/',''),('📁',2,'collaborative/','협업 필터링'),('📄',3,'matrix_factor.py','SVD++'),
        ('📁',2,'deep_learning/','딥러닝'),('📄',3,'neural_cf.py','Neural CF'),('📁',1,'04_evaluation/',''),
        ('📄',2,'metrics.py','평가 지표'),('📄',2,'ablation.ipynb','모델 비교'),('📁',1,'05_deploy/',''),
        ('📄',2,'Dockerfile','컨테이너'),('📄',2,'api_server.py','FastAPI'),('📁',1,'06_paper/',''),
        ('📄',2,'main.tex','LaTeX 논문'),('📄',1,'README.md','문서')
    ]
    
    y = 260
    for icon, indent, name, desc in fs:
        x = 240 + indent * 40
        add_text(svg, x, y, icon, size=20, fill='white')
        c = '#4ec9b0' if icon == '📁' else '#ce9178'
        add_text(svg, x+35, y, name, size=18, fill=c, family='Monaco')
        if desc:
            add_text(svg, x+35+len(name)*10, y, f'  # {desc}', size=16, fill='#6a9955')
        y += 28
    
    add_text(svg, W/2, 1010, '💡 컴퓨터공학: 코드 버전 관리와 재현 가능한 실험', size=20, fill='#858585', anchor='middle')
    return svg

def gen_sociology():
    svg, r = create_svg_base(W, H)
    add_rect(svg, 0, 0, W, H, fill=COLORS['bg'])
    add_text(svg, W/2, 80, '사회학 연구 프로젝트 구조', size=48, fill='white', weight='bold', anchor='middle')
    add_text(svg, W/2, 140, '노동자 정체성 질적 연구', size=28, fill='#888', anchor='middle')
    add_rect(svg, 200, 220, 1520, 760, fill='#252526', stroke='#3e3e42', stroke_width=2, rx=8)
    
    fs = [
        ('📁',0,'labor_identity/',''),('📁',1,'01_설계/',''),('📄',2,'research_question.md','연구 질문'),
        ('📄',2,'sampling.md','표집 전략'),('📄',2,'interview_guide.md','면접 가이드'),('📄',2,'consent.pdf','동의서'),
        ('📁',1,'02_현장조사/',''),('📁',2,'fieldnotes/','현장 노트'),('📄',3,'factory_visit.md','공장 방문'),
        ('📄',3,'union_meeting.md','노조 회의'),('📁',2,'interviews/','인터뷰'),('📄',3,'interview_01.md','참여자 A'),
        ('📄',3,'interview_02.md','참여자 B'),('📁',3,'audio/','녹음 (암호화)'),('📁',1,'03_분석/',''),
        ('📁',2,'coding/','코딩'),('📄',3,'open_coding.md','개방 코딩'),('📄',3,'axial_coding.md','축 코딩'),
        ('📄',3,'selective_coding.md','선택 코딩'),('📁',2,'memos/','메모'),('📄',3,'theoretical_memo.md','이론적 메모'),
        ('📁',1,'04_논문/',''),('📄',2,'manuscript.md','논문 초안'),('📄',2,'literature.md','문헌 검토'),
        ('📁',1,'05_윤리/',''),('📄',2,'irb_protocol.pdf','IRB 승인'),('📄',2,'anonymization.md','익명화 기록'),
        ('📄',1,'README.md','개요')
    ]
    
    y = 260
    for icon, indent, name, desc in fs:
        x = 240 + indent * 40
        add_text(svg, x, y, icon, size=20, fill='white')
        c = '#4ec9b0' if icon == '📁' else '#ce9178'
        add_text(svg, x+35, y, name, size=18, fill=c, family='Monaco')
        if desc:
            add_text(svg, x+35+len(name)*10, y, f'  # {desc}', size=16, fill='#6a9955')
        y += 27
    
    add_text(svg, W/2, 1010, '💡 사회학: 연구 윤리와 데이터 익명화가 필수', size=20, fill='#858585', anchor='middle')
    return svg

def gen_music():
    svg, r = create_svg_base(W, H)
    add_rect(svg, 0, 0, W, H, fill=COLORS['bg'])
    add_text(svg, W/2, 80, '음악학 연구 프로젝트 구조', size=48, fill='white', weight='bold', anchor='middle')
    add_text(svg, W/2, 140, '바로크 오페라 분석 연구', size=28, fill='#888', anchor='middle')
    add_rect(svg, 200, 220, 1520, 760, fill='#252526', stroke='#3e3e42', stroke_width=2, rx=8)
    
    fs = [
        ('📁',0,'baroque_opera/',''),('📁',1,'01_악보/',''),('📁',2,'original_scores/','원본'),
        ('📄',3,'handel_rinaldo.mscz','MuseScore'),('📄',3,'vivaldi.xml','MusicXML'),('📁',2,'transcriptions/','편곡'),
        ('📄',3,'aria_analysis.pdf','화성 분석용'),('📁',1,'02_음원/',''),('📁',2,'recordings/','녹음'),
        ('📄',3,'1980_gardiner.flac','역사적 연주'),('📄',3,'2020_modern.mp3','현대 해석'),('📁',2,'samples/','발췌'),
        ('📄',3,'recitative.wav','레치타티보'),('📁',1,'03_분석/',''),('📄',2,'harmonic.md','화성 분석'),
        ('📄',2,'form_structure.md','형식 구조'),('📄',2,'text_music.md','가사-음악'),('📁',2,'viz/','시각화'),
        ('📄',3,'melodic_contour.png','선율 윤곽'),('📁',1,'04_역사맥락/',''),('📁',2,'documents/','문헌'),
        ('📄',3,'libretto.pdf','원본 대본'),('📄',3,'reviews.md','초연 평론'),('📁',1,'05_논문/',''),
        ('📄',2,'thesis.md','논문 초안'),('📁',2,'examples/','악보 예시'),('📄',3,'da_capo.png','다 카포'),
        ('📄',2,'bibliography.bib','참고문헌'),('📄',1,'README.md','개요')
    ]
    
    y = 260
    for icon, indent, name, desc in fs:
        x = 240 + indent * 40
        add_text(svg, x, y, icon, size=20, fill='white')
        c = '#4ec9b0' if icon == '📁' else '#ce9178'
        add_text(svg, x+35, y, name, size=18, fill=c, family='Monaco')
        if desc:
            add_text(svg, x+35+len(name)*10, y, f'  # {desc}', size=16, fill='#6a9955')
        y += 27
    
    add_text(svg, W/2, 1010, '💡 음악학: 악보와 음원 파일 형식 관리가 핵심', size=20, fill='#858585', anchor='middle')
    return svg

if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    
    mockups = [
        ('Life Science', 'life-science-project-folders', gen_life),
        ('Computer Science', 'cs-project-folders', gen_cs),
        ('Sociology', 'sociology-project-folders', gen_sociology),
        ('Music', 'music-project-folders', gen_music),
    ]
    
    for name, filename, func in mockups:
        print(f'🎨 Generating: {name}')
        svg = func()
        svg_path = f'{OUT}/{filename}.svg'
        png_path = f'{OUT}/{filename}.png'
        save_svg(svg, svg_path)
        print(f'✅ SVG: {svg_path}')
        convert_svg_to_png(svg_path, png_path)
        print(f'✅ PNG: {png_path}')
    
    print(f'\n✅ Generated {len(mockups)} discipline-specific folder structures')
