import json

from textual.app import ComposeResult
from textual.widgets import TabPane, Input, Label, ListView, ListItem

from models.LLM import LLM


class OverviewPane(TabPane):
    llm = LLM()

    input = Input(placeholder="What are you about to do?")

    good_list_view_title = Label("🤠 The Good!")
    good_list_view = ListView()

    bad_list_view_title = Label("🙅 The Bad.")
    bad_list_view = ListView()

    ugly_list_view_title = Label("🤮 The Ugly...")
    ugly_list_view = ListView()

    def compose(self) -> ComposeResult:
        yield self.input

        yield self.good_list_view_title
        yield self.good_list_view

        yield self.bad_list_view_title
        yield self.bad_list_view

        yield self.ugly_list_view_title
        yield self.ugly_list_view

    def on_input_submitted(self, message: Input.Submitted) -> None:
        action = message.value.strip()
        if not action:
            return

        # Call the LLM with our template
        res = self.llm.chat_good_bad_ugly(action)
        if not res:
            self.input.value = "Bad response"
            return

        # Helper to populate a ListView from a list of strings
        def populate(view: ListView, items: list[str]):
            view.clear()
            for item in items:
                view.append(ListItem(Label(item)))

        # Repopulate each list
        populate(self.good_list_view, res.get("good", []))
        populate(self.bad_list_view,  res.get("bad",  []))
        populate(self.ugly_list_view, res.get("ugly", []))

        self.input.value = ""
