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
}

def time_str(hours, minutes):
    hours = hours % 12
    formatstr = 'Het is {}'

    if 0 < minutes < 3:
        return formatstr.format(hour_table[hours] + ' uur')
    if 2 < minutes < 8:
        return formatstr.format('vijf over ' + hour_table[hours])
    if 7 < minutes < 13:
        return formatstr.format('tien over ' + hour_table[hours])
    if 12 < minutes < 18:
        return formatstr.format('kwart over ' + hour_table[hours])
    if 17 < minutes < 23:
        return formatstr.format('tien voor half ' + hour_table[hours+1])
    if 22 < minutes < 28:
        return formatstr.format('vijf voor half ' + hour_table[hours+1])
    if 27 < minutes < 33:
        return formatstr.format('half ' + hour_table[hours+1])
    if 32 < minutes < 38:
        return formatstr.format('vijf over half ' + hour_table[hours+1])
    if 37 < minutes < 43:
        return formatstr.format('tien over half ' + hour_table[hours+1])
    if 42 < minutes < 48:
        return formatstr.format('kwart voor ' + hour_table[hours+1])
    if 47 < minutes < 53:
        return formatstr.format('tien voor ' + hour_table[hours+1])
    if 52 < minutes < 58:
        return formatstr.format('vijf voor ' + hour_table[hours+1])
    if 57 < minutes < 60:
        return formatstr.format(hour_table[hours+1] + ' uur')
