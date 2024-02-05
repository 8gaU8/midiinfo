from typing import Literal, Union

from fire import Fire


def print_midi_info_pygame():
    print("using backend: pygame")
    import pygame.midi as m

    m.init()
    dev_num = m.get_count()
    outputs = []
    inputs = []
    for dev_id in range(dev_num):
        (interf, name, is_input, is_output, _) = m.get_device_info(dev_id)
        msg = f"\n\t{dev_id}: {name.decode()} [{interf.decode()}]"
        if is_input == 1:
            inputs.append(msg)
        elif is_output == 1:
            outputs.append(msg)
    print(" Inputs: ", *inputs)
    print("Outputs: ", *outputs)
    m.quit()


def print_midi_info_rtmidi():
    print("using backend: rtmidi")
    from rtmidi import MidiIn, MidiOut  # type: ignore

    def print_ports_names(midi_port: Union[MidiIn, MidiOut]):
        for i, port in enumerate(midi_port.get_ports()):
            print(f"\t{i}: {port}")

    midiout = MidiOut()
    midiin = MidiIn()

    print("Outputs: ")
    print_ports_names(midiout)
    print("Inputs: ")
    print_ports_names(midiin)


def print_midi_info(backend: Literal["pygame", "rtmidi"] = "pygame"):
    """
    Args:
        backend (Literal['pygame', 'rtmidi'], optional): 'pygame' or 'rtmidi'.

    """
    if backend == "pygame":
        print_midi_info_pygame()
        return
    if backend == "rtmidi":
        print_midi_info_rtmidi()
        return


def main_cli():
    Fire(print_midi_info)
