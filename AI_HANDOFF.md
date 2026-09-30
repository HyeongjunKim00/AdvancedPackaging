# AI Handoff

## 현재 상태
- ECTC 후보는 V-Die 전용 단상 die-gap direct cooling이며, Cu thermal bridge 형상을 열·유압 관점에서 평가하는 방향이다.
- 사용자는 Cu pillar가 서로 마주 보는 두 die를 열적으로 연결하고 간격을 정하며 기계적으로 지지한다고 정의했다. 전기 interconnect 용도는 아니다.
- 사용자는 V-Die 논문이 VLSI 2026에 한 편 발표되었으나, 그 논문에서 구체적인 cooling method를 명확하게 제안하지는 않았다고 정정했다. 이전의 “V-Die 논문이 die-gap microfluidic cooling을 이미 구체적으로 제안했다”는 서술은 2차 보도를 원 논문 내용처럼 일반화한 것으로 정정한다.
- 초록의 문제 후보는 구체적 V-Die cooling design의 미정립성과 Cu thermal bridge의 열전달 대 유압손실 trade-off다. 선행 문헌 점검 후에만 research gap으로 단정한다.

## 완료 작업
- 연구 범위는 V-Die-only, 단상 inter-die direct cooling으로 논의 중.
- 비교 후보: 같은 gap의 pillar-free flow channel vs opposing die를 잇는 Cu thermal bridge 배열.
- 변수 후보: gap/pillar height를 연동하고, pillar diameter, pitch, 배열을 변경한다.
- 동일 펌프동력 조건을 주 비교로 두고 die별 Tmax, die-to-die temperature spread, ΔP/pump power, 유량분배를 평가하는 스토리라인을 정리했다.
- 이전 V-Die cooling prior-art 표현에 대한 정정 및 초록 흐름을 [Thermal Research Log](Research/Thermal/Research_Log.md)에 기록했다.

## 미완료 작업
- VLSI 2026 원 논문에서 냉각에 관해 실제로 제시한 내용과 범위를 직접 확인.
- Cu thermal bridge 접촉저항/완전 접합 가정 및 유체 접촉면 정의.
- 실제 die geometry, gap, power map, 단상 유체와 DLC 운전조건 결정.
- US 11,515,232 및 관련 논문/특허를 확인해 novelty 문구 범위 설정.
- CHT 또는 실험을 수행해 초록 정량 결과 확보; 결과 전 성능 수치 쓰지 않음.

## 핵심 참고자료
- [Thermal Research Log](Research/Thermal/Research_Log.md) — 초록 논리와 정정 내역.
- [VLSI 2026 V-Die 원 논문](서지/원문 링크 아직 미확보; 다음 작업에서 확인 필요)
- [Intel US 11,515,232](https://patents.google.com/patent/US11515232B2/en) — conductive bumps 사이 냉각의 유사 선행 개념; 청구항/구조 차이 검토 필요.
- [Tom's Hardware V-Die article](https://www.tomshardware.com/tech-industry/semiconductors/researchers-turn-hbm-on-its-side-to-tackle-ai-memorys-heat-wall-korean-v-die-and-japanese-mosaic-designs-promise-higher-bandwidth-denser-stacks-and-cooler-future-gpus) — V-Die 냉각을 설명하는 2차 보도이며 원 논문 해석과 구별한다.

## 다음 AI용 프롬프트
사용자는 VLSI 2026 V-Die 논문이 한 편 있으며 구체적인 냉각 방식을 명확히 제안한 것은 아니라고 정정했다. 이전의 2차 기사 기반 설명을 원 논문의 확정 사실로 반복하지 마라. 초록 스토리라인은 AI/3D memory thermal need → V-Die 열관리 과제 → 구체적인 cooling design의 미정립성(원문 검토 후 확정) → opposing die를 잇는 비전기적 Cu thermal bridge의 열전달/유압 trade-off → 단상 die-gap CHT, pillar-free baseline 및 동일 펌프동력 비교 → 실측/계산 결과와 의의로 구성한다. Cu bridge의 gap(height), diameter, pitch/array를 설계 변수로 두되, 정량 결과는 생성하지 않는다. VLSI 원 논문과 특허 선행을 우선 확인하고 Research Log/Handoff를 유지한다.