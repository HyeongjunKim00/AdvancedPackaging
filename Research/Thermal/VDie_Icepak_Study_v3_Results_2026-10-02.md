# V-die inter-die Cu-pillar cooling — Icepak 결과 요약 (2026-10-02 새벽 실행분)

> 전부 Ansys Icepak 2026.1 (PyAEDT 1.7.0) 해석 결과. 수치는 아래 **가정**에 종속됨. "추정"이라고 표시한 것은 해석값이 아니라 해석값을 선형 스케일링/외삽한 것.

## 0. 이번 세션에서 고친 것 (중요)
1. v1 실패 원인: AEDT가 자동 생성한 **공기 Region(50% 패딩)** 때문에 입·출구/대칭면이 내부면이 됨 → "face does not have mesh". Region 패딩 0 + Region 자체를 물로 지정 + gap 단면 2D sheet에 opening으로 해결.
2. v2 첫 시도: `change_region_padding`에 스칼라를 넘겨 +X만 0이 됨 → 6방향 리스트로 수정, Region bbox 자동 검증 추가.
3. **v2 9케이스 DOE(DOE_screening_v2_20261001_231759)의 pillar 케이스는 반복 상한 100에서 멈춤(미수렴) → 사용 금지.** v3부터 상한 400, 반복 수 기록 (모든 v3 케이스 ≤110회에서 수렴 기준 도달).
4. Top-side 기준 모델: Region 면 wall 및 "Temperature" source가 AEDT에서 무시됨(2619 °C, 4727 °C) → die 상단 면에 `Fixed Temperature` source + ambient 25 °C로 해결하고, 저장된 .aedt를 다시 읽어 경계 타입을 검증.

## 1. 모델과 가정
**대표구간(segment) 모델** — `RunScript/vdie_study_v3.py`
- 단위셀: [반 die A (100 µm) | gap (물, Cu pillar) | 반 die B (100 µm)], die 중심면 단열(=교대 배열 stack의 대칭), 횡방향(±Z) symmetry.
- 구간: 유동방향 2.4 mm (입구 0.6 + pillar 1.2 + 출구 0.6) × 횡 1.2 mm.
- 열부하: 모든 die 3 W/die 균일(2.48 W/cm²), **die A에만 I/O hotspot 0.3×0.3 mm, +50 W/cm²** (가정값, 실제 V-die 전력맵 아님) → die A = 활성 die, die B = 이웃 die.
- 물 25 °C 입구, 상수 물성(k 0.607, ρ 997, cp 4181, μ 8.9e-4), 정상 **층류**, 단상, Si(148)·Cu(398) 공액 열전도. Re_Dh ≤ 1,120 (gap 250 µm·2 m/s 최대) → 층류 가정 범위 내. pillar 후류의 비정상 와류는 정상 해석으로 표현 안 됨(한계).
- 출력: hotspot 최고온도, die A/B 최고·평균, ΔT_die-die(=Tmax_A − Tmax_B), Δp, 펌핑동력.
- **동일 펌핑동력 비교**: 유속 0.5/1/2 m/s 결과를 log(펌핑동력)에 대해 선형 보간(외삽 없음). 펌핑동력은 40-die stack 기준으로 환산 = 구간값 × (121/2.88) × 39 gap (모든 gap 균일 공급, 매니폴드 손실 제외 — 가정).

**전체 die 모델** — `RunScript/vdie_fullDie_baseline.py`
- 11×11 mm die, 200 µm Si, 3 W/die 균일, [반 die | gap | 반 die] 단위셀.
- Top-side: gap 정체 공기, die 상단 모서리 25 °C **이상적 등온 cold plate** (TIM/plate 저항 0 → 비교상 top-side에 가장 유리), 인터포저 쪽 단열.
- Inter-die: 빈 채널(pillar 없음), 물 0.5/1 m/s, 상단 cold plate 없음.

