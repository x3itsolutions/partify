"""Copyright 2011 Fred Hatfull

This file is part of Partify.

Partify is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Partify is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Partify.  If not, see <http://www.gnu.org/licenses/>."""

from multiprocessing import Manager

last_updated_times = None
manager = None

desired_player_state = None

def init_desired_player_state():
	global manager
	global desired_player_state

	if manager is None:
		manager = Manager()
	if desired_player_state is None:
		desired_player_state = manager.dict()
	
	desired_player_state['state'] = "play"
	desired_player_state['trans_fn'] = "play"

def update_desired_player_state(state, transition_fn):
	global manager
	global desired_player_state

	desired_player_state['state'] = state
	desired_player_state['trans_fn'] = transition_fn

def get_desired_player_state():
	global manager
	global desired_player_state

	return desired_player_state['state'], desired_player_state['trans_fn']

def init_times():
	global manager
	global last_updated_times
	if manager is None:
		manager = Manager()
	if last_updated_times is None:
		last_updated_times = manager.dict()

def update_time(key, time):
	global manager
	global last_updated_times
	last_updated_times[key] = time

def get_time(key):
	global manager
	global last_updated_times
	if key not in last_updated_times:
		last_updated_times[key] = 0
	return last_updated_times[key]