# AI Handoff

## 현재 상태
- ECTC 주제 후보는 GPU 위 수직 V-Die 패키지용 열관리이며, 단상/2상과 시뮬레이션/실험 범위는 미확정이다.
- 사용자가 외부 side-wrap 냉각보다 처음 제안한 “수직 die 사이 Cu pillar를 배치하고 간극으로 coolant를 흐르게 하는” 구상을 다시 고려 중이다.
- 이 구상은 V-Die inter-die microfluidic 방향과 잘 맞지만, 일반적인 Cu conductive bump 사이 액체냉각은 Intel US 11,515,232 선행 특허에 이미 나타난다. “Cu pillar + die 사이 유체” 자체를 신규성으로 주장하면 안 된다.

## 완료 작업
- 개념을 외부 cold plate fin 개선이 아닌 package-integrated inter-die microfluidic cooling으로 분류했다.
- 좁은 검증 질문을 제안했다: pillar 없는 채널 대비 Cu pillar 배열의 지름/피치/배치가 동일 펌프동력 또는 명시한 ΔP 조건에서 die별 Tmax·온도 균일성에 어떤 영향을 주는지 비교.
- 예상 trade-off는 wetted area/유동 교란으로 인한 열전달 개선 가능성과 유로 차단·압력강하·유량 불균일·막힘 위험이다. 전기/열 접촉 상태를 가정으로 명시해야 한다.
- 근거 및 한계는 [Thermal Research Log](Research/Thermal/Research_Log.md)에 추가했다.

## 미완료 작업
- V-Die 원 VLSI 자료에서 die 간격, 냉각 유로, pillar 구조/역할을 확인.
- US 11,515,232의 청구항 및 patent family를 조사하고 V-Die와의 구조 차이를 명확화.
- pillar의 기능이 interconnect, thermal post, flow disturbance 중 무엇인지 연구팀 기준을 확보.
- 실제 열원맵/기하/유체 운전 범위에 맞춰 CFD 비교 및 검증 계획을 세움.
- 결과가 확보되기 전까지 초록에 정량 결과나 성능 개선을 쓰지 않음.

## 핵심 참고자료
- [Thermal Research Log](Research/Thermal/Research_Log.md)
- [Intel US 11,515,232, Liquid cooling through conductive interconnect](https://patents.google.com/patent/US11515232B2/en) — Cu conductive bumps 사이 coolant 선행 개념.
- [V-Die 및 MOSAIC 소개](https://www.tomshardware.com/tech-industry/semiconductors/researchers-turn-hbm-on-its-side-to-tackle-ai-memorys-heat-wall-korean-v-die-and-japanese-mosaic-designs-promise-higher-bandwidth-denser-stacks-and-cooler-future-gpus) — V-Die의 die 사이 microfluidic 소개(2차 보도).
- [OCP cold plate guide](https://www.opencompute.org/documents/ocp-cold-plate-development-and-qualification-with-integrated-comments-pdf) — 외부 cold plate 일반 제작 참고; inter-die microfluidic과 구분.

## 다음 AI용 프롬프트
사용자는 V-Die 수직 die 사이 Cu pillar를 배치하고 그 사이로 유체를 흐르게 하는 아이디어로 ECTC 초록을 검토한다. 우선 Intel US 11,515,232가 conductive Cu bumps 사이 냉각수를 이미 다룬다는 점을 반영해 broad novelty를 주장하지 마라. V-Die-specific geometry, pillar geometry/role, nonuniform heat map, matched pumping power에서의 thermal-hydraulic optimization 또는 실험 TTV가 차별 기여 후보인지 살펴라. pillar가 wetted area와 mixing을 늘릴 수 있지만 ΔP, maldistribution, clogging을 악화시킬 수도 있는 가설로 취급한다. 원 VLSI 자료/치수/열원맵을 먼저 확보하고 수치 결과를 발명하지 않는다. Research Log와 handoff를 업데이트한다.