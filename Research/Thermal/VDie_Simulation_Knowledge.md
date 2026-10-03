# V-Die Inter-Die Cooling — 논의·결정·교훈 정리 (AI 참고용)

> 목적: 다음 AI가 이 문서만 읽고 V-Die Cu pillar 냉각 연구의 **의도, 결정, 근거, 실패 교훈**을 이어받게 한다.
> 결과 수치의 상세는 [study v3 결과](VDie_Icepak_Study_v3_Results_2026-10-02.md), [10-die 결과](VDie_10Die_Stack_Results_2026-10-02.md)에 있다. 이 문서는 "왜 그렇게 했는가"를 남긴다.
> **2026-10-03 방향 전환: 먼저 [10-03 방향 전환 문서](VDie_Direction_Change_2026-10-03.md)를 읽을 것.** pillar는 고정된 지지 구조체, 스윕 변수는 냉각수·유량·passivation. 아래 1절의 "pillar = fin/bridge, trade-off 정량화가 기여"는 10-02까지의 관점이다.
> 최종 갱신: 2026-10-03 (Claude, Cowork 세션). 새 논의가 생기면 이 문서를 **덮어쓰지 말고 해당 절을 갱신**하고, 날짜를 남긴다.

---

## 1. 연구 의도 (사용자가 원하는 구조)

- 수직으로 세운 DRAM die stack(V-Die) 사이의 좁은 gap에 **단상 물을 직접 흘려** 냉각한다.
- gap에는 **전기적으로 쓰지 않는 Cu pillar**가 마주 보는 두 die 면을 잇는다. pillar의 역할은 두 가지다.
  1. 젖음 면적을 늘리는 fin (die → pillar → 냉각수)
  2. die 사이 열전도 bridge (die → pillar → 이웃 die)
- 두 역할이 경쟁한다: hotspot은 낮아지지만 이웃 die가 데워지고, 유동 저항이 늘어난다. **이 trade-off의 정량화가 연구 기여**다.
- 범위 밖: GPU, 상부 cold plate 설계 최적화, 기계적 응력/지지 효과(해석하지 않았으므로 주장 금지).

## 2. 사용자 결정 기록 (변경 시 여기 갱신)

| 날짜 | 결정 | 이유/맥락 |
|---|---|---|
| 10-01 | die 11×11×0.2 mm, gap 175 µm(125–250 스윕), 3 W/die, 물 25 °C | 사용자 입력. 3 W/die는 확정값이 아니라 첫 모델 기준 |
| 10-01 | GPU 제외, Si 인터포저 포함 | V-Die 자체 열특성만 본다 |
| 10-02 | **연구는 시뮬레이션만** (공정 내용 미포함) | 리뷰어 SK1 코멘트: 실험이면 공정(전해도금, passivation), 시뮬레이션이면 top-side 대비 저감 효과·적층 한계·유동 physics(층류 등)를 써야 함 |
| 10-02 | I/O hotspot은 **die 하단 가장자리, 활성/비활성 die 교대** | 실제 V-Die I/O 위치. ΔT_die-die를 보기 위해 교대 배치 |
| 10-02 | 전체 stack 해석은 **40장 → 10장으로 축소** | 40장은 메쉬 제어 불가 + AEDT 크래시 (5절) |
| 10-02 | **top-side cold plate 케이스는 gap에 유체 없음** | 사용자: "cold plate로 direct cooling하는 구조에선 유체가 들어갈 필요 없음" |
| 10-02 | pillar는 stack 전체에서 **I/O hotspot 주변 1.2×1.2 mm에만** | 전면 pillar(gap당 ~5,300개)는 AEDT로 불가. 1/4·1/2 대칭 모델은 대칭이 성립하지 않아 기각 (4절) |
| 10-02 | **최종 비교는 2구조**: (A) die 위 cold plate + **TIM 포함**(gap 유체 없음), (B) die 사이 Cu pillar direct cooling | 사용자: die 윗면 25 °C 고정은 TIM 병목을 무시해 비현실적 → 폐기 |
| 10-02 | I/O 열원은 **die 하단 가장자리 전체 폭의 PHY 띠**(높이 0.5 mm), pillar도 이 띠를 따라 배치 | 사용자: PHY는 하단에 고르게 있어야 함. 중앙 0.3 mm 점 hotspot은 물리적으로 부적절 → 폐기 |
| 10-02 | 모든 die 동일 열부하 → 적층방향 **1/2 대칭 모델 허용** | pillar 개수(10-die 전체 ~2,300개, 7.5M cells) 부담 |
| 10-02 | 열부하 근거: DRAM die 1.2 W + I/O 0.3 W = 1.5 W/die (UCLA j84의 HBM 8-high 12 W: die 1.2 W, buffer 2.4 W를 die별 I/O로 분배, PHY 비율 20 %) | 50 W/cm² 임의 hotspot 폐기 |
| 10-02 | TIM: 20 W/mK, 75 µm (IEEE HIR 2023 Ch.20, 0.0375 K·cm²/W). cold plate: 등가 HTC 4,000 W/m²K(arXiv 2503.04049, 강제 액체대류) 기본, 30,000은 민감도 | 출처 있는 값 우선, 낙관값은 민감도로만 |
| 10-02 | 깃헙에는 **AI가 배울 수 있는 정리 문서(md) 중심**으로 올린다 | 결과 파일·그림·스크립트를 무작위로 올리는 것은 사용자 의도가 아님 |
| 10-03 | 다이 수 스케일링(21/47 die, 15 mm 고정 stack) **폐기** | 이전 AI가 임의 추가. 시뮬과 전제도 불일치(t=0.2 mm vs 1.325 mm) |
| 10-03 | 냉각수·cold plate 기준 온도 **45 °C** | ASHRAE W45(JEDEC 아님). 스크립트 v7d `--tin 45` |
| 10-03 | **공정 내용 포함, 실물 데모 예정** (10-02 "시뮬레이션만" 결정 번복) | 지도교수 코멘트 |
| 10-03 | pillar **고정**(최소 지지, matrix), 최적화 제외. 스윕은 냉각수 종류·유량·passivation 재료/두께 | 지도교수 코멘트. die 면 passivation, pillar는 미passivation, 이웃 wafer 뒷면에 본딩 |
| 10-03 | pillar 후보 높이 100 µm × Ø100 µm (공정 가능 최소 Ø50 µm) | 미확정. gap = pillar 높이 |

