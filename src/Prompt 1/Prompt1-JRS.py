from utils.Capture import Capture
import os
import matplotlib


matplotlib.use('TKAgg')
# Disable tensorflow output
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

capture_stream = Capture()
capture_stream.capture_pipeline(debug=True, display=True)