## 2. 검증
| 항목 | Icepak | 해석해/기준 | 차이 |
|---|---|---|---|
| Top-side Tmax 상승 (q‴H²/2k) | 50.40 K | 50.7 K | 0.6 % |
| Top-side Tavg 상승 (q‴H²/3k) | 33.60 K | 33.8 K | 0.6 % |
| Full-die inter-die Δp, 0.5 m/s (12μUL/h² + 입구) | 2.16 kPa | 1.92 kPa (완전발달분만) | 입구효과로 타당 |
| 메쉬 세분화 (78k→140k cells, d50p150 stag, 1 m/s) | hotspot 0.25 %, ΔT_die-die 1 %, Δp 0.3 % | — | 통과 |
| 메쉬 세분화 (155k→251k, 빈 채널) | 온도 <0.1 %, **Δp 8 %** | — | 빈 채널 Δp는 ±8 % 불확도로 볼 것 |

## 3. 핵심 결과

### 3.1 Top-side cold plate vs inter-die 냉각 (SK1 코멘트) — fig3, fig4
| 11×11 mm die, 3 W/die | Tmax 상승 | 펌핑동력 (39 gap) |
|---|---|---|
| Top-side 이상적 cold plate | **50.4 K** (75.4 °C) | — |
| Inter-die 물 0.5 m/s (pillar 없음) | **1.54 K** | 0.081 W |
| Inter-die 물 1.0 m/s | **1.12 K** | 0.375 W |
- 동일 3 W/die에서 die 온도 상승 **약 33× 감소** (0.5 m/s).
- 이유(물리): top-side는 200 µm 두께 Si 단면(11 mm × 0.2 mm)을 통해 11 mm를 전도해야 함 → 두께에 반비례. Inter-die는 die 면 전체가 바로 냉각수에 닿아 국부적으로 열 제거.
- **die 수 확장(fig4, 추정)**: 14.8 mm stack 길이 고정, gap 175 µm에서 die 수를 늘리면 die가 얇아짐 → top-side ΔT ∝ 1/t. 3 W/die·이상적 cold plate 기준 85 °C 한계 ≈ 43 die (t≈169 µm), 95 °C ≈ 46 die (t≈145 µm). Inter-die 냉각은 die 면에서 국부 제거라 두께 의존성이 약함 — 단, N=40에서만 해석했고 얇은 die의 hotspot 확산 악화는 미해석(추정 곡선).
- 허용 die 전력(선형, 85 °C/25 °C 입구, t=200 µm): top-side ≈ 3.6 W/die vs inter-die(0.5 m/s) ≈ 0.51 K/W → 수십 W/die 수준 (상수 물성 선형 외삽 — **추정**, 비등·물성 변화 미반영).

### 3.2 Pillar 형상 효과 — 동일 펌핑동력 (40-die stack 1 W 기준), gap 175 µm — fig1
기준: 빈 채널 hotspot 상승 1.041 K, ΔT_die-die 0.547 K, 이웃 die(B) 상승 0.494 K

| 형상 | hotspot 상승 (K) | 감소율 | ΔT_die-die (K) | 감소율 | die B 변화 (K) |
|---|---|---|---|---|---|
| d75/p150 staggered | 0.657 | **−37 %** | 0.127 | −77 % | +0.037 |
| d75/p150 in-line | 0.683 | −34 % | 0.130 | −76 % | +0.060 |
| d50/p150 staggered | 0.728 | −30 % | 0.212 | −61 % | +0.022 |
| d50/p150 in-line | 0.752 | −28 % | 0.215 | −61 % | +0.043 |
| d50/p200 staggered | 0.803 | −23 % | 0.291 | −47 % | +0.018 |
| d50/p200 in-line | 0.829 | −20 % | 0.271 | −50 % | +0.064 |
| d30/p150 in-line | 0.865 | −17 % | 0.338 | −38 % | +0.034 |
| d50/p300 in-line | 0.916 | −12 % | 0.360 | −34 % | +0.063 |

