# Thermal Research Log

새 조사나 실험 계획마다 아래 항목을 복사해 기록합니다. 아직 수행하지 않은 조사·실험 결과를 미리 채우지 않습니다.

## YYYY-MM-DD — 제목

### 질문 / 문제 정의
- 어떤 열 병목 또는 설계 제약을 다루는가?

### 조건과 범위
- 패키지/열원 구조:
- 냉각 방식 및 작동 유체:
- 입구 온도·유량 또는 펌프동력:
- 기준 구조와 비교 조건:

### 근거
| 주장 또는 결과 | 출처/링크 | 근거 등급 | 원문 확인 여부 |
|---|---|---|---|
| | | A / B / C / 추론 | |

### 성능 지표
- 최고 온도·온도 분포:
- 열저항(기준 온도와 정의 포함):
- 압력강하·펌프동력/COP:
- 막힘·누설·열사이클 등 신뢰성:

### 해석과 한계
- 관측 사실:
- 해석/추론:
- 비교상의 한계 또는 미확인 사항:

### 다음 행동 / 결정
- [ ] 
## 2026-09-30 — 외부 AI 콜드플레이트 조사본 수신 및 1차 정리

### 질문 / 문제 정의
- ECTC 연구 논의를 공랭 히트싱크 일반론에서 AI/HPC 시스템의 액체식 콜드플레이트 설계로 구체화할 때, 문헌상 어떤 설계 병목과 연구축이 후보가 되는가?

### 조건과 범위
- 자료: [2026-09-30 통합 연구동향: 콜드플레이트 액체 냉각](Incoming/2026-09-30_콜드플레이트_ChatGPT.md)
- 문서가 표방하는 범위: 2024–2026 전자소자·AI/HPC·데이터센터 액체 냉각, 원 조사본과 추가 부록 통합.
- 이번 기록은 문서 내용을 읽고 구조화한 것이며 개별 논문·수치·DOI를 원문 대조하지 않았다.

### 근거
| 주장 또는 결과 | 출처/링크 | 근거 등급 | 원문 확인 여부 |
|---|---|---|---|
| 콜드플레이트 연구는 미세채널 크기 조정 외에 매니폴드/유량 분배, 비균일 열부하, 제조 제약, 패키지 통합, 신뢰성과 시스템 경계로 확장된다는 것이 조사본의 종합 | 위 통합 조사본, 특히 0–2장 및 34장 | [C: AI 종합 조사본] | 아니오 |
| 유효한 설계 평가는 최고온도·열저항과 함께 ΔP/펌프동력, 온도 균일성, 제조·신뢰성 조건을 함께 다뤄야 한다는 것이 조사본의 권고 | 위 통합 조사본 23–26, 34.21–34.22절 | [C: AI 종합 조사본의 해석/권고] | 아니오 |
| 조사본이 제안하는 잠재적 연구 공백은 실제 비균일 발열지도, 매니폴드 유량 분배와 hotspot 냉각의 공동 설계, warm-water 조건, as-built 제조오차, 과도응답, 패키지/TIM/콜드플레이트 연계, 신뢰성 검증 등 | 위 통합 조사본 21–22, 34.19–34.24절 | [C: AI 종합 조사본의 해석] | 아니오 |

### 성능 지표
- 후보 열 지표: Tmax, 온도 범위/표준편차, 정의가 명시된 Rth, 냉각수 온도 상승.
- 후보 유압 지표: ΔP, 유량, 펌프동력, 유량 분배 불균일도.
- 공정·신뢰성 후보: 최소 형상 크기, 표면 거칠기, 실제 제작 형상 편차, 막힘/침식/부식/누설 및 시간에 따른 성능 변화.
- 비교 조건은 동일 유량뿐 아니라 동일 ΔP 또는 동일 펌프동력 기준 중 연구 질문에 맞는 조건을 명시해야 한다는 것이 조사본의 방법론적 권고다. 어떤 지표를 채택할지는 미정이다.

### 해석과 한계
- **자료에서 읽은 핵심:** “열전달계수를 높이는 채널 모양”만 제안하기보다, 실제 열부하 지도를 냉각수 유로에 어떻게 대응시키고 그 대가인 압력손실·펌프동력과 제조·패키지 제약을 어떻게 제한할지 문제를 정의하는 편이 더 설득력 있다는 방향이다.
- **현재 ECTC 논의에 대한 추론:** 기존 콜드플레이트를 기준으로 한다면 우선 후보는 `비균일 열원 + 매니폴드/유량 분배 + 압력강하 예산 + 실험 검증` 조합이다. 이는 후보이지 선정된 주제나 확인된 novelty 주장이 아니다.
- 원문 문서는 149 KB 규모의 통합 자료이고 상당수 문헌 항목은 초록/검색 결과 기반이라고 문서 자체가 밝힌다. 인용된 연구 존재 여부, 서지, 수치, 조건, 비교 정의는 검증되지 않았다. 특히 W/cm² 수치만으로 서로 다른 규모의 콜드플레이트를 비교하지 않는다.
- 자료 안의 추천 연구 방향은 원저자의 종합·추론으로 취급하고, 연구계의 확정 사실처럼 인용하지 않는다.

### 다음 행동 / 결정
- [ ] 사용자가 원하는 콜드플레이트 시스템/패키지와 실제 실험 가능한 열원·냉각 루프 조건을 정한다.
- [ ] 조사본의 후보 방향 중 사용자 장비·TTV·제작 공정에 맞는 범위를 고른다.
- [ ] 선택한 방향의 핵심 주장과 수치를 1차 논문/공식 자료로 대조하고 시험 조건을 추출한다.
- [ ] 주제 확정 전에는 단상/2상 또는 특정 구조를 결정된 것으로 취급한다.
## 2026-09-30 — V-Die 패키지와 콜드플레이트 간 구조 불일치 (가설)

### 질문 / 문제 정의
- V-Die에서 die를 세워 I/O와 메모리 용량을 늘리는 구조라면, 기존 콜드플레이트의 어떤 설계 가정이 더 이상 맞지 않을 수 있는가?

### 조건과 범위
- 기준 구조: 사용자가 설명한 V-Die 개념(수직 배치 DRAM die, 측면 I/O, GPU/HBM과 다른 크기·형상 가능성). 상세 단면, 치수, 발열지도는 아직 미제공.
- 이 항목은 개념 단계의 열설계 추론이며, 특정 상용 콜드플레이트의 성능을 사실로 단정하지 않는다.

### 근거
| 주장 또는 결과 | 출처/링크 | 근거 등급 | 원문 확인 여부 |
|---|---|---|---|
| AI/HPC 콜드플레이트 연구는 유량 분배, 비균일 열원, 패키지/계면과의 공동 설계를 문제 후보로 다룬다는 종합 | [콜드플레이트 조사본](Incoming/2026-09-30_콜드플레이트_ChatGPT.md) | [C: AI 조사본, 미검증] | 아니오 |
| 평면형 패키지 상부 접촉을 전제로 한 냉각 경계가 수직 die의 측면과 inter-die 간극 접근에 부적합할 수 있다는 가설 | 사용자가 설명한 V-Die 형상 + 콜드플레이트 조사본에서 도출 | [추론] | 해당 V-Die 단면 및 냉각 배치 미확인 |

