# AI Handoff

## 현재 상태
- ECTC 주제는 GPU 위 수직 V-Die를 덮는 cold plate의 열 시뮬레이션으로 탐색 중이다. 단상/2상, 구체 형상, 기준 조건은 확정되지 않았다.
- 사용자의 핵심 우려: V-Die 묶음 바깥을 side-wrap로 냉각하면 냉각 면적/열원 접근성이 충분치 않아 효과가 제한적일 수 있다.
- 핵심 구분은 냉각 방향(위/옆)이 아니라 냉각수가 바깥 perimeter만 접하는지, 각 수직 die의 넓은 면 사이를 흐르는지다.

## 완료 작업
- 상부 cold plate + 외부 side manifold 구조를 다룬 Azubuike의 Binghamton M.S. thesis (2025)를 확인했다. 따라서 상부+측면 냉각이라는 넓은 개념 자체는 선행이 있다.
- V-Die 사이 microfluidic channel은 외부 plate의 side wrap과 다른 패키지 내부 냉각 구조이며, V-Die 제안에 이미 등장한다.
- 사용자의 최근 우려를 기록했다: 외부 perimeter 냉각은 내부 die에 대한 열경로를 줄이지 못할 수 있다. side orientation 자체가 면적이 작다는 뜻은 아니며, 실제 wetted surface 및 열원까지의 열전도 경로가 결정요인이다.
- 상세 내용과 출처는 [Thermal Research Log](Research/Thermal/Research_Log.md)에 있다.

## 미완료 작업
- V-Die 단면도에서 각 대안의 실제 wetted area와 열원-냉각면 전도거리를 계산.
- 바깥 perimeter side-wrap, top-only plate, die-gap microfluidics의 냉각 경계를 구조적으로 비교.
- 실제 die별 발열지도, 재료, 열접촉/계면조건, 유량 및 ΔP 조건 확보.
- 단순 screening CHT 모델로 외부 side-wrap가 top-only보다 유의미한 개선을 주는지 판단. 결과가 미미하면 주제 방향을 재검토.

## 핵심 참고자료
- [Thermal Research Log](Research/Thermal/Research_Log.md)
- [Azubuike, Binghamton M.S. thesis (2025)](https://www.researchgate.net/publication/400983203_CFD_ANALYSIS_OF_COMBINED_COLD-PLATE_AND_SIDE-MANIFOLD_COOLING_OF_3D-STACKED_CHIPS_FOR_ENHANCED_THERMAL_MANAGEMENT) — top cold plate + side manifolds 선행.
- [OCP Cold Plate Development and Qualification](https://www.opencompute.org/documents/ocp-cold-plate-development-and-qualification-with-integrated-comments-pdf) — 일반 cold plate channel fabrication.
- [V-Die 및 MOSAIC 소개](https://www.tomshardware.com/tech-industry/semiconductors/researchers-turn-hbm-on-its-side-to-tackle-ai-memorys-heat-wall-korean-v-die-and-japanese-mosaic-designs-promise-higher-bandwidth-denser-stacks-and-cooler-future-gpus) — V-Die die 사이 microfluidic 소개(2차 보도).

## 다음 AI용 프롬프트
사용자는 V-Die 바깥을 감싸는 외부 side-cooling이 큰 효과가 없을 수 있다고 우려한다. 이 우려를 열경로 기준으로 평가하라: 바깥 perimeter만 냉각하는 경우 내부 die의 열경로를 줄이지 못할 수 있지만, 수직 die의 넓은 면 사이로 유체가 흐르면 wetted area와 열원 근접성이 커진다. 두 구조는 별개다. 단면도에서 실제 유체 접촉면과 die별 열원-냉각면 거리부터 확인하고, top-only 대비 outer side-wrap의 screening simulation 가치가 있는지 판단하라. V-Die 사이 microfluidics는 기존 제안 축이므로 novelty로 단정하지 않는다. 사실과 추론을 분리하고 Research Log와 handoff를 유지한다.