# ECTC Heat-Sink Research — Conversation Handoff

작성일: 2026-09-30  
저장소: [HyeongjunKim00/AdvancedPackaging](https://github.com/HyeongjunKim00/AdvancedPackaging)

## Objective
AI 가속기·HBM·3D 패키징을 위한 히트싱크/액체 냉각 연구 주제를 ECTC 초록으로 좁힌다. 이번 문서는 연구 방향 논의, 합의된 원칙, 선행기술과 미해결 질문을 다음 AI가 이어받도록 기록한다. 연구 수행이나 결과 수치 검증을 완료한 문서는 아니다.

## Current Understanding
- 연구실 지도 의견: **DLC 테스트 셋업 구축이 최우선**. 박사 연구는 (1) conventional heatsink 개선(예: vapor chamber, impinging jet 등), (2) V-Die 및 direct-to-silicon liquid cooling 데모를 탐색한다. V-Die 사이 Cu-pillar 배치로 microchannel을 만드는 아이디어가 포함된다.
- 사용자는 ECTC 주제로 우선 heat-sink 설계를 논의하고 있다. 그러나 연구 질문, 대상 구조, 냉각 방식, 운전 조건은 아직 결정되지 않았다.
- 단상/2상도 미결정이다. 단상은 시험·제어와 기준 비교가 상대적으로 단순해 첫 기준선 후보로 제안되었지만, 이는 **권고일 뿐 결정이 아니다**.
- 히트싱크 구조 설계의 가치는 표면적 자체가 아니라 유동 분배와 대류 열전달을 개선하면서 압력강하·펌프동력·공간 제약을 함께 만족시키는 데 있다. 따라서 문제는 실제 제약 조건을 고정해 정의해야 한다.
- 후보 문제 정의(미합의): **비균일 발열 AI 패키지에서 제한된 설치 공간과 냉각 동력 안에 hotspot을 낮추면서 열저항, 압력강하, 펌프동력을 함께 평가한다.**
- 열 spreader/lid는 열 확산뿐 아니라 die 높이 편차 보상, 평탄 접촉면, 패키지 강성·warpage 관리, 체결 하중으로부터 die 보호, TIM bond-line 관리 기능이 있다. 제거 시 계면을 줄일 수 있지만 기계·신뢰성 문제가 생길 수 있다. die 파손율을 정량 비교한 근거는 조사 자료에서 확인되지 않았다.
- 사용자는 짧고 집중된 답변을 선호한다. 결론을 먼저 말하고, 한 번에 한 문제씩 다룬다.

## Key Findings

### 연구 배경·문제
- 표면적이나 유량을 늘리는 것만으로는 충분한 연구 문제가 되지 않는다. 구조는 열전달과 압력강하를 동시에 바꾸며, 실제 시스템에서는 펌프동력·풋프린트·비균일 hotspot이 제약이 될 수 있다.
- 사용자가 공유한 실험/문헌 요약에는 마이크로채널의 열저항 개선과 큰 압력강하 증가가 함께 보고된 예가 있다. 모든 성능 수치는 기준 온도, 유량, 열부하, 채널 크기가 같을 때만 비교해야 한다.
- 냉각수 유량을 2배로 해도 peak 온도가 약 8°C 낮아지는 데 그쳤다는 수치는 리뷰의 2차 인용으로 제시됨. 원문 확인 전 일반 법칙처럼 쓰지 않는다.
- 3D HBM-on-GPU 시뮬레이션은 상부 단일면 냉각에서 열 문제가 커질 수 있음을 제시한다(사용자가 공유한 imec 요약: GPU 최고 141.7°C 대 2.5D 기준선 69.1°C). 원문 조건을 확인한 뒤 인용한다.
- Microsoft GH200 direct-to-silicon 요약에서는 GPU 개선 폭(열저항 51–60%)이 HBM(27–37%)보다 큰 것으로 보고됨. HBM이 별도 cold-plate/TIM 열경로에 남는 점을 연구 질문 후보로 검토할 수 있다. 출처는 사용자가 공유한 2차 요약이며 ECTC 논문 원문 확인이 필요하다.
- 고온 입구수(예: 45°C)와 상승하는 패키지 전력은 열설계 배경 후보지만, 특정 제품 전력 수치는 출처와 정의(TDP/TGP/패키지/랙)를 구분한다. Rubin 계열 수치는 충돌·루머가 많으므로 확정값으로 쓰지 않는다.

### 선행기술·차별성
- Direct-to-silicon 냉각 개념은 TSMC와 Microsoft 등의 선행 실증이 있어 그 자체로 V-Die의 신규성이라고 주장하지 않는다.
- 사용자가 공유한 보도 요약상 UNIST V-Die는 VLSI 2026에서 발표됐으며, 제안 아키텍처/시뮬레이션과 제작 중 프로토타입을 구분해야 한다. 원문·연구계획서와의 동일성은 확인되지 않았다.
- **US 11515232, “Liquid cooling through conductive interconnect”**는 도전성 bump/pillar 사이 냉각 유로를 포함하는 선행 특허 후보다. 청구항·출원인·패밀리·법적 상태를 확인해야 하며, 공개만으로 침해/권리 범위를 단정하지 않는다.
- arXiv:2609.24343 “Beyond HBM-on-GPU: Thermal Design Envelope…”는 cooling cavity 개념이 V-Die와 가까울 수 있어 novelty 확인 우선순위가 높다. 사용자가 공유한 조사 요약은 본문 미열람 상태다.
- 따라서 가능한 차별성은 **실제 적층/비균일 발열 TTV 실측**, HBM 경로 개선, 열저항과 ΔP·펌프동력·막힘/신뢰성 동시 평가일 수 있다. 모두 현재는 연구 공백 가설이며 “최초” 또는 “선행연구 없음”으로 쓰지 않는다.

### 설계·측정 원칙
- 열저항은 기준 온도를 정의한다(예: (R_{th}=(T_{j,max}-T_{inlet})/P)); 서로 다른 기준 정의를 직접 비교하지 않는다.
- 가능한 지표: 최고 접합온도와 온도 분포, 열저항, 열유속, ΔP, 펌프동력(ΔP×체적유량), COP, 유량/입구 온도, hotspot map, 누설·막힘·침식·열사이클 신뢰성.
- 균일 발열 시험과 hotspot/비균일 전력맵 시험을 구분한다. TTV에서 열원 구획, 센서 위치, calibration 및 불확도를 기록한다.
- V-Die 미세 유로라면 clogging과 필터 요구를 설계 제약 후보로 삼는다. OCP PG25 지침의 50 µm 이하 필터(25 µm 권장)는 원문 기준 확인 후 시험 사양에 반영한다.
- vapor chamber는 열을 퍼뜨리는 spreader이고, cold plate는 최종적으로 열을 냉각수로 넘기는 장치이므로 역할을 구분한다.

## Important Decisions
- 아직 **최종 ECTC 주제, 단상/2상, 대상 히트싱크 형상, 비교 기준, 운전 조건을 결정하지 않았다.**
- 수치 없는 상태에서 초록의 성능 향상값이나 시뮬레이션-실측 정합도를 만들지 않는다.
- 사실·출처 주장·추론을 분리한다. 사용자가 제공한 조사 표기의 A/B/C/추론 등급을 유지하되, 실제 인용 전 원문을 확인한다.
- 개인 연구 저장소: AI 작업은 시작 시 `PROJECT_CONTEXT.md`, `TODO.md`, `AI_HANDOFF.md`를 읽고, 종료 시 handoff를 갱신한다. 조사 기록은 적절한 `Research/` 하위 폴더에 둔다.
- 대화 중 리서치 폴더 5개(Thermal, Packaging, RF, EHD, Topic_Exploration)와 각 `README.md`, `Research_Log.md` 초안을 GitHub에 생성했다. 이번 문서는 Topic_Exploration에 추가한다.

## Open Questions
1. ECTC 초록의 실제 타깃은 conventional cold plate/heat sink 개선인가, V-Die 사이 냉각 채널 실증인가?
2. 목표 패키지와 열원: HBM+logic 구성, die 수·배치·높이, 발열량 및 비균일 전력맵은 무엇인가?
3. 연구실 DLC 셋업의 가능한 유체, 최대 유량·압력, 입구 온도, 히터 전력, 측정 센서는 무엇인가?
4. 단상 기준선에서 어느 제약(최고 온도, 풋프린트, 펌프동력, TIM/warpage)이 실제 한계인가?
5. V-Die와 US 11515232 및 arXiv 2609.24343의 구조적 중복과 남는 차별점은 무엇인가?
6. 85/95/105°C로 충돌하는 HBM 온도 한계 중 적용할 JEDEC/제조사 사양은 무엇인가?
7. TSMC ECTC 2025/2026 및 Microsoft ECTC 2026의 원문 시험 조건·유량·reticle 규모·압력강하는 무엇인가?

## Next Actions
1. 먼저 타깃을 하나로 좁힌다: conventional cold plate geometry 개선 또는 V-Die interlayer cooling 실증.
2. 연구실에서 구현 가능한 운전 범위와 기준 히트싱크를 정하고, 열원/센서가 포함된 TTV 요구사항을 작성한다.
3. 관련 선행기술 우선 확인: arXiv 2609.24343, US 11515232, UNIST VLSI 2026 원문/프로토타입 상태.
4. TSMC·Microsoft 결과와 OCP 지침은 원문·정의·측정 조건을 확인하고, 비교 가능 여부를 표로 정리한다.
5. 그 뒤에만 연구 질문, 성능 지표, 초록 스토리를 작성한다. 결과가 아직 없다면 초록을 실험 계획형으로 제한한다.

## References
아래는 대화에서 제공된 핵심 출처 링크다. 이 문서 작성 과정에서 모두 독립적으로 원문 검증한 것은 아니다.

- TSMC CoWoS direct-to-silicon, ECTC 2025: [DOI 10.1109/ECTC51687.2025.00131](https://doi.org/10.1109/ECTC51687.2025.00131)
- TSMC CoWoS-R micropillar, ECTC 2026: [DOI 10.1109/ECTC51846.2026.00092](https://doi.org/10.1109/ECTC51846.2026.00092)
- Microsoft microfluidic cooling: [Microsoft source article](https://news.microsoft.com/source/features/innovation/microfluidics-liquid-cooling-ai-chips/)
- imec 3D HBM-on-GPU thermal study: [imec press release](https://www.imec-int.com/en/press/imec-mitigates-thermal-bottleneck-3d-hbm-gpu-architectures-using-system-technology-co)
- V-Die and MOSAIC coverage: [Tom's Hardware, 2026-07-10](https://www.tomshardware.com/tech-industry/semiconductors/researchers-turn-hbm-on-its-side-to-tackle-ai-memorys-heat-wall-korean-v-die-and-japanese-mosaic-designs-promise-higher-bandwidth-denser-stacks-and-cooler-future-gpus)
- Interconnect cooling patent: [US 11515232](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11515232)
- Potential cooling-cavity prior art: [arXiv 2609.24343](https://arxiv.org/abs/2609.24343)
- OCP coolant/filtration guidance: [PG25 guidelines](https://www.opencompute.org/documents/ocp-pg25-guidelines-v1-0-0-pdf), [OAI liquid-cooling guidelines](https://www.opencompute.org/documents/oai-system-liquid-cooling-guidelines-in-ocp-template-mar-3-2023-update-pdf)
- Microchannel thermal-hydraulic trade-off experiment: [Applied Thermal Engineering article](https://www.sciencedirect.com/science/article/pii/S1359431116330459)
- Research review on 3D integrated thermal management: [Communications Engineering review](https://www.nature.com/articles/s44172-026-00590-y)

## Suggested Prompt
> 이 저장소의 `PROJECT_CONTEXT.md`, `TODO.md`, `AI_HANDOFF.md`, 그리고 `Research/Topic_Exploration/ECTC_HeatSink_Conversation_Handoff_2026-09-30.md`를 먼저 읽어라. 사용자는 AI/3D 패키지용 ECTC heat-sink 연구 주제를 정하는 중이며, 아직 주제·냉각 방식·시험 조건을 확정하지 않았다. 답변은 간결하게 하고, 사실·출처 주장·추론을 구분하라. 먼저 conventional heat-sink 개선과 V-Die interlayer cooling 중 실제로 풀 문제를 정하도록 돕고, 제시된 선행기술(arXiv 2609.24343, US 11515232, VLSI 2026 V-Die)과 차별성을 원문 기준으로 확인하라. 측정되지 않은 결과나 수치를 만들지 말고, 연구실 TTV/DLC 운전 한계를 확인하기 전 성능 목표를 단정하지 마라.