## 3. 확인된 결론 (근거 등급 포함)

| 결론 | 근거 | 신뢰도 |
|---|---|---|
| top-side 냉각은 die 높이방향 전도가 병목: ΔTmax ≈ q‴H²/2k ≈ 50 K (3 W, 200 µm) | Icepak 50.4 K vs 해석해 50.7 K | 높음 (해석해 검증) |
| die 사이 수냉 0.5 m/s: 1.5 K(단위셀) / 3.0 K(10-die, 끝단 die 포함) | Icepak, Δp 해석해와 일치 | 높음 |
| 동일 펌핑동력에서 pillar 이득: d75/p150 staggered → hotspot −37 %, ΔT_die-die −77 % | 대표구간 53케이스, 메쉬 독립성 확인 | 중간 (hotspot 크기·세기 가정) |
| 유량 4배 증가만으로는 hotspot −17 % → hotspot은 Si 내부 확산이 지배 | 대표구간 | 중간 |
| pillar는 이웃 die를 데운다 (+0.02~0.16 K) | 대표구간 + 10-die | 높음 (경향) |
| 10-die stack Tmax는 **한쪽만 냉각되는 끝단 die**가 결정, pillar로 안 바뀜 | 10-die | 높음 (경향), 외측 냉각은 미해석 |
| top-side는 14.8 mm stack에서 ~43장부터 85 °C 초과 | 1D 해석식, N=40에서만 검증 | 낮음 (외삽, "추정" 표기 필수) |


