from scraper import setup, scrap, debug_feedback

#-- MAIN --
if __name__ == "__main__":
    setup(
        browser_path="C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe",
        mode="chrome",
        
        # no tocar
        rate_limit=14,
        feedback=debug_feedback,

        # archivar o recopilar enlaces sin archivar (lo segundo es mucho más rápido)
        archive=False
    )

    with open("url_list.txt", "r") as file:
        url_list = file.read().splitlines()
    # print(url_list)
    scrap(url_list, start=None, end=None)