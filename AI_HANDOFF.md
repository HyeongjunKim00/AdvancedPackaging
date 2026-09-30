# AI Handoff

## 현재 상태
- ECTC 열 시뮬레이션 주제는 V-Die-on-GPU 외부 콜드플레이트 설계다. 주제·구체 형상·기준 조건은 미정이다.
- 사용자가 정정함: 높이 차 concern은 GPU와 HBM이 아니라 GPU와 수직으로 세운 V-Die 사이에 있다. 사용자가 말한 V-Die는 약 10 mm 수직 형상일 수 있으나 실제 단면/기준면은 확인되지 않았다.
- 사용자는 기계적 접촉압 해석이 아니라 열 시뮬레이션 중심의 연구를 원한다.

## 완료 작업
- 연구 범위를 GPU/V-Die의 열원별 열경로, 외부 콜드플레이트의 냉각면/유로 커버리지, 유량 분배가 온도장에 미치는 영향으로 수정했다.
- 가능한 설계변수로 V-Die sidewall 커버리지, 냉각 채널 높이·위치, GPU 상면 냉각 영역, 매니폴드 유량 배분을 기록했다. 구조응력 해석은 현 범위에서 제외했다.
- 적용 조건과 모델링 고려사항은 [Thermal Research Log](Research/Thermal/Research_Log.md)에 기록했다. 앞선 HBM 10 mm 치수 해석은 concern과 무관하므로 적용하지 않는다.

## 미완료 작업
- 실제 V-Die/GPU 단면, 돌출 높이의 기준, 외부 콜드플레이트의 접촉/근접 면을 확인한다.
- GPU와 V-Die별 전력/열유속 맵과 물성을 설정한다.
- 열전도-대류 모델의 범위와 고정 TIM/contact resistance 조건을 결정한다.
- 기준 콜드플레이트와 V-Die 맞춤 유로를 같은 열부하 및 입구/유량(또는 펌프동력) 조건에서 비교한다.
- 출력 지표: GPU/V-Die별 Tmax, 온도 편차, Rth 및 필요 시 ΔP.

## 핵심 참고자료
- [V-Die 열 시뮬레이션 문제 범위](Research/Thermal/Research_Log.md)
- [콜드플레이트 조사본](Research/Thermal/Incoming/2026-09-30_콜드플레이트_ChatGPT.md) — 원문·수치 검증 미완료.
- [ECTC 대화 핸드오프](Research/Topic_Exploration/ECTC_HeatSink_Conversation_Handoff_2026-09-30.md)

## 다음 AI용 프롬프트
사용자는 V-Die-on-GPU의 GPU/V-Die 높이 차에 따른 열 시뮬레이션을 원하며 HBM 대상이 아니고 기계적 분석도 원하지 않는다. V-Die 단면과 냉각 경계를 먼저 확인하라. fin 형상 개선으로 미리 한정하지 말고, 냉각면/유로의 위치 및 V-Die sidewall 커버리지와 die별 열원/유량 분배가 GPU·V-Die Tmax와 온도 편차에 미치는 영향을 질문으로 구성하라. 실제 치수와 전력 맵이 없으면 숫자를 가정하지 말고 필요한 입력으로 표시하라.