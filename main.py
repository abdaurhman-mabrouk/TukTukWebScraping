import os, sys
import datetime
import json
import requests
from bs4 import BeautifulSoup
from colorama import init
from termcolor import colored

# Initialize colorama
init()


# The Main Program Function
def main():

    # Function For Movies Scraping By Number of Page
    def scrapeMovies():

        print("if You Want to Select All Pages Type '*' \n")

        pageNum = input("Select Page Number: ")
        moviesQuantity = input("Select Movies Quantity That You Want (1 : 30): ")

        if pageNum == "*" or pageNum == "":

            print(
                "You going To Scrape All of The Pages of This Website, So This May Take a Sevral Minutes."
            )

            pageNum = 1
            mainPage = requests.get(
                f"https://t40.tuktukcinema1.buzz/category/movies-1/",
                timeout=3,
            )
            pagesNum = int(
                BeautifulSoup(mainPage.content, "html.parser")
                .find("ul", {"class": "page-numbers"})
                .find_all("li")[-2]
                .find("a")
                .text.strip()
            )
        else:
            int(pageNum)
            pagesNum = 1

        mainPage = requests.get(
            f"https://t40.tuktukcinema1.buzz/category/movies-1/?page={pageNum}",
            timeout=3,
        )

        src = mainPage.content
        soup = BeautifulSoup(src, "html.parser")
        moviesList = soup.find("ul", {"class": "Blocks--List"})
        resultsGenre = (
            soup.find("div", {"class": "archiveTitle"}).find("h1").text.strip()
        )
        moviesDivs = moviesList.find_all("div", {"class": "Block--Item"})

        # Checking of The Wanted Movies Quantity
        if moviesQuantity == "" or moviesQuantity is None:
            moviesNum = len(moviesDivs)
        else:
            moviesNum = int(moviesQuantity)

        # Looping Over Movies Pages
        for i in range(pagesNum):
            print(f"Page Number: {i}")
            # Looping Over Each Movie Details
            for j in range(moviesNum):

                # Movie Page Link
                moviePageLink = moviesDivs[j].find("a").get("href")
                moviePageRes = requests.get(moviePageLink, timeout=3)
                moviePageElements = moviePageRes.content
                soup = BeautifulSoup(moviePageElements, "html.parser")

                # Movie Div
                movieDiv = soup.find("div", {"class": "MainSingle"})

                # Movie Number
                movieNum = j

                # Movie Name
                def movieName():
                    if (
                        movieDiv.find("div", {"class": "MasterSingleMeta"})
                    ) is not None:
                        if (
                            movieDiv.find("div", {"class": "MasterSingleMeta"}).find(
                                "h1"
                            )
                        ) is not None:
                            if (
                                movieDiv.find("div", {"class": "MasterSingleMeta"})
                                .find("h1")
                                .find("a")
                            ) is not None:
                                return (
                                    movieDiv.find("div", {"class": "MasterSingleMeta"})
                                    .find("h1")
                                    .find("a")
                                    .text
                                )
                            return "Not Found"
                        return "Not Found"
                    return "Not Found"

                movieName = movieName()

                # Movie Image Link
                def movieIamgeLink():
                    if (movieDiv.find("div", {"class": "left"})) is not None:
                        if (
                            movieDiv.find("div", {"class": "left"}).find(
                                "div", {"class": "image"}
                            )
                        ) is not None:
                            if (
                                movieDiv.find("div", {"class": "left"})
                                .find("div", {"class": "image"})
                                .find("img")
                                .get("src")
                            ) is not None:
                                return (
                                    movieDiv.find("div", {"class": "left"})
                                    .find("div", {"class": "image"})
                                    .find("img")
                                    .get("src")
                                )
                            return "Not Found"
                        return "Not Found"
                    return "Not Found"

                movieImageLink = movieIamgeLink()

                # Movie Story
                def movieStory():
                    if (
                        movieDiv.find("div", {"class": "MasterSingleMeta"})
                    ) is not None:
                        if (
                            movieDiv.find("div", {"class": "MasterSingleMeta"}).find(
                                "div", {"class": "story"}
                            )
                        ) is not None:
                            if (
                                movieDiv.find("div", {"class": "MasterSingleMeta"})
                                .find("div", {"class": "story"})
                                .find("p")
                            ) is not None:
                                return (
                                    movieDiv.find("div", {"class": "MasterSingleMeta"})
                                    .find("div", {"class": "story"})
                                    .find("p")
                                ).text
                            return "Not Found"
                        return "Not Found"
                    return "Not Found"

                movieStory = movieStory()

                # Movie Type
                def movieType():
                    if (
                        movieDiv.find("div", {"class": "MasterSingleMeta"})
                    ) is not None:
                        if (
                            movieDiv.find("div", {"class": "MasterSingleMeta"}).find(
                                "div", {"class": "MediaQueryRight"}
                            )
                        ) is not None:
                            if (
                                movieDiv.find("div", {"class": "MasterSingleMeta"})
                                .find("div", {"class": "MediaQueryRight"})
                                .find("div", {"class": "catssection"})
                            ) is not None:
                                if (
                                    movieDiv.find("div", {"class": "MasterSingleMeta"})
                                    .find("div", {"class": "MediaQueryRight"})
                                    .find("div", {"class": "catssection"})
                                    .find_all("li")[0]
                                ) is not None:
                                    if (
                                        movieDiv.find(
                                            "div", {"class": "MasterSingleMeta"}
                                        )
                                        .find("div", {"class": "MediaQueryRight"})
                                        .find("div", {"class": "catssection"})
                                        .find_all("li")[0]
                                        .find_all("a")
                                    ) is not None:
                                        types = (
                                            movieDiv.find(
                                                "div", {"class": "MasterSingleMeta"}
                                            )
                                            .find("div", {"class": "MediaQueryRight"})
                                            .find("div", {"class": "catssection"})
                                            .find_all("li")[0]
                                            .find_all("a")
                                        )
                                        typesNum = len(types)
                                        for g in range(typesNum):
                                            return f"'{types[g].text}',"
                                    return "Not Found"
                                return "Not Found"
                            return "Not Found"
                        return "Not Found"
                    return "Not Found"

                movieType = movieType()

                # Movie Genres
                def movieGenres():
                    if (
                        movieDiv.find("div", {"class": "MasterSingleMeta"})
                    ) is not None:
                        if (
                            movieDiv.find("div", {"class": "MasterSingleMeta"}).find(
                                "div", {"class": "MediaQueryRight"}
                            )
                        ) is not None:
                            if (
                                movieDiv.find("div", {"class": "MasterSingleMeta"})
                                .find("div", {"class": "MediaQueryRight"})
                                .find("div", {"class": "catssection"})
                            ) is not None:
                                if (
                                    movieDiv.find("div", {"class": "MasterSingleMeta"})
                                    .find("div", {"class": "MediaQueryRight"})
                                    .find("div", {"class": "catssection"})
                                    .find_all("li")[1]
                                ) is not None:
                                    if (
                                        movieDiv.find(
                                            "div", {"class": "MasterSingleMeta"}
                                        )
                                        .find("div", {"class": "MediaQueryRight"})
                                        .find("div", {"class": "catssection"})
                                        .find_all("li")[1]
                                        .find_all("a")
                                    ) is not None:
                                        genres = (
                                            movieDiv.find(
                                                "div", {"class": "MasterSingleMeta"}
                                            )
                                            .find("div", {"class": "MediaQueryRight"})
                                            .find("div", {"class": "catssection"})
                                            .find_all("li")[1]
                                            .find_all("a")
                                        )
                                        genresNum = len(genres)
                                        for g in range(genresNum):
                                            return f"'{genres[g].text}',"
                                    return "Not Found"
                                return "Not Found"
                            return "Not Found"
                        return "Not Found"
                    return "Not Found"

                movieGenres = movieGenres()

                movieDataNum = len(
                    movieDiv.find("div", {"class": "MasterSingleMeta"})
                    .find("div", {"class": "MediaQueryRight"})
                    .find("ul", {"class": "RightTaxContent"})
                    .find_all("li")
                )

                if movieDataNum >= 8:
                    # Movie Time
                    def movieTime():
                        if (
                            movieDiv.find("div", {"class": "MasterSingleMeta"})
                        ) is not None:
                            if (
                                movieDiv.find(
                                    "div", {"class": "MasterSingleMeta"}
                                ).find("div", {"class": "MediaQueryRight"})
                            ) is not None:
                                if (
                                    movieDiv.find("div", {"class": "MasterSingleMeta"})
                                    .find("div", {"class": "MediaQueryRight"})
                                    .find("ul", {"class": "RightTaxContent"})
                                ) is not None:
                                    if (
                                        movieDiv.find(
                                            "div", {"class": "MasterSingleMeta"}
                                        )
                                        .find("div", {"class": "MediaQueryRight"})
                                        .find("ul", {"class": "RightTaxContent"})
                                        .find_all("li")[0]
                                    ) is not None:
                                        if (
                                            movieDiv.find(
                                                "div", {"class": "MasterSingleMeta"}
                                            )
                                            .find("div", {"class": "MediaQueryRight"})
                                            .find("ul", {"class": "RightTaxContent"})
                                            .find_all("li")[0]
                                            .find("strong")
                                        ) is not None:
                                            return (
                                                movieDiv.find(
                                                    "div", {"class": "MasterSingleMeta"}
                                                )
                                                .find(
                                                    "div", {"class": "MediaQueryRight"}
                                                )
                                                .find(
                                                    "ul", {"class": "RightTaxContent"}
                                                )
                                                .find_all("li")[0]
                                                .find("strong")
                                                .text
                                            )
                                        return "Not Found"
                                    return "Not Found"
                                return "Not Found"
                            return "Not Found"
                        return "Not Found"

                    movieTime = movieTime()

                    # Movie Date
                    def movieDate():
                        if (
                            movieDiv.find("div", {"class": "MasterSingleMeta"})
                        ) is not None:
                            if (
                                movieDiv.find(
                                    "div", {"class": "MasterSingleMeta"}
                                ).find("div", {"class": "MediaQueryRight"})
                            ) is not None:
                                if (
                                    movieDiv.find("div", {"class": "MasterSingleMeta"})
                                    .find("div", {"class": "MediaQueryRight"})
                                    .find("ul", {"class": "RightTaxContent"})
                                ) is not None:
                                    if (
                                        movieDiv.find(
                                            "div", {"class": "MasterSingleMeta"}
                                        )
                                        .find("div", {"class": "MediaQueryRight"})
                                        .find("ul", {"class": "RightTaxContent"})
                                        .find_all("li")[1]
                                    ) is not None:
                                        if (
                                            movieDiv.find(
                                                "div", {"class": "MasterSingleMeta"}
                                            )
                                            .find("div", {"class": "MediaQueryRight"})
                                            .find("ul", {"class": "RightTaxContent"})
                                            .find_all("li")[1]
                                            .find("a")
                                        ) is not None:
                                            return (
                                                movieDiv.find(
                                                    "div", {"class": "MasterSingleMeta"}
                                                )
                                                .find(
                                                    "div", {"class": "MediaQueryRight"}
                                                )
                                                .find(
                                                    "ul", {"class": "RightTaxContent"}
                                                )
                                                .find_all("li")[1]
                                                .find("a")
                                                .text
                                            )
                                        return "Not Found"
                                    return "Not Found"
                                return "Not Found"
                            return "Not Found"
                        return "Not Found"

                    movieDate = movieDate()

                    # Movie Languages
                    def movieLanguages():
                        if (
                            movieDiv.find("div", {"class": "MasterSingleMeta"})
                        ) is not None:
                            if (
                                movieDiv.find(
                                    "div", {"class": "MasterSingleMeta"}
                                ).find("div", {"class": "MediaQueryRight"})
                            ) is not None:
                                if (
                                    movieDiv.find("div", {"class": "MasterSingleMeta"})
                                    .find("div", {"class": "MediaQueryRight"})
                                    .find("ul", {"class": "RightTaxContent"})
                                ) is not None:
                                    if (
                                        movieDiv.find(
                                            "div", {"class": "MasterSingleMeta"}
                                        )
                                        .find("div", {"class": "MediaQueryRight"})
                                        .find("ul", {"class": "RightTaxContent"})
                                        .find_all("li")[2]
                                    ) is not None:
                                        if (
                                            movieDiv.find(
                                                "div", {"class": "MasterSingleMeta"}
                                            )
                                            .find("div", {"class": "MediaQueryRight"})
                                            .find("ul", {"class": "RightTaxContent"})
                                            .find_all("li")[2]
                                            .find("a")
                                        ) is not None:
                                            return (
                                                movieDiv.find(
                                                    "div", {"class": "MasterSingleMeta"}
                                                )
                                                .find(
                                                    "div", {"class": "MediaQueryRight"}
                                                )
                                                .find(
                                                    "ul", {"class": "RightTaxContent"}
                                                )
                                                .find_all("li")[2]
                                                .find("a")
                                                .text
                                            )
                                        return "Not Found"
                                    return "Not Found"
                                return "Not Found"
                            return "Not Found"
                        return "Not Found"

                    movieLanguages = movieLanguages()

                    # Movie Quality
                    def movieQuality():
                        if (
                            movieDiv.find("div", {"class": "MasterSingleMeta"})
                        ) is not None:
                            if (
                                movieDiv.find(
                                    "div", {"class": "MasterSingleMeta"}
                                ).find("div", {"class": "MediaQueryRight"})
                            ) is not None:
                                if (
                                    movieDiv.find("div", {"class": "MasterSingleMeta"})
                                    .find("div", {"class": "MediaQueryRight"})
                                    .find("ul", {"class": "RightTaxContent"})
                                ) is not None:
                                    if (
                                        movieDiv.find(
                                            "div", {"class": "MasterSingleMeta"}
                                        )
                                        .find("div", {"class": "MediaQueryRight"})
                                        .find("ul", {"class": "RightTaxContent"})
                                        .find_all("li")[3]
                                    ) is not None:
                                        if (
                                            movieDiv.find(
                                                "div", {"class": "MasterSingleMeta"}
                                            )
                                            .find("div", {"class": "MediaQueryRight"})
                                            .find("ul", {"class": "RightTaxContent"})
                                            .find_all("li")[3]
                                            .find("a")
                                        ) is not None:
                                            return (
                                                movieDiv.find(
                                                    "div", {"class": "MasterSingleMeta"}
                                                )
                                                .find(
                                                    "div", {"class": "MediaQueryRight"}
                                                )
                                                .find(
                                                    "ul", {"class": "RightTaxContent"}
                                                )
                                                .find_all("li")[3]
                                                .find("a")
                                                .text
                                            )
                                        return "Not Found"
                                    return "Not Found"
                                return "Not Found"
                            return "Not Found"
                        return "Not Found"

                    movieQuality = movieQuality()

                    # Movie Countries
                    def movieCountries():
                        if (
                            movieDiv.find("div", {"class": "MasterSingleMeta"})
                        ) is not None:
                            if (
                                movieDiv.find(
                                    "div", {"class": "MasterSingleMeta"}
                                ).find("div", {"class": "MediaQueryRight"})
                            ) is not None:
                                if (
                                    movieDiv.find("div", {"class": "MasterSingleMeta"})
                                    .find("div", {"class": "MediaQueryRight"})
                                    .find("ul", {"class": "RightTaxContent"})
                                ) is not None:
                                    if (
                                        movieDiv.find(
                                            "div", {"class": "MasterSingleMeta"}
                                        )
                                        .find("div", {"class": "MediaQueryRight"})
                                        .find("ul", {"class": "RightTaxContent"})
                                        .find_all("li")[4]
                                    ) is not None:
                                        if (
                                            movieDiv.find(
                                                "div", {"class": "MasterSingleMeta"}
                                            )
                                            .find("div", {"class": "MediaQueryRight"})
                                            .find("ul", {"class": "RightTaxContent"})
                                            .find_all("li")[4]
                                            .find_all("a")
                                        ) is not None:
                                            countries = (
                                                movieDiv.find(
                                                    "div", {"class": "MasterSingleMeta"}
                                                )
                                                .find(
                                                    "div", {"class": "MediaQueryRight"}
                                                )
                                                .find(
                                                    "ul", {"class": "RightTaxContent"}
                                                )
                                                .find_all("li")[4]
                                                .find_all("a")
                                            )
                                            countriesNum = len(countries)
                                            for c in range(countriesNum):
                                                return f"'{countries[c].text}',"
                                        return "Not Found"
                                    return "Not Found"
                                return "Not Found"
                            return "Not Found"
                        return "Not Found"

                    movieCountries = movieCountries()

                    # Movie Outputers
                    def movieOutputers():
                        if (
                            movieDiv.find("div", {"class": "MasterSingleMeta"})
                        ) is not None:
                            if (
                                movieDiv.find(
                                    "div", {"class": "MasterSingleMeta"}
                                ).find("div", {"class": "MediaQueryRight"})
                            ) is not None:
                                if (
                                    movieDiv.find("div", {"class": "MasterSingleMeta"})
                                    .find("div", {"class": "MediaQueryRight"})
                                    .find("ul", {"class": "RightTaxContent"})
                                ) is not None:
                                    if (
                                        movieDiv.find(
                                            "div", {"class": "MasterSingleMeta"}
                                        )
                                        .find("div", {"class": "MediaQueryRight"})
                                        .find("ul", {"class": "RightTaxContent"})
                                        .find_all("li")[5]
                                    ) is not None:
                                        if (
                                            movieDiv.find(
                                                "div", {"class": "MasterSingleMeta"}
                                            )
                                            .find("div", {"class": "MediaQueryRight"})
                                            .find("ul", {"class": "RightTaxContent"})
                                            .find_all("li")[5]
                                            .find_all("a")
                                        ) is not None:
                                            outputers = (
                                                movieDiv.find(
                                                    "div", {"class": "MasterSingleMeta"}
                                                )
                                                .find(
                                                    "div", {"class": "MediaQueryRight"}
                                                )
                                                .find(
                                                    "ul", {"class": "RightTaxContent"}
                                                )
                                                .find_all("li")[5]
                                                .find_all("a")
                                            )
                                            outputersNum = len(outputers)
                                            for t in range(outputersNum):
                                                return f"'{outputers[t].text}',"
                                        return "Not Found"
                                    return "Not Found"
                                return "Not Found"
                            return "Not Found"
                        return "Not Found"

                    movieOutputers = movieOutputers()

                    # Movie Directors
                    def movieDirectors():
                        if (
                            movieDiv.find("div", {"class": "MasterSingleMeta"})
                        ) is not None:
                            if (
                                movieDiv.find(
                                    "div", {"class": "MasterSingleMeta"}
                                ).find("div", {"class": "MediaQueryRight"})
                            ) is not None:
                                if (
                                    movieDiv.find("div", {"class": "MasterSingleMeta"})
                                    .find("div", {"class": "MediaQueryRight"})
                                    .find("ul", {"class": "RightTaxContent"})
                                ) is not None:
                                    if (
                                        movieDiv.find(
                                            "div", {"class": "MasterSingleMeta"}
                                        )
                                        .find("div", {"class": "MediaQueryRight"})
                                        .find("ul", {"class": "RightTaxContent"})
                                        .find_all("li")[6]
                                    ) is not None:
                                        if (
                                            movieDiv.find(
                                                "div", {"class": "MasterSingleMeta"}
                                            )
                                            .find("div", {"class": "MediaQueryRight"})
                                            .find("ul", {"class": "RightTaxContent"})
                                            .find_all("li")[6]
                                            .find_all("a")
                                        ) is not None:
                                            directors = (
                                                movieDiv.find(
                                                    "div", {"class": "MasterSingleMeta"}
                                                )
                                                .find(
                                                    "div", {"class": "MediaQueryRight"}
                                                )
                                                .find(
                                                    "ul", {"class": "RightTaxContent"}
                                                )
                                                .find_all("li")[6]
                                                .find_all("a")
                                            )
                                            directorsNum = len(directors)
                                            for t in range(directorsNum):
                                                return f"'{directors[t].text}',"
                                        return "Not Found"
                                    return "Not Found"
                                return "Not Found"
                            return "Not Found"
                        return "Not Found"

                    movieDirectors = movieDirectors()

                    # Movie actors
                    def movieActors():
                        if (
                            movieDiv.find("div", {"class": "MasterSingleMeta"})
                        ) is not None:
                            if (
                                movieDiv.find(
                                    "div", {"class": "MasterSingleMeta"}
                                ).find("div", {"class": "MediaQueryRight"})
                            ) is not None:
                                if (
                                    movieDiv.find("div", {"class": "MasterSingleMeta"})
                                    .find("div", {"class": "MediaQueryRight"})
                                    .find("ul", {"class": "RightTaxContent"})
                                ) is not None:
                                    if (
                                        movieDiv.find(
                                            "div", {"class": "MasterSingleMeta"}
                                        )
                                        .find("div", {"class": "MediaQueryRight"})
                                        .find("ul", {"class": "RightTaxContent"})
                                        .find_all("li")[7]
                                    ) is not None:
                                        if (
                                            movieDiv.find(
                                                "div", {"class": "MasterSingleMeta"}
                                            )
                                            .find("div", {"class": "MediaQueryRight"})
                                            .find("ul", {"class": "RightTaxContent"})
                                            .find_all("li")[7]
                                            .find_all("a")
                                        ) is not None:
                                            actors = (
                                                movieDiv.find(
                                                    "div", {"class": "MasterSingleMeta"}
                                                )
                                                .find(
                                                    "div", {"class": "MediaQueryRight"}
                                                )
                                                .find(
                                                    "ul", {"class": "RightTaxContent"}
                                                )
                                                .find_all("li")[7]
                                                .find_all("a")
                                            )
                                            actorsNum = len(actors)
                                            for t in range(actorsNum):
                                                return f"'{actors[t].text}',"
                                        return "Not Found"
                                    return "Not Found"
                                return "Not Found"
                            return "Not Found"
                        return "Not Found"

                    movieActors = movieActors()

                else:
                    pass

                # Movie Watching and Downloading Link
                def movieVideoLink():
                    if (
                        movieDiv.find("div", {"class": "MasterSingleMeta"})
                    ) is not None:
                        if (
                            movieDiv.find("div", {"class": "MasterSingleMeta"}).find(
                                "div", {"class": "MediaQueryLeft"}
                            )
                        ) is not None:
                            if (
                                movieDiv.find("div", {"class": "MasterSingleMeta"})
                                .find("div", {"class": "MediaQueryLeft"})
                                .find("div", {"class": "right"})
                            ) is not None:
                                if (
                                    movieDiv.find("div", {"class": "MasterSingleMeta"})
                                    .find("div", {"class": "MediaQueryLeft"})
                                    .find("div", {"class": "right"})
                                    .find("a")
                                ) is not None:
                                    return (
                                        movieDiv.find(
                                            "div", {"class": "MasterSingleMeta"}
                                        )
                                        .find("div", {"class": "MediaQueryLeft"})
                                        .find("div", {"class": "right"})
                                        .find("a")
                                        .get("href")
                                    )
                                return "Not Found"
                            return "Not Found"
                        return "Not Found"
                    return "Not Found"

                movieVideoLink = movieVideoLink()

                # Write The Movies Scraped Data To a File.txt
                with open(
                    "Movies_Scraped_Data.txt", "a", encoding="utf-8"
                ) as f:
                    f.write("__" * 160)
                    f.write("\n")
                    f.write(f"Website Link: 'https://t40.tuktukcinema1.buzz' \n")
                    f.write(f"Website Name: 'TukTuk Cinema' \n")
                    f.write(f"Results Genre: '{resultsGenre}' \n")
                    f.write(f"Page Number: {pageNum} \n")
                    f.write(f"Movie Number: '{movieNum}' \n")
                    f.write(f"Movie Name: '{movieName}' \n")
                    f.write(f"Movie Link: '{moviePageLink}' \n")
                    f.write(f"Movie Image Link: '{movieImageLink}' \n")
                    f.write(f"Movie Story: '{movieStory}' \n")
                    f.write(f"Movie Type: {movieType} \n")
                    f.write(f"Movie Genres: {movieGenres} \n")
                    f.write(f"movie Time: '{movieTime}' \n")
                    f.write(f"movie Date: '{movieDate}' \n")
                    f.write(f"movie Languages: '{movieLanguages}' \n")
                    f.write(f"movie Quality: '{movieQuality}' \n")
                    f.write(f"movie Countries: '{movieCountries}' \n")
                    f.write(f"movie Outputers: '{movieOutputers}' \n")
                    f.write(f"movie Directors: '{movieDirectors}' \n")
                    f.write(f"movie Actors: '{movieActors}' \n")
                    f.write(f"movie Watching Link: '{movieVideoLink}' \n")
                    f.write("__" * 160)
                    f.write("\n")
                    f.close()

                # Print The Scraped Movies Data
                print("\n")
                print("__" * 160)
                print(f"Results Genre: '{resultsGenre}' \n")
                print(f"Page Number: {pageNum}")
                print(f"Movie Number: {movieNum} ")
                print(f"Movie Name: {movieName} ")
                print(f"Movie Page Link: {moviePageLink} ")
                print(f"Movie Image Link: {movieImageLink} ")
                print(f"Movie Story: {movieStory} ")
                print(f"Movie Type: {movieType} ")
                print(f"Movie Genres: {movieGenres} ")
                print(f"Movie Time: {movieTime} ")
                print(f"Movie Date: {movieDate} ")
                print(f"movie Languages: '{movieLanguages}' ")
                print(f"Movie Quality: {movieQuality} ")
                print(f"Movie Countries: {movieCountries} ")
                print(f"Movie Outputers: {movieOutputers} ")
                print(f"movie Directors: {movieDirectors} ")
                print(f"movie Actors: {movieActors} ")
                print(f"Movie Watching Link: '{movieVideoLink}' \n")
                print("__" * 160)
                print("\n")

            if pagesNum is None:
                pagesNum = 403

            if pageNum == "*":
                pageNum += 1

        print("The Data Scraping is Done.")
        print(
            "The Scraped Data File Path: 'F:/CODING/projects/Python/TukTukCinemaScraping/Movies_Scraped_Data.txt'"
        )
        scrapeMovies()

    # Function For Scrape The Recents of The Website (TukTuk Cinema)
    def scrapeSeries():
        seriesPage = requests.get(
            f"https://t40.tuktukcinema1.buzz/sercat/%d9%85%d8%b3%d9%84%d8%b3%d9%84%d8%a7%d8%aa-%d8%a7%d8%ac%d9%86%d8%a8%d9%8a/",
            timeout=3,
        )
        src = seriesPage.content
        soup = BeautifulSoup(src, "html.parser")
        seriesList = soup.find("ul", {"class": "Blocks--List"})
        seriesDivs = seriesList.find_all("div", {"class": "Block--Item"})

        seriesNum = len(seriesDivs)

        # Looping Over Each Series Details
        for i in range(seriesNum):

            # Series Page Link
            seriesPageLink = seriesDivs[i].find("a").get("href")
            seriesPageRes = requests.get(seriesPageLink, timeout=3)
            seriesPageElements = seriesPageRes.content
            soup = BeautifulSoup(seriesPageElements, "html.parser")

            seriesLink = seriesPageLink

            seriesDiv = soup.find("div", {"class": "MainSingle"})

            seriesImageLink = (
                seriesDiv.find("div", {"class": "left"})
                .find("div", {"class": "image"})
                .find("img")
                .get("src")
            )
            seriesName = (
                soup.find("div", {"class": "MasterSingleMeta"})
                .find("h1")
                .find("a")
                .text
            )
            seriesStory = (
                soup.find("div", {"class": "MasterSingleMeta"})
                .find("div", {"class": "story"})
                .find("p")
                .text
            )

            seriesWDLink = (
                soup.find("div", {"class": "MasterSingleMeta"})
                .find("div", {"class": "MediaQueryLeft"})
                .find("div", {"class": "right"})
                .find("a")
                .get("href")
            )

            print(f"Series Link: '{seriesLink}'")
            print(f"Series Name: '{seriesName}'")
            print(f"Series Story: '{seriesStory}'")
            print(f"Series Image Link: '{seriesImageLink}'")
            print(f"Series Watch and Download Link: '{seriesWDLink}'")
            print("\n")

    # Function For Animes Scraping
    def scrapeAnimes():

        pageNum = 1
        animesPage = requests.get(
            f"https://t40.tuktukcinema1.buzz/sercat/%D9%82%D8%A7%D8%A6%D9%85%D8%A9-%D8%A7%D9%84%D8%A7%D9%86%D9%85%D9%8A/?page={pageNum}",
            timeout=3,
        )
        animesPageElement = animesPage.content

        soup = BeautifulSoup(animesPageElement, "html.parser")
        animesList = soup.find("ul", {"class": "Blocks--List"})
        animesDivs = animesList.find_all("div", {"class": "Block--Item"})

        animesDivsNum = len(animesDivs)
        pagesNum = int(
            soup.find("ul", {"class": "page-numbers"}).find_all("li")[-2].find("a").text
        )

        print(colored(pagesNum, "yellow"))

        for p in range(pagesNum):
            for d in range(animesDivsNum):
                animeName = (
                    animesDivs[d]
                    .find("a")
                    .find("div", {"class": "Block--Info"})
                    .find("h3")
                    .text
                )
                print(f"{p}.{d} '{animeName}'")

            pageNum += 1
            animesPage = requests.get(
                f"https://t40.tuktukcinema1.buzz/sercat/%D9%82%D8%A7%D8%A6%D9%85%D8%A9-%D8%A7%D9%84%D8%A7%D9%86%D9%85%D9%8A/?page={pageNum}",
                timeout=3,
            )
            animesPageElement = animesPage.content
            soup = BeautifulSoup(animesPageElement, "html.parser")

            animesList = soup.find("ul", {"class": "Blocks--List"})
            animesDivs = animesList.find_all("div", {"class": "Block--Item"})

            # Check if this is The Last Page of Animes List Pages
            animesDivsNum = len(animesDivs)

    # Function For Scrape The Recents of The Website (TukTuk Cinema)
    def scrapeRecents():
        recentsPage = requests.get(
            "https://t40.tuktukcinema1.buzz/recent/",
            timeout=3,
        )
        src = recentsPage.content
        soup = BeautifulSoup(src, "html.parser")
        recentsList = soup.find("ul", {"class": "Blocks--List"})
        recentsDivs = recentsList.find_all("div", {"class": "Block--Item"})

        recentsNum = len(recentsDivs)

        # Looping Over Each Movie Details
        for i in range(recentsNum):

            # Movie Page Link
            recentPageLink = recentsDivs[i].find("a").get("href")
            recentPageRes = requests.get(recentPageLink, timeout=2)
            recentPageElements = recentPageRes.content
            soup = BeautifulSoup(recentPageElements, "html.parser")

            recentLink = recentPageLink

            recentDiv = soup.find("div", {"class": "MainSingle"})

            recentImageLink = (
                recentDiv.find("div", {"class": "left"})
                .find("div", {"class": "image"})
                .find("img")
                .get("src")
            )
            recentName = (
                soup.find("div", {"class": "MasterSingleMeta"})
                .find("h1")
                .find("a")
                .text
            )
            recentStory = (
                soup.find("div", {"class": "MasterSingleMeta"})
                .find("div", {"class": "story"})
                .find("p")
                .text
            )

            recentWDLink = (
                soup.find("div", {"class": "MasterSingleMeta"})
                .find("div", {"class": "MediaQueryLeft"})
                .find("div", {"class": "right"})
                .find("a")
                .get("href")
            )

            print(f"Recent Link: '{recentLink}'")
            print(f"Recent Name: '{recentName}'")
            print(f"Recent Story: '{recentStory}'")
            print(f"Recent Image Link: '{recentImageLink}'")
            print(f"Recent Watch and Download Link: '{recentWDLink}'")
            print("\n")

    # Function For TVShows Scraping
    def scrapeTvShows():
        showsPage = requests.get(
            f"https://t40.tuktukcinema1.buzz/sercat/%d8%a8%d8%b1%d8%a7%d9%85%d8%ac-%d8%aa%d9%84%d9%81%d8%b2%d9%8a%d9%88%d9%86%d9%8a%d8%a9/",
            timeout=3,
        )
        src = showsPage.content
        soup = BeautifulSoup(src, "html.parser")
        showsList = soup.find("ul", {"class": "Blocks--List"})
        showsDivs = showsList.find_all("div", {"class": "Block--Item"})

        showsNum = len(showsDivs)
        pagesNum = int(
            soup.find("ul", {"class": "page-numbers"}).find_all("li")[-2].text.strip()
        )
        # Loop Over Each Page Content
        for p in range(pagesNum):

            print(f"TV Shows Pages Number: {pagesNum} \n")

            print(f"Page Number: {p}")
            print(f"Page Shows Number: {showsNum}")
            print(f"\n")

            # Looping Over Each Show Details
            for i in range(showsNum):

                # TV Show Page Link
                showPageLink = showsDivs[i].find("a").get("href")
                showPageRes = requests.get(showPageLink, timeout=3)
                showPageElements = showPageRes.content
                soup = BeautifulSoup(showPageElements, "html.parser")
                showLink = showPageLink

                showDiv = soup.find("div", {"class": "MainSingle"})

                showImageLink = (
                    showDiv.find("div", {"class": "left"})
                    .find("div", {"class": "image"})
                    .find("img")
                    .get("src")
                )

                showName = (
                    soup.find("div", {"class": "MasterSingleMeta"})
                    .find("h1")
                    .find("a")
                    .text
                )

                showStory = (
                    soup.find("div", {"class": "MasterSingleMeta"})
                    .find("div", {"class": "story"})
                    .find("p")
                    .text
                )

                print(f"Show Link: '{showLink}'")
                print(f"Show Name: '{showName}'")
                print(f"Show Story: '{showStory}'")
                print(f"Show Image Link: '{showImageLink}'")
                print("\n")

            showsPage = requests.get(
                f"https://t40.tuktukcinema1.buzz/sercat/%d8%a8%d8%b1%d8%a7%d9%85%d8%ac-%d8%aa%d9%84%d9%81%d8%b2%d9%8a%d9%88%d9%86%d9%8a%d8%a9/?page={p}",
                timeout=3,
            )
            main()

    # Function For Scarping By Searching Keyword
    def searchScrape():
        searchKeyword = input("Enter The Search Keyword: ")

        searchUrl = f"https://t40.tuktukcinema1.buzz/?s={searchKeyword}"
        searchPageRes = requests.get(searchUrl, timeout=5)
        searchPageElements = BeautifulSoup(searchPageRes.content, "html.parser")

        searchPageResults = searchPageElements.find("ul", {"class": "Blocks--List"})
        resultsDivs = searchPageResults.find_all("div", {"class": "Block--Item"})
        resultsPagesNum = searchPageElements.find("ul", {"class": "page-numbers"})

        # Checking Results Pages Number is Greater Than 1
        if resultsPagesNum is not None:
            resultsPagesNum = len(
                searchPageElements.find("ul", {"class": "page-numbers"})
                .find_all("li")[-2]
                .text
            )
        else:
            resultsPagesNum = 1

        resultsNum = len(resultsDivs)

        # Checking Results is Greater Than 0
        if resultsNum is None or resultsNum == 0:
            resultsNum = 0

        print(f"The Results Pages Number: {resultsPagesNum}")
        print(f"The Results Number: {resultsNum}")

        # Print The Search Results
        print(("__" * 20) + "\n")
        print("The Results: \n")

        for i in range(resultsNum):

            resultMovieName = resultsDivs[i].find("a").get("title")
            resultMovieLink = resultsDivs[i].find("a").get("href")

            print("__" * 90)
            print(f"|{i}.'{resultMovieName}'")
            print(f"|Movie Link: '{resultMovieLink}'")
            print("__" * 90)

        print(("__" * 20) + "\n")
        searchScrape()

    # ----------------------- CLI Commands ----------------------- #
    print("Chose From Services Menu: ")
    print("1.Scrape Movies")
    print("2.Scrape Series")
    print("3.Scrape Animes")
    print("4.Scrape TV Shows")
    print("5.Scrape Recents")
    print("0.Exit")
    print("\n")
    userInput = input("Select->")

    if userInput == "1":
        print("Chose From Services Menu: ")
        print("1.Scrape Movies By Number of Page")
        print("2.Scrape By Searching Keyword")
        print("00.Back To Main Menu")
        print("0.Exit \n")
        userInput = input("Select->")

        if userInput == "0":
            sys.exit()

        elif userInput == "1":
            scrapeMovies()

        elif userInput == "2":
            searchScrape()

        elif userInput == "00":
            main()

    elif userInput == "2":
        scrapeSeries()

    elif userInput == "3":
        scrapeAnimes()

    elif userInput == "4":
        scrapeTvShows()

    elif userInput == "5":
        scrapeRecents()

    elif userInput == "0":
        sys.exit()


if __name__ == "__main__":
    main()
