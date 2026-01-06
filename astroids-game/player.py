import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED


"""Player-controlled ship represented as a triangle.

    The player is centered at ``position`` (provided by :class:`CircleShape`) and
    rendered as a triangle oriented by ``rotation`` (degrees). Movement and
    turning use constants from :mod:`constants` (``PLAYER_SPEED`` and
    ``PLAYER_TURN_SPEED``), and the ship's size is set by ``PLAYER_RADIUS``.

    Attributes:
        position (pygame.Vector2): Center position inherited from
            :class:`CircleShape`.
        radius (float): Radius inherited from :class:`CircleShape`.
        rotation (float): Rotation in degrees; 0 corresponds to the down
            (0, 1) direction used by pygame vectors.

    Public methods:
        triangle(): Return three points (pygame.Vector2) forming the ship's
            triangle for rendering.
        draw(screen): Render the ship on the given surface.
        rotate(dt): Rotate the ship by ``PLAYER_TURN_SPEED * dt``.
        move(dt): Move the ship in the direction of ``rotation`` by
            ``PLAYER_SPEED * dt``.
        update(dt): Handle user input (W/A/S/D) to move and rotate the ship.
"""
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

        # Drawing the player as a triangle
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    

    def move(self, dt):
        unit_vector = pygame.Vector2(0,1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)