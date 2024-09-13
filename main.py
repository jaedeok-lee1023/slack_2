import os

import arrow
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from kurly import clusters

# 환경 변수에서 Slack 토큰, 채널을 로드
load_dotenv()
SLACK_TOKEN = os.environ.get("SLACK_TOKEN")
def send_slack_message(message, channel):
    try:
        client = WebClient(token=SLACK_TOKEN)
        client.chat_postMessage(channel=channel, text=message)
    except SlackApiError as e:
        print(f"Error sending message to {channel} : {e}")
def main():
    for cluster in clusters:
        # 메시지 제목 설정
        header = f":loudspeaker: *『인사총무팀 공지』*\n\n"


        notice_msg = (
            f"안녕하세요? 평택 클러스터 구성원 여러분!\n\n평택 클러스터 6층 컬리스라운지(휴게실) 사용 에티켓 안내드립니다.\n\n"
            f"\n"
            f"\n"
            f":ck11: *컬리스 라운지 내 기물을 바르게 사용해 주세요~* 모두가 함께 사용하는 물품입니다!\n"
            f":ck11: 다음 사람을 배려하여 *의자와 테이블에 발을 올리지 말아주세요!*\n"
            f":ck11: 간단한 취식 후 *뒷정리도 아름답게 부탁 드려요!*\n"
            f":ck11: 센터 전 구역 에서는 *취사 활동 (전기를 활용한 포트 등) 금지 입니다!*\n"
            f":ck11: *부속동 (직원식당) 3층에서 취식이 가능 하오니 많은 이용 바랍니다!*\n"
            f":ck11: *냉난방기기 설정 온도는 여름철에는 23-26℃, 겨울철에는 18-20℃ 유지 바랍니다.*\n\n"
            f"\n"
            f"\n"
            f"*문의사항 : 인사총무팀 총무/시설 담당자*\n\n"
            f"감사합니다.\n"
        )

        # 메시지 본문
        body = header + notice_msg

        # 슬랙 채널에 전송
        send_slack_message(body, cluster.channel)

if __name__ == "__main__":
    main()
