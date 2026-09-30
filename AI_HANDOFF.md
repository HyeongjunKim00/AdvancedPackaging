# AI Handoff

## 현재 상태
- GitHub 저장소를 AI 지원 첨단 패키징 연구의 기준 문서(source of truth)로 운영하도록 공통 지침과 AI별 진입 파일을 마련했다.
- AI 앱이 GitHub 저장소를 자동으로 공유받는 것은 아니다. 각 앱에서 저장소 접근 및 지침 적용 여부를 실제 확인해야 한다.
- 연구 초점은 AI/HBM/3D 패키징용 ECTC 히트싱크 주제 탐색이다. 정확한 연구 질문, 구조, 단상/2상 선택, 기준선과 DLC 시험 조건은 미결정이다.
- 공개 저장소이므로 비공개 데이터, 미공개 원고, 과제 기밀은 올리지 않는다.

## 완료 작업
- 공통 원칙을 [AI_GUIDE.md](AI_GUIDE.md)에 정리: 파일 읽기 순서, 사용자 최신 요청 우선, 근거 등급, 출처 기록, Fact/claim/Inference 구분, 작업 종료 인계.
- AI별 진입점 추가: [AGENTS.md](AGENTS.md), [CLAUDE.md](CLAUDE.md), [GEMINI.md](GEMINI.md), [.github/copilot-instructions.md](.github/copilot-instructions.md).
- [README.md](README.md)에 시작 절차, Research 폴더 지도, 공개 저장소 주의사항 추가.
- [PROJECT_CONTEXT.md](PROJECT_CONTEXT.md)를 활성 연구 맥락과 사용자 선호에 맞게 보완.
- [TODO.md](TODO.md)를 워크플로 확인, 연구 질문·DLC 셋업 정의, 열관리 근거 정리 순으로 재정렬. 항목은 미완료로 유지.
- [Research/README.md](Research/README.md)에 분야별 폴더 지도와 연구 기록 원칙 추가.
- 변경 파일을 다시 읽어 주요 내용과 링크 구조를 확인했다. 조사 결과 추가나 Research 로그 변경은 이번 작업 범위에 포함하지 않았다.

## 미완료 작업
- 사용하는 각 AI 앱(Codex, Claude, Gemini, Copilot)에서 이 저장소에 실제 접근 가능한지, 해당 도구가 진입 파일과 import 문법을 적용하는지 확인.
- 저장소 접근이 안 되는 앱은 세션 시작 프롬프트에 README 및 AI_GUIDE, PROJECT_CONTEXT, TODO, AI_HANDOFF를 제공하거나 GitHub 연동을 설정.
- ECTC 연구 질문, 실제 열 병목, 비교 구조, 측정 항목 및 DLC 운전 범위를 정한다.
- V-Die/direct-to-silicon 선행기술과 시험 조건을 원문 확인하고 novelty를 평가한다.
- TODO의 HBM 냉각, TIM/lid 병목, DLC 동향 및 제품 로드맵 조사 항목은 미완료다.

## 핵심 참고자료
- [AI_GUIDE.md](AI_GUIDE.md) — AI 공통 규칙
- [README.md](README.md) — 시작 안내 및 저장소 지도
- [TODO.md](TODO.md) — 우선순위와 미완료 항목
- [ECTC Heat-Sink 대화 인계](Research/Topic_Exploration/ECTC_HeatSink_Conversation_Handoff_2026-09-30.md) — 연구 논의, 후보 문제 정의, 선행기술 위험
- [GitHub Copilot CLI instructions](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions)
- [GitHub Copilot customization reference](https://docs.github.com/en/copilot/reference/customization-cheat-sheet)
- [Claude Code memory/imports](https://docs.anthropic.com/zh-CN/docs/claude-code/memory)
- [Gemini CLI GEMINI.md context](https://google-gemini.github.io/gemini-cli/docs/cli/gemini-md.html)

## 다음 AI용 프롬프트
이 저장소에서 작업하기 전에 AI_GUIDE.md, PROJECT_CONTEXT.md, TODO.md, AI_HANDOFF.md를 순서대로 읽어라. 사용자의 최신 직접 요청을 우선하고, 요청하지 않은 조사나 파일 변경은 하지 마라. 저장소 지침이 현재 AI 앱에서 자동 적용되는지 먼저 확인하되, 확인할 수 없으면 그 한계를 명시하라. 연구 논의는 한국어로 간결하게 진행하고 사실·출처 주장·추론을 구분하라. 연구 내용은 관련 Research 로그에 출처와 조건을 남기고, 작업 종료 시 이 파일의 필수 다섯 항목을 갱신하라.
