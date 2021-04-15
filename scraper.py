import scraper_functions as sf


def scraper():
    print("start the functions")
    links = sf.get_links()
    data = sf.get_data_frame(links)

    return data
    # Functions

    #    name = pd.DataFrame(data)

    # saving the dataframe
    # df.to_csv('link.csv', index=False)
