import taipy as tp

# Previous configuration of scenario
...

page = """
Name: <|{input_name}|input|>
<|submit|button|on_action=submit_scenario|>

Message: <|{message}|text|>
"""

input_name = "Taipy"
message = None


def submit_scenario(state):
    state.scenario.input_name.write(state.input_name)
    state.scenario.submit(wait=True)
    state.message = scenario.message.read()


if __name__ == "__main__":
    tp.Core().run()
    scenario = tp.create_scenario(scenario_cfg)
    tp.Gui(page).run()