def plot_months(dataset, year):
    df = dataset[(dataset.date.dt.year == 2020)][['month', 'P']].groupby('month').sum().reset_index()
    
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16,6))
    axes[0].bar(df.index, df['P'])
    axes[1].plot(df.index, df['P'].cumsum())

    value = df['P'].mean()
    axes[0].axhline(value, linestyle='--', color='green')
    axes[0].annotate('%0.0f' % value, xy=(1, value), xytext=(8, 0), xycoords=('axes fraction', 'data'), textcoords='offset points')

    value = df['P'].cumsum().max()
    axes[1].annotate('%0.0f' % value, xy=(1, value), xytext=(8, 0), xycoords=('axes fraction', 'data'), textcoords='offset points')

    axes[0].set_title('Generated energy [kWh] per month')
    axes[1].set_title('Total generated energy [kWh] over the year')
    axes[0].set_xlabel('Month')
    axes[1].set_xlabel('Month')
    axes[0].set_ylabel('kWh')
    #axes[1].set_ylabel('kWh')
    axes[0].set_ylim(0, (int(df['P'].max()/100)+2)*100)
    
plot_months(df, year)