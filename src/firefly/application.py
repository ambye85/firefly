"""Application is the entrypoint to the Firefly game engine."""
from abc import ABC
from abc import abstractmethod


class Application(ABC):
    """Application should be subclassed by clients."""

    def __init__(self):
        self._running = False

    @abstractmethod
    def on_update(self):
        pass

    def run(self):
        self._running = True
        while self._running:
            self.on_update()

    def should_close(self, close):
        self._running = not close


def launch(create_app):
    """Launches the application.

    create_app: function that returns an instantiated application.
    """
    app = create_app()
    app.run()
