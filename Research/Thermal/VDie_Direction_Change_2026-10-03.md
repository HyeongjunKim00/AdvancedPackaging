# V-Die inter-die cooling — 방향 전환과 45 °C 결과 (2026-10-03)

> 작성: Claude (Cowork), 2026-10-03. 이전 AI 세션의 인수인계 내용 중 일부가 사용자 의도와 달라 새 세션에서 원본 결과 파일로 재검증했다. 이 문서가 10-03 기준 최신 결정이다. 상세 교훈은 [Simulation Knowledge](VDie_Simulation_Knowledge.md).

## 1. 사용자가 원하는 비교 (재확인)
- (A) 10 die를 세우고 **die 윗면에 cold plate**(TIM 포함), gap에는 유체 없음
- (B) cold plate 없이 **die 사이 gap 전체에 냉각수**, Cu pillar가 die 간격을 유지
- 이 두 구조의 냉각 성능 비교가 핵심. 다이 수 스케일링(21/47 die, 15 mm 고정 stack 가정)은 이전 AI가 임의로 넣은 것 → **폐기**. "리뷰어 SK1이 적층 한계를 요구"했다는 인수인계 문구도 근거로 쓰지 말 것.

## 2. 지도교수 코멘트 반영 — 방향 전환
- **공정 내용을 꺼낸다.** 실물(2-die 데모 수준) 제작 예정. ECTC는 데모를 선호.
- 논리: wafer-level로 die 공정 → wafer끼리 적층 → dicing → 세워서 base die에 실장. die 사이를 띄울 **구조체(Cu pillar bump)가 공정상 필요**하고, 그 gap을 냉각에 활용한다.
  - 정확한 표현: pillar가 없으면 die 면이 맞붙어 **냉각수가 들어갈 공간이 없고 윗면 모서리로만 방열**된다. ("HBM처럼 직렬 열저항이 쌓인다"는 부정확 — 맞붙어도 각 die 열은 위로 빠짐.)
- **pillar는 고정**(지지에 필요한 최소한, 단순 matrix 배열). pillar 지름·높이·배치 최적화는 이번 초록에서 제외 → 차년도 과제(배치 최적화, die 간 신호 라우팅 겸용).
- 대신 스윕할 변수:
  1. 냉각수 종류: water vs 유기계 dielectric coolant(공개 물성 있는 것, 예: HFE 계열 — 제품명 미확인)
  2. 유량/유속
  3. passivation 재료(AlN vs Al₂O₃)와 두께 — 냉각수 침투 깊이가 최소 두께를 정하고, 두께가 열저항을 늘리는 trade-off. 침투는 MD 시뮬레이션 영역이라 Ansys 범위 밖(초록에는 계획으로만).
- 구조: die 면은 passivation, **Cu pillar는 passivation 안 함**(passivation 위에 Cu 성장). pillar는 **이웃 wafer 뒷면**에 본딩.
- PR을 passivation 대신 남기는 안은 기각(adhesion 약해 유동에 씻겨 나감, 유기 냉각수에 용해 가능).
- Figure: (a) V-die + inter-die direct liquid cooling 개념 schematic + 러프한 시뮬레이션. 3D 그림이면 gap zoom-in.

## 3. pillar 형상 후보
- 사용자 공정 가능 범위: 직경 최소 50 µm, 높이 ~30 µm (더 높일 수 있음).
- 검토안: **높이 100 µm × 직경 100 µm** (AR 1:1). 문헌상 전해도금 Cu pillar 높이 >100 µm, AR 최대 6:1 시연 [B: IMAPS 논문 요약, 원문 PDF 부분 확인] — 공정상 무리 없음. 상용 AR 1:1~2:1.
- 실제 과제: 두꺼운 PR(110–120 µm), wafer 내 높이 균일도(CD 5 % → 높이 10 % 변동 보고) → 평탄화 필요 가능, 뒷면 본딩 방식(솔더 캡 시 gap 증가).
- 유체 영향 [추론, 평행평판 층류]: Δp ∝ 1/gap² (같은 유속). gap 30 µm면 175 µm 대비 ~34배, 100 µm면 ~3배. 좁은 gap은 h ≈ k/gap으로 열전달은 유리.
- 미정: pitch(지지 최소 개수; 1 mm pitch면 die당 ~100개 수준).
- 출처: https://imapsource.org/api/v1/articles/56281-advanced-lithography-and-electroplating-approach-to-form-high-aspect-ratio-copper-pillars.pdf

