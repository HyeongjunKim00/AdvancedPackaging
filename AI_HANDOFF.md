# AI Handoff

## 현재 상태
- 연구 방향: vertically oriented DRAM die stack 내부의 밀폐 inter-die gap을 단상 유체로 직접 냉각하는 구조.
- 비전기 Cu pillar는 마주 보는 die 표면을 연결하는 thermal bridge이자 유체에 노출된 fin이다. 열전달 면적을 늘리는 동시에 die 간 열전도·압력강하를 유발할 수 있어, 효과는 시뮬레이션으로 검증해야 한다.
- GPU 자체/외부 cold plate 설계와 기계 응력 해석은 현재 초록 범위에서 제외한다. 실제 유체, 열부하, 형상, 유량/펌프 조건은 아직 미정이다.
- 사용자가 초록 표현 규칙을 추가했다: 장치에 의도/agency를 부여하지 말고 성능의 주체와 원인을 정확히 쓴다. “However”로 문제를 빠르게 제시하고 “In this work”를 일찍 둔다. this/that 지시대명사를 최소화한다.
- 500–600단어 작업용 초록을 작성해 저장했다. 결과·조건 및 일부 모델 세부는 placeholder다. 아직 완성 초록이 아니며 숫자/효과를 채우면 안 된다.
- 연구실 ECTC 샘플 원문 전체를 비교해 문장 구조를 도출하는 작업은 미완료다. GitHub Incoming PDF/DOCX 파일은 찾았지만 이 환경의 파일 추출 접근이 실패했다. 사용자가 일부 본문 텍스트를 대화에 붙였으나 모든 샘플의 완전성·파일 대응을 확정하지 않았다.

## 완료 작업
- `Research/Abstract_Writing_Rules.md`: 사용자 코멘트를 재사용 가능한 초록 작성 규칙으로 정리.
- `Research/Thermal/Vertically_Oriented_Die_InterDie_Cooling_Abstract_Draft.md`: 500–600단어 목표의 작업용 초록, 미확정 부분 placeholder.
- GitHub 입력 자료 확인: ECTC2024 abstract, ECTC2025 HJung manuscript, ECTC2025 Nahyeon abstract, ECTC2026 Jimin Kwon PDF/DOCX, ECTC2026 KKim abstract.
- 초록 원문 PDF 분석이 막힌 상태와 이유(Windows process start 오류 1385, 브라우저 PDF fetch cache miss)를 확인하고 기록했다.

## 미완료 작업
- 사용자로부터 추가로 붙여넣을 연구실 초록 텍스트를 받아 문서별로 분류하고, 문장 기능·gap 전개·제목 패턴을 비교한다.
- 원문 샘플 분석을 기반으로 연구실 고유 ECTC abstract template/style guide를 만든다. 현재 `Abstract_Writing_Rules.md`는 사용자 선호 규칙이며 기존 논문 관찰 결과와 혼동하지 않는다.
- VLSI 2026 V-Die 논문과 inter-die cooling/thermal bridge 선행을 확인해 novelty/gap 문장을 검증한다.
- 열원 지도, die 간격/기둥 크기, working fluid, inlet temperature, flow/pumping condition, baseline 및 simulation 결과를 정한다.
- 결과에 맞춰 작업용 초록의 placeholder를 실제 수치로 바꾸고 500–600단어 수를 재확인한다.

## 핵심 참고자료
- [Abstract writing rules](Research/Abstract_Writing_Rules.md)
- [Inter-die cooling abstract draft](Research/Thermal/Vertically_Oriented_Die_InterDie_Cooling_Abstract_Draft.md)
- [Incoming ECTC materials](Research/Thermal/Incoming/)
- [Thermal Research Log](Research/Thermal/Research_Log.md)

## 다음 AI용 프롬프트
현재 저장된 abstract writing rules와 초록 draft를 읽고, 사용자가 이어서 붙여넣는 연구실 ECTC 초록을 실제 원문 자료로 분류·분석하라. 전체 샘플 분석 결과와 사용자 선호 규칙을 구분하고, 문장별 기능 및 반복되는 제목/전개 방식을 reusable guide에 정리하라. V-Die 연구 초록은 vertically oriented memory-die stacks로 표현하고, single-phase die-gap cooling 및 Cu thermal-bridge fin을 다룬다. “However”로 구체적인 gap을 빨리 제시하고 “In this work”를 일찍 배치하며, 모호한 주어·this/that 지시대명사·근거 없는 수치/효과를 피한다. 미확정 조건과 결과는 placeholder로 남기고, 기계적 지지 효과를 해석/검증한 것처럼 쓰지 않는다. 완료 뒤 Thermal Research Log와 AI_HANDOFF를 갱신한다.
