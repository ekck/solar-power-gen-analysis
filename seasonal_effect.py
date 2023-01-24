def get_best_day_of_season(df, year, season):
    return df[(df.date.dt.year == year) & (df.season == season)][['date', 'P']].groupby('date').sum(). \
           idxmax()[0].strftime('%Y%m%d')

def plot_day_extended(dataset, day, fig, ax1, title, ymax):
    dataset_one_day = dataset[day:day]

    ax2 = ax1.twinx()
    ax1.fill(dataset_one_day.index, dataset_one_day.elevation.clip(0), color = 'wheat', ls='--', label='Sun elevation')
    ax1.plot(dataset_one_day.index, dataset_one_day.zenith, color = 'cyan', label='Sun Zenith')
    for name in dataset_one_day.location.unique():
        ax2.plot(dataset_one_day[dataset_one_day.location == name]['P'].cumsum(), label=name)
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    ax1.set_title(title + ' (' + day[6:9] + '/' + str(day)[4:6] + ')')
    ax1.set_ylim(0,150)
    ax2.set_ylim(0,ymax)
    myFmt = mdates.DateFormatter('%H')
    ax1.xaxis.set_major_formatter(myFmt)

def plot_seasons(dataset, year):
    dataset = dataset[(dataset['date'].dt.year == year)].sort_values(['time', 'location'])
    maxval = dataset[['date', 'location', 'P']].groupby(['date', 'location']).sum().max()[0]
    maxval = int((maxval/10) + 1)*10

    fig, axs = plt.subplots(2, 2, figsize = (12, 10))
    fig.patch.set_facecolor('xkcd:light gray')

    plot_day_extended(dataset, get_best_day_of_season(dataset, year, 1), fig, axs[0,0], 'winter', maxval)
    plot_day_extended(dataset, get_best_day_of_season(dataset, year, 2), fig, axs[0,1], 'autumn', maxval)
    plot_day_extended(dataset, get_best_day_of_season(dataset, year, 3), fig, axs[1,0], 'summer', maxval)
    plot_day_extended(dataset, get_best_day_of_season(dataset, year, 4), fig, axs[1,1], 'fall', maxval)

plot_seasons(df, 2020)