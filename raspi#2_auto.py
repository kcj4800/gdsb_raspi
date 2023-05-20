#
#      공대선배 라즈베리파이썬 부팅시 파이썬 자동실행 방법
#      youtube 바로가기: https://www.youtube.com/c/공대선배
#      LED를 1초마다 켜고 끄는 코드

# git config --list : git 정보 확인
# vscode로 git push 실패 -> VNC Viewer로 파일 끌어다 직접올리기
# 터미널에서 opencv 버젼 확인 : python3 -> import cv2 -> cv2.__version__
# 가상환경에서 실행하는 경로 : /home/pi/cctv_project/gdsb_env/bin/python3.9 /home/pi/cctv_project/raspi#2_auto.py

import RPi.GPIO as GPIO     # 라즈베리파이 GPIO 관련 모듈을 불러옴
import time                 # 시간관련 모듈을 불러옴

GPIO.setmode(GPIO.BCM)      # GPIO 핀들의 번호를 지정하는 규칙 설정

### 이부분은 아두이노 코딩의 setup()에 해당합니다
LED_pin = 17                  # LED 핀은 라즈베리파이 GPIO 17번핀으로 
GPIO.setup(LED_pin, GPIO.OUT)   # LED 핀을 출력으로 설정

### 이부분은 아두이노 코딩의 loop()에 해당합니다
try:                                    # 이 try 안의 구문을 먼저 수행하고
    while True:                         # 무한루프 시작: 아두이노의 loop()와 같음
        GPIO.output(LED_pin, GPIO.HIGH) # LED 핀에 HIGH 신호 인가(LED 켜짐)
        time.sleep(1)                   # 1초간 대기 : 아두이노의 delay(1000)과 같음
        GPIO.output(LED_pin, GPIO.LOW)  # LED 핀에 LOW 신호 인가(LED 꺼짐)
        time.sleep(1)                   # 1초간 대기

### 이부분은 반드시 추가해주셔야 합니다.
finally:                                # try 구문이 종료되면
    GPIO.cleanup()                      # GPIO 핀들을 초기화


# 부팅시 자동으로 프로그램 실행되게 하는 방법. 
# 복잡한 프로그램일때는 time.sleep(10)등을 추가해서 다른 장비들이 모두 연결 된 후 실행하도록 한다.
# 참고 : https://m.blog.naver.com/emperonics/221770579539

# 방법 1 : rc.local 방법 - 주의!!! 코드에 에러가 있을시 부팅이 안됨.
# 1. VSCode에서 실행할 python 파일을 실행
# 2. 실행 터미널 옆의 명령어를 그대로 복사하여 메모장에 저장
# 3. 라즈베리파이에 원격(혹은 ssh)로 접속
# 4. 터미널을 열고, sudo nano /etc/rc.local 입력
# 5. 맨 하단 exit 0 바로 윗줄에 복사해둔 명령어를 붙여넣고 끝에 &를 붙임
'''
fi
/home/pi/cctv_project/gdsb_env/bin/python3.9 /home/pi/cctv_project/raspi#2_auto.py&
exit 0
'''
# 6. 다시 실행하여 확인


# 방법 2 : .bashrc 방법 - 부팅시 뿐아니라 새로운 터미널이 열리거나 ssh 연결이 들어올때도 실행된다.
# sudo nano /home/pi/.bashrc
# 마지막 줄에 실행하고자 하는 파일과 명령어를 입력
# echo Running at boot 라는 메시지가 먼저 뜨고 다음에 프로그램 실행

'''
fi

echo Runnig at boot
sudo /home/pi/cctv_project/gdsb_env/bin/python3.9 /home/pi/cctv_project/raspi#2_auto.py
'''

# echo로 Running at boot 라는 메시지가 먼저 뜨고 다음에 프로그램 실행하도록 코딩한 것. 지워도 상관 없다.
 
 
# 방법 3 : lxterminal로 자동 부팅시 터미널을 실행시키는 방법
# sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
# 마지막 줄에 @lxterminal - e 와 부팅시 터미널에서 실행하고자 하는 파일과 명령어 입력

'''
@lxpanel --profile LXDE-pi
@pcmanfm --desktop --profile LXDE-pi
@xscreensaver -no-splash
@lxterminal -e python3 /home/pi/auto.py
'''
 