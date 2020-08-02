#!/usr/bin/env python
from firefly import application
from firefly.application import Application
from firefly.application import Layer


class SandboxLayer(Layer):
    def __init__(self, sandbox):
        super(SandboxLayer, self).__init__("sandbox layer")
        self.sandbox = sandbox
        self.frames = 0

    def on_attach(self) -> None:
        print("Sandbox layer attached")

    def on_detach(self) -> None:
        print("Sandbox layer detached")

    def on_update(self) -> None:
        self.frames += 1
        if self.frames >= 10:
            self.sandbox.should_close(True)
        print("Sandbox layer updated")


class Sandbox(Application):
    def __init__(self):
        super(Sandbox, self).__init__()


def create_sandbox() -> Sandbox:
    sandbox = Sandbox()
    sandbox.append_layer(SandboxLayer(sandbox))
    return sandbox


def main():
    application.launch(create_sandbox)


if __name__ == "__main__":
    main()
