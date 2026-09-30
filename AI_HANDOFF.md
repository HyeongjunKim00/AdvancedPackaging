# AI Handoff

## 현재 상태
- ECTC 주제는 **V-Die에 한정한 die-gap direct cooling의 열·유압 설계**로 범위를 좁히는 방향을 논의 중이다. 사용자는 GPU까지 immersion/direct cooling할지 대신 V-Die만 직접 냉각하는 가정을 고려한다.
- 제안되는 연구 시스템은 V-Die 수직 die 사이의 coolant passage와 Cu pillar 배열이다. “direct cooling”은 밀폐 inter-die 유로로 die 표면에서 냉각하는 것으로 정의할 수 있으며, 열린 bath immersion과 혼동하지 않는다.
- GPU cold plate shape는 1차 연구범위에서 제외할 수 있지만, V-Die 하부에 GPU가 주는 열영향은 하부 heat-flux/temperature/equivalent thermal-resistance 경계 또는 simplified GPU solid로 반영해야 한다.
- 직접냉각 가정은 단상/2상 선택을 자동 결정하지 않는다. 구현 가능한 유체/셋업에 따라 별도 결정해야 한다.

## 완료 작업
- GPU+V-Die 공통냉각, 분리냉각, 2-zone cooler 시나리오를 정리한 뒤 사용자 제안에 따라 V-Die-only 범위로 좁히는 것이 연구 질문을 단순화할 수 있다고 제안.
- Cu pillar-free channel을 baseline, Cu-pillar channel을 design으로 두고, 같은 geometry/inlet/heat load에서 주 비교를 동일 pumping power로 수행하는 후보를 설정.
- 핵심 지표: 각 die Tmax, die-to-die temperature spread, coolant temperature rise, ΔP/pumping power, flow distribution.
- 수계 유체와 Cu pillar를 결합할 때 전기 절연/패시베이션은 명시적 가정이며, 공정 실현 검증 사실이 아님.
- 자세한 근거와 미결정 사항은 [Thermal Research Log](Research/Thermal/Research_Log.md).

## 미완료 작업
- GPU→V-Die 하부 열경계조건을 정량화할 자료 확보 또는 단순화 방법 결정.
- V-Die 원 자료에서 die gap, coolant routing, pillar geometry/role 확인.
- 실제 DLC 셋업에 맞춰 단상/2상 및 유체 선택.
- Cu pillar가 전기 interconnect인지 thermal post/flow feature인지 구분하고 전기절연 가정 정의.
- US 11,515,232 특허 청구항과 V-Die 원 학회자료를 비교해 novelty를 좁힘.
- Simulation/measurement results가 나오기 전에는 초록의 정량 성능 주장을 작성하지 않음.

## 핵심 참고자료
- [Thermal Research Log](Research/Thermal/Research_Log.md)
- [Intel US 11,515,232](https://patents.google.com/patent/US11515232B2/en) — conductive bump/interconnect 사이 냉각 선행 개념.
- [V-Die 소개](https://www.tomshardware.com/tech-industry/semiconductors/researchers-turn-hbm-on-its-side-to-tackle-ai-memorys-heat-wall-korean-v-die-and-japanese-mosaic-designs-promise-higher-bandwidth-denser-stacks-and-cooler-future-gpus) — V-Die die-gap cooling에 관한 2차 보도.
- [OCP Cold Plate Guide](https://www.opencompute.org/documents/ocp-cold-plate-development-and-qualification-with-integrated-comments-pdf) — 일반 cold plate 참고자료; V-Die inter-die cooler와 구분.

## 다음 AI용 프롬프트
사용자가 GPU cold plate 전체 형상까지 동시에 다루지 않고 V-Die만 direct cooling하는 범위로 좁히려 한다. 이 방향을 검토할 때 GPU를 완전히 무시하지 말고 V-Die 하부에 heat-flux/temperature/equivalent-resistance boundary 또는 simplified GPU solid로 열영향을 반영하라. die-gap direct cooling은 밀폐 inter-die channel로 정의하고 open-bath immersion과 구분한다. Cu pillar-free channel과 Cu-pillar channel을 동일 열원/inlet 조건 및 matched pumping power에서 비교해 die별 Tmax, temperature spread, ΔP, pump power를 평가하는 질문을 구체화하라. Direct cooling은 단상/2상을 자동 결정하지 않으므로 actual DLC setup에 맞춰 선택한다. V-Die 원 자료와 US 11,515,232 선행을 비교하여 novelty를 신중히 다루고, 모든 연구기록과 handoff를 유지한다.