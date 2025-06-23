from textual.app import App
from textual.widgets import Header, Footer

from ui.screens.home.Home import Home

class TerminalApp(App):
    TITLE="Celph-Aware"
    CSS_PATHS = ["ui/styles/app.css"]
    BINDINGS = [
        ("q", "quit", "Quit"),
        ("h", "toggle_help", "Help"),
    ]

    async def action_toggle_help(self) -> None:
        pass

    def compose(self):
        yield Header(icon="🚀", show_clock=True)

        self.push_screen(Home())
        
        yield Footer()
