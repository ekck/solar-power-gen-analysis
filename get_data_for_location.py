def get_data_for_location(lat, lon, panels,
                          startdate = pd.Timestamp('2005-01-01'), enddate = pd.Timestamp('2020-12-31')):
    """
    Determine the solarradiation and generated power for a given solar panel configuration.
    For each hour between startdate and enddate the data is retrieved and calculated.
    :param lat: Latitude of the location
    :param lon: Longitude of the location
    :param panels: panel locations
    :return: 
    """
    poas = {}
    poalist = []
    for panel in panels:
        poa = obtain_panel_power_data(lat, lon, startdate, enddate, 
                                      panel['name'], panel['tilt'], panel['azimuth'], panel['nopanels'], panel['power'])
        poas[panel['name']] = poa
        poalist.append(poa)
                          
    dataset = pd.concat(poalist).sort_index()
    
    dataset = pd.merge(
        pvlib.solarposition.get_solarposition(dataset.index.unique(), lat, lon)[['zenith', 'elevation', 'azimuth']], 
        dataset,
        left_index=True, right_index=True).drop_duplicates()
    dataset = dataset.sort_values(['time', 'location'])
    dataset['month'] = dataset.index.month
    dataset['season'] = 1 + (dataset.month - 1) // 3
    return dataset