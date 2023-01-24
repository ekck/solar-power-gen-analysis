def get_best_day(dataset, year):
    dataset = df[df['date'].dt.year == year]
    dataset = dataset[['date', 'P']].groupby('date').sum()
    return dataset.idxmax()[0].strftime('%Y%m%d')

def plot_a_day(dataset, day):
    day_data = dataset[day:day][['P', 'location']]

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16,6))
    for name in day_data.location.unique():
        axes[0].plot(day_data[day_data.location == name]['P'], label=name, linestyle='dotted')
        axes[1].plot(day_data[day_data.location == name]['P'].cumsum(), label=name, linestyle='dotted')
        value = day_data[day_data.location == name]['P'].cumsum().max()
        plt.annotate('%0.0f' % value, xy=(1, value), xytext=(8, 0), xycoords=('axes fraction', 'data'), textcoords='offset points')

    axes[0].plot(day_data.groupby(day_data.index).sum()['P'], label='total')
    axes[1].plot(day_data.groupby(day_data.index).sum()['P'].cumsum(), label='total')
    value = day_data.groupby(day_data.index).sum()['P'].cumsum().max()
    plt.annotate('%0.0f' % value, xy=(1, value), xytext=(8, 0), xycoords=('axes fraction', 'data'), textcoords='offset points')

    axes[0].legend(loc='upper left')
    axes[1].legend(loc='upper left')
    axes[0].set_title('Generated energy [kWh] per hour (' + day + ')')
    axes[1].set_title('Total generated energy [kWh] over the day (' + day + ')')
    axes[0].xaxis.set_major_formatter(mdates.DateFormatter('%H'))
    axes[1].xaxis.set_major_formatter(mdates.DateFormatter('%H'))

    axes[0].set_xlabel('Hour')
    axes[1].set_xlabel('Hour')
    axes[0].set_ylabel('kWh')
    axes[1].set_ylabel('kWh')

 
best_day = get_best_day(df, 2020)
plot_a_day(df, best_day)