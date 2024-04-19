import random
import pygame
import sys
from models.character import Character
from models.gun import Gun
from scenes.lose_screen import LoseScreen  # Import màn hình thua
from scenes.win_screen import WinScreen    # Import màn hình thắng


class PVE:
    def __init__(self, screen, model) -> None:
        self.screen = screen
        self.model = model
        self.running = True

        _character = Character(100, 100, (300, 400), 1, screen, "character1")
        _gun = Gun(_character, 10)
        _enemy = Character(100, 100, (500, 400), -1, screen, "character2")

        _gun_enemy = Gun(_enemy, 10)

        _character.enemy = _enemy
        _enemy.enemy = _character

        all_sprites = pygame.sprite.Group()
        all_sprites.add(_character)
        all_sprites.add(_gun)
        all_sprites.add(_enemy)
        all_sprites.add(_gun_enemy)

        MOVE_SPEED = 5  # Giảm tốc độ di chuyển của enemy để không lại quá gần character
        last_shot_time = 0
        last_shot_time_e = 0
        shoot_delay = 500
        reload_time = 2000
        reloaded_time = 0
        reloaded_time_e = 0
        num_move_e = 10
        move_count_e = 0
        direct_e = random.choice([1, -1])
        clock = pygame.time.Clock()

        # Tải hình ảnh nền và thay đổi kích thước nếu cần thiết
        background_image = pygame.image.load('res/images/bg.png')
        background_rect = background_image.get_rect()
        pygame.display.set_caption('PVE')

        while self.running:
            current_time = pygame.time.get_ticks()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    self.running = False

            # Kiểm tra trạng thái của nhân vật

            if not _character.alive():
                # Chuyển sang màn hình thua cuộc
                self.model.current_screen = 'lose'
                all_sprites.empty()
                self.running = False

            elif not _enemy.alive():
                # Chuyển sang màn hình thắng
                self.model.current_screen = 'win'
                all_sprites.empty()
                self.running = False

            else:
                screen.blit(background_image, background_rect)

            all_sprites.draw(screen)

            keys = pygame.key.get_pressed()
            dx, dy = 0, 0
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                dx -= MOVE_SPEED
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                dx += MOVE_SPEED
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                _character.isJump = True
            if keys[pygame.K_RETURN] and current_time - last_shot_time > shoot_delay:
                bull = _gun.shoot()
                if bull:
                    all_sprites.add(bull)
                last_shot_time = current_time

            if _gun.current_bull == _gun.max_bull and reloaded_time == 0:
                reloaded_time = current_time
            else:
                if _gun.current_bull == _gun.max_bull and current_time - reloaded_time > reload_time:
                    _gun.current_bull = 0
                    reloaded_time = 0
            if _character.alive() and _enemy.alive():
                # enemy play
                # Kiểm tra khoảng cách và điều chỉnh hành động của enemy
                dy_e = 0
                dx_e = 0
                bullets_char = _gun.bullets
                check_have_moved = True
                for bul in bullets_char:
                    if abs(bul.rect.x - _enemy.rect.centerx) < 70:
                        if _enemy.rect.top - random.randrange(0,20) < bul.rect.y < _enemy.rect.bottom + random.randrange(0,20):
                            rand_rang = random.randrange(0,100)
                            print(rand_rang)
                            if (not _enemy.isJump) and 33 < rand_rang < 63:
                                _enemy.isJump = True
                            else:
                                dx_e -= MOVE_SPEED * _enemy.direct
                        else:
                            if _enemy.isJump:
                                dx_e += MOVE_SPEED * _enemy.direct
                            else:
                                check_have_moved = False
                if (check_have_moved):
                    move_count_e += 1
                    dx_e += MOVE_SPEED * direct_e
                    if (move_count_e == num_move_e):
                        move_count_e = 0
                        direct_e = random.choice([1, -1])
                        # elif _enemy.isJump
                        #     else:
                        #         dx_e -= MOVE_SPEED
                # if distance > 200 and distance < 600:
                #     dx_e += MOVE_SPEED if bool(random.getrandbits(1)) else -MOVE_SPEED

                # Tự động bắn character
                if current_time - last_shot_time_e > shoot_delay:
                    bull = _gun_enemy.shoot()
                    if bull:
                        all_sprites.add(bull)
                    last_shot_time_e = current_time
                if _gun_enemy.current_bull == _gun_enemy.max_bull and reloaded_time_e == 0:
                    reloaded_time_e = current_time
                else:
                    if _gun_enemy.current_bull == _gun_enemy.max_bull and current_time - reloaded_time_e > reload_time:
                        _gun_enemy.current_bull = 0
                        reloaded_time_e = 0

                # flip
                if (_character.direct == 1 and _character.rect.x > _enemy.rect.x) or (
                        _character.direct == -1 and _character.rect.x <= _enemy.rect.x):
                    _character.flip()
                    _enemy.flip()

                # va chạm
                bullets_group = pygame.sprite.Group()
                bullets_group.add(_gun.bullets)
                bullets_group.add(_gun_enemy.bullets)
                if len(bullets_group) > 0:
                    hits = pygame.sprite.groupcollide(bullets_group, all_sprites, False, False)
                    for bullet, targets in hits.items():
                        for target in targets:
                            if isinstance(target, Character):
                                if (bullet.gun.character.enemy == target):
                                    target.hp -= bullet.damage
                                    if (target.hp <= 0):
                                        target.kill()
                                    bullet.die()
                # update
                if all_sprites.has(_character):
                    if (dx_e > 0 and 750 > _character.rect.x) or (dx_e < 0 and 0 < _character.rect.x):
                        _character.update(dx, dy)
                    else:
                        _character.update(0, dy)
                if all_sprites.has(_gun):
                    _gun.update()
                if all_sprites.has(_enemy):
                    if (dx_e > 0 and 750 > _enemy.rect.x) or (dx_e < 0 and 0 < _enemy.rect.x):
                        _enemy.update(dx_e, dy_e)
                    else:
                        _enemy.update(0, dy_e)
                if all_sprites.has(_gun_enemy):
                    _gun_enemy.update()
                _character.jump()
                _enemy.jump()
            else:
                if _character.alive():
                    _character.update(0, 0)
                    _gun.update()
                else:
                    _enemy.update(0, 0)
                    _gun_enemy.update()

            pygame.display.flip()
            clock.tick(60)