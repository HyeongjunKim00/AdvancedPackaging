# AI Handoff

## 현재 상태
- 활성 연구 주제: V-Die 전용 단상 inter-die cooling. 서로 마주 보는 die 사이의 비전기 Cu thermal bridge/pillar를 열전달 구조로 고려하며, die 간격 및 유로와 열·유압 특성을 시뮬레이션하는 방향.
- 사용자는 ECTC 2024–2026 연구실 초록/원고 5개를 읽고 문장 역할, 전개 구조, 제목 스타일을 추출해 재사용 가능한 Markdown 가이드를 만들길 요청함.
- GitHub `Research/Thermal/Incoming/`에서 5개 PDF와 Jimin Kwon 2026 DOCX가 확인됨. GitHub API로 파일명·크기는 확인했으나 PDF 본문은 추출하지 못함. Windows shell과 CUA 프로세스 시작이 오류 1385로 실패했고, 브라우저 PDF 텍스트 읽기도 캐시 미스가 발생함. 따라서 원문에 기반한 분석이나 가이드는 아직 작성하지 않음.

## 완료 작업
- GitHub Incoming 폴더에서 입력 파일 확인:
  - `ECTC2024_Abstract_Submitted.pdf`
  - `나현_ECTC2025_Abstract_final_JM.pdf`
  - `ECTC2025_HJung_Manuscript.pdf`
  - `ECTC2026_Abstract_Jimin Kwon.pdf`
  - `ECTC2026_Abstract_Jimin Kwon.docx`
  - `ECTC2026_KKim_Abstract_V6_HJung.pdf`
- 파일을 직접 분석하지 못한 상태를 명시함. 확인 전 내용을 추측해 요약하지 않음.

## 미완료 작업
- 위 문서의 실제 본문 추출 및 5개 고유 초록/원고 분석 (Jimin Kwon DOCX/PDF는 동일본 여부 확인).
- 문장별 rhetorical function, 문제 정의→기존 접근→gap→기여→결과/의의 전개, 제목 문형, 시제·태, 결과 수치 제시 패턴을 정리한 재사용 가이드 생성.
- Research Log에 분석 결과 반영.
- 분석된 구조를 V-Die 초록에 적용하되 측정 전 결과는 placeholder로 유지.

## 핵심 참고자료
- [Incoming abstracts and manuscripts](https://github.com/HyeongjunKim00/AdvancedPackaging/tree/main/Research/Thermal/Incoming)
- [Thermal Research Log](https://github.com/HyeongjunKim00/AdvancedPackaging/blob/main/Research/Thermal/Research_Log.md)
- 연구실 초록 작성 방식의 목표는 사용자가 제시한 예시처럼 문장 기능과 순서가 분명한 인과적 구조를 파악하는 것.

## 다음 AI용 프롬프트
GitHub의 `Research/Thermal/Incoming/`에서 ECTC 2024–2026 PDF/DOCX를 실제로 읽을 수 있는 문서 추출 기능을 사용하라. 먼저 PDF와 Word 본문 접근을 검증하고, Jimin Kwon DOCX와 PDF의 동일 여부를 확인하라. 5개 고유 자료를 문장별 기능 및 제목 구성 기준으로 비교하고, 공통 공식과 문서별 변형을 분리한 `Research/ECTC_Abstract_Writing_Guide.md`를 작성하라. `Research/Thermal/Research_Log.md`와 이 파일도 갱신하라. 사실과 해석을 구분하고, 자료에 없는 수치·결과를 만들지 말라.
