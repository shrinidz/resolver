from behave.model_core import Status

def before_scenario(context, scenario):
    context.scenario_status = "passed"

def after_scenario(context, scenario):
    print(f"Scenario '{scenario.name}': {context.scenario_status}")

def after_step(context, step):
    if step.status == Status.failed:
        context.scenario_status = "failed"
    elif step.status == Status.skipped:
        context.scenario_status = "skipped"

def after_all(context):
    if hasattr(context, "driver"):
        context.driver.quit()

