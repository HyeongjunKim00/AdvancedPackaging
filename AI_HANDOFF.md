# AI Handoff

## 현재 상태
- ECTC 후보는 GPU 위 수직 V-Die를 덮는 외부 콜드플레이트의 열성능 시뮬레이션이다. 사용자는 구조/접촉력 해석보다 열 시뮬레이션에 집중하고, 현실적인 제작 형상을 원한다.
- 중요한 신규 선행 사례: Azubuike의 Binghamton M.S. thesis (2025)는 상부 micro-finned cold plate와 3D stacked chips 측면의 coolant side-manifold를 결합한 외부 냉각을 CFD로 분석했다. 따라서 상부 plate + 측면 유체냉각의 넓은 개념 자체를 신규라고 주장할 수 없다.
- V-Die 사이 microfluidic channel은 V-Die 제안의 기존 축이다. 외부 side-manifold와 die 사이 채널을 혼동하지 않는다.
- V-Die의 실제 단면·치수·전력 맵 및 제작 제약은 미확정이다. 단상/2상, baseline 및 ECTC 문제정의도 아직 최종 선택 전이다.

## 완료 작업
- 관련 선행 냉각 개념을 세 부류로 구분했다: (1) top cold plate + 외부 side manifold, (2) V-Die 옆면을 따라가는 밀폐 금속 유로, (3) V-Die 내부 die 사이 microfluidics.
- OCP 가이드는 cold-plate base/cover에 유로를 가공하고 접합·밀봉하는 일반 제조 옵션을 제공한다. 이를 V-Die에 적용하는 것은 제조 검증된 공정이 아니라 설계 추론이다.
- 기존 Binghamton thesis는 현재 연구 아이디어와 넓게 겹치는 선행이므로 novelty 검토 우선순위를 올렸다. 출처 등급과 상세 기록은 [Thermal Research Log](Research/Thermal/Research_Log.md)에 있다.

## 미완료 작업
- Azubuike thesis 원문 그림/단면·경계조건을 V-Die의 사용자가 말한 상부 덮개 배치와 상세 비교.
- V-Die 원 학회 자료 및 관련 특허를 조사해 측면 유로 관련 선행 범위/차별점 확정.
- V-Die 단면, die별 전력지도, 높이·간격·재료 및 가공 가능한 최소 형상 확보.
- top-only baseline과 V-Die-specific 측면/상부 냉각안의 CHT 비교 문제 정의. 동일 입구 조건과 동일 유량 또는 동일 펌프동력 중 비교 기준을 선택하고 GPU/V-Die Tmax, 온도 편차, ΔP를 산출.

## 핵심 참고자료
- [Thermal Research Log](Research/Thermal/Research_Log.md) — 이번 선행 사례 검토와 이전 V-Die 논의.
- [Azubuike, CFD Analysis of Combined Cold-Plate and Side-Manifold Cooling of 3D-Stacked Chips (Binghamton M.S. thesis, 2025)](https://www.researchgate.net/publication/400983203_CFD_ANALYSIS_OF_COMBINED_COLD-PLATE_AND_SIDE-MANIFOLD_COOLING_OF_3D-STACKED_CHIPS_FOR_ENHANCED_THERMAL_MANAGEMENT) — 상부 plate+측면 manifold CFD 선행; 저널 논문 아님.
- [OCP Cold Plate Development and Qualification](https://www.opencompute.org/documents/ocp-cold-plate-development-and-qualification-with-integrated-comments-pdf) — 통상 cold plate 유로·접합 제조 옵션.
- [V-Die 및 MOSAIC 소개](https://www.tomshardware.com/tech-industry/semiconductors/researchers-turn-hbm-on-its-side-to-tackle-ai-memorys-heat-wall-korean-v-die-and-japanese-mosaic-designs-promise-higher-bandwidth-denser-stacks-and-cooler-future-gpus) — V-Die die 사이 microfluidic 소개(2차 기사).

## 다음 AI용 프롬프트
사용자는 위쪽에서 V-Die를 덮는 콜드플레이트 배치로 열 시뮬레이션 ECTC 주제를 찾고 있다. “die를 감싸거나 측면까지 냉각하는 cold plate가 있었나?”에는 예가 있다: Azubuike의 2025 Binghamton M.S. thesis가 top micro-finned cold plate + 3D-stacked chip 측면 side-manifold를 CFD로 다뤘다. 따라서 side cooling 자체를 novelty로 주장하지 말고, 원문 단면과 사용자 V-Die 배치를 비교한 뒤 V-Die-specific 형상/비균일 열원/동일 펌프동력 성능 등 좁고 검증 가능한 차별점을 찾아라. V-Die 사이 채널은 별도 package-integrated microfluidics이며 제안 구조에 이미 등장한다. Facts, source claims, inference를 구분하고 사용자 Research Log와 이 handoff를 갱신하라.