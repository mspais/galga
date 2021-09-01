controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    projectile = sprites.createProjectileFromSprite(img`
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
        `, spacePlane, 200, 0)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite2, otherSprite2) {
    otherSprite2.destroy(effects.disintegrate, 500)
    info.changeLifeBy(-1)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    sprite.destroy()
    otherSprite.destroy(effects.fire, 100)
    info.changeScoreBy(1)
})
let alien: Sprite = null
let projectile: Sprite = null
let spacePlane: Sprite = null
spacePlane = sprites.create(img`
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
    `, SpriteKind.Player)
controller.moveSprite(spacePlane, 200, 200)
spacePlane.setFlag(SpriteFlag.StayInScreen, true)
info.setLife(3)
game.onUpdateInterval(500, function () {
    alien = sprites.create(img`
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
        `, SpriteKind.Enemy)
    alien.setVelocity(-100, 0)
    alien.setPosition(160, randint(0, 120))
})
