from firefly import application
from firefly.application import Application
from firefly.application import Layer
from firefly.application import LayerSystem


def test_application():
    """Application on update called once per frame until exit requested."""

    class ApplicationLayer(Layer):
        on_attach_count = 0
        on_update_count = 0
        on_detach_count = 0

        def __init__(self, debug_name, app_stub):
            super(ApplicationLayer, self).__init__(debug_name)
            self.app_stub = app_stub

        def on_attach(self):
            ApplicationLayer.on_attach_count += 1

        def on_update(self):
            ApplicationLayer.on_update_count += 1
            if ApplicationLayer.on_update_count >= self.app_stub.max_updates:
                self.app_stub.should_close(True)

        def on_detach(self):
            ApplicationLayer.on_detach_count += 1

    class ApplicationStub(Application):
        def __init__(self, max_updates):
            super(ApplicationStub, self).__init__()
            self.max_updates = max_updates

    def create_application():
        app = ApplicationStub(2)
        app.append_layer(ApplicationLayer("application layer", app))
        return app

    application.launch(create_application)

    assert ApplicationLayer.on_attach_count == 1, "On attach failed"
    assert ApplicationLayer.on_update_count == 2, "On update failed"
    assert ApplicationLayer.on_detach_count == 1, "On detach failed"


class LayerStub(Layer):
    def __init__(self, debug_name):
        super(LayerStub, self).__init__(debug_name)

        self.was_attached = False
        self.was_updated = False
        self.was_detached = False

    def on_attach(self):
        self.was_attached = True

    def on_detach(self):
        self.was_detached = True

    def on_update(self):
        self.was_updated = True


class TestLayerSystem:
    def test_append_single_layer(self):
        """Append a single layer to the layer system"""
        layer = LayerStub("layer")
        layers = LayerSystem()

        layers.append(layer)

        assert [layer for layer in layers] == [layer]

    def test_append_multiple_layers(self):
        """Append multiple layers to the layer system retains ordering"""
        layer1 = LayerStub("layer 1")
        layer2 = LayerStub("layer 2")
        layers = LayerSystem()

        layers.append(layer1)
        layers.append(layer2)

        assert [layer for layer in layers] == [layer1, layer2]

    def test_remove_last_layer(self):
        """Remove the last layer that was appended to the system"""
        layer1 = LayerStub("layer 1")
        layer2 = LayerStub("layer 2")
        layers = LayerSystem()

        layers.append(layer1)
        layers.append(layer2)
        layers.remove(layer2)

        assert [layer for layer in layers] == [layer1]

    def test_remove_any_layer(self):
        """Remove the first layer that was appended to the system"""
        layer1 = LayerStub("layer 1")
        layer2 = LayerStub("layer 2")
        layers = LayerSystem()

        layers.append(layer1)
        layers.append(layer2)
        layers.remove(layer1)

        assert [layer for layer in layers] == [layer2]

    def test_on_attach(self):
        """Layer's on_attach() method is called when appending to system"""
        layer = LayerStub("layer")
        layers = LayerSystem()

        layers.append(layer)

        assert layer.was_attached

    def test_on_update(self):
        """Layer's on_update() method is called"""
        layer = LayerStub("layer")
        layers = LayerSystem()

        layers.append(layer)
        for layer in layers:
            layer.on_update()

        assert layer.was_updated

    def test_on_detach(self):
        """Layer's on_detach() method is called when removing from system"""
        layer = LayerStub("layer")
        layers = LayerSystem()

        layers.append(layer)
        layers.remove(layer)

        assert layer.was_detached
