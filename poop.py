import pygame
import random
#############################################################
#게임 초기화
pygame.init()

#게임창 설정
screen_width = 480
screen_heigt = 640
screen = pygame.display.set_mode((screen_width, screen_heigt))

#타이틀 설정
pygame.display.set_caption("POOP Game")

#FPS
clock = pygame.time.Clock()
#############################################################

# 1. 사용자 게임 초기화(배경화면, 게임 이미지, 좌표, 속도, 폰트 등)

#배경 이미지 설정
background = pygame.image.load("C:/python-project/background.png")

#캐릭터 설정
character = pygame.image.load("C:/python-project/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_heigt - character_height

#캐릭터, 적 캐릭터 이동속도
character_speed = 0.6
enemy_speed = 0.6

#이동할 좌표
#캐릭터 좌표
to_x = 0
#적 캐릭터 좌표
enemy_to_y = 0


#적 캐릭터 설정
enemy = pygame.image.load("C:/python-project/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randrange(0, 410)
enemy_y_pos = 0

#폰트 정의
game_font = pygame.font.Font(None, 40)

#총 시간
total_time = 61

#시작시간
start_ticks = pygame.time.get_ticks() #현재 tick을 받음

# 2. 이벤트 처리 (키보드, 마우스 처리)

#이벤트 루프
running = True
while running:
    dt = clock.tick(30)#게임화면의 초당 프레임수를 설정
    print('1')#무한루프 확인 값

    for event in pygame.event.get():#어떤 이벤트가 발생했는지 체크
        if event.type == pygame.QUIT:#창이 닫히는 이벤트 체크
            running = False

        if event.type == pygame.KEYDOWN:#키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= character_speed 
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed 

        if event.type == pygame.KEYUP:#방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0            
        print('11111111')#이벤트처리 확인 값

    #캐릭터, 적 캐릭터의 속도변화
    enemy_to_y += enemy_speed - 0.5
    enemy_y_pos += enemy_to_y 

    character_x_pos += to_x * dt
    enemy_y_pos += enemy_to_y * dt

    #적 캐릭터의 세로 경계값 처리 및  추후의 적 캐릭터의 랜덤생성
    if enemy_y_pos < 0:
        enemy_y_pos = 0
    elif enemy_y_pos > screen_heigt - enemy_height:
        enemy_y_pos = 0
        enemy_to_y = 0
        enemy_x_pos = random.randrange(0, 410)

    #캐릭터의 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    #캐릭터의 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_heigt - character_height:
        character_y_pos = screen_heigt - character_height

    #충돌 처리 (각 사각형의 정보 받기)
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print('충돌했습니다.')
        running = False

    screen.blit(background, (0, 0))#배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))#캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))#적 캐릭터 그리기

    #타이머 집어 넣기
    #경과된 시간(s) 계산 (1000을 나눈 이유는 ms이기 때문에 곱하기 1000을 해야 초 단위가 나옴)
    elasped_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render(str(int(total_time - elasped_time)), True, (255, 255, 255))
    screen.blit(timer, (10, 10))

    if total_time - elasped_time <= 0:
        print('시간경과.')
        running = False

    pygame.display.update()#게임화면 리셋

            

#게임종료
pygame.quit()