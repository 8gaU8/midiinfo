from typing import Union

from rtmidi import MidiIn, MidiOut  # type: ignore


def _print_ports_names(midi_port: Union[MidiIn, MidiOut]):
    for i, port in enumerate(midi_port.get_ports()):
        print(f"\t{i}: {port}")


def print_midi_info():
    midiout = MidiOut()
    midiin = MidiIn()

    print("Outputs: ")
    _print_ports_names(midiout)
    print("inputs: ")
    _print_ports_names(midiin)


def main_cli():
    print_midi_info()