### 성능 지표
- 실제 V-Die 열원에서 die별 Tmax 및 온도 불균일도.
- 수직 die별 유체 분배량/속도, 각 gap의 ΔP 및 총 펌프동력.
- 냉각 경계가 상부 면, 측면, die 사이 gap 중 어디에 놓이는지에 따른 열저항.
- 패드 접근/절연, 실링, die 기계적 지지와 유체 유로가 공존 가능한지.

### 해석과 한계
- **가설:** 기존 콜드플레이트의 개선 지점을 단순히 채널 표면적이 아니라, 평면 패키지의 상부 접촉면 중심 설계와 V-Die의 수직 열전달면·좁은 die 간극 사이의 기하학적 불일치에서 찾을 수 있다.
- 더 구체적으로는 (1) 좁은 die 사이 gap으로 유체를 공급·회수하는 매니폴드/유로, (2) die별 발열량에 맞춘 유량 배분, (3) die 측면 냉각 시 패드·실링·기계 지지와의 양립이 설계 변수 후보이다.
- JEDEC 규격을 벗어난 치수 자체는 열 병목의 증거가 아니다. 전력/발열 변화도 die 수 또는 DRAM 용량만으로 비례한다고 가정할 수 없다. 실제 전력지도와 경계조건이 필요하다.
- 이 가설은 현재 V-Die 단면·die 간격·패드 위치·예상 전력 맵이 없어 검증되지 않았다. direct-to-silicon 또는 die 간 냉각 선행기술과도 대조하지 않았다.

### 다음 행동 / 결정
- [ ] V-Die 단면도에서 냉각수 접근 가능한 면, 간격, 패드, 지지부, 씰 경계를 표시한다.
- [ ] 기준 콜드플레이트가 실제 어느 면을 냉각하는지와 TIM/접촉 경로를 도식화한다.
- [ ] GPU/DRAM die별 예상 전력 또는 heater 분할 TTV 열지도를 정의한다.
- [ ] 상부 냉각 vs 측면/갭 냉각의 비교 기준 및 ΔP 예산을 정한다.
## 2026-09-30 — V-Die 냉각 경계 후보 구분

### 사용자 지정 방향
- 우선 구상: V-Die가 GPU 위에 놓인 패키지에서 V-Die 바깥면에 외부 콜드플레이트를 부착한다.
- 확장 가능성: V-Die를 이루는 die 사이 간극에 유체를 흘려 inter-die 직접 냉각을 구현한다.

### 문제 정의 후보
- 기준안 A — 외부 측면 콜드플레이트: 외부 냉각면에서 내부 DRAM die까지 이어지는 열전도 경로와 접촉/계면, 외측면으로의 열집중, GPU와 DRAM 간 열경로를 평가한다.
- 확장안 B — die 사이 유체 냉각: 냉각 경계를 내부 die 간극으로 옮겨 내부 die의 열경로를 줄일 가능성을 평가한다. 이 구성은 기존 콜드플레이트 개선이라기보다 패키지 통합 microfluidic cooling으로 분류하는 편이 정확하다.

### 비교와 주의
- 두 방식의 비교축 후보: die별 Tmax/온도편차, 열저항, 유량별 ΔP와 펌프동력, 유량분배, 제작·실링·전기 I/O 간섭, 신뢰성.
- 외부 콜드플레이트를 현실적 baseline으로 설정하고, inter-die 유체는 성능·통합 난이도가 다른 확장 구조로 분리한다.
- V-Die의 실제 die 방향/간격/외측 접촉면, GPU 냉각 경계, die별 전력은 아직 도식화되지 않아 구체적인 우열이나 열적 이득을 주장할 수 없다.
- inter-die 유체 흐름은 가능성 제안이며, 선행기술·제작 가능성·누설/막힘·절연/부식 제약은 검증 전이다.

### 다음 행동
- [ ] V-Die 단면에 GPU, DRAM die, 외부 콜드플레이트, 잠재적 inter-die 유로, I/O와 실링 경계를 함께 표시한다.
- [ ] 기준안 A의 열전도 경로와 예상 병목을 먼저 정의한다.
- [ ] B는 A와 분리하여 추가 냉각 경계 후보로 검토한다.
## 2026-09-30 — 외부 측면 콜드플레이트 연구가 fin 최적화로만 수렴하는지

### 논의 요점
- 콜드플레이트 연구가 fin 형상만 다뤄야 하는 것은 아니다. fin은 국소 대류를 높이는 설계변수 중 하나다.
- V-Die 연구의 차별화 후보는 V-Die die별/비균일 열원, 열원이 외부 냉각면까지 거치는 3D 패키지 열경로, 외측 접촉 구조, 유량 분배, die 수·간격 변화에 따른 온도 편차와 고정 유압 예산 아래의 성능이다.
- 단, 패키지·계면·열원 분포를 제외하고 단순 냉각판 유로만 시뮬레이션하면 결과가 fin pitch/형상 비교로 축소되어 보일 위험이 있다.

### 미정 사항
- 어떤 V-Die 면이 외부 콜드플레이트와 접촉하는지, 각 DRAM die에서 접촉면까지 열이 어떤 재료/계면을 통과하는지 단면 기준으로 확인되지 않았다.
- 실제 GPU/DRAM 전력 지도와 실험 검증 가능성도 미정이다.

### 후보 문제 문장 [추론]
- “V-Die die별 비균일 발열과 패키지 열경로를 포함할 때, 외부 측면 콜드플레이트가 die 수/간격 변화에도 die별 최고온도와 온도편차를 제어할 수 있는가? 유량 분배 설계가 제한된 ΔP 또는 펌프동력에서 이를 개선하는가?”
- 이 질문을 설정한 뒤 manifold, 접촉면 또는 fin 형상 중 실제 지배 병목을 확인한다. fin 형상은 원인 분석 후 선택할 설계변수로 둔다.
## 2026-09-30 — GB200 콜드플레이트와 GPU/HBM 높이 불일치 concern

### 사용자가 제기한 concern
- 큰 콜드플레이트가 GPU와 HBM처럼 높이가 다른 부품 위에 놓일 때, 단차/공차를 어떻게 맞추고 균일한 열접촉·하중을 유지하는가?
- 사용자는 GPU 775 µm, HBM 약 10 mm라고 언급했으나 두 수치의 기준면과 방향은 확인되지 않았다.

### 확인된 정보
- JEDEC JESD238A HBM3 치수표의 공개 미러에서 HBM3 device 평면 치수 X/Y는 각각 10.975 mm, Z 적층 높이는 구성별 695/720/745 µm로 표기된다. 따라서 10 mm는 수직 stack height가 아니라 평면 footprint를 지칭했을 가능성이 높다. 이 자료는 공식 JEDEC 호스트에서 직접 열람한 것이 아니라 표준 문서 공개 미러다.
- NVIDIA의 DGX GB 하드웨어 가이드는 냉각수가 매니폴드를 거쳐 tray 내 CPU/GPU에 부착된 cold plate를 통과한다고 설명하지만, GPU/HBM 상면 단차나 GB200 package-level 접촉 치수는 공개 가이드 검색 범위에서 확인되지 않았다.

