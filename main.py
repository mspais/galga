def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . 7 7 7 7 7 7 7 7 7 7 . . . . 
                    . . 7 5 5 5 5 5 5 5 5 7 . . . . 
                    . . 7 7 7 7 7 7 7 7 7 7 . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        spacePlane,
        200,
        0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    sprite.destroy()
    otherSprite.destroy(effects.fire, 100)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    otherSprite2.destroy(effects.disintegrate, 500)
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

alien: Sprite = None
projectile: Sprite = None
spacePlane: Sprite = None
spacePlane = sprites.create(img("""
        ....................
            ....................
            ....666.............
            .....6666...........
            ......66666...666...
            ...666666666.669966.
            ..66666666666699996.
            66666666666666666666
            6666666666666666666.
            .......6666.........
            ......66666.........
            ......6666..........
            .....66666..........
            ....66666...........
            ....6666............
            ...666..............
    """),
    SpriteKind.player)
controller.move_sprite(spacePlane, 200, 200)
spacePlane.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
info.set_life(3)

def on_update_interval():
    global alien
    alien = sprites.create(img("""
            . . . . . 6 6 6 6 6 6 . . . . . 
                    . . . . 6 6 9 9 9 9 6 6 . . . . 
                    . . . 6 6 9 9 c c 9 9 6 6 . . . 
                    . . 6 6 9 9 c c 6 9 9 9 6 6 . . 
                    . 6 6 9 9 9 9 c 6 6 9 9 9 6 6 . 
                    6 6 9 9 9 9 9 9 6 6 9 9 9 9 6 6 
                    6 9 9 9 6 6 6 6 9 6 9 9 c 9 9 6 
                    6 9 c 6 6 6 9 9 9 6 9 c c c 9 6 
                    6 9 c c c 9 6 9 9 9 6 6 6 c 9 6 
                    6 9 9 c 9 9 6 9 6 6 6 6 9 9 9 6 
                    6 6 9 9 9 9 6 6 9 9 9 9 9 9 6 6 
                    . 6 6 9 9 9 6 6 c 9 9 9 9 6 6 . 
                    . . 6 6 9 9 9 6 c c 9 9 6 6 . . 
                    . . . 6 6 9 9 c c 9 9 6 6 . . . 
                    . . . . 6 6 9 9 9 9 6 6 . . . . 
                    . . . . . 6 6 6 6 6 6 . . . . .
        """),
        SpriteKind.enemy)
    alien.set_velocity(-100, 0)
    alien.set_position(160, randint(0, 120))
game.on_update_interval(500, on_update_interval)
