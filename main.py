import os
import sys
import datetime
import arrow
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from kurly import clusters

# 🎯 한국 공휴일 목록 (YYYY-MM-DD 형식)
HOLIDAYS = {
    "2026-01-01",  # 신정
    "2026-02-16",  # 설 연휴
    "2026-02-17",  # 설날
    "2026-02-18",  # 설 연휴
    "2026-03-02",  # 대체공휴일
    "2026-05-05",  # 어린이날
    "2026-05-25",  # 대체공휴일
    "2026-06-03",  # 지방선거
    "2026-08-17",  # 대체공휴일
    "2026-09-24",  # 추석 연휴
    "2026-09-25",  # 추석
    "2026-10-05",  # 대체공휴일
    "2026-10-09",  # 한글날
    "2026-12-25",  # 크리스마스
}

# 📆 오늘 날짜 가져오기
today = datetime.date.today().strftime("%Y-%m-%d")

# 🚫 오늘이 공휴일이면 실행하지 않고 종료
if today in HOLIDAYS:
    print(f"📢 오늘({today})은 공휴일이므로 실행하지 않습니다.")
    sys.exit(0)

# 환경 변수에서 Slack 토큰 로드
load_dotenv()
SLACK_TOKEN = os.environ.get("SLACK_TOKEN")

def send_slack_message(message, channel):
    try:
        client = WebClient(token=SLACK_TOKEN)
        client.chat_postMessage(channel=channel, text=message)
    except SlackApiError as e:
        print(f"⚠️ Error sending message to {channel} : {e}")

def main():
    for cluster in clusters:
        # 메시지 제목 설정
        header = f"*[공지｜컬리스라운지 및 휴게시설 에티 안내]*\n\n\n"


        notice_msg = (
            f"1. *중요도* : 중\n"
            f"2. *대상* : 평택 클러스터 임직원 전체\n"
            f"3. *주요 내용*\n\n"
            f"\n"
            f"안녕하세요? 평택 클러스터 구성원 여러분!\n\n"
            f"우리 클러스터 컬리스라운지 (휴게실) 사용 에티켓에 대해\n"
            f"안내 드리오니, 많은 협조 부탁드리겠습니다.\n\n"
            f"\n"
            f":ck11: *컬리스 라운지 내 기물을 바르게 사용해 주세요~* 모두가 함께 사용하는 물품입니다!\n"
            f":ck11: 다음 사람을 배려하여 *의자와 테이블에 발을 올리지 말아주세요!*\n"
            f":ck11: 간단한 취식 후 *뒷정리도 아름답게 부탁 드려요!*\n"
            f":ck11: 센터 전 구역 에서는 *취사 활동 (전기를 활용한 포트 등) 금지 입니다!*\n"
            f":ck11: *부속동 (직원식당) 3층에서 취식이 가능 하오니 많은 이용 바랍니다!*\n"
            f":ck11: *냉난방기기 설정 온도는 여름철에는 23-26℃, 겨울철에는 18-20℃ 유지 바랍니다.*\n\n"
            f":point_right: (Click) *<https://static.wixstatic.com/media/50072f_d7df2e2179f5427688dd4c4501165974~mv2.png|컬리스 라운지 에티켓>*\n"
            f"\n"
            f"\n"
            f"*:slack: 문의사항 : 인사총무팀 총무/시설 담당자*\n\n"
            f"감사합니다.\n"
        )

        # 메시지 본문
        body = header + notice_msg

        # 슬랙 채널에 전송
        send_slack_message(body, cluster.channel)

if __name__ == "__main__":
    main()
