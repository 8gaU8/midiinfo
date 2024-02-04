import pygame.midi as m


def print_midi_info():
    m.init()
    dev_num = m.get_count()
    outputs = []
    inputs = []
    for dev_id in range(dev_num):
        (interf, name, is_input, is_output, is_opened) = m.get_device_info(dev_id)
        if is_input == 1:
            inputs.append("\n\t" + str(dev_id) + ": " + name.decode())
        elif is_output == 1:
            outputs.append("\n\t" + str(dev_id) + ": " + name.decode())
    print(" inputs: ", *inputs)
    print("outputs: ", *outputs)
    m.quit()


def main():
    print_midi_info()


def main_cli():
    main()


if __name__ == "__main__":
    main_cli()
