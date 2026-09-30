# AI Handoff

## 현재 상태
- 활성 연구는 AI/HBM/3D 패키징용 ECTC 콜드플레이트 설계다. 구체적 문제, 냉각 구조, 기준선, TTV 조건은 미결정이다.
- 사용자가 설명한 V-Die는 DRAM die를 세워 측면 I/O를 늘리고 메모리 용량을 확장하려는 구조다. die 크기/형상이 기존 GPU-HBM 평면 패키지와 다를 수 있다.
- 현재 문제 정의 후보는 평면 패키지 상부 접촉을 전제로 한 콜드플레이트와 V-Die의 수직 die 측면·die 사이 간극 간 기하학적 불일치다. 이는 검증되지 않은 가설이다.

## 완료 작업
- V-Die 관련으로 지적할 콜드플레이트 설계점은 단순 표면적이 아니라 좁은 die 사이 유로에 대한 공급·회수 매니폴드, die별 유량 분배, 측면 냉각과 I/O·실링·기계 지지의 양립 가능성으로 좁혀 보았다.
- 해당 가설과 미확인 요소를 [Thermal Research Log](Research/Thermal/Research_Log.md)에 [추론]으로 기록했다.
- 중요 제한: 비표준 die 크기 자체는 열 문제의 증거가 아니며, DRAM 용량 증가만으로 전력이 비례한다고 단정하지 않는다. 실제 단면, die 간격, 전력지도와 냉각 경계가 필요하다.

## 미완료 작업
- V-Die 단면도에서 냉각 가능한 면, gap, 패드 위치, 씰 및 지지 구조를 확인한다.
- 기준 콜드플레이트의 접촉면과 TIM/열경로를 실제 V-Die 배치와 비교한다.
- die별 발열지도 또는 heater 분할 TTV와 유량/압력 측정 가능 범위를 정한다.
- 상부 냉각과 측면/갭 냉각을 비교할 기준, ΔP 예산, 열저항 정의를 정한다.
- direct-to-silicon/interlayer cooling 선행기술을 원문 확인해 novelty를 점검한다.

## 핵심 참고자료
- [V-Die 콜드플레이트 가설 및 확인 항목](Research/Thermal/Research_Log.md)
- [콜드플레이트 통합 조사본](Research/Thermal/Incoming/2026-09-30_콜드플레이트_ChatGPT.md) — 2차 AI 조사본, 수치·서지 미검증.
- [V-Die 연구 대화 인계](Research/Topic_Exploration/ECTC_HeatSink_Conversation_Handoff_2026-09-30.md)

## 다음 AI용 프롬프트
먼저 AI_GUIDE.md, PROJECT_CONTEXT.md, TODO.md, AI_HANDOFF.md를 읽어라. 사용자가 설명한 V-Die의 구조를 기준으로 콜드플레이트 문제를 논의하되, “평면 상부 접촉 vs 수직 die 측면/좁은 gap 접근”은 아직 가설임을 유지하라. V-Die 단면, die 간격, I/O/씰/지지부, die별 전력지도와 실험 가능한 TTV/유량/ΔP 범위를 먼저 확인하라. 전력 증가나 냉각 병목을 용량/JEDEC 이탈만으로 단정하지 마라. 조사본의 수치와 novelty는 원문 검증 전 확정하지 말고, 대화는 간결하게 핵심 한 가지씩 진행하라.