from pprint import pprint

import brainflow
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds, BrainFlowPresets

board_id = BoardIds.CYTON_BOARD.value
pprint(BoardShim.get_board_descr(board_id))
print(BoardShim.get_board_descr(board_id))

params = BrainFlowInputParams()
# params.serial_port = "/dev/ttyUSB0"
board = BoardShim(BoardIds.CYTON_BOARD, params)

# board.prepare_session()
# board.start_stream()

print(board.get_timestamp_channel(board_id))
print(board.get_eeg_channels(board_id))
# print(board.get_current_board_data(board_id)) 
print(board.get_sampling_rate(board_id))
print(BoardShim.get_board_presets(board_id))