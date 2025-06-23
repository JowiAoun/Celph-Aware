from textual.screen import Screen
from textual.app import ComposeResult
from textual.widgets import TabbedContent

from ui.screens.home.panes.OverviewPane import OverviewPane

class Home(Screen):
    def compose(self) -> ComposeResult:
        with TabbedContent(initial="overview"):
            yield OverviewPane("Overview", id="overview")