## 3.5 v7 결과 (2026-10-02 저녁, 1.5 W/die, PHY 띠, 10-die / 1/2 대칭)
| 구조 | Tmax (°C) | 비고 |
|---|---|---|
| (A) cold plate + TIM, h = 4,000 W/m²K | 151.5 | cold plate 대류가 지배(약 95 K). h는 일반 강제 액체대류 문헌값 |
| (A') cold plate + TIM, h = 30,000 W/m²K | 69.9 | 고성능 microchannel cold plate 가정(민감도) |
| (B0) die 사이 수냉, pillar 없음 (1/2) | 26.8 | Δp 1,952 Pa — 전체 10-die와 동일 → 1/2 대칭 검증 |
| (B) die 사이 수냉, PHY 띠 Cu pillar (1/2) | 27.2 | Δp 2,045 Pa (+4.8 %), **PHY 온도 상승 오히려 +26 %** |

- **교훈 1:** pillar가 velocity inlet 면에 붙어 있으면(0.04 mm) 유동이 전혀 안 풀림(Δp = 0, 수백 °C). 입·출구에서 pillar-free 구간(0.6 mm)을 둘 것.
- **교훈 2 (물리, 가설):** gap 높이 11 mm 중 하단 0.6 mm에만 pillar 띠를 두면, 저항이 큰 pillar 영역을 피해 냉각수가 위쪽 빈 공간으로 **우회(bypass)** → PHY 근처 유속 감소 → 오히려 뜨거워짐. 대표구간(단위셀) 모델은 pillar가 단면 전체를 채워 우회가 불가능했기 때문에 이득이 나왔음. 모든 die 동일 발열이라 pillar의 die 간 열전달 효과도 없음. → pillar는 **단면 전체 배치 또는 유동 가이드(유로를 PHY 쪽으로 몰기)** 가 필요. 유속장 확인 필요.

## 3.6 v7c/v7d 결과 (2026-10-03)
- 상세 표는 [10-03 문서](VDie_Direction_Change_2026-10-03.md) 4절. 핵심: 같은 유속에서 전체 높이 pillar는 피크 상승 −31 %이지만 Δp 7.5배; **펌핑동력을 맞춘 빈 채널(1.37 m/s)과 차이 0.06 K** → pillar 열적 이득 주장 금지.
- 45 °C (A): 171.5 / 89.9 °C (h 4,000 / 30,000), 25 °C 대비 정확히 +20 K.
- 3.5절의 v7b(PHY 띠 pillar) 결과는 bypass로 무효 처리.

## 4. 하지 말아야 할 주장 / 초록 표현 교정
- (10-03) "pillar가 냉각 성능을 높인다" → 펌핑동력 기준으로 근거 없음. pillar = 지지·gap 유지.
- (10-03) "pillar가 microchannel을 형성" → 부정확. 유로는 die 사이 gap.
- (10-03) "완전발달 층류라 h가 유속에 둔감" → 틀림(열적 입구길이 ~21 mm > 11 mm).
- (10-03) "구조체 없으면 HBM처럼 직렬 열저항 누적" → 부정확. 문제는 냉각수 접근 불가(윗면 모서리로만 방열).
- (10-03) "45 °C는 JEDEC 표준" → 틀림. ASHRAE W45.

- "coolant/pillar가 thermal crosstalk을 줄인다" → **틀림**. 이웃 die를 가장 잘 분리하는 것은 pillar 없는 gap. 올바른 표현: 냉각수가 열적 접지 역할, pillar는 약간의 die 간 결합을 대가로 hotspot을 낮추고 온도를 균일화.
- "40-die stack을 해석했다" → 금지. 40-die는 메쉬가 gap을 해상하지 못해 유동 결과가 무효. 유효한 전체 stack 해석은 10-die.
- "pillar를 die 전면에 깔았을 때 stack 결과" → 없음. 전면 pillar 효과는 대표구간 모델 결과로만 말한다.
- I/O hotspot(0.3×0.3 mm, +50 W/cm²)과 3 W/die는 **가정값**임을 항상 표기.
- 1/4, 1/2 대칭 모델 제안 시 주의: 유동방향(입·출구), 높이방향(인터포저/hotspot vs 상단), 적층방향(짝수 die + 교대 배치) 모두 대칭이 깨진다. 적층방향 1/2은 배치를 …I A | A I…로 바꿔야만 가능.
- 절대 온도 상승이 ~1–3 K로 작다(3 W/die). 초록에는 %·K/W·top-side 대비 비율로 표현. 모델은 열부하에 선형(상수 물성).

## 5. Icepak/PyAEDT 교훈 (재발 방지)

실패 → 원인 → 해결 순서. 모두 AEDT 2026.1, PyAEDT 1.7.0에서 확인.

1. **입·출구 면에 mesh 없음 → Populate Solver Input에서 Engine Detected Error**
   원인: AEDT가 공기 Region(50 % 패딩)을 자동 생성 → 물 박스 면이 내부면이 됨.
   해결: Region 패딩 0, Region 재료 = Water, 입·출구는 gap 단면 2D sheet에 opening.
2. `change_region_padding("0", ...)`은 **+X만** 바꾼다 → 6방향 리스트로 넘기고 bbox 검증.
3. **기본 반복 상한 100** → pillar 케이스 미수렴인데 결과는 나옴. 상한 400–500으로 올리고 `.SOV` 파일명에서 반복 수를 기록해 수렴 여부 판정.
4. top-side 등온 경계: Region 면 wall은 고체 die 면에 적용 안 됨(2,600 °C). `assign_source(..., "Temperature")`는 0 W Total Power로 **조용히 저장**됨. → `thermal_condition="Fixed Temperature"` + ambient 25 °C, 그리고 **저장된 .aedt를 다시 읽어 경계 타입 검증**.
5. **Multi-level meshing(MLM)** 이 얇은 gap을 3셀로 거칠게 만들어 Δp를 1/3로 과소예측. MaxElementSize·MinElementsInGap을 바꿔도 셀 수가 동일했다. → 수동 global mesh에서 `EnableMLM=False`, x 25 µm(gap 7셀).
6. 메쉬 영역 두 개가 부분 교차하면 검증 오류. 객체 수백 개를 한 mesh region에 넣으면 AEDT 연결 끊김. 모델 박스를 refinement 용도로 넣으면 die와 intersect 오류.
   → hotspot + **pillar 패치의 극단 pillar 몇 개만** 묶은 단일 local region(수동 25 µm).
7. pillar 케이스 solver 크래시("execution error on server") → `MaxSizeRatio=2`로 셀 크기 전이를 완만하게.
8. 실패 원인이 로그에 없을 때: 실패 직후 같은 세션에서 `odesktop.GetMessages(project, design, sev)`를 파일로 저장. 프로젝트를 다시 열면 메시지가 비어 있다.
9. (10-03) **Windows MAX_PATH 260자**: 케이스 폴더명이 길면 solver가 `grid_output` 복사에 실패("path not found"). 폴더명을 짧게.
10. (10-03) pillar가 단면 일부(하단 띠)에만 있으면 유동이 빈 공간으로 bypass → 오히려 뜨거워짐. pillar는 단면 전체에.
11. 검증 기준선: 빈 채널 Δp는 평행평판 층류 12μUL/h² + 입구효과와 비교, top-side는 q‴H²/2k와 비교. 이 두 검증 없이 결과를 쓰지 않는다.

## 6. 작업 환경 교훈

- 실행은 사용자 Windows PC(Ansys 설치, 라이선스 4코어)에서 `RunScript/auto_runner.py`가 `RunScript/queue/*.request`(한 줄: `스크립트 인자`)를 순서대로 실행. 같은 이름 케이스는 `_rN` 폴더로 새로 만든다(기존 프로젝트 재오픈 시 객체 중복).
- 실행기는 한 번 훑을 때 요청 목록을 고정한다 → 우선순위를 바꾸려면 아직 안 돌린 요청 파일의 **내용**을 바꾼다.
- PC 절전 시 실행·연결 모두 끊김. GUI 모드 AEDT는 대형 모델에서 크래시 대화상자로 멈춤 → `non_graphical=True` 권장, 대화상자는 사용자에게 Cancel 요청.
- **Linux 샌드박스에서 사용자 git 레포에 git 명령 금지**: 삭제 불가한 `.git/index.lock`을 남겨 사용자 git을 막는다. git 작업은 Windows 쪽 스크립트로.
- 파일 전송 후 원격 파일이 갱신되지 않은 사례가 있었다 → 수정본은 새 파일명으로 보내고 `grep`으로 내용 확인 후 실행.
- 하드웨어보다 **라이선스 코어 수(기본 4코어)** 가 병목. RAM 경험칙 ~1.5–2 GB/백만 셀.

## 6.5 열린 설계 질문 (논의 예정)
- **밀봉 높이**: die 하단(I/O 범프, 언더필)이 밀봉되면 냉각수가 PHY 띠에 직접 닿지 못한다 → pillar 위치·효과가 달라짐. 현재 모델은 gap이 인터포저 면까지 열려 있다고 가정.
- **입·출구/매니폴드**: 현재는 모든 gap 균일 유입(이상적 매니폴드). 분배통로(plenum)는 관 하나의 유량을 모든 gap에 고르게 나누는 공간이며, 통로 내 압력강하가 크면 유량 불균일 발생.
- **층류 근거**: 채널 Re<1,200; pillar 기준 Re_d ≈ 80 (0.5 m/s) ~ 340 (2 m/s). 구속된 pin-fin 배열에서 vortex shedding 시작 Re_d는 문헌 확인 필요(Brunschwiler 등 interlayer cooling 연구). 0.5 m/s는 정상 층류 가능성 높음, 고유속은 transient로 확인 필요.

## 7. 열린 질문 / 다음 작업

1. 실제 V-Die I/O 전력맵으로 hotspot 가정 교체.
2. 끝단 die 외측 냉각(추가 gap 또는 cold wall) 효과.
3. 얇은 die(100–150 µm) 직접 해석으로 top-side 적층 한계 외삽 검증.
4. 39 gap 매니폴드 유량 분배.
5. 초록 수정본에 10-die 수치 반영 ([수정본](Abstract_Methods_Results_Revision_2026-10-02.md)).
