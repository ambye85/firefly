from firefly import application
from firefly.application import Application


def test_application():
    """Application on update called once per frame until exit requested."""

    class ApplicationStub(Application):
        call_count = 0

        def on_update(self):
            ApplicationStub.call_count += 1
            if ApplicationStub.call_count >= 1:
                print("HERE")
                self.should_close(True)

    application.launch(lambda: ApplicationStub())

    assert ApplicationStub.call_count == 1
