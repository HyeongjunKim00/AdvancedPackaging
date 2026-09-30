# AI Handoff

## 현재 상태
- ECTC 후보는 V-Die에 한정한 단상 die-gap direct cooling이다.
- 사용자가 정한 조건: die 간격도 설계변수에 포함, Cu pillar는 전기 interconnect가 아닌 열전달 목적, 단상 유동.
- GPU cold plate 전체 형상은 1차 범위 밖이지만 GPU→V-Die 하부의 열영향은 적절한 경계조건/간략 모델로 반영한다.
- 가장 중요한 미결정: 열전달 Cu pillar가 한쪽 die에 열적으로 접합된 fin/post인지, 양쪽 die를 잇는 thermal bridge인지.

## 완료 작업
- 잠정 질문: die gap 및 Cu pillar 형상이 die별 Tmax/온도 불균일도와 유압 손실 간 trade-off에 미치는 영향.
- baseline은 pillar-free inter-die channel, design은 비전기적 thermal Cu-pillar channel로 설정하는 후보.
- 동일 총 발열/inlet 조건에서 동일 펌프동력 비교가 핵심 후보이며 ΔP/유량·온도 지표를 함께 기록한다.
- 기록: [Thermal Research Log](Research/Thermal/Research_Log.md).

## 미완료 작업
- pillar의 열 접합 방식과 접촉 열저항 결정.
- V-Die 실제 die gap, die 형상, pillar diameter/pitch 범위 및 발열 지도 확인.
- 단상 유체 종류, inlet condition, 가용 펌프동력/유량을 실험 셋업 기준으로 결정.
- GPU 하부 열경계조건을 정하고 CHT 모델 범위를 확정.
- US 11,515,232 및 V-Die 원 자료를 대조해 novelty를 좁힘.

## 핵심 참고자료
- [Thermal Research Log](Research/Thermal/Research_Log.md)
- [Intel US 11,515,232](https://patents.google.com/patent/US11515232B2/en) — conductive bump 사이 유체냉각 선행. 사용자의 Cu pillar는 전기 interconnect가 아닌 thermal feature라고 구별하되, claims 검토는 필요.
- [V-Die 소개](https://www.tomshardware.com/tech-industry/semiconductors/researchers-turn-hbm-on-its-side-to-tackle-ai-memorys-heat-wall-korean-v-die-and-japanese-mosaic-designs-promise-higher-bandwidth-denser-stacks-and-cooler-future-gpus) — V-Die die-gap cooling에 관한 2차 보도.
- [OCP Cold Plate Guide](https://www.opencompute.org/documents/ocp-cold-plate-development-and-qualification-with-integrated-comments-pdf) — 일반 cold plate 참고; V-Die inter-die flow와는 구별.

## 다음 AI용 프롬프트
사용자가 확정한 초기 조건은 V-Die-only direct cooling, die gap을 설계변수로 포함, Cu pillar는 전기 interconnect가 아닌 열전달용, 단상 유동이다. 먼저 Cu pillar가 한쪽 die에 접합된 fin/post인지 양쪽 die를 잇는 thermal bridge인지 결정하도록 돕고, 이 물리 정의를 모델링 전에 고정하라. Pillar-free 유로와 Cu-pillar 유로를 비교하고, gap/diameter/pitch 설계가 Tmax·die-to-die temperature spread와 ΔP/pumping power에 미치는 영향을 평가하는 질문을 구체화한다. 단상 유체/경계조건은 DLC 셋업에 맞춰 확인하고, GPU는 완전히 무시하지 말고 V-Die 하부 열경계로 반영한다. 출처·추론을 분리하고 로그 및 handoff를 갱신한다.