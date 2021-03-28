from __future__ import annotations

from typing import Callable, Iterator, List

"""Application is the entrypoint to the Firefly game engine."""
from abc import ABC


class Application(ABC):
    """Application should be subclassed by clients."""

    def __init__(self) -> None:
        self._layers: LayerSystem = LayerSystem()
        self._running: bool = False

    def append_layer(self, layer: Layer):
        """Append a `Layer` to the application."""
        self._layers.append(layer)

    def run(self) -> None:
        self._running = True
        while self._running:
            for layer in self._layers:
                layer.on_update()

        for layer in self._layers:
            self._layers.remove(layer)

    def should_close(self, close: bool) -> None:
        self._running = not close


def launch(create_app: Callable[[], Application]) -> None:
    """Launches the application.

    create_app: function that returns an instantiated application.
    """
    app = create_app()
    app.run()


class Layer(ABC):
    """Layer's provide independent units of functionality.
    As a minimum, you should have one layer which provides your main
    `Application` logic. Override the relevant methods to define behaviour
    specific to your application.
    """

    def __init__(self, debug_name: str) -> None:
        self._debug_name: str = debug_name

    def __repr__(self) -> str:
        return f'Layer("{self._debug_name}")'

    def on_attach(self) -> None:
        """On attach is called when a Layer is attached to a `LayerSystem`."""
        pass

    def on_detach(self) -> None:
        """On detach is called when a Layer is removed from a `LayerSystem`."""
        pass

    def on_update(self) -> None:
        """On update is called by the `Application` to update the Layer."""
        pass


class LayerSystem:
    """LayerSystem is a data structure for managing `Layer`s."""

    def __init__(self) -> None:
        self._layers: List[Layer] = []

    def __iter__(self) -> Iterator[Layer]:
        return iter(self._layers)

    def append(self, layer: Layer) -> None:
        """Append a `Layer`."""
        self._layers.append(layer)
        layer.on_attach()

    def remove(self, layer: Layer) -> None:
        """Remove a `Layer`."""
        self._layers.remove(layer)
        layer.on_detach()
