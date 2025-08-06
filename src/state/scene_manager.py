from state.transition import Transition


class SceneManager:
    def __init__(self, screen, base_scene):
        self._screen = screen
        self._base_scene = base_scene(self, self._screen)
        self.__stack = [self._base_scene]
        self.create_transition_mappings()

    def update(self, events, dt):
        result = self.current_scene.run(events, dt)
        if isinstance(result, Transition):
            self.handle_transition(result)

    def handle_transition(self, transition):
        allowed = getattr(self.current_scene, "allowed_transitions", set())
        if transition.type not in allowed:
            raise Exception(
                f"Invalid transition '{transition.type}' from {type(self.current_scene).__name__}"
            )

        self._transition_map[transition.type](**transition.data)

    @property
    def current_scene(self):
        return self.__stack[-1]

    @current_scene.setter
    def current_scene(self, scene):
        self.__stack.append(scene)

    @current_scene.deleter
    def current_scene(self):
        return self.__stack.pop()

    def stack(self):
        return self.__stack

    def clear(self):
        self.__stack = []

    def reset_scene(self, transition):
        self.clear()
        self.current_scene = transition

    def create_transition_mappings(self):
        raise NotImplementedError(
            "Scene Manager must implement a create_transition_mapping",
            type(self).__name__,
        )
