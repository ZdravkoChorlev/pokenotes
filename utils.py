import os


def save_note(filename, note):
    """
    save text note to a file
    :param filename: the name of the file
    :param note: text to be saved
    :return: None
    """
    home = os.path.expanduser("~")
    storage_file = os.path.join(home, filename)

    with open(storage_file, "a+") as file:
        file.write(note)
        file.write("\n")
        file.close()
