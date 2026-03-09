import capture_results
capture_results.start()

import sea_level_predictor
from unittest import main
import traceback

program = None
runtime_error = None

try:
    sea_level_predictor.draw_plot()

    program = main(module="test_module", exit=False)

except Exception as e:
    runtime_error = e
    traceback.print_exc()

finally:
    capture_results.finish(program, runtime_error)