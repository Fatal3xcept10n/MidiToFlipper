def createFmf(fmfList, fmf_dir):
    bpm = fmfList[0]

    content = f"Filetype: Flipper Music Format\n"
    content += f"Version: 0\n"
    content += f"BPM: {bpm}\n"
    content += f"Duration: 4\n"
    content += f"Octave: 4\n"
    content += "Notes: " + ', '.join(str(n) for n in fmfList[1:])

    with open(fmf_dir, 'w') as file:
        file.write(content)