읽는 법:
- **같은 펌핑동력에서도 pillar가 이득**: 모든 pillar 형상이 hotspot을 낮춤. 면적분율(d/p)↑일수록 효과↑ (d75/p150 > d50/p150 > d50/p200 > d30/p150 ≈ d50/p300).
- **경쟁 효과 확인**: pillar가 die A→die B로 열을 전달 → die B 온도는 +0.02~0.06 K 상승, 대신 ΔT_die-die는 60–77 % 감소(열적 균일화). 초록의 "redistributing heat between adjacent dies"를 정량화하는 지표.
- **Staggered vs in-line**: 같은 d/p에서 staggered가 hotspot 2–4 %p 추가 감소, die B 상승은 더 작음. 단 staggered는 같은 유속에서 Δp가 큼(d75p150: 0.5 m/s에서 4.37 vs 2.31 kPa) — 동일 펌핑동력 비교에선 그래도 우세.
- 펌핑동력을 0.5 → 2 W로 4배 올려도 빈 채널 hotspot은 1.14 → 0.94 K로 17 %만 감소 → hotspot은 **유동보다 die 내부 확산이 지배**, 그래서 고전도 pillar가 유량 증가보다 효율적.
- ΔT_die-die는 pillar 있을 때 유속↑에 따라 약간 증가 (냉각수가 die B 쪽 열을 더 빨리 가져가 die B가 상대적으로 더 식음).

### 3.3 Gap 효과 (동일 펌핑동력 1 W)
| | gap 125 | gap 175 | gap 250 |
|---|---|---|---|
| 빈 채널 hotspot (K) | 1.005 | 1.041 | 1.085 |
| d50/p150 in-line | 0.752 | 0.752 | 0.753 |
| d75/p150 in-line | 0.729 | 0.683 | 0.641 |
- 빈 채널은 gap이 좁을수록 약간 유리(열전달계수 ∝ 1/Dh), d75 pillar는 gap이 클수록 유리(pillar가 길어져 젖음 면적↑, 같은 펌핑동력에서 유속 여유↑). d50은 gap 무관.
- d50/p150 staggered (043/044 추가): gap 125/175/250 → hotspot 0.721/0.728/0.764 K (같은 gap 빈 채널 대비 −28/−30/−30 %), ΔT_die-die −63/−61/−59 %.
- **gap 125 µm에서는 pillar 이득이 줄어듦**(d75: −27 % vs gap 250: −41 %) — pillar 높이 = gap이라 짧은 pillar의 fin 면적 감소. 설계 규칙 후보: "pillar 이득은 gap/d 비에 따라 커짐".

## 4. 한계 / 다음 단계
- I/O hotspot 크기·세기, 3 W/die는 가정. 실제 V-die 전력맵 필요. 결과는 열부하에 **선형**이라 ΔT는 부하 비례 스케일 가능(상수 물성 가정 하).
- Segment 모델은 die 전체 길이(11 mm)의 냉각수 온도 상승(0.5 m/s에서 ~0.75 K, full-die 해석에 포함됨)을 포함 안 함 → pillar 비교는 상대값으로 사용.
- 40-die 전체 매니폴드 유량 분배, 인터포저/언더필 열경로, top-side + inter-die 병용은 미해석.
- 정상 층류 가정: pillar 후류 비정상성 미반영.
- 전체 53 케이스 OK, 모두 수렴(최대 110회 < 상한 400).

## 5. 파일
- 스크립트: `RunScript/vdie_study_v3.py`, `RunScript/vdie_fullDie_baseline.py`, `RunScript/auto_runner.py`
- 원자료: `Runs/study_v3/results.csv`, `Runs/study_v3/fulldie_results.csv`, 케이스별 .aedt
- 후처리: `analyze_v3.py` → fig1 (gap별 T vs 펌핑동력), fig2 (Δp vs 유속), fig3 (top-side vs inter-die), fig4 (die 수 스케일링), `matched_pumping_power.csv`
- 재실행: PowerShell에서 `py -3.12 ...\RunScript\auto_runner.py` 실행 후 `RunScript\queue\NNN_name.request`에 한 줄(`스크립트 인자`) 넣으면 순서대로 실행. 이미 OK인 케이스는 skip.
