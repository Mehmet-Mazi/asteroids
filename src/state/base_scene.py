class BaseScene:
    def __init__(self, scene_manager, screen):
        self.scene_manager = scene_manager
        self.screen = screen

    def on_enter(self):
        pass

    def on_exit(self):
        pass
    
    def run(self):
        raise NotImplementederror("Scene must implement run()")