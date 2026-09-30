# AI Handoff

## 현재 상태
- ECTC 후보는 V-Die 패키지 열관리이며, 사용자는 Cu pillar 사이 inter-die coolant를 넣는 방향을 고려한다.
- 중요한 미결정사항: 냉각수가 GPU까지 직접 접촉하는지, V-Die만 냉각하는지, die-gap이 열린 dielectric-fluid cavity인지 밀폐 microchannel인지.
- V-Die가 GPU 상면을 덮으면 GPU cold plate의 직접 접촉면이 가릴 수 있으므로, V-Die footprint와 GPU 냉각 경계 확인이 구조 설계의 선행조건이다.

## 완료 작업
- 외부 side-wrap 단독은 내부 die의 열경로를 충분히 줄이지 못할 수 있다고 정리했다.
- Cu pillar + die 사이 coolant는 열교환면/유동 교란 개선 가능성과 ΔP·유량불균일·막힘의 trade-off로 제안했다. broad concept은 Intel US 11,515,232와 겹칠 수 있어 novelty를 넓게 주장하지 않는다.
- 냉각 시나리오 후보를 (1) GPU+V-Die 공통 직접 냉각, (2) GPU cold plate와 V-Die 내부 냉각 분리, (3) GPU flat zone과 V-Die raised manifold를 결합한 2-zone cooler로 나눴다.
- 상세는 [Thermal Research Log](Research/Thermal/Research_Log.md)에 기록.

## 미완료 작업
- 실제 V-Die-on-GPU 단면, footprint, 부착면, GPU 냉각 가능 면 확인.
- die-gap의 냉각 유체 경계가 열린 dielectric immersion인지 sealed microchannel인지 결정.
- GPU와 V-Die 각각의 열원 및 유체 공급/회수 경로를 정의.
- 위 시나리오를 고정한 뒤 pillar-free channel과 Cu-pillar channel을 동등한 펌프동력/ΔP 조건에서 비교.
- patent claims/family 및 V-Die 원 학회자료를 확인해 novelty를 좁힘.

## 핵심 참고자료
- [Thermal Research Log](Research/Thermal/Research_Log.md)
- [Intel US 11,515,232](https://patents.google.com/patent/US11515232B2/en) — conductive bumps 사이 액체 냉각 선행 개념.
- [V-Die 설명 기사](https://www.tomshardware.com/tech-industry/semiconductors/researchers-turn-hbm-on-its-side-to-tackle-ai-memorys-heat-wall-korean-v-die-and-japanese-mosaic-designs-promise-higher-bandwidth-denser-stacks-and-cooler-future-gpus) — die 사이 microfluidic cooling 2차 보도.
- [OCP Cold Plate guide](https://www.opencompute.org/documents/ocp-cold-plate-development-and-qualification-with-integrated-comments-pdf) — conventional cold plate 제작의 참고자료.

## 다음 AI용 프롬프트
다음 토론에서는 Cu pillar 형상을 정하기 전에 V-Die-on-GPU 단면의 냉각 경계를 확정하라. V-Die가 GPU 상면을 덮으면 GPU cold plate의 직접 접촉이 가려질 수 있다. 실제 노출면을 확인해 (a) GPU+V-Die 공통 직접 냉각, (b) GPU cold plate와 V-Die die-gap coolant 분리, (c) GPU flat zone + V-Die raised manifold 2-zone cooler 중 가능한 시나리오를 도식화하라. 열린 dielectric-fluid cavity와 sealed inter-die microchannel을 혼동하지 말고, 물 사용 시 전기 격리/실링 가정을 명시한다. 시나리오 고정 후에만 pillar-free 대비 Cu-pillar design의 thermal-hydraulic comparison을 정의한다. Facts/inference 분리 및 저장소 handoff/log 규칙을 따른다.