hour_table = {
        0: 'twaalf',
        1: 'een',
        2: 'twee',
        3: 'drie',
        4: 'vier',
        5: 'vijf',
        6: 'zes',
        7: 'zeven',
        8: 'acht',
        9: 'negen',
        10: 'tien',
        11: 'elf',
        12: 'twaalf',
        13: 'een',
        14: 'twee',
        15: 'drie',
        16: 'vier',
        17: 'vijf',
        18: 'zes',
        19: 'zeven',
        20: 'acht',
        21: 'negen',
        22: 'tien',
        23: 'elf',
        24: 'twaalf',
}

def time_str(hours, minutes):
    formatstr = 'Het is {}'

    if minutes < 20:
        hour = hour_table[hours]
    elif hours < 24:
        hour = hour_table[hours+1]
    else:
        hour = hour_table[1]

    if 0 < minutes < 3:
        return formatstr.format(hour + ' uur')
    if 2 < minutes < 8:
        return formatstr.format('vijf over ' + hour)
    if 7 < minutes < 13:
        return formatstr.format('tien over ' + hour)
    if 12 < minutes < 18:
        return formatstr.format('kwart over ' + hour)
    if 17 < minutes < 23:
        return formatstr.format('tien voor half ' + hour)
    if 22 < minutes < 28:
        return formatstr.format('vijf voor half ' + hour)
    if 27 < minutes < 33:
        return formatstr.format('half ' + hour)
    if 32 < minutes < 38:
        return formatstr.format('vijf over half ' + hour)
    if 37 < minutes < 43:
        return formatstr.format('tien over half ' + hour)
    if 42 < minutes < 48:
        return formatstr.format('kwart voor ' + hour)
    if 47 < minutes < 53:
        return formatstr.format('tien voor ' + hour)
    if 52 < minutes < 58:
        return formatstr.format('vijf voor ' + hour)
    if 57 < minutes < 60:
        return formatstr.format(hour + ' uur')
