#!/usr/bin/env python
from firefly import application
from firefly.application import Application


class Sandbox(Application):
    def on_update(self):
        print("Sandbox updating")
        self.should_close(True)


def create_app() -> Sandbox:
    return Sandbox()


def main():
    application.launch(create_app)


if __name__ == "__main__":
    main()