### 해석과 한계
- **[추론]** 연구 대상은 “HBM이 10 mm 높다”가 아니라, package/substrate 기준면에서 GPU 및 각 HBM cold-plate contact surface의 실제 z-height 차이, 공차, warpage와 체결 하중 분포일 가능성이 높다.
- flat cold-plate base가 높이가 다른 접촉면을 동시에 덮으면 stepped contact surface, 부품별 독립 cold plate/thermal pedestal, 국소 compliant TIM/gap filler, spring/flexure load path 등이 설계 보상 후보가 된다. TIM을 두껍게 해 단차를 흡수하면 열저항이 증가할 수 있으므로 접촉 압력/BLT와 열성능을 함께 평가해야 한다.
- 10 mm를 실제 수직 단차로 가정한 구조 설계나 수치 모델링은 보류한다. 사용한 775 µm 값의 대상(실리콘 두께, 패키지 높이 또는 stack spec)도 확인이 필요하다.

### 다음 행동
- [ ] 동일 패키지 기준면을 표시한 GB200/V-Die 단면 또는 도면 확보.
- [ ] GPU 상면과 각 HBM stack 상면의 z-height 및 허용공차를 분리 기록.
- [ ] 실제 step을 기준으로 rigid-flat, stepped/pedestal, compliant/segmented contact 구조를 비교할지 검토.
- [ ] 측정/시뮬레이션 지표: die별 Tmax, TIM BLT/접촉 열저항, 접촉 압력 분포, warpage/응력, ΔP/펌프동력(유로 설계가 포함될 경우).
## 2026-09-30 — 범위 수정: V-Die 높이 차의 열 시뮬레이션

### 사용자 정정
- 앞서 높이 차를 HBM과 GPU 간 차이로 기록했으나, 사용자가 정정함: concern의 대상은 HBM이 아니라 GPU와 수직 배치된 V-Die다.
- 사용자는 구조·접촉력 등 기계 해석이 아니라 열 시뮬레이션을 통한 연구를 구상한다.

### 열 시뮬레이션 관점의 문제 후보 [추론]
- 수직 V-Die가 GPU보다 높게 돌출되는 형상에서 외부 콜드플레이트의 냉각 경계/유로 형상이 GPU와 V-Die의 열원별 열경로와 온도 분포를 어떻게 바꾸는가?
- 후보 설계변수: V-Die 노출면을 덮는 냉각 면적, sidewall 채널 위치·높이, GPU 상면 냉각 영역, 공통 매니폴드에서의 유량 배분 및 유로 높이.
- 후보 비교: 기준 콜드플레이트 vs V-Die 형상에 맞춘 sidewall/step-conformal flow passage. 구조 접촉응력 분석은 현 범위에서 제외한다.

### 모델링 주의
- 열원은 GPU와 V-Die를 구분해 부여하고, V-Die die별 발열이 균일하다고 가정하는 경우 그 가정을 밝힌다.
- 고체 열전도와 유체 대류를 결합하고, 콜드플레이트/패키지/TIM의 열경로를 포함할지 범위를 명시한다. 기계 해석을 제외하더라도 TIM 두께 또는 접촉 열저항은 고정 경계조건/입력값으로 둘 수 있다.
- 비교 시 입구온도, 유량 또는 펌프동력, 총 열부하, 재료물성, 기준 열저항을 동일하게 유지하고 die별 Tmax·온도편차와 ΔP를 평가한다.
- 10 mm는 사용자의 정정된 V-Die 수직 치수 설명으로 취급하되, 실제 단면 기준 및 형상은 도면/모델로 확인 전이다. 앞선 HBM 10 mm 추정은 이 V-Die concern에 적용하지 않는다.

### 다음 행동
- [ ] V-Die의 방향, GPU 대비 돌출 높이, 냉각판이 접촉/근접하는 면을 단면도로 고정한다.
- [ ] GPU/V-Die별 전력 또는 열유속, 재료와 열경계조건을 결정한다.
- [ ] 단순 fin 최적화보다 냉각 경계의 위치/커버리지와 유량 배분을 비교하는 시뮬레이션 질문을 구체화한다.
## 2026-09-30 — 콜드플레이트 상부 덮개 배치 확인

### 사용자 지정 형상
- 외부 콜드플레이트는 V-Die 옆면에 붙이는 것이 아니라 위쪽을 덮는 배치다.

### 열 시뮬레이션 의미 [추론]
- 같은 평면 바닥의 콜드플레이트가 GPU 상면과 위로 돌출된 V-Die를 어떻게 열적으로 연결하는지가 모델의 첫 질문이다.
- 평면 접촉으로 V-Die 상단만 냉각하는 경우와, V-Die 측면/주변을 유체가 지나가도록 콜드플레이트 내부 또는 하부에 유로/공간을 두는 경우는 다른 냉각 경계조건이므로 구분해야 한다.
- 초기 비교 후보: 기준 평면형 콜드플레이트 vs V-Die 형상에 맞춘 바닥 단차/공간 및 coolant passage. 목표 지표는 GPU·V-Die 최고온도와 온도 편차, 필요 시 ΔP다. 접촉응력은 분석 범위에서 제외한다.
- 775 µm와 약 10 mm의 기준면 및 방향은 여전히 확인 전이며, 이를 실제 Δh로 바로 입력하지 않는다.

### 다음 행동
- [ ] 콜드플레이트가 V-Die 측면을 감싸거나 유체가 측면을 흐르는지, 상단 edge 접촉만 하는지 도식에서 확인한다.
- [ ] 같은 package 기준으로 GPU/V-Die 높이와 열원 위치를 고정한 뒤 첫 conjugate heat-transfer model을 정의한다.
## 2026-09-30 — V-Die 측면 인접 밀폐 유로의 제작 현실성

