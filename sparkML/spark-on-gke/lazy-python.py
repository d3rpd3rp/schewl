cats = ["quarter","stock","date","open","high","low","close","volume","percent_change_price","percent_change_volume_over_last_wk","previous_weeks_volume","next_weeks_open","next_weeks_close",\
        "percent_change_next_weeks_price","days_to_next_dividend","percent_return_next_dividend"]

for name in cats:
    print('public String get' + name + '(){')
    print('    return {};'.format(name))
    print('}')
    print('public String set' + name + '(){')
    print('    this.name = {};'.format(name))
    print('}')