import pygame


image_path = "images/"
IMAGES = {
    "player" : {

        "idle" : [
            pygame.image.load(image_path + "player/idle0.png"),
            pygame.image.load(image_path + "player/idle1.png"),
            pygame.image.load(image_path + "player/idle2.png"),
        ],

        "run" : [
            pygame.image.load(image_path + "player/run0.png"),
            pygame.image.load(image_path + "player/run1.png"),
            pygame.image.load(image_path + "player/run2.png"),
        ],

        "punch" : [
            pygame.image.load(image_path + "player/punch0.png"),
            pygame.image.load(image_path + "player/punch1.png"),
            pygame.image.load(image_path + "player/punch2.png"),
        ]
    }
}