### 자료에서 확인한 제작 방식
- OCP Cold Plate Development and Qualification 가이드는 cold plate base와 top cover 사이에 유로를 두고, 유로를 base 또는 cover에 가공한 뒤 braze, friction-stir welding, soldering 또는 O-ring으로 조립·밀봉하는 구조를 기술한다. 각 접합 방식은 압력 지지, 재료/유체 적합성, 비용, 누설 신뢰성 등의 상충이 있다.
- 근거: [OCP Cold Plate Development and Qualification](https://www.opencompute.org/documents/ocp-cold-plate-development-and-qualification-with-integrated-comments-pdf), pp. 6–9. [A: 공식 OCP 문서 직접 확인]

### V-Die 적용 아이디어 [추론]
- 현실성 있는 1차 열모델 후보는 V-Die 표면에 냉각수를 직접 접촉시키지 않고, CNC 가공된 금속 cold-plate base 안의 밀폐 유로가 V-Die 측면을 따라가도록 하고 cover로 봉합하는 방식이다.
- 이는 일반 cold plate 제작 원리를 V-Die 외형에 적용한 설계 가설이다. 동일 형상의 V-Die 제작·실험 가능성을 확인한 근거는 아직 없다.
- V-Die 사이 간극에 직접 냉각수를 넣는 구조는 별도의 package-integrated/inter-die microfluidic architecture로 분리한다. 기존 V-Die 제안 기사에는 die 사이 microfluidic 채널이 소개되어 있으므로 novelty를 단정하지 않는다.

### 시뮬레이션 문제 정의 후보
- “평면형 기준 콜드플레이트와 V-Die 측면 인접 밀폐 유로형 콜드플레이트 중 어느 설계가 같은 입구 조건 및 유압 예산에서 GPU/V-Die별 Tmax와 온도 불균일도를 더 낮추는가?”
- 모델 변수 후보: cold-plate cavity/slot 높이, sidewall 인접 유로 위치, 유로 단면, GPU 영역 유로와 V-Die 영역 유량 분배.
- 모델링은 고체 열전도와 유체 대류를 결합한다. TIM/접촉 열저항은 고정 입력으로 두고, 기계 응력/접촉력은 다루지 않는다.
- [A: OCP 제작공정 근거]와 [추론: V-Die에의 적용]을 구분한다. 측면 인접 유로의 V-Die 실현성은 제작팀/공정 접근성 확인이 필요하다.
## 2026-09-30 — 3D die 측면을 따라가는 cold plate/side-manifold 선행 개념

### 질문 / 문제 정의
- 수직 V-Die의 옆면을 감싸거나 따라가며 냉각하는 외부 cold plate가 이미 제안된 적이 있는가?

### 확인된 선행 개념
- Chukwudi Azubuike의 Binghamton University M.S. thesis (2025), *CFD Analysis of Combined Cold-Plate and Side-Manifold Cooling of 3D-Stacked Chips for Enhanced Thermal Management*는 상부 micro-finned cold plate와 칩 스택 측면의 coolant manifold를 결합한 외부 냉각 구조를 CFD로 분석한다. 초록/본문 발췌는 side manifold가 칩 옆면에 유체를 직접 접촉시켜 측면에서도 열을 제거한다고 설명한다. 따라서 “3D 적층 다이의 상부 cold plate에 sidewall coolant manifold를 추가해 측면을 냉각한다”는 넓은 개념은 이미 제안·해석된 선행 사례가 있다. [B: 학위논문 원문이 저자 업로드본으로 ResearchGate에서 확인됨; 학위논문, 저널/학회 논문 아님]
- 논문 초록은 parallel-flow 및 impinging-flow 구성, 8개 die, die당 50–150 W 조건을 보고하며 성능 개선 수치도 제시한다. 이번 답변에서는 해당 성능 수치를 독립 검증하지 않았고 연구 성과 근거로 사용하지 않는다.
- V-Die 자체도 upright DRAM die 사이의 package-integrated microfluidic channel을 제안한다는 보도가 있다. 이는 외부 cold plate의 side manifold와 다른 구조다. [B: Tom's Hardware 2차 기사]
- OCP cold-plate 가이드는 금속 base/cover 안에 유로를 가공하고 접합·밀봉하는 통상 제작 옵션을 설명한다. 이는 sealed-channel plate 제작의 일반 근거이지, V-Die에 맞춘 side-wrap 제품의 제작 검증은 아니다. [A: 공식 OCP 가이드]

### 구분과 의미
- (1) 상부 cold plate + 스택 바깥 측면에 coolant가 직접 흐르는 side manifold: 선행 thesis와 상당히 가까움.
- (2) V-Die 옆면을 따라가는 밀폐 금속 plate 내부 유로: 외부 냉각 구조의 다른 구현 가능성이나, 해당 V-Die 형상에 대한 정확한 선행 여부는 미확정.
- (3) V-Die 다이 사이 간극으로 냉각수를 보내는 inter-die microfluidics: 패키지 내부 유로이며 V-Die 제안에서 이미 제시된 축.
- 따라서 “die를 감싸는 cold plate는 선행이 없다” 또는 “side cooling 자체가 novelty”라고 주장하면 안 된다. 이 선행 사례는 사용자의 구조와 재료·형상·유체 접촉 방식이 같다는 뜻은 아니지만, 주제 범위를 좁힐 필요가 있다.

### 연구 차별점 후보 [추론]
- 기존 3D stacked-chip side-manifold CFD와 구별하려면 V-Die 특유의 GPU+upright-DRAM 3D 형상, die별 비균일 발열, 상부 덮개형 외부 plate의 유로/커버리지, 동일 펌프동력 또는 ΔP에서의 GPU/V-Die Tmax 및 온도 균일도 등을 연구 질문에 구체적으로 넣어야 한다.
- 가장 직접적인 비교는 top-only plate 대 top-plus-V-Die-sidewall cooling이며, 실제 V-Die 단면·열원 맵을 사용해야 한다. inter-die microfluidics는 별도 확장안으로 남긴다.
- 정확한 novelty 판단 전에 논문/학위논문 원문과 특허 청구항을 체계적으로 대조해야 한다.

### 근거
| 주장 또는 결과 | 출처/링크 | 근거 등급 | 원문 확인 여부 |
|---|---|---|---|
| 3D stacked chips의 상부 cold plate + 측면 side manifolds를 결합한 외부 냉각을 CFD 분석한 M.S. thesis 존재 | [Azubuike, Binghamton University thesis, 2025](https://www.researchgate.net/publication/400983203_CFD_ANALYSIS_OF_COMBINED_COLD-PLATE_AND_SIDE-MANIFOLD_COOLING_OF_3D-STACKED_CHIPS_FOR_ENHANCED_THERMAL_MANAGEMENT), DOI: 10.13140/RG.2.2.13933.65763 | [B: 저자 업로드 학위논문] | 초록·상세 발췌 확인; 기관 저장소 레코드 독립 확인은 못함 |
| V-Die proposal places microfluidic channels between adjacent upright DRAM dies | [Tom's Hardware V-Die/MOSAIC report](https://www.tomshardware.com/tech-industry/semiconductors/researchers-turn-hbm-on-its-side-to-tackle-ai-memorys-heat-wall-korean-v-die-and-japanese-mosaic-designs-promise-higher-bandwidth-denser-stacks-and-cooler-future-gpus) | [B: 2차 기사] | 기사 확인; 원 학회자료 미확인 |
| 일반 cold plate channels can be machined into base/cover and sealed using several joining options | [OCP Cold Plate Development and Qualification](https://www.opencompute.org/documents/ocp-cold-plate-development-and-qualification-with-integrated-comments-pdf) | [A: 공식 가이드] | 직접 확인 |

### 다음 행동 / 결정
- [ ] Azubuike thesis 원문에서 실제 side-manifold 단면/유체 접촉 영역과 모델 경계조건을 확인하고, 사용자의 위쪽 덮개 배치와 차이를 그림으로 대조한다.
- [ ] 해당 thesis와 V-Die 원 학회자료, 관련 특허의 청구항·구조를 비교해 연구 질문의 novelty 범위를 정한다.
- [ ] 주제 문구에서 “side cooling 신규 제안” 대신 V-Die-specific thermal design/비균일 열부하/동일 펌프동력 비교 등 검증 가능한 기여를 정의한다.

## 2026-09-30 — V-Die 바깥 둘레 측면 냉각의 유효 면적 concern

### 사용자 관찰
- V-Die 외부에 cold plate를 두고 바깥 측면만 냉각하면, 종래 hotspot 위에 유로를 배치해 열원에 직접 냉각을 집중하는 설계 이점이 줄어들 수 있다는 우려.
- 옆면이라는 방향 자체가 냉각 면적을 작게 만드는 것은 아니다. die의 넓은 면이 수직으로 노출되어 유체에 젖으면 면적은 클 수 있다. 핵심은 냉각수가 die 묶음의 바깥 면만 접하는지, die 사이의 각 넓은 면을 접하는지다.

### 해석 [추론]
- 외부 side-wrap plate가 V-Die 배열의 바깥 perimeter만 냉각하면, 내부 die의 열은 여전히 die/지지 구조를 통해 바깥으로 전달되어야 하므로 내부 die의 열경로를 짧게 만들지 못할 수 있다. 따라서 “감싸는 면적이 늘어 효율이 오른다”고 가정할 수 없다.
- 각 V-Die 사이에 유체가 흐르면 반복되는 넓은 die 면에서 직접 열을 제거할 수 있어 면적과 열원 근접성이 달라진다. 다만 이는 외부 cold plate의 개선이라기보다 패키지 내부 inter-die microfluidic 냉각이며, V-Die 제안에 이미 포함된 개념이다.
- 외부 cold plate의 열적 기여가 의미 있는지는 die별 열원 위치, 유체 접촉 면적, 냉각면까지 고체 열전도 거리/재료, interface resistance, 유량 및 ΔP를 포함한 모델로 판단해야 한다. 단순 면적만으로 효율을 결론내리지 않는다.

### 다음 행동
- [ ] 단면도에서 유체가 닿는 면을 색으로 표시하고, 외부 perimeter wetted area와 inter-die wetted area를 따로 산출한다.
- [ ] 사용자가 우려하는 배치가 바깥면 side-wrap인지, 각 die gap을 통과하는 manifold인지 도식으로 확정한다.
- [ ] 외부 side-wrap가 바깥 die에만 열적으로 접근한다면 이를 주된 개선안으로 밀지 말고, top-only baseline 대비 이득을 먼저 screening simulation으로 확인한다.
- [ ] 내부 die-gap 냉각은 별도 구조/공정 난이도와 V-Die 선행개념을 고려해 확장안으로 취급한다.

## 2026-09-30 — V-Die die-gap Cu-pillar coolant concept as ECTC candidate

### Candidate question
- Could Cu pillars placed in the coolant gaps between upright V-Die memory dies improve heat transfer enough to justify the added hydraulic resistance, compared with an empty inter-die channel?

### Relevant prior art / fact
- V-Die has already been reported with microfluidic cooling channels between adjacent upright DRAM dies. [B: Tom's Hardware 2차 보도; original VLSI paper not reviewed here]
- Intel patent US 11,515,232, *Liquid cooling through conductive interconnect*, explicitly describes coolant flowing between dies through conductive bumps, including copper bumps; the patent text also discusses bump dimensions, insulated bump surfaces for water use, manifold/filtering, and optionally separate fluid paths for the interconnect gaps and cold plate. This is close prior art for the broad “conductive Cu pillars plus inter-die coolant” concept. The V-Die orientation/application may differ, but novelty cannot rest on that broad combination. [A: patent text surfaced/read; patent claim scope/legal status analysis not performed]
- Citation: [US 11,515,232](https://patents.google.com/patent/US11515232B2/en).

### Potential thermal-fluid hypothesis [Inference]
- Cu pillars might increase wetted area and disturb/renew thermal boundary layers, improving heat removal from the die faces. They also occupy flow area and can increase pressure drop, induce flow maldistribution or particle clogging. Their thermal/electrical connection can also change heat spreading between dies; do not assume it is beneficial.
- This is package-integrated inter-die microfluidic cooling, not merely a conventional external cold-plate fin redesign.

### A testable simulation question
- “For a V-Die inter-die channel, how do Cu-pillar diameter, pitch, and arrangement affect die-level peak temperature and temperature nonuniformity at matched pumping power (or explicitly matched ΔP), relative to a pillar-free channel?”
- Keep die gap, die geometry/materials, heat map, coolant inlet condition, and total thermal load controlled. Report Tmax by die, temperature spread, ΔP, flow distribution, and pumping power. Compare at least empty-gap channel vs pillar array; optionally include a conventional microchannel baseline.
- A convincing abstract requires actual simulation/measurement results; do not draft quantitative results before they exist.

### Limitations / open questions
- Obtain the original V-Die geometry and its die-gap microfluidic description; the news article is not sufficient for exact geometry.
- Determine whether the proposed Cu pillars are thermal posts, electrical interconnects, flow turbulators, or a combination. Their bonding/contact and electrical insulation assumptions affect the thermal model.
- Check US 11,515,232 claim language and related patent families before asserting novelty or freedom to operate. This note is a novelty warning, not legal advice.
- Establish whether the ECTC contribution is a V-Die-specific design envelope/thermohydraulic optimization, an experimental TTV demonstration, or both.

## 2026-09-30 — V-Die 냉각 시나리오와 GPU cold-plate 경계

### 질문
- V-Die die-gap을 immersion-like하게 냉각할 때 GPU까지 유체에 노출할지, GPU cold plate를 별도로 유지할지, 그 형상을 어떻게 정의할지.

### 설계 시나리오 [추론]
1. **GPU와 V-Die를 함께 직접 냉각하는 공통 유체 공간**: 패키지 안의 GPU 냉각면과 V-Die 사이를 하나의 밀폐 유체 공간으로 연결한다. 전기 접점·패드·Cu pillar의 유체 적합성, 절연/패시베이션, 패키지 seal이 선결 조건이다. 물을 쓰려면 전기적 격리와 부식/누설 관리가 필요하고, dielectric coolant를 쓰면 물성/점도/열용량과 펌프 조건을 다시 설정해야 한다. [일반 열유체/패키지 추론; 재료 적합성 데이터 미확인]
2. **하이브리드 분리 냉각**: GPU에는 conventional cold plate를 유지하고, V-Die die-gap에는 별도 manifold/microfluidic loop를 둔다. 열기여도를 분리하기 쉽고 현실적인 비교 기준을 제공한다. 단, V-Die가 GPU 상면을 덮는 구조라면 GPU cold plate의 직접 접촉면이 물리적으로 가려질 수 있으므로 V-Die footprint/부착 위치를 먼저 확정해야 한다.
3. **통합형 2-zone cooler**: GPU 위에는 평면 cold-plate base, V-Die 영역에는 raised cavity/manifold와 die-gap 유로를 둔다. 두 영역은 분리된 유로 또는 제어 가능한 병렬 유로로 구성한다. 패키지에 맞춘 특수 cooler가 필요하며, 실제 형상은 단면도 없이 확정할 수 없다.

### 핵심 구조 문제
- V-Die가 GPU 열접촉면을 완전히 덮으면 “GPU cold plate는 그대로 유지”가 불가능할 수 있다. GPU의 열을 빼낼 수 있는 실제 노출 상면, 주변부, 패키지/기판 방향 열경로를 도면에서 확인해야 한다.
- V-Die die-gap을 흐르는 냉각수는 열린 immersion bath인지, die 사이에 봉합된 microchannel인지 구분한다. 두 번째는 immersion이라기보다 package-integrated direct liquid cooling이며 전기 절연 문제가 달라진다.
- 초록의 Cu pillar 비교는 먼저 냉각 경계를 고정해야 한다. 권장 1차 baseline 후보는 동일 GPU cooling boundary를 유지한 상태에서 V-Die gap의 pillar-free channel과 Cu-pillar channel을 비교하는 것이다. 다만 실제 GPU 면이 가려져 GPU 냉각경계를 구현할 수 있는지 확인 전에는 이를 확정하지 않는다.

### 다음 행동
- [ ] V-Die가 GPU 위에서 차지하는 footprint와 die attach/contact를 단면으로 고정한다.
- [ ] GPU의 열이 빠져나가는 면 및 현재 cold plate가 접촉할 수 있는 영역을 표시한다.
- [ ] V-Die 유로를 열린 dielectric-fluid cavity와 sealed microchannel 중 무엇으로 가정할지 선택한다.
- [ ] GPU/V-Die 각 열원을 독립적으로 정의하고, coolant inlet/outlet, 유로 분리/공유를 도식화한다.
- [ ] 시나리오가 고정된 뒤 Cu pillar 유무/피치/직경을 주요 인자로 하는 열·유압 비교를 설계한다.

## 2026-10-01 — 연구범위를 V-Die direct cooling으로 한정하는 선택지

### 사용자 제안
- GPU와 V-Die 전체 시스템의 냉각 아키텍처를 동시에 설계하기보다, V-Die만을 연구 대상으로 두고 die-gap direct cooling을 전제로 할지 검토.

### 권장 범위 [연구 설계 추론]
- ECTC 1차 질문은 **V-Die의 die-gap coolant passage와 Cu pillar 배열의 열-유압 성능**에 한정할 수 있다.
- GPU 콜드플레이트의 형상을 연구 변수로 포함하지 않는다. 대신 GPU가 V-Die 하부에 주는 영향을 완전히 제거하지 않고, V-Die 하부에 열유속/온도/등가 thermal-resistance 경계조건을 부여하거나 단순화한 GPU solid를 포함한다. 어떤 조건인지 초록과 모델에 명시한다.
- 직접 냉각은 “die 사이 밀폐된 inter-die microchannel/유로를 통해 유체가 die 표면에서 열을 받는 구조”로 우선 정의한다. 열린 dielectric bath immersion과 혼용하지 않는다. 직접냉각 가정만으로 단상/2상 유동 선택이 결정되지는 않는다.
- Cu pillar는 유로 내 열전달 보강 요소로 둘지, 전기 interconnect를 겸하는지 명시한다. 수계 유체를 가정할 경우 conductor와의 전기 절연/패시베이션을 모델 전제에 넣어야 한다. 이번 단계에서는 공정 실현이 검증된 사실로 취급하지 않는다.

### 질문/비교 후보
- “V-Die die-gap direct liquid cooling에서 Cu pillar의 유무·직경·피치가 기준 열원과 inlet 조건에서 die별 Tmax 및 온도 편차와 ΔP/pumping power 사이 trade-off를 어떻게 바꾸는가?”
- baseline: pillar-free inter-die channel.
- design: 동일 die gap 및 inlet/heat load에서 Cu-pillar channel. 이후 동일 펌프동력 비교를 주 분석으로 하고, 동일 유량 결과는 부가 비교로 고려.
- 지표: die별 Tmax, die-to-die temperature spread, coolant temperature rise, ΔP, pumping power, 유량 균일도.
- GPU 냉각 자체의 성능 향상이나 전체 패키지 냉각 우월성을 주장하지 않는다.

### 남은 결정
- [ ] GPU→V-Die 열경계조건을 실제 데이터 기반 heat flux, 등가 thermal resistance, 또는 단순화 GPU solid 중 선택.
- [ ] sealed inter-die channel을 실제 설계 가정으로 둘 수 있는지 V-Die 단면/공정자료 확인.
- [ ] 단상/2상 여부 및 유체를 DLC 셋업에서 구현 가능한 범위와 맞춰 결정.
- [ ] Cu pillar 기능(전기 접속/열전달/유동교란)과 절연 가정 정의.
- [ ] 원 V-Die 자료 및 US 11,515,232 선행과 구별되는 contribution을 설정.

## 2026-10-01 — V-Die 냉각 연구의 초기 설계 선택 확정

### 사용자가 정한 조건
- 연구 범위는 우선 V-Die 직접 냉각으로 한정한다. GPU cold plate 전체 설계는 우선 범위 밖이다.
- V-Die 사이 die gap도 설계/시뮬레이션 변수로 고려한다.
- Cu pillar는 전기적 interconnect가 아니라 열전달/냉각 목적의 구조로 고려한다.
- 유동은 단상으로 설정한다.

### 연구 질문 후보 [추론]
- “단상 die-gap direct cooling에서 die 간격과 비전기적 Cu pillar 형상이 die별 Tmax/온도 편차와 ΔP/펌프동력 간 trade-off를 어떻게 바꾸는가?”
- 최소 비교 후보: pillar 없는 유로 vs Cu-pillar 유로; die gap을 포함해 간격 변화에 따른 성능을 비교한다.
- 비교는 동일 inlet condition/총 발열 조건을 유지하고, 열성능은 동일 펌프동력 조건을 주 기준 후보로 둔다. 동일 유량 결과는 참고로 별도 제시할 수 있다.

### 미정된 핵심 물리 가정
- 열전달용 pillar가 die 한쪽 면에만 열적으로 접합된 fin/post인지, 서로 마주 보는 두 die를 연결하는 thermal bridge인지 미정이다.
- pillar가 유체 안에 떠 있거나 열원과 열적으로 접촉하지 않으면 고전도성 copper fin으로 해석할 수 없다. 열전달 증진 요소로 모델링하려면 die에서 pillar로 이어지는 열경로/접촉 저항을 정의해야 한다.
- pillar가 양쪽 die를 잇는 경우 열을 die 간에 전도해 분배할 수 있으므로, 단순히 “냉각핀”과 동일한 물리로 취급하지 않는다.
- 단상 유체가 물인지 다른 유체인지, 유로 밀봉/전기 절연 방식, 실제 제작 가능한 gap/pillar 치수는 미정이다. 단상 선택만으로 유체가 결정된 것은 아니다.

### 다음 행동
- [ ] pillar 접합 형태를 fin(post) 또는 inter-die thermal bridge 중 하나로 정한다.
- [ ] V-Die 기하에서 gap 및 pillar 직경/피치/배치의 현실적인 범위를 원자료·공정능력과 맞춘다.
- [ ] 단상 유체와 입구 온도/유량 또는 펌프동력 범위를 DLC 시험 셋업에 맞춰 정한다.
- [ ] Cu pillar 없는 기준안과 pillar 설계안을 conjugate heat-transfer 모델로 비교한다.

## 2026-10-01 — Cu fin의 열적·기하학적 정의 구체화

### 사용자 지정 구조
- Cu fin/pillar는 서로 마주 보는 V-Die 두 die를 연결하는 열전달 기둥이다.
- 사용자 의도상 전기 interconnect가 아니며, die 사이 간격을 잡고 기계적으로 지지하는 역할도 갖는다.
- 냉각 유체는 기둥 사이/주변 단상 유로를 흐른다.

### 열모델 의미 [해석]
- 열적으로는 양쪽 die와 접촉한 Cu thermal bridge/bridging fin으로 모델링한다. 두 die의 열이 pillar로 들어가고, pillar 표면에서 유체로 대류할 수 있다.
- 이 구조는 단순히 die 한쪽에 붙은 fin이 아니다. Cu가 양쪽 die를 열적으로 잇기 때문에 두 die 사이 열 크로스토크/열 재분배가 생길 수 있고, 방향에 따라 이득 또는 불이익이 될 수 있다.
- 기하상 pillar height는 마주 보는 die 간격과 직접 연결된다. die gap과 pillar height를 독립변수로 동시에 변화시킬 수 없다(접촉/브레이징 두께를 무시하는 1차 모델 기준). gap parametric sweep에서는 각 gap에 맞는 pillar height를 함께 바꾼다.
- 기계적 지지/간격 유지 기능은 연구 동기 및 구조 정의에 포함하되, 이번 사용자의 범위에 따라 응력·변형·좌굴 해석은 수행하지 않는다. thermal contact는 양쪽 면 접합으로 가정하거나 contact resistance를 명시한다.
- pillar가 비전기적 기능이어도 Cu는 도전성이 있으므로 전기 active region과의 간격/절연/passivation은 실제 패키지 가정으로 해결돼야 한다. 열 시뮬레이션에서는 electrical isolation을 구조 전제로 둘 수 있으나, 이를 검증된 공정으로 서술하지 않는다.

### 업데이트된 연구 질문 후보
- “단상 냉각 V-Die에서 양쪽 die를 잇는 Cu thermal-bridge fin의 높이(=die gap), 직경 및 피치가 die-level Tmax, die-to-die thermal coupling, 압력강하와 pumping power 간 trade-off를 어떻게 바꾸는가?”
- baseline은 동일 gap의 pillar-free channel. pillar design은 같은 gap을 Cu bridge로 부분 점유하며 coolant는 주변을 통과한다.
- 동일 입구 조건/총 열부하를 유지하고 동일 pumping power를 주 비교조건으로 고려한다. die별 Tmax와 온도차, coolant outlet temperature, ΔP/유량분배를 함께 보고한다.

## 2026-10-01 — V-Die 선행 논문의 냉각 범위 정정 및 초록 스토리라인

### 사용자 정정
- V-Die 아키텍처로 발표된 논문은 VLSI 2026의 한 편이며, 해당 논문이 구체적인 냉각 방식/유로/열유압 설계를 명확하게 제안한 것은 아니라는 점을 사용자가 정정했다.
- 이전 메모의 “V-Die 제안에 die 사이 microfluidic channel이 이미 포함된다”는 표현은 Tom's Hardware 등 2차 보도 설명을 바탕으로 했으며, 원 VLSI 논문 본문을 직접 확인한 결과가 아니다. 이를 확정적인 원 논문 내용처럼 일반화하지 않는다.
- 초록 문제 정의에서는 “기존 V-Die 냉각 구조를 개선한다”보다 “V-Die 열관리의 구체적인 냉각 구조/열유압 설계가 명확히 정립되지 않았다”를 후보로 둔다. 다만 이 gap 표현도 원 VLSI 논문 및 더 넓은 문헌 검토 후 확정한다.

### 잠정 초록 흐름 [추론]
1. 넓은 배경: AI 가속기용 3D memory integration은 고대역폭·고집적 구조의 열관리를 중요하게 만든다.
2. 대상 문제: 수직 V-Die 사이에서 die 냉각과 간격/유로 유지가 함께 고려되어야 한다.
3. 기존 접근: V-Die 아키텍처는 VLSI 2026에서 발표되었지만, 사용자의 확인에 따르면 구체적 cooling channel/pillar 열유압 설계는 해당 논문에서 명확히 제안되지 않았다. 원문 대조 전에는 이를 초록에서 단정하지 않는다.
4. 해결되지 않은 질문: opposing die를 잇는 비전기적 Cu thermal bridge가 열을 유체로 전달하는 효과와 유로 차단/압력강하 사이 trade-off가 V-Die 형상에서 어떻게 나타나는가.
5. 이번 연구: 단상 die-gap direct cooling에서 gap 및 Cu bridge 형상(높이=gap, 직경, 피치/배열)을 parametric CHT로 비교하고, pillar-free baseline과 동일 펌프동력 조건에서 평가.
6. 결과/의의: 실제 계산/측정 후 die별 Tmax, die 간 온도편차 및 ΔP/pump power를 수치로 채운다. 결과 전에는 효과 수치를 쓰지 않는다.
- Intel US 11,515,232에는 conductive bumps 사이 유체냉각 선행 개념이 있으므로, 넓은 “Cu interconnect + liquid between dies” 최초성은 주장하지 않는다. V-Die-specific 열-유압 설계, pillar의 비전기 thermal-bridge 기능과 matched-pumping-power 평가 범위에서 contribution을 정의한다.

### 다음 행동
- [ ] VLSI 2026 원 논문에서 cooling 관련 실제 서술·그림·가정 확인.
- [ ] 문헌/특허 선행기술을 추가 대조한 뒤 “해결되지 않은 부분” 문장을 확정.
- [ ] 초록에 넣을 결과값은 CHT/실험 완료 후 채운다.

## 2026-10-01 — ECTC 초록의 작업용 제목·스토리라인 초안

### 사용자 목표
- 초록을 무작위 문장 나열이 아니라, 연구실 기존 초록의 수사적 문장 순서와 각 문장의 기능을 분석한 뒤 같은 구조로 작성하고 싶다.
- 사용자가 향후 연구실 기존 제목/초록 예시를 보내기로 했다. 그 자료를 받으면 문장별 역할, 배경에서 gap으로 좁히는 순서, 방법·결과·의의 배치, 어조/길이를 추출한다.

### 현재 임시 스토리라인 [초안, 문헌 gap 미확정]
1. 3D memory/AI accelerator의 집적도·대역폭 증가와 열관리 필요.
2. V-Die는 DRAM die를 수직 배치해 I/O/용량 확장성을 겨냥하며, die 사이 gap의 열관리 설계가 필요.
3. 3D package liquid cooling 및 conductive-interconnect coolant 연구는 선행이 있으므로 배경에 인정.
4. V-Die에서 opposing die를 잇고 간격을 유지하는 비전기 Cu thermal bridge의 열 전달과 유압 손실 간 trade-off를 구체 문제로 둔다. 이 특정 gap claim은 VLSI 2026 원문 및 관련 선행 조사 후 확정한다.
5. 단상 inter-die cooling에서 pillar-free baseline과 Cu bridge design을 CHT로 비교, gap/height, diameter, pitch/array를 평가.
6. 결과 문장에 matched pumping power에서의 die별 Tmax/온도편차 변화 및 ΔP를 실제 수치로 삽입.
7. 얻은 설계 지침의 범위와 V-Die thermal design에 대한 의의로 마무리.

### 임시 제목
- 우선 후보: *Thermal–Hydraulic Design of Copper Thermal Bridges for Single-Phase Inter-Die Cooling in V-Die Memory*
- 이는 working title이며, 실험/시뮬레이션 범위와 결과에 따라 수정.

### 작업용 영문 초록 뼈대
Three-dimensional memory integration in AI accelerators increases the need for effective thermal management. The V-Die architecture arranges DRAM dies vertically to increase memory integration and I/O density, while creating inter-die gaps that require a defined cooling strategy. Although liquid cooling of 3D packages and coolant transport through conductive interconnects have been explored, the thermal-hydraulic role of non-electrical copper bridges connecting opposing V-Die surfaces remains to be established for this architecture. Here, we propose a single-phase inter-die cooling structure in which copper thermal bridges connect adjacent dies, define the die spacing, and provide additional heat-transfer area while coolant flows around them. A conjugate heat-transfer model is used to compare pillar-free channels with copper-bridge channels while varying the die gap, bridge diameter, and pitch under [matched pumping power / other finalized condition]. The optimized configuration [INSERT VERIFIED RESULTS: die-level Tmax/temperature spread, ΔP, pump power, and conditions]. These results [INSERT supported design insight] and provide a thermal-hydraulic design basis for cooling V-Die memory systems.

- This draft is deliberately provisional. The prior-art/gap sentence must be checked against the VLSI 2026 paper and relevant patents/papers; outcome sentence cannot be completed before actual simulation/measurement.
- User's future lab abstracts should be used to revise rhetorical structure and style; do not assume this draft's sentence order is the lab's final formula.

### 다음 행동
- [ ] 사용자가 연구실 기존 제목·초록을 보내면 문장 기능/전환/길이/어조를 분석해 reusable outline으로 정리.
- [ ] VLSI 2026 original paper and adjacent prior art checked for exact cooling disclosure.
- [ ] Define model conditions and obtain verified results before final abstract drafting.

## 2026-10-01 — 연구실 ECTC 초록 샘플 PDF 수신, 본문 확인 대기

### 요청
- 사용자가 ECTC 2024/2025/2026 초록·원고 PDF 다섯 편을 참고해 초록의 문장 구조와 연구실 writing pattern을 추출하고, 향후 재사용할 별도 Markdown guide를 만들도록 요청했다.

### 접근 상태
- 전달된 자료는 Dropbox 로컬 Windows 경로로만 제공됨.
- 현재 세션에서 해당 경로의 파일 본문을 읽을 수 없었으며, PDF 내용은 분석하지 않았다. 일반적인 초록 작성 지식을 샘플 분석 결과처럼 기록하지 않는다.
- 파일명 목록: ECTC2024_Abstract_Submitted.pdf; 나현_ECTC2025_Abstract_final_JM.pdf; ECTC2025_HJung_Manuscript.pdf; ECTC2026_Abstract_Jimin Kwon.pdf; ECTC2026_KKim_Abstract_V6_HJung.pdf.

### 다음 행동
- [ ] 사용자가 PDF를 저장소 Research/Thermal/Incoming/에 업로드하거나 채팅에 직접 첨부하면 내용을 읽고 비교한다.
- [ ] 문장별 rhetorical function, paragraph order, gap-to-contribution transition, title pattern, tense/voice, word count, result presentation을 정리한다.
- [ ] 관찰된 공통 패턴/개별 예외를 구분한 재사용 가능한 별도 Markdown guide를 생성하고 AI_HANDOFF를 갱신한다.


## 2026-10-01 — Vertically oriented die stack cooling abstract draft

### 사용자 지정 작성 조건 (Fact: user-provided)
- 본문 용어는 “V-Die” 대신 “vertically oriented die stacks / vertically oriented DRAM dies”를 사용한다.
- 초록은 대략 500–600 words를 목표로 한다.
- 모호한 주어를 피한다. AI 가속기 자체에 의도·행위를 부여하기보다, 예를 들어 processor throughput이 memory capacity/bandwidth에 의존한다고 정확히 쓴다.
- 문제 정의 전환에 “However”를 일찍 사용하고, “In this work”로 기여를 초반에 밝힌다.
- this/that 지시대명사를 최소화하고, 주어·물리적 메커니즘을 명시한다.

### 현재 모델/초록 범위 (Fact: user-provided)
- 수직 배치 DRAM die 사이를 단상 유체로 직접 냉각하는 개념.
- 비전기 Cu pillar는 마주 보는 die 표면을 연결하며, 냉각 목적의 fin/thermal bridge로 고려한다.
- 사용자는 우선 열 시뮬레이션을 통한 초록 작성을 원했고, 기계적 지지 효과의 해석은 현재 범위가 아니다.
- GPU cold plate 자체의 구조 설계는 현재 초록의 중심 범위가 아니다.

### 초록 framing (Inference; 검증되지 않은 연구 가설)
- Cu pillar는 wetted area를 늘려 die에서 fluid로의 열전달을 도울 수 있다.
- Pillar가 양쪽 die에 접촉하므로 die 간 열전도/thermal coupling도 만들 수 있다. 이것이 이득인지 손해인지는 simulation 결과로 확인해야 한다.
- 설계변수 후보: inter-die gap(기둥 높이와 연계), pillar diameter/pitch/layout, coolant flow. 평가 후보: die별 Tmax, die 간 온도차, 온도 불균일도, ΔP, pumping power.
- top-mounted cold plate는 외부 노출면을 냉각한다는 일반 설명에서 출발해, 수직 die의 opposing sidewalls 사이 냉각 경계가 별도의 설계 질문이라는 초안 논리를 구성했다. 문헌 기반 novelty/gap으로 단정하지 않는다.

### 기록한 산출물
- [Abstract writing rules](../Abstract_Writing_Rules.md) — 사용자 작성 선호를 규칙으로 정리.
- [Work-in-progress abstract](Vertically_Oriented_Die_InterDie_Cooling_Abstract_Draft.md) — 약 500–600단어 작업 초안, 실제 조건/결과 placeholder.
- [AI handoff](../../AI_HANDOFF.md) — 현재 상태와 다음 단계.

### 남은 입력
- 실제 die heat map/thermal load, geometry, gap·pillar ranges, coolant properties, inlet condition, flow/pump budget, baseline, simulation result 및 validation.
- 연구실 샘플 초록 문서별 텍스트와 파일명 대응. 사용자가 붙여넣은 원문 조각과 전체 PDF 분석 결과를 혼동하지 않는다.
- VLSI 2026 V-Die 논문 및 관련 inter-die cooling prior art를 확인한 뒤 novelty/gap 문장을 확정한다.


## 2026-10-01 — 기존 시뮬레이션 방식 확인 및 Icepak 상태

### 질문 / 문제 정의
- 사용자의 이전 Ansys 실행 workflow를 파악하고, 로컬에 실행 가능한 Icepak 열해석 모델이 있는지 확인.

### 조건과 범위
- Incoming에 업로드된 대화록과 사용자의 ECTC 2027 작업 폴더의 AEDT 파일/결과를 확인.
- Icepak 모델을 생성하거나 실행하지 않았으며 열 결과도 없음.

### 근거
| 주장 또는 결과 | 출처/링크 | 근거 등급 | 원문 확인 여부 |
|---|---|---|---|
| 업로드된 기존 시뮬레이션 대화록은 CPW gap sweep을 수행한 HFSS workflow이며, scripted AEDT build/run, 오류 로그 확인, 반복 sweep/export, CSV 및 matplotlib 후처리를 포함함 | [Incoming 대화록](Incoming/261001_기존%20시뮬레이션%20방식.txt) | [A: 사용자 제공 기록] | 전체 텍스트 확인 |
| 확인한 ECTC 2027 AEDT 결과 폴더에 HFSSDesign1.asol이 있으며, 사용자의 ECTC_abstract_형준 폴더에서는 AEDT/CAD 형상을 찾지 못함 | 로컬 Dropbox의 ECTC 2027 작업 폴더 | [A: 로컬 파일 메타데이터] | 파일명·결과 파일 확인 |
| 확인 범위 내 Icepak 해석 프로젝트는 아직 확인되지 않음; 사용자는 이전에는 전기 해석만 수행했을 가능성이 있다고 정정함 | Incoming 대화록 및 사용자 정정 | [A: 사용자 제공 기록] | 확인 |

### 성능 지표
- 적용할 수 있는 HFSS workflow 패턴: 별도 Run 폴더, 스크립트 기반 실행, 로그/산출물 감시, solver 실패 진단, CSV·그림 후처리.
- Icepak 시뮬레이션 지표/조건/결과: 미정. HFSS workflow 정보만으로 열 모델의 geometry, 재료, 열원, 유체 경계조건을 결정할 수 없음.

### 다음 작업
- V-die용 실제 geometry/CAD, die별 열부하 및 국소 I/O hotspot, 재료, 단상 유체/입구 조건, 비교 기준 구조, 유량 또는 펌프동력을 확인한 뒤 별도 Icepak Run을 구성한다.
