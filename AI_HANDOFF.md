# AI Handoff

## 현재 상태
- ECTC 후보는 V-Die 전용 단상 die-gap direct cooling이다.
- 사용자가 정한 Cu structure: fin/pillar가 서로 마주 보는 두 die를 열적으로 연결하며, gap을 정하고 기계적 지지도 제공한다. 전기 interconnect 용도는 아니다.
- 따라서 열모델의 적절한 이름은 한쪽 표면 fin보다 **Cu thermal bridge / bridging fin**이다. 두 die를 연결하는 고체 열전도와 pillar 주위 coolant 대류를 모두 모델링한다.
- GPU cold plate 전체 형상은 1차 범위 밖이지만, GPU→V-Die 열영향은 하부 heat-flux/temperature/equivalent resistance boundary 또는 simplified GPU solid로 남긴다.
- 기계적 지지 기능은 구조 설명에 포함하지만, 사용자는 구조응력 해석을 원하지 않는다.

## 완료 작업
- 연구 범위: V-Die die-gap 단상 direct cooling; die gap과 Cu pillar 형상을 변수로 고려.
- baseline: 같은 die gap의 pillar-free channel.
- design: Cu pillars bridging opposing die surfaces; 유체는 pillar 사이/주변을 흐름.
- gap과 pillar height는 양쪽 접촉 가정에서 기하학적으로 연결되므로 independent sweep으로 두지 않는다.
- 주요 trade-off: pillar가 die 양쪽의 열을 유체로 전달하고 유동을 교란할 수 있지만, flow area 축소/ΔP 증가/유량 불균일과 die-to-die thermal cross-talk을 일으킬 수 있다.
- 연구 질문 및 모델 해석은 [Thermal Research Log](Research/Thermal/Research_Log.md)에 추가했다.

## 미완료 작업
- Cu thermal bridge와 die 사이 접촉을 완전 접합으로 둘지, contact resistance를 적용할지 결정.
- 실제 gap/diameter/pitch/배열과 active electrical region 사이 절연 가정 확인.
- die별 power map 및 GPU 하부 열경계 확정.
- 단상 유체와 inlet temp/flow 또는 pumping power DLC 셋업 조건에 맞춤.
- US 11,515,232 및 V-Die 원 자료와 구조 차이/novelty 확인.
- 열·유압 모델 수행 및 검증계획 수립. 결과가 없으면 성능 수치 주장 금지.

## 핵심 참고자료
- [Thermal Research Log](Research/Thermal/Research_Log.md)
- [Intel US 11,515,232](https://patents.google.com/patent/US11515232B2/en) — conductive bumps 사이 냉각 선행; 사용자의 구조는 thermal bridge 중심이지만 prior art 청구항 대조 필요.
- [V-Die 소개](https://www.tomshardware.com/tech-industry/semiconductors/researchers-turn-hbm-on-its-side-to-tackle-ai-memorys-heat-wall-korean-v-die-and-japanese-mosaic-designs-promise-higher-bandwidth-denser-stacks-and-cooler-future-gpus) — V-Die die-gap cooling에 관한 2차 보도.

## 다음 AI용 프롬프트
사용자 지정 Cu fin/pillar는 opposing V-Die surfaces를 연결하는 thermal bridge이며 gap을 정하고 die를 기계적으로 지지한다. 전기 interconnect가 아니다. 다음 작업은 이를 one-sided fin이 아닌 양면 열접촉 Cu post로 모델링하고, post height를 die gap과 연동하라. 구조응력 분석은 하지 않되 thermal contact assumption을 명시한다. 동일 gap pillar-free 채널 대비, Cu bridge diameter/pitch/array에 대해 die-level Tmax, die-to-die thermal coupling, ΔP/pump power, flow uniformity를 단상 CHT로 비교할 질문을 구체화한다. Cu bridge가 양 die 사이 열을 전달해 thermal cross-talk도 만들 수 있음을 포함하고, 공정/절연은 검증되지 않은 가정으로 표시한다. 출처·추론 및 repository handoff/log 규칙을 따른다.