## 4. 결과 (10 die, 1.5 W/die, PHY 띠 20 %, Si 물성 상수)
| 케이스 | 냉각수/기준 온도 | Tmax (°C) | Δp (Pa) | 펌핑 (W) |
|---|---|---|---|---|
| (A) cold plate + TIM, h 4,000 | 25 °C | 151.5 | – | – |
| (A) h 30,000 | 25 °C | 69.9 | – | – |
| (A) h 4,000 | **45 °C** | 171.5 | – | – |
| (A) h 30,000 | **45 °C** | 89.9 | – | – |
| (B) gap 175 µm, pillar 없음, 0.5 m/s (1/2) | 25 °C | 26.82 | 2,073 | 0.018 |
| (B) gap 175 µm, 전체 높이 pillar Ø150/p300, 0.5 m/s (1/2) | 25 °C | 26.25 | 15,618 | 0.135 |
| (B) pillar 없음, 1.37 m/s (펌핑 맞춤 시도) | 25 °C | 26.31 | 6,547 | 0.155 |
| (B) gap 175 µm, pillar 없음, 0.5 m/s (1/2) | **45 °C** | 46.78 | 1,448 | 0.013 |
| (B) gap 175 µm, 전체 높이 pillar Ø150/p300, 0.5 m/s (1/2) | **45 °C** | 46.24 | 13,110 | 0.114 |
- 45 °C (A)는 25 °C 대비 정확히 +20 K → 모델 선형성 확인 [시뮬레이션].
- **펌핑동력을 맞추면 pillar의 열적 이득은 거의 없음**(0.06 K). "pillar가 피크 상승 30 % 저감"은 같은 유속 기준일 때만 성립. → pillar는 냉각 소자가 아니라 **지지·gap 유지 구조체**로 서술.
- 45 °C 근거: **ASHRAE TC9.9 W45** 액체냉각 등급(시설 공급수 ≤45 °C). JEDEC 아님. [B]
- (A)는 불리하게 잡힌 가정이 있음: h = 4,000은 낮은 편(상용 microchannel cold plate 바닥면 등가 h ~10⁴–10⁵ [추론, 원문 미확인]), cold plate가 stack footprint로 잘려 열 퍼짐 없음. 반대로 Si k 상수(148 W/mK)는 고온에서 (A)를 낙관적으로 만든다. (A) 비교 기준은 h 30,000을 주 케이스로 두는 방안 검토 중.

## 5. B가 이기는 물리 (초록 핵심 메시지)
- gap 안 h(~10⁴)는 좋은 cold plate와 비슷하다. 차이는 **냉각 면적**: (A) stack 윗면 ~39 mm² vs (B) die 양면 10×2×121 mm² ≈ 2,400 mm² (~60배) [추론, 형상 계산].
- 이전 인수인계의 "완전발달 층류라 h가 유속에 둔감"은 틀림: 열적 입구길이 ≈ 0.05·Re·Pr·D_h ≈ 21 mm > 채널 11 mm → 전 구간 열적 발달 중.

## 6. 초록 인트로 문장 (사용자와 합의한 방향, 미확정)
- "investigate" 대신 **propose**.
- V-die 약점 서술: 수직 die는 HBM의 직렬 열저항을 피하지만, 열이 die 높이 전체를 이동해 **좁은 윗면 모서리로만** 빠져나간다.
- 제안 문장 초안: "In this work, we propose an inter-die direct liquid cooling architecture for V-die stacks, in which coolant flows through the gaps maintained by Cu pillars between adjacent dies, expanding the wetted area from the narrow top edges to the entire die faces."
- pillar를 "microchannel을 형성한다"고 쓰지 말 것(유로는 gap이고 pillar는 그 안의 기둥).
- 공정 문단 초안(wafer-level passivation → Cu pillar 전해도금 → wafer 적층·본딩 → dicing → 수직 실장) 작성 중.

## 7. 다음 작업
1. 새 기준 형상 확정: gap = pillar 높이(100 µm 후보), pillar Ø, pitch.
2. 새 형상으로 (A) vs (B) 재계산, 45 °C 기준.
3. 냉각수(water vs 유기계) × 유량 스윕, passivation 층을 박막 열저항으로 포함.
4. 초록 공정 문단·결과 문단 작성.

## 8. 추가 결과 (2026-10-04): 20 die, gap 100 µm, 45 °C, 스크립트 v7e
| 케이스 | Tmax (°C) | 상승 (K) | Δp (Pa) | 펌핑 (W) |
|---|---|---|---|---|
| (A) cold plate + TIM, h 4,000 | 190.9 | 145.9 | – | – |
| (A) h 30,000 | AEDT 일시 오류로 2회 실패, 재실행 필요 | | | |
| (B) pillar 없음, 0.5 m/s (1/2) | 46.92 | 1.92 | 3,700 | 0.039 |
| (B) Cu pillar Ø100/p500 정사각, gap당 440개(20열, 입·출구 0.7 mm 비움), 0.5 m/s (1/2) | 46.84 | 1.84 | 4,650 | 0.049 |
- (A)가 10 die/gap 175 µm(171.5 °C)보다 높은 이유: die가 촘촘해져 윗면 열유속 증가(손계산과 일치). die당 전력 고정이면 die 수만 늘려서는 (A) Tmax가 거의 안 변함 → 고정 footprint 밀도(pitch) 스윕이 핵심.
- 성긴 pillar(p500)는 온도 −4 %, Δp +26 % → spacer 서술과 일치.
- v7e 옵션: `--gap`, `--square`, pillar 열 유동방향 중앙 정렬(입·출구 `--yinset` 이상 비움).
- 다음: 사용자 CAD(22열, gap당 484개 = `--yinset 0.2`)로 별도 프로젝트 폴더(CAD/RunScript/Runs/Results/Documents)에서 재계산 예정.
