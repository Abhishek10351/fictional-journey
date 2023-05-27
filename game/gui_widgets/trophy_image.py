import arcade


class TrophyImage(arcade.gui.UIImage, arcade.gui.UIInteractiveWidget):
    def __init__(self, image_path, x=0, y=0, image_size=80, image_id=None, description=""):

        super().__init__(arcade.load_texture(image_path, hit_box_algorithm=arcade.hitbox.algo_detailed),
                         x=0, y=0, width=image_size, height=image_size)

        self.image_id = image_id
        self.description = description
        self.image_size = image_size

    def do_render(self, surface):
        surface.clear()
        self.prepare_render(surface)
        # arcade.draw_rectangle_filled(0, 0, self.width*2, self.height*2, (46, 204, 113))
        surface.draw_texture(
            x=0,
            y=0,
            width=self.width,
            height=self.height,
            tex=arcade.load_texture(
                "assets/gui/textures/glassPanel_projection.png")
        )
        surface.draw_texture(

            x=self.width/10,
            y=self.width/10,
            width=4*self.width/5,
            height=4*self.height/5,
            tex=self.texture
        )
