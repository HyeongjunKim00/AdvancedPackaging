# AI Handoff

## 현재 상태
- ECTC 연구 후보는 V-Die/GPU 패키지에서 콜드플레이트가 이종 die 접촉면의 높이 차를 수용하는 설계 문제다.
- 사용자가 GPU 775 µm, HBM 약 10 mm로 설명했으나 치수 방향/기준면이 확인되지 않았다. HBM3 규격 미러에서는 약 11 × 11 mm 평면 크기와 약 0.7 mm stack height가 별도 표기되어 10 mm는 footprint일 가능성이 크다. 실제 package top-height mismatch는 아직 미확인이다.
- 외부 cold plate가 우선안이며 die 사이 유체 냉각은 별도 확장안.

## 완료 작업
- flat cold plate가 높이가 다른 GPU/HBM 접촉면을 덮을 때 가능한 보상 구조를 정리했다: stepped contact base/pedestal, die별 분할 접촉 구조, compliant TIM/gap filler, spring/flexure load path.
- 단차를 TIM만으로 흡수하면 BLT 및 열접촉 저항이 커질 수 있어, thermal contact와 압력/warpage를 함께 평가해야 한다는 가설을 기록했다.
- 치수 혼동과 검증 항목을 [Thermal Research Log](Research/Thermal/Research_Log.md)에 반영했다. GB200 상세 접촉 치수는 확인되지 않았다.

## 미완료 작업
- GPU·HBM 상면의 동일 package 기준 z-height, 실제 단차·공차·warpage를 도면/실측으로 확인한다.
- 775 µm가 가리키는 부품 치수와 10 mm가 평면 footprint인지 수직 높이인지 확인한다.
- 실제 단차에 맞춰 rigid flat / stepped pedestal / compliant segmented contact 후보를 비교한다.
- TIM bond-line thickness, contact pressure, die별 Tmax, warpage/stress를 통합한 시뮬레이션 범위를 정의한다.
- 설계 유로를 바꾸는 경우 ΔP와 pump power도 포함한다.

## 핵심 참고자료
- [Thermal Research Log](Research/Thermal/Research_Log.md) — package-height mismatch concern과 검증 과제.
- [JEDEC JESD238A HBM3 공개 미러](https://studylib.net/doc/28550091/jesd238a-hbm3) — 평면 X/Y 및 stack Z 치수 표; 공식 JEDEC 페이지에서 직접 확인하지 않음.
- [NVIDIA DGX GB200 hardware guide](https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html) — coldplate 냉각 맥락, 세부 die 상면 치수는 미제공.
- [콜드플레이트 조사본](Research/Thermal/Incoming/2026-09-30_콜드플레이트_ChatGPT.md) — 원문 수치 검증 미완료.

## 다음 AI용 프롬프트
V-Die/GPU 콜드플레이트 문제를 GPU와 DRAM의 실제 상면 높이 차 및 기계적/열적 접촉 문제로 다뤄라. 10 mm를 HBM stack 높이라고 단정하지 마라. 먼저 동일 package 기준면에 대한 GPU/HBM z-height, footprint, tolerance, warpage를 분리해 확인하라. 이후 flat plate, stepped/pedestal base, compliant/segmented interface를 비교하고 TIM BLT·contact pressure·die별 Tmax·stress를 연결하라. 실제 도면이 없으면 연구 가설과 필요한 입력만 정리하